popc -> lipid type
```
lipid and x > 0
```

view atoms that are cut at boundary
```
same residue as lipid and x>0
```

Nitrogen atome
```
lipid and y>0 and name N
```


Solvation
```
gmx pdb2gmx -f prot_mem_pore.pdb  -o prot_pore_processed.gro -ignh -ter -water spc
```
MET-1 - 1:NH3+      
0: COO-

port_pro...gro -> visualize in vmd, change box size
```
pbc set {92 92 140}
```