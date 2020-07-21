benzylicAcidRearrangement = [ruleGMLString("""
rule [
    ruleID "Benzylic Acid Rearrangement"
    left  [  
        edge [ source 1 target 3 label "-" ]
		edge [ source 2 target 3 label "=" ]
		edge [ source 4 target 5 label "=" ]
		edge [ source 3 target 4 label "-" ]
		edge [ source 4 target 6 label "-" ]
        edge [ source 7 target 8 label "-" ]
    ]
    context [
        node [ id 1 label "C" ]
		node [ id 2 label "O" ]
		node [ id 3 label "C" ]
		node [ id 4 label "C" ]
		node [ id 5 label "O" ]
		node [ id 6 label "C" ]
        node [ id 7 label "O" ]
		node [ id 8 label "H" ]
        node [ id 9 label "H" ]

    ]
    right [
        edge [ source 2 target 3 label "=" ]
		edge [ source 3 target 4 label "-" ]
		edge [ source 4 target 1 label "-" ]
		edge [ source 4 target 5 label "-" ]
        edge [ source 4 target 6 label "-" ]
		edge [ source 7 target 3 label "-" ]
        edge [ source 9 target 7 label "-" ]
        edge [ source 5 target 8 label "-" ]
	]

]""")]
print(inputRules)

postSection ("Input Rules")
for a in inputRules:
	a.print()