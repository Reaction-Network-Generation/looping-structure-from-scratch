"""
Count cumulative structural isomers as a function of generation
Plot N_isomers(gen) vs. exact mass 
"""

from rdkit.Chem.rdMolDescriptors import CalcMolFormula
from rdkit.Chem.Descriptors import ExactMolWt
from rdkit.Chem import MolFromSmiles

import matplotlib.pyplot as plt
import matplotlib.gridspec as gspec

def count_struct_isomers(smiles_list):
	"""
	Counts the number of molecules with the same molecular formula
	Keyword arguments:
	smiles_list -- a list of smiles strings of the set/subset of molecules to look at
	Returns: 
	"""
	# formula: isomer count
	dict_isomers = {}
	# formula : smiles list
	dict_smiles = {}
	# weight : isomer count
	dict_exactwt = {}
	
	for mol_smiles in smiles_list:
		mol = MolFromSmiles(mol_smiles)
		formula = CalcMolFormula(mol)
		weight = ExactMolWt(mol)
		if formula in dict_isomers.keys():
			dict_isomers[formula] += 1 # increase the isomer count by 1
			dict_smiles[formula].append(mol_smiles) # These are MOD's smiles, not RDKit's
			dict_exactwt[weight] += 1 # Weight calculated by RDKit, not MOD's in-built
		else:
			dict_isomers[formula] = 1
			dict_smiles[formula] = [mol_smiles]
			dict_exactwt[weight] = 1
	return dict_exactwt # modify this as per your needs


def plot_spectra(exactwt_freq_dict, gen):
	"""
	Stacked Bar Plot using matplotlib
	"""
	# which marker (dot) color to use for which generation
	gen_colors = ['blue', "green", "darkorange", "crimson", 'black']
	
	weights = exactwt_freq_dict.keys()
	freqs = exactwt_freq_dict.values()
	plt.bar(weights, freqs, width=0.5, color=list(reversed(gen_colors))[gen-1], label=f'Generation {gen}')
	plt.xlabel("Exact Mass")
	plt.ylabel("Cumulative Frequency")
	plt.yscale("log")
	#ax[gen-1].set_yscale('log')
	#ax[gen-1].set_yticks([10,100,1000])
	plt.title("Mass spectra of simulated glucose network")
	#plt.setp(stemlines, linestyle="-", color=gen_colors[gen-1], linewidth=0.5)
	#plt.setp(markers, markersize=2, label=f"Generation {gen}")
	#ax[gen-1].legend(loc='upper left')
	#plt.show()

def plot_lollipop(exactwt_freq_dict, gen):
	# which marker (dot) color to use for which generation
	gen_colors = ["blue", "red", "cyan", "green", "magenta"]
	
	weights = exactwt_freq_dict.keys()
	freqs = exactwt_freq_dict.values()
	# if basefmt is not " " it will draw a coloured horizontal baseline at y=0
	(markers, stemlines, baseline) = plt.stem(weights, freqs, basefmt="gray",
				 markerfmt=f"{gen_colors[gen-1][0]}o", use_line_collection=True)
	plt.xlabel("Exact Mass")
	plt.ylabel("Cumulative Frequency")
	plt.yscale("log")
	plt.ylim(bottom=0.625)
	#ax[gen-1].set_yscale('log')
	#ax[gen-1].set_yticks([10,100,1000])
	plt.title("Mass spectra of simulated glucose network")
	plt.setp(stemlines, linestyle="-", color='gray', linewidth=0.5)
	plt.setp(markers, markersize=2, label=f"Generation {gen}")

# Only one fig
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
#fig, ax = plt.subplots(5, sharex=True, sharey=True)
#fig.suptitle("Mass spectra of the model reaction network")
gs = gspec.GridSpec(4,4)
# Plot exact wt vs. number of compounds
with open("glucose/glucose_degradation_output.txt") as output:
	lines = output.readlines()
	gen_smiles_dict = {}
	for line in lines:
		comps = line.split("\t")
		gen = int(comps[0][1])
		smiles_str = comps[1]
		if gen in gen_smiles_dict:
			gen_smiles_dict[gen].append(smiles_str)
		else:
			gen_smiles_dict[gen] = [smiles_str]
	
	# List of smiles upto Nth generation
	cumulative_list = []
	for gen, smiles_list in gen_smiles_dict.items():
		cumulative_list.extend(smiles_list)
	count = 0
	for gen in range(len(gen_smiles_dict.keys()), 0, -1):
		exactwt_count = count_struct_isomers(cumulative_list)
		plot_spectra(exactwt_count, gen)

		#ax2 = fig.add_subplot(111)
		#plot_lollipop(exactwt_count, gen)
		cumulative_list = [x for x in cumulative_list if x not in gen_smiles_dict[gen]]
	plt.legend(loc='upper left')
	plt.show()