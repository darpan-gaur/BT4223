added -maxwanr 10 to grompp command to suppress warnings
```
gmx grompp -f minim.mdp -c system_solv_ions.gro -p topol.top -o em.tpr -maxwarn 10
gmx mdrun -v -deffnm em
```

Equilibration
```
gmx make_ndx -f em.gro -o index.ndx
...
 > 2 | 5
 > q
```

```
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o nvt.tpr
```