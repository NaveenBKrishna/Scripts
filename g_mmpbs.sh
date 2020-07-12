#!/bin/bash

export APBS=/usr/bin/apbs
export OMP_NUM_THREADS=10



source /usr/local/gromacs/2019.1/bin/GMXRC

gmx make_ndx -f em.tpr -o index.ndx <<EOF
1|13|14
1|13
q
EOF

gmx trjconv -f md.xtc -s em.tpr -n index.ndx -o md_center.xtc -pbc nojump -ur compact -center -boxcenter tric  <<EOF
24
24
EOF

../../../g_mmpbsa -f md_center.xtc -s new.tpr -n index.ndx -i ../../../pbsa.mdp -pdie 2 -pbsa -decomp  -mm energy_MM.xvg -pol polar.xvg -apol apolar.xvg  << EOF
25
14
EOF
python ../../../MmPbSaStat.py -m energy_MM.xvg -p polar.xvg -a apolar.xvg -of full_energy.dat -os summary_energy.dat

