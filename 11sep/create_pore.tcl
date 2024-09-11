mol new combined.pdb
set sel [as top "not (same residue as (lipid within 1 of protein))"]
$sel writepdb prot_pore_lipid1.pdb
quit

