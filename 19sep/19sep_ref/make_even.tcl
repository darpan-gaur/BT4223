mol new prot_mem_pore.pdb
set nup [as top "same residue as (name N and z>0 and (resname POPC and index %101=0 or index % 203=0 ))"] 
$nup writepdb fix.pdb
quit


