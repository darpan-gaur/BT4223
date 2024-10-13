Steps used for the project, similar to lysosome in water
- 
- Search and select pdb file from rcsb: 6w75.
- Used alphafold to get missing residues.
- Removed water and made clear pdb file.
- Used charm gui pdb reader/manipulator, pre-process pdb.

Gromacs from here
- 
pdb2gmax, generate topology
```
gmx pdb2gmx -f step1_pdbreader.pdb  -o protein_processed.gro -water spce
```
Defining the Unit Cell & Adding Solvent
```
gmx editconf -f protein_processed.gro -o protein_newbox.gro -c -d 1.0 -bt cubic
gmx solvate -cp protein_newbox.gro -cs spc216.gro -o proein_solv.gro -p topol.top
```
Adding ions
```
wget http://www.mdtutorials.com/gmx/lysozyme/Files/ions.mdp
gmx grompp -f ions.mdp -c protein_solv.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o protein_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```
Energy Minimization
```
wget http://www.mdtutorials.com/gmx/lysozyme/Files/minim.mdp
gmx grompp -f minim.mdp -c protein_solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -v -deffnm em
```
Equilibration
```
wget http://www.mdtutorials.com/gmx/lysozyme/Files/nvt.mdp
gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
gmx mdrun -v -deffnm nvt
```
Equilibration, Part 2
```
wget http://www.mdtutorials.com/gmx/lysozyme/Files/npt.mdp
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
gmx mdrun -v -deffnm npt
```
Production MD
```
wget http://www.mdtutorials.com/gmx/lysozyme/Files/md.mdp
gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md.tpr
gmx mdrun -v -deffnm md
```
Analysis
```
gmx trjconv -s md_0_1.tpr -f md_0_1.xtc -o md_0_1_noPBC.xtc -pbc mol -center
"1 0"
```
