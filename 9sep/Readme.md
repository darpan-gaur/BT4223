Set path to plugins to home directory

copy .vmdrc file to home directory with updated path to plugins

align protein and membrane

```
vmd -f step4_lipid.pdb -f prt_align.pdb 
```
- allign to 0 and same mem.pdb
```
cat prt_align.pdb mem.pdb >combined.pdb
```
