from Teambuilder import mostResistancesTeam

n = 6
guessQuality = 0.83
print('Desired size of team: ', n, 'with desired quality: ', guessQuality)
#Teams, resistances, quality = mostResistancesTeam(n,'gen7','gen7', guessQuality)
Teams, resistances, quality = mostResistancesTeam(n,'gen5Regional','gen5RegionalNoDualWeaknes', guessQuality)
print('\nThe most resistances are found')
print('given a team size of: ', n)
print('with resistances: ', resistances)
print('corresponding to quality: ', quality)
print()
for team in Teams:
    print('-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-')
    print(team.getParty())
    print('-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-')
    print()
if not Teams: print('No parties found')
else: print('All parties checked!')
