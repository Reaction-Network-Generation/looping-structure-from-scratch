include("common.py")

def esterFormationHydrolysisExchangeGen():
	r = RuleGen("Ester Formation Hydrolysis Exchange")
	r.label = "term"
	r.left.extend([
		'# OC(A)OR',
		'edge [ source 0 target 3 label "-" ]',
		'# HNRR',
		'edge [ source 100 target 101 label "-" ]',
	])
	r.context.extend([
		'# OC(A)OR',
		'node [ id 0 label "C" ]',
		'node [ id 1 label "O" ]',
		'node [ id 2 label "*" ]',
		'node [ id 3 label "O" ]',
		'edge [ source 0 target 1 label "=" ]',
		'edge [ source 0 target 2 label "-" ]',
		'# HOR',
		'node [ id 100 label "O" ]',
		'node [ id 101 label "H" ]',
		'node [ id 102 label "*" ]',
		'edge [ source 100 target 102 label "-" ]',
	])
	r.right.extend([
		'# OCN',
		'edge [ source 0 target 100 label "-" ]',
		'# HOR',
		'edge [ source 3 target 101 label "-" ]',
	])
	r.constraints.extend([
		'# TODO: not carbonyl',
		'constrainAdj [',
		'\tid 102 count 0 op "="',
		'\tnodeLabels [ label "O" ]',
		'\tedgeLabels [ label "=" ]',
		']',
	])
	for r1 in attach_H_C(r, 3, 4):
		yield r1.loadRule()

esterFormationHydrolysisExchange = [a for a in esterFormationHydrolysisExchangeGen()]
