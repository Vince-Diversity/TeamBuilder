# Teambuilder Environment
import random, numpy, math

# order:
# normal, grass, water, fire, ghost, ice, bug, flying, poison, electric,
# rock, ground, steel, fighting, psychic, dragon, dark, fairy
nonExistentTypings = [
('normal', 'water'), ('normal','ghost'),('normal','ice'),('normal','bug'),
('normal','poison'),('normal','rock'),('normal','steel'),
('grass','fire'),('grass','electric'),
('water','fire'),
('fire','ice'),('fire','electric'),('fire','steel'),('fire','fairy'),
('ghost','bug'),('ghost','electric'),('ghost','rock'),('ghost','fighting'),
('ghost','psychic'),('ghost','dragon'),
('ice','bug'), ('ice','poison'), ('ice','electric'),('ice','dragon'),
('bug','ground'),('bug','psychic'),('bug','dragon'),('bug','dark'),
('flying','none'),
('poison','electric'),('poison','rock'),('poison','steel'),('poison','psychic'),
('poison','fairy'),
('electric','fighting'),('electric','dragon'),('electric','dark'),
('rock','fighting'),
('ground','fighting'),('ground','fairy'),
('steel','dragon'),
('fighting','fairy'),
('psychic','dragon'),
('dragon','fairy')
]

# order:
# normal, grass, water, fire, ghost, ice, bug, flying, poison, electric,
# rock, ground, steel, fighting, psychic, dragon, dark, fairy
hasDualWeakness = [
('normal','ice'),('normal','rock'),('normal','steel'),
('grass','ice'),('grass','bug'),('grass','flying'),('grass','ground'),('grass','steel'),
('grass','fighting'),('grass','psychic'),('grass','dragon'),('grass','dark'),('grass','fairy'),
('water','flying'),('water','rock'),('water','ground'),
('fire','bug'),('fire','flying'),('fire','poison'),('fire','electric'),('fire','rock'),('fire','ground'),
('ghost','psychic'),
('ice','flying'),('ice','rock'),('ice','steel'),('ice','fairy'),
('bug','grass'),('bug','flying'),('bug','steel'),('bug','fighting'),
('flying','gound'),('flying','dragon'),
('electric','steel'),
('poison','rock'),('poison','steel'),('poison','fighting'),
('rock','ground'),('rock','steel'),('rock','fairy'),
('ground','dragon'),
('fighting','dark')
]

# Only obtained after E4 or late or is just a bad switch in
gen5postE4 = [
('water','dark'), ('dragon','dark'),('flying','dark'),('rock','dark'),
('fire','dragon'),('electric','dragon'),('ice','dragon'),
('flying','rock'),
#('flying','steel')
]

levitateAdjustmentgen5  =[
('electric','none'),('ground','dragon'),('rock','psychic'),('ground','psychic'),
('ghost','none'),('psychic','none'),('steel','psychic'),('ice','none'),('dragon','dark')
]

# order:
# normal, grass, water, fire, ghost, ice, bug, flying, poison, electric,
# rock, ground, steel, fighting, psychic, dragon, dark, fairy
# feel free to order the most preferred typings first
gen5Regional = [
('flying','electric'),('grass','none'),('fire','none'),('fire','fighting'),
('water','none'),('normal','none'),('dark','none'),('normal','flying'),
('bug','grass'),('electric','none'),('fighting','none'),
('steel','fighting'),('bug','poison'),('poison','none'),('electric','steel'),
('flying','poison'),('flying','psychic'),('rock','none'),
('rock','ground'),('rock','steel'),('ground','none'),('ground','steel'),
('psychic','none'),('ice','none'),('ground','dark'),
('bug','rock'),('fighting','dark'),('ground','dragon'),
('ghost','none'),('water','rock'),('flying','rock'),('steel','none'),
('grass','poison'),('bug','flying'),('bug','fighting'),
('bug','none'),('water','flying'),('bug','steel'),('normal','grass'),
('ground','psychic'),('fire','bug'),('bug','electric'),
('grass','steel'),('water','ghost'),('dragon','none'),('fire','ghost'),
('flying','steel'),('fire','ground'),('ghost','flying'),
('rock','psychic'),('ground','flying'),('steel','dark'),
('rock','fighting'),('grass','fighting'),('water','ground'),('electric','ground'),
('water','psychic'),('water','ice'),('flying','dragon'),('steel','psychic'),
('ice','dark'),('ice','flying'),('ice','ground'),('ghost','ground'),
('grass','flying'),('poison','fighting'),
('water','dark'), ('dragon','dark'),('flying','dark'),('rock','dark'),
('fire','dragon'),('electric','dragon'),('ice','dragon')
# Won't be encountered
#('fire','psychic'),('psychic','fighting'),('normal','psychic'),('water','fighting')
]

testRegional =  [('fire', 'ghost'), ('grass', 'ghost'), ('grass', 'none'), ('fire', 'none'), ('ghost', 'none')]

# (defender, attacker)
# resistance: 0, immunity: -1, neutral: 1, effective: 2
## Changed to gen 5 typechart!
effectiveness = {
('normal','normal') : 1, ('normal','grass') : 1, ('normal', 'fire'): 1,
('normal','water') : 1, ('normal','ghost') : -1, ('normal','ice') : 1,
('normal','bug') : 1, ('normal','flying') : 1, ('normal','poison') : 1,
('normal','electric') : 1, ('normal','rock') : 1, ('normal','ground') : 1,
('normal','steel') : 1, ('normal','fighting') : 2, ('normal','psychic') : 1,
('normal','dragon') : 1, ('normal','dark') : 1, ('normal','fairy') : 1,
('grass', 'normal') : 1, ('grass','grass') : 0, ('grass','water') : 0,
('grass','fire') : 2, ('grass','ghost') : 1, ('grass','ice') : 2,
('grass','bug') : 2, ('grass','flying') : 2, ('grass','poison') : 2,
('grass','electric') : 0, ('grass','rock') : 1, ('grass','ground') : 0,
('grass','steel') : 1, ('grass','fighting') : 1, ('grass','psychic') : 1,
('grass','dragon') : 1, ('grass','dark') : 1, ('grass','fairy') : 1,
('water', 'normal') : 1, ('water','grass') : 2, ('water','water') : 0,
('water','fire') : 0, ('water','ghost') : 1, ('water','ice') : 0,
('water','bug') : 1, ('water','flying') : 1, ('water','poison') : 1,
('water','electric') : 2, ('water','rock') : 1, ('water','ground') : 1,
('water','steel') : 0, ('water','fighting') : 1, ('water','psychic') : 1,
('water','dragon') : 1, ('water','dark') : 1, ('water','fairy') : 1,
('fire', 'normal') : 1, ('fire','grass') : 0, ('fire','water') : 2,
('fire','fire') : 0, ('fire', 'ghost') : 1, ('fire', 'ice') : 0,
('fire','bug') : 0, ('fire','flying') : 1, ('fire','poison') : 1,
('fire','electric') : 1, ('fire','rock') : 2, ('fire','ground') : 2,
('fire','steel') : 0, ('fire','fighting') : 1, ('fire','psychic'): 1,
('fire','dragon') : 1, ('fire','dark') : 1, ('fire','fairy') : 0,
('ghost','normal') : -1, ('ghost','grass') : 1, ('ghost','water') : 1,
('ghost','fire') : 1, ('ghost','ghost') : 2, ('ghost','ice') : 1,
('ghost','bug') : 0, ('ghost','flying') : 1, ('ghost','poison') : 0,
('ghost','electric') : 1, ('ghost','rock') : 1, ('ghost','ground') : 1,
('ghost','steel') : 1, ('ghost','fighting') : -1, ('ghost','psychic') : 1,
('ghost','dragon') : 1, ('ghost','dark') : 2, ('ghost','fairy') : 1,
('ice','normal') : 1, ('ice','grass') : 1, ('ice','water') : 1,
('ice','fire') : 2, ('ice','ghost') : 1, ('ice','ice') : 0,
('ice','bug') : 1, ('ice','flying') : 1, ('ice','poison') : 1,
('ice','electric') : 1, ('ice','rock') : 2, ('ice','ground') : 1,
('ice','steel') : 2, ('ice','fighting') : 2, ('ice','psychic') : 1,
('ice','dragon') : 1, ('ice','dark') : 1, ('ice','fairy') : 1,
('bug','normal') : 1, ('bug','grass') : 0, ('bug','water') : 1,
('bug','fire') : 2, ('bug','ghost') : 1, ('bug','ice') : 1,
('bug','bug') : 1, ('bug','flying') : 2, ('bug','poison') : 1,
('bug','electric') : 1, ('bug','rock') : 2, ('bug','ground') : 0,
('bug','steel') : 1, ('bug','fighting') : 0, ('bug','psychic') : 1,
('bug','dragon') : 1, ('bug','dark') : 1, ('bug','fairy') : 1,
('flying','normal') : 1, ('flying','grass') : 0, ('flying','water') : 1,
('flying','fire') : 1, ('flying','ghost') : 1, ('flying','ice') : 2,
('flying','bug') : 0, ('flying','flying') : 1, ('flying','poison') : 1,
('flying','electric') : 2, ('flying','rock') : 2, ('flying','ground') : -1,
('flying','steel') : 1, ('flying','fighting') : 0, ('flying','psychic') : 1,
('flying','dragon') : 1, ('flying','dark') : 1, ('flying','fairy') : 1,
('poison','normal') : 1, ('poison','grass') : 0, ('poison','water') : 1,
('poison','fire') : 1, ('poison','ghost') : 1, ('poison','ice') : 1,
('poison','bug') : 0, ('poison','flying') : 1, ('poison','poison') : 0,
('poison','electric') : 1, ('poison','rock') : 1, ('poison','ground') : 2,
('poison','steel') : 1, ('poison','fighting') : 0, ('poison','psychic') : 2,
('poison','dragon') : 1, ('poison','dark') : 1, ('poison','fairy') : 0,
('electric','normal') : 1, ('electric','grass') : 1, ('electric','water') : 1,
('electric','fire') : 1, ('electric','ghost') : 1, ('electric','ice') : 1,
('electric','bug') : 1, ('electric','flying') : 0, ('electric','poison') : 1,
('electric','electric') : 0, ('electric','rock') : 1, ('electric','ground') : 2,
('electric','steel') : 0, ('electric','fighting') : 1, ('electric','psychic') : 1,
('electric','dragon') : 1, ('electric','dark') : 1, ('electric','fairy') : 1,
('rock','normal') : 0, ('rock','grass') : 2, ('rock','water') : 2,
('rock','fire') : 0, ('rock','ghost') : 1, ('rock','ice') : 1,
('rock','bug') : 1, ('rock','flying') : 0, ('rock','poison') : 0,
('rock','electric') : 1, ('rock','rock') : 1, ('rock','ground') : 2,
('rock','steel') : 2, ('rock','fighting') : 2, ('rock','psychic') : 1,
('rock','dragon') : 1, ('rock','dark') : 1, ('rock','fairy') : 1,
('ground','normal') : 1, ('ground','grass') : 2, ('ground','water') : 2,
('ground','fire') : 1, ('ground','ghost') : 1, ('ground','ice') : 2,
('ground','bug') : 1, ('ground','flying') : 1, ('ground','poison') : 0,
('ground','electric') : -1, ('ground','rock') : 0, ('ground','ground') : 1,
('ground','steel') : 1, ('ground','fighting') : 1, ('ground','psychic') : 1,
('ground','dragon') : 1, ('ground','dark') : 1, ('ground','fairy') : 1,
('steel','normal') : 0, ('steel','grass') : 0, ('steel','water') : 1,
#('steel','fire') : 2, ('steel','ghost') : 1 , ('steel','ice') : 0,
('steel','fire') : 2, ('steel','ghost') : 0 , ('steel','ice') : 0,
('steel','bug') : 0, ('steel','flying') : 0, ('steel','poison') : -1,
('steel','electric') : 1, ('steel','rock') : 0, ('steel','ground') : 2,
('steel','steel') : 0, ('steel','fighting') : 2, ('steel','psychic') : 0,
#('steel','dragon') : 0, ('steel','dark') : 1, ('steel','fairy') : 0,
('steel','dragon') : 0, ('steel','dark') : 0, ('steel','fairy') : 0,
('fighting','normal') : 1, ('fighting','grass') : 1, ('fighting','water') : 1,
('fighting','fire') : 1, ('fighting','ghost') : 1, ('fighting','ice') : 1,
('fighting','bug') : 0, ('fighting','flying') : 2,('fighting','poison') : 1,
('fighting','electric') : 1, ('fighting','rock') : 0, ('fighting','ground') : 1,
('fighting','steel') : 1, ('fighting','fighting') : 1, ('fighting','psychic') : 1,
('fighting','dragon') : 1, ('fighting','dark') : 0, ('fighting','fairy') : 2,
('psychic','normal') : 1, ('psychic','grass') : 1, ('psychic','water') : 1,
('psychic','fire') : 1, ('psychic','ghost') : 2, ('psychic','ice') : 1,
('psychic','bug') : 2, ('psychic','flying') : 1, ('psychic','poison') : 1,
('psychic','electric') : 1, ('psychic','rock') : 1, ('psychic','ground') : 1,
('psychic','steel') : 1, ('psychic','fighting') : 0, ('psychic','psychic') : 0,
('psychic','dragon') : 1, ('psychic','dark') : 2, ('psychic','fairy') : 1,
('dragon','normal') : 1, ('dragon','grass') : 0, ('dragon','water') : 0,
('dragon','fire') : 0, ('dragon','ghost') : 1, ('dragon','ice') : 2,
('dragon','bug') : 1, ('dragon','flying') : 1, ('dragon','poison') : 1,
('dragon','electric') : 0, ('dragon','rock') : 1, ('dragon','ground') : 1,
('dragon','steel') : 1, ('dragon','fighting') : 1, ('dragon','psychic') : 1,
('dragon','dragon') : 2, ('dragon','dark') : 1, ('dragon','fairy') : 2,
('dark','normal') : 1, ('dark','grass') : 1, ('dark','water') : 1,
('dark','fire') : 1, ('dark','ghost') : 0, ('dark','ice') : 1,
('dark','bug') : 2, ('dark','flying') : 1, ('dark','poison') : 1,
('dark','electric') : 1, ('dark','rock') : 1, ('dark','ground') : 1,
('dark','steel') : 1, ('dark','fighting') : 2, ('dark','psychic') : 0,
('dark','dragon') : 1, ('dark','dark') : 0, ('dark','fairy') : 2,
('fairy','normal') : 1, ('fairy','grass') : 1, ('fairy','water') : 1,
('fairy','fire') : 1, ('fairy','ghost') : 1, ('fairy','ice') : 1,
('fairy','bug') : 0, ('fairy','flying') : 1, ('fairy','poison') : 2,
('fairy','electric') : 1, ('fairy','rock') : 1, ('fairy','ground') : 1,
('fairy','steel') : 2, ('fairy','fighting') : 0, ('fairy','psychic') : 1,
('fairy','dragon') : -1, ('fairy','dark') : 0, ('fairy','fairy') : 1,
# gen5 adjustments - KeyError
#('levitate','normal') : 1, ('levitate','grass') : 1, ('levitate','water') : 1,('levitate','fire') : 1, ('levitate','ghost') : 1, ('levitate','ice') : 1,('levitate','bug') : 0, ('levitate','flying') : 1, ('levitate','poison') : 2,('levitate','electric') : 1, ('levitate','rock') : 1, ('levitate','ground') : -1,('levitate','steel') : 2, ('levitate','fighting') : 0, ('levitate','psychic') : 1,('levitate','dragon') : -1, ('levitate','dark') : 0,
}

#typings which resists itself
# only needed for same type counter, not very useful
#normal, grass, water, fire, ghost, ice, bug, flying, poison, electric,
#rock, ground, steel, fighting, psychic, dragon, dark, fairy
sameResistances = [
('grass','none'), ('water','none'),('fire','none'),('ice','none'),
('poison','none'), ('electric','none'),
('water','ice'), ('bug','poison'),
('grass','electric'), ('fire','electric'), ('ice','electric')
]

def getEffectiveness():
    return effectiveness

def sameResist():
    return sameResistances

def getTypingList(cond):
    if cond == 'grasswaterfire':
        return makeTypings(['grass','water','fire'])
    if cond == 'normalgrasswaterfire':
        return makeTypings(['normal','water','grass','fire'])
    if cond == 'normalgrassghost':
        return makeTypings(['normal', 'grass', 'ghost'])
    if cond == 'grassfireghost':
        return makeTypings(['grass','fire','ghost'])
    if cond == 'grasswaterghost':
        return makeTypings(['grass','water','ghost'])
    if cond == 'dual1-5':
        return makeTypings(['normal','grass','water','fire','ghost'])
    if cond == 'mono1-5':
        return makeMonoTypings(['normal','grass','water','fire','ghost'])
    if cond == 'mono1-4':
        return makeMonoTypings(['normal','grass','water','fire'])
    if cond == 'mono2-4':
        return makeMonoTypings(['grass','water','fire'])
    if cond == 'dual1-10':
        return makeTypings(['normal', 'grass', 'water', 'fire', 'ghost',
        'ice', 'bug', 'flying', 'poison', 'electric'])
    if cond == 'gen7':
        return makeTypings(['normal', 'grass', 'water', 'fire', 'ghost',
            'ice', 'bug', 'flying', 'poison', 'electric',
            'rock', 'ground', 'steel', 'fighting', 'psychic',
            'dragon', 'dark', 'fairy'])
    if cond == 'gen5RegionalNoDualWeaknes':
        return makeTypingsDefender(gen5Regional)
    if cond == 'gen5Regional':
        return gen5Regional
    if cond == 'testRegional':
        return makeTypings2(testRegional)

def makeTypings(typeList):
    typingList = []
    addDualtypes(typeList, typingList)
    addMonotypes(typeList, typingList)
    return typingList

# used for regional runs
def makeTypings2(typingList):
    returnList = []
    for typing in typingList:
        if feasibleGen5(typing):
            returnList.append(typing)
    return returnList

# used for regional runs
def makeTypingsDefender(typingList):
    returnList = []
    for typing in typingList:
        if feasibleGen5(typing):
            returnList.append(typing)
    return returnList

def feasibleGen5(typing):
    return typing not in hasDualWeakness and typing not in gen5postE4

def makeMonoTypings(typeList):
    typingList = []
    addMonotypes(typeList, typingList)
    return typingList

def addDualtypes(typeList, typingList):
    n = len(typeList)
    IJ = makeListOrder(n)
    for ij in IJ:
        typing = (typeList[ij[0]],typeList[ij[1]])
        if typingExists(typing):
            typingList.append(typing)
    return None

def addMonotypes(typeList, typingList):
    n = len(typeList)
    for i in range(n):
        typing = (typeList[i],'none')
        typingList.append(typing)
    return None

def typingExists(typing):
    return typing not in nonExistentTypings

def makeListOrder(n):
    indexing = []
    for i in range(n):
        for j in range(i,n):
            if i != j:
                indexing.append((i,j))
    random.shuffle(indexing)
    return indexing

def makeEffectivenessMatrix():
    values = [value for value in effectiveness.values()]
    numpyValues = numpy.array(values)
    n = math.sqrt(len(values))
    m = int(n)
    n = m
    return numpyValues.reshape(n,m)
