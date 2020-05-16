# TODO: Fix exception: rmgpy.exceptions.ForbiddenStructureException:
#  Species C2O from reaction library Glarborg/C3 is globally forbidden.
#  You may explicitly allow it, but it will remain inert unless found in a seed mechanism or reaction library.

database(
    thermoLibraries = ['primaryThermoLibrary'],
 #   seedMechanisms = [],
#    kineticsDepositories=['training'],
 #   kineticsFamilies='default',
 #   kineticsEstimator='rate rules',
    reactionLibraries = [] # 'Glarborg/C3' wasn't allowing C20
)

## isomeric smiles for glucose: C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O
## canonical smiles for glucose: 'C(C1C(C(C(C(O1)O)O)O)O)O'
species(
    label='glycine',
    reactive=True,
    structure=SMILES('NCC(=O)O'),
)

species(
    label='HCN',
    reactive=True,
    structure=SMILES('C#N')
)

simpleReactor(
    temperature=(800,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        'glycine':.5,
        'HCN':0.5
    },
    terminationTime=(1e-8,'s'),
    terminationConversion={
        'glycine':0.01
    },
    sensitivity=('HCN','glycine')
)

## Absolute and relative tolerance(s)
## I don't understand what exactly these do
simulator(
    atol=1e-16,
    rtol=1e-8,
)

# The code doesn't run if the model section is not even defined
model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000,
    filterReactions=True,
)

options(
    units='si',
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True,
)