with_formaldehyde = False
include("../main.py")
include("../../rules/alkeneAdditionElimination.py")
postChapter("HCN Oligmerisation")

hcn = smiles("C#N", name="Hydrogen Cyanide")
water = smiles("O", name="Water")

'''dg = dgDump(inputGraphs, inputRules, "../dumps/formose_4_rounds.dg")
print("Finished loading from dump file")'''

# Number of generations we want to perform
generations = 3

dg = DG(graphDatabase=inputGraphs,
	labelSettings=LabelSettings(LabelType.Term, LabelRelation.Specialisation))

subset = inputGraphs
universe = []
# In the following block, apart from generating the reactions, we may print structures
# and reactions forming them that are not in the MS
#postSection("Structures not found in MS")
with dg.build() as b:
	for gen in range(generations):
		start_time = time.time()
		print(f"Starting round {gen+1}")
		res = b.execute(addSubset(subset) >> addUniverse(universe) >> strat, verbosity=2)
		end_time = time.time()
		print(f"Took {end_time - start_time} seconds to complete round {gen+1}")
		print('Original subset size:', len(res.subset))

		# The returned subset and universe do not contain redundant tautomers
		#subset, universe = clean_taut(dg, res, algorithm="CMI")
		subset, universe = res.subset, res.universe
		#print('Subset size after removal:', len(subset))
		# This step replaces the previous subset (containing tautomers) with the cleaned subset
		#res = b.execute(addSubset(subset) >> addUniverse(universe))
		# now compare how man
		# y of these simulations were found in the MS data.
		#compare_sims(dg, gen+1, print_extra=False)
		#export_to_neo4j(dg_obj = dg, generation_num = gen)
		write_gen_output(subset, gen, reaction_name="hcn_olig")
	print('Completed')

# Dump the dg so it can be loaded again quickly without having to generate it from scratch.
f = dg.dump()
print("Dump file: ", f)

check_sdf_matches(dg, "../../data/HCNfixed.sdf.sdf")