get unique resnames
```
set sel [as top all]
set resnames [lsort -unique [$sel get resname]]
```

option in genion :- 15 - SOL

```
ions, water, protein, lipid
```

add ions
```
gmx genion -s ions.tpr -o system_solv_ions.gro -p topol.top -pname K -nname CL -conc 0.15
```