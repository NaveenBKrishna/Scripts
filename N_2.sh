!/bin/bash

grep "PMP" mod.pdb > PMP.pdb
grep "EST E" mod.pdb > EST.pdb
grep -v "PMP" mod.pdb > protein_EST
grep -v "EST" protein_EST > protein.pdb

gmx pdb2gmx -f protein.pdb -o conf.pdb -ignh -lys -renum 1 -merge no <<EOF
5
1
1
1
0
1
1
0
EOF
sed '21 a #include "../../../atomtype.itp"' ./topol.top >t0
sed '22 a #include "../../../PMP_new.itp"' ./t0 >t1
sed '23 a #include "../../../EST_new.itp"' ./t1 > t2
sed '/Protein_chain_B     1/ a \PMP       2' ./t2 > NNN
sed '/PMP       2/ a \EST       1' ./NNN > topol.top
grep -vwE "(TER|ENDMDL)" conf.pdb > frame_new.pdb
cat frame_new.pdb PMP.pdb  EST.pdb > a.pdb 
gmx editconf -f a.pdb -o latest.gro -d 1.0 -bt triclinic -c
gmx solvate -cp latest.gro -cs spc216.gro -p topol.top -o solv.pdb
gmx grompp -f ../../../em.mdp -c solv.pdb -p topol.top -o ions.tpr -maxwarn 1
gmx genion -s ions.tpr -o solv_ions.pdb -p topol.top -pname NA -neutral <<EOF
16
EOF
gmx grompp -f ../../../em_real.mdp -c solv_ions.pdb -p topol.top -o em.tpr -maxwarn 1
gmx mdrun -v -deffnm em -nt 8
gmx make_ndx -f em.gro -o index.ndx <<EOF
1|13|14
1|13
q
EOF
gmx grompp -f ../../../nvt.mdp -c em.gro -p topol.top -o nvt.tpr -n index.ndx 
gmx mdrun -v -deffnm nvt -nt 8
gmx grompp -f ../../../npt.mdp -c nvt.gro -t nvt.cpt -p topol.top -o npt.tpr -n index.ndx 
gmx mdrun -v -deffnm npt -nt 8
gmx grompp -f ../../../md.mdp -c npt.gro -t npt.cpt -p topol.top -o md.tpr -n index.ndx 
gmx mdrun -v -deffnm md -nt 8

#interaction_energy_calculation
python ../../../interaction_energy.py

#sh ../../../mutate.sh

rm PMP.pdb EST.pdb protein_EST t0 t1 t2 NNN *# a.pdb latest.gro solv.pdb solv_ions.pdb conf.pdb  *.trr  protein.pdb  *.mdp   step*.pdb *temp* *.edr   frame_new.pdb

