# 28Aug
Initialize gromacs

source /usr/local/gromacs/bin/GMXRC
# Building Biphasic Systems

## Step 1: Prepare the hydropobic layer
### Method 1: Random insertion
```bash
gmx insert-molecules -ci chx.gro -nmol 1200 -box 5 5 5 -o chx_box.gro
```
chx.gro is the coordinate file for cycloexane.


### Method 2: Specific insertion
```bash
gmx genconf -f chx.gro -nbox 8 8 8 -o chx_box.gro
```

## Step 2: Add Water to Construct
```bash
gmx editconf -f chx_box.gro -o chx_newbox.gro -box 4.30795 4.30795 8.6159 -center 2.153975 2.153975 2.153975
```

```bash
gmx solvate -cp chx_newbox.gro -cs spc216.gro -p chx.top -o chx_solv.gro
```