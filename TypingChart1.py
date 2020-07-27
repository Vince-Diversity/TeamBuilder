# Makes a resistance chart for all specified typings
# defending typing are rows, attacking are columns
# identify resistance or immunity if identifier <= 1
from Environment import getEffectiveness
import numpy

effectiveness = getEffectiveness()

class ResistanceChart:

    def __init__(self, attackers, defenders):
        self.typingChart = []
        self.transposeTypingChart = []
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

    def getRow(self):
        for k in range(len(self.typingChart)):
            yield self.typingChart[k]

    def getCol(self):
        for k in range(len(self.transposeTypingChart)):
            yield self.transposeTypingChart[k]

    def makeIdentifier(self, attacker, defender):
        if self.isMonoType(attacker): possibilities = [0]
        else:   possibilities = [0, 0]
        for i in range(len(possibilities)):
            if not self.isMonoType(defender):
                possibilities[i] = self.makeDualIdentifier(defender, attacker[i])
            else:
                possibilities[i] = self.makeMonoIdentifier(defender[0], attacker[i])
        return max(possibilities)

    def makeDualIdentifier(self, defender, attack):
        effects = [0, 0]
        for k in range(len(defender)):
            k_effect = effectiveness[(defender[k], attack)]
            if self.isMonoImmune(k_effect):  return -1
            effects[k] = k_effect
        return sum(effects)

    def makeMonoIdentifier(self, defendType, attackType):
        effect = effectiveness[(defendType, attackType)]
        if self.isMonoImmune(effect):    return -1
        else: return effect + 1

    def isMonoType(self, typing):
        return typing[1] == 'none'

    def isResistant(self,identifier):
        return identifier <= 1

    def isMonoImmune(self,identifier):
        return identifier < 0

    def getChart(self):
        return self.typingChart

    def getTransposeChart(self):
        return self.transposeTypingChart

    def getColTyping(self):
        return self.colTypings

    def getRowTyping(self):
        return self.rowTypings
