get unique residues
```
set sel [as top all]
lsort -unique [$sel get resname]
```

get only chlorine
```
set sel [as top "name CL"]
lsort -unique [$sel get resname]
$sel num
```

get lipid
``` 
rename POPC
```

```
same residue as resname POPC and index 1
```

get center of lipid
```
set sel [as top "resname POPC"]
measure center $sel
```

```
measure minmax $sel
```

get top and bottom replet
```
name N and resname POPC and z>70
name N and resname POPC and z<70
```

thickness of lipid membrane (see z axis difference)
```
set sel [as top "name N and resname POPC and z>70"]
set sel1 [as top "name N and resname POPC and z<70"]
vecsub [measure center $sel] [measure center $sel1]
```
