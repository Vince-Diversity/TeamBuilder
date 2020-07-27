from Environment import getTypingList, makeEffectivenessMatrix
from TypingChart import ResistanceChart
from Teambuilder import listParties, mostResistancesTeam, resistQuality

def testMostResistancesParty(n,colCond,rowCond):
    parties, guarantees, quality = mostResistancesTeam(n,colCond,rowCond)
    for party in parties:
        print('\nMost resistances party:')
        print(party.getParty())
        print("with resistances: ", party.getGuaranteedResistCount())
        print('and quality ', quality)
        print()

#testMostResistancesParty(2,'grasswaterfire','grasswaterfire')
#testMostResistancesParty(2,'dual1-5','dual1-5')
# This one actually gives a quality 1 team
# (fire, ghost), (normal, fire), (normal, grass)
#testMostResistancesParty(3,'dual1-5','dual1-5')
#testMostResistancesParty(2,'grasswaterfire','normalgrasswaterfire')

def testListParties(n,cond1,cond2):
    listParties(n,cond1,cond2,0)

#testListParties(2,'grasswaterfire','grasswaterfire')
#testListParties(2,'dual1-5','dual1-5')
#testListParties(3,'dual1-5','dual1-5')

def testTypingChart(attacker, defender):
    typingList = getTypingList(defender)
    colTypingList = getTypingList(attacker)
    chart = ResistanceChart(colTypingList, typingList)
    print('Chart object: ', chart)
    chartContent = chart.getChart()
    print('Chart: ', chartContent)
    print('Chart values: \n', chart.makeValueMatrix())
    print('Corresponding to resistance chart: \n', chart.makeResistanceMatrix())
    print('TypingList: ', colTypingList, '\n VS', typingList)

#testTypingChart('grasswaterfire','grasswaterfire')
testTypingChart('grasswaterghost','grasswaterghost')
#testTypingChart('grassfireghost','grassfireghost')

def testEffectivenessMatrix():
    print('Effectiveness matrix:\n')
    print(makeEffectivenessMatrix())

#testEffectivenessMatrix()

def testGetTypingList(cond):
    print('TypingList: ', getTypingList(cond))

testGetTypingList('grasswaterfire')
