# Makes a resistance chart for all specified typings
# defending typing are rows, attacking are columns
# identify resistance or immunity if identifier <= 1
from Environment import getEffectiveness
import numpy

effectiveness = getEffectiveness()

# Chart of a possibility for stab resisted switch in
# without stab super effective repercussion
class ResistanceChart:

    def __init__(self, attackers, defenders):
        self.typingChart = []
        self.colTypings = attackers
        self.rowTypings = defenders
        self.makeTypingChart(defenders, attackers)

    def makeTypingChart(self, rowTypings, colTypings):
        chart = {}
        for row in rowTypings:
            for col in colTypings:
                chart[(row,col)] = self.makeIdentifier(col, row)
        self.typingChart = chart
        return self.typingChart

    def makeValueMatrix(self):
        values = [value for value in self.typingChart.values()]
        numpyValues = numpy.array(values)
        n = len(self.rowTypings)
        m = len(self.colTypings)
        return numpyValues.reshape(n,m)

    def makeResistanceMatrix(self):
        values = [int(self.isResistant(value)) for value in self.typingChart.values()]
        numpyValues = numpy.array(values)
        n = len(self.rowTypings)
        m = len(self.colTypings)
        return numpyValues.reshape(n,m)

    def makeIdentifier(self, attacker, defender):
        monoDefender = self.isMonoType(defender)
        if self.isMonoType(attacker):
            if monoDefender:
                return self.makeMonoMonoIdentifier(defender, attacker[0])
            else:
                return self.makeDualMonoIdentifier(defender, attacker[0])
        else:
            return self.makeDualIdentifier(defender,attacker,monoDefender)

    def makeDualIdentifier(self, defender, attacker, monoDefender):
        k = 0
        for attackType in attacker:
            if monoDefender:
                identj = self.makeMonoMonoIdentifier(defender, attackType)
            else:
                identj = self.makeDualMonoIdentifier(defender, attackType)
            if self.isResistant(identj):
                threat = attacker[1-k]
                if monoDefender:
                    idthr = self.makeMonoMonoIdentifier(defender, threat)
                else:
                    idthr = self.makeDualMonoIdentifier(defender, threat)
                if self.isMonoWeakTo(idthr):   return 2
                else: return identj
            k += 1
        return 3

    def makeDualMonoIdentifier(self, defender, attackType):
        effects = [0, 0]
        for k in range(len(defender)):
            k_effect = effectiveness[(defender[k], attackType)]
            if self.isMonoImmune(k_effect):  return -1
            effects[k] = k_effect
        return sum(effects)

    def makeMonoMonoIdentifier(self, defender, attackType):
        effect = effectiveness[(defender[0], attackType)]
        if self.isMonoImmune(effect):    return -1
        else: return effect + 1

    def isMonoType(self, typing):
        return typing[1] == 'none'

    def isResistant(self, identifier):
        return identifier <= 1

    def isMonoWeakTo(self, identifier):
        return identifier >= 3

    def isMonoImmune(self, identifier):
        return identifier < 0

    def getChart(self):
        return self.typingChart

    def getColTyping(self):
        return self.colTypings

    def getRowTyping(self):
        return self.rowTypings
