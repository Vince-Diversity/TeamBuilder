# Tests some of Teambuilder's features

from Environment import getTypingList, makeEffectivenessMatrix
from TypingChart import ResistanceChart
from Teambuilder import listParties

def testEffectivenessMatrix():
    print('Effectiveness matrix:\n')
    print(makeEffectivenessMatrix())

def testGetTypingList(cond):
    print('TypingList: ', getTypingList(cond))

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
#    print('Transpose chart: ', [k for k in chart.getTransposeChart()])

def testPartyAttributes():
    print('\nTest same type counter:')
    listParties(2,'grasswaterfire','grasswaterfire')
    print('test immunity count')
    listParties(2,'normalgrassghost','normalgrassghost')

def testListParties():
    ListParties(3,'dual1-5','dual1-5')

#testEffectivenessMatrix()

#testGetTypingList('grasswaterfire')
#testTypingChart('mono2-4','grasswaterfire')
#testTypingChart('grasswaterfire','grasswaterfire')
#testTypingChart('normalgrassghost','normalgrassghost')
#testTypingChart('mono2-4','normalgrassghost')

#testPartyAttributes()

#testListParties()
