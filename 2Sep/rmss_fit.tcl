mol new 8wjh_clean.pdb 
mol new model_4.pdb 
set sel0 [ atomselect 0 "name C and protein "]
set sel1 [ atomselect 1 "name C and protein and resid 1 to 305 312 to 327 334 to 517"]
$sel0 num
$sel1 num
set all [atomselect 1 all]
$all move [measure fit $sel1 $sel0] 
$all writepdb moved.pdb 
quit
