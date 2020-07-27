# Finds parties of size n
# with resistance to a subset of typings cond

from Environment import getTypingList, sameResist
from TypingChart import ResistanceChart
import TypingChart1
from itertools import combinations

def mostResistancesTeam(n, colCond, rowCond, guessQuality):
    parties, chart = listParties(n, colCond, rowCond, guessQuality)
    mostResistedParties = []
    mostGuarantees = 0
    for party in parties:
        guarantees = party.getGuaranteedResistCount()
        if guarantees > mostGuarantees:
            mostResistedParties = [party]
            mostGuarantees = guarantees
        elif guarantees == mostGuarantees:
            mostResistedParties.append(party)
    quality = resistQuality(mostGuarantees, chart)
    return mostResistedParties, mostGuarantees, quality

def listParties(n, colCond, rowCond, guessQuality):
    parties = []
    typingList = getTypingList(rowCond)
    colTypingList = getTypingList(colCond)
    chart = ResistanceChart(colTypingList, typingList)
    guaranteeChart = TypingChart1.ResistanceChart(colTypingList,typingList)
    print('Using environment: ', colTypingList, '\n VS\n', typingList)
    print('Using chart: \n', chart.makeResistanceMatrix())
    print('of size ', len(chart.getRowTyping()), 'x', len(chart.getColTyping()))
    print()
    for party in partyGenerator(n, typingList, chart, guaranteeChart):
        guarantees = party.getGuaranteedResistCount()
        tryQuality = resistQuality(guarantees, chart)
        if tryQuality > guessQuality:
            print('\nFound party!')
            print('-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-')
            print(party.getParty())
            print('-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-')
            print('with quality', tryQuality)
            print()
            parties.append(party)
    return parties, chart

def resistQuality(resistances, chart):
    comparison = len(chart.getColTyping())
    return resistances/comparison

def partyGenerator(n, typingList, chart, guaranteeChart):
    leadTypingSame = True
    previousLeadTyping = ()
    for party in guessGenerator(n, typingList):
        partyCont = party.getParty()
        if partyCont[0] != previousLeadTyping:
            leadTypingSame = False
        if not leadTypingSame:
            print('Checking Lead Typing',partyCont[0])
            leadTypingSame = True
        previousLeadTyping = partyCont[0]
        if conditionsMet(party, chart, guaranteeChart):    yield party

def guessGenerator(n, typingList):
    for tupleGuess in combinations(typingList, n):
        yield Party(tupleGuess)

def conditionsMet(party, chart, guaranteeChart):
    colTypings = chart.getColTyping()
    foundCounter = False
    for colTyping in colTypings:
        for b in existsCounter(colTyping, party, chart):
            if not b: return False
    party.guaranteedResistCount(countGuaranteedResist(party,chart,guaranteeChart))
#    party.immunityCount(countImmunities(party, chart))
#    party.sameTypeCount(countSameTypings(party, chart))
    return True

def existsCounter(foe, party, chart):
    chartContent = chart.getChart()
    for member in party.getParty():
        identifier = chartContent[(member, foe)]
        if chart.isResistant(identifier):
            return True
    yield False

def countGuaranteedResist(party, chart, guaranteeChart):
    def counter(party, chart):
        colTypings = chart.getColTyping()
        rowTypings = chart.getRowTyping()
        guaranteeChartContent = guaranteeChart.getChart()
        for attacker in guaranteeChart.getColTyping():
            for finding in findGuarantee(party, attacker, guaranteeChartContent):
                yield 1
    def findGuarantee(party, attacker, guaranteeChartContent):
        for member in party.getParty():
            identifier = guaranteeChartContent[(member, attacker)]
            if guaranteeChart.isResistant(identifier):
                yield 1
                return
    return sum(counter(party,chart))

def countImmunities(party, chart):
    def counter(party, chart):
        chartContent = chart.getChart()
        for member in party.getParty():
            for attacker in chart.getColTyping():
                identifier = chartContent[(member, attacker)]
                yield -identifier if identifier < 0 else 0
    return sum(counter(party, chart))

def countSameTypings(party, chart):
    def counter(party, chart):
        chartContent = chart.getChart()
        checkOptions = False
        for attacker in chart.getColTyping():
            for member in party.getParty():
                identifier1 = chartContent[(member, attacker)]
                if chart.isResistant(identifier1):
                    if member == attacker and member in sameResist():
                        yield 1
                        checkOptions = True
                    if checkOptions:
                        for option in party.getParty():
                            identifier2 = chartContent[(option, attacker)]
                            if chart.isResistant(identifier2):
                                if option != attacker:
                                    yield -1
                                    checkOptions = False
                        checkOptions = False
    return sum(counter(party, chart))

def monoTypeCounter(chart, cols):
    for col in cols:
        if chart.isMonoType(col):   yield 1

# pick n elements from m defending typings
# if match is on same type, raise same type count
class Party:

    def __init__(self, contents):
        self.party = contents
        self.sameTypeCounter = 0
        self.immunityCounter = 0
        self.guaranteedResists = 0

    def getParty(self):
        return self.party

    def getSameTypeCount(self):
        return self.sameTypeCounter

    def getWeakessCount(self):
        return self.immunityCounter

    def getGuaranteedResistCount(self):
        return self.guaranteedResists

    def sameTypeCount(self, identifier):
        self.sameTypeCounter += identifier
        return self.sameTypeCounter

    def immunityCount(self, identifier):
        self.immunityCounter += identifier
        return self.immunityCounter

    def guaranteedResistCount(self, identifier):
        self.guaranteedResists += identifier
        return self.guaranteedResists
