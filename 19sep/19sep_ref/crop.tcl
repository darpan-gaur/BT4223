mol new combined.pdb
set sel [as top "not (same residue as (resname POPC and within 1.5 of protein))"]
$sel num
$sel writepdb prot_mem_pore.pdb

quit

