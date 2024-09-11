mol new moved.pdb
package require Orient
namespace import Orient::orient
set sel [atomselect top "noh and protein"]
set all [as top all]
set c [vecinvert [measure center $all]]
$all moveby $c
set I [draw principalaxes $sel]
set A [orient $sel [lindex $I 2] {0 0 1}]
$all move $A
set I [draw principalaxes $sel]
set A [orient $sel [lindex $I 1] {0 1 0}]
$all move $A
set I [draw principalaxes $sel]
set A [orient $sel [lindex $I 1] {1 0 0}]
$all move $A
$all writepdb align_channel.pdb
$all set beta 0
$sel set beta 1
$all move [transaxis x 12]
$all move [transaxis y 14]
$all moveby [vecinvert [measure center $all]] 
$all writepdb prt_align.pdb
quit
