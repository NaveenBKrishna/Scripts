#!/bin/bash
#source /usr/local/gromacs/2019.1/bin/GMXRC
#move pdb files in corresponding folder with frame number

#input="/home/projects/qz1903/TAIC/Umbella_sampling_windows_US4/ES3/screening/list_pdb"

#while read -r line
#cd /home/projects/qz1903/TAIC/Umbella_sampling_windows_US4/ES3/screening/
#o
#kdir $line
#cp $line.pdb $line/. 
#cp pymol_mutate_V1.py pymol_mutate_V2.py mutated_list.txt mutation_list.txt Create_mutation.py $line/.   
#cp ter_create1.sh $line/.
#cd $line

#sh ter_create1.sh
#rm $line.pdb
#python Create_mutation.py 

#input2="/home/projects/qz1903/TAIC/Umbella_sampling_windows_US4/ES3/screening/mutated_list2.txt"
#while read -r line1
#do
#cd $line1
#cp ../../../ter .
sed -n '/A 429/,/OC2 ASP A 856/p' *.pdb > 1.txt
sed -i 's/ A / B /g' 1.txt 
sed -n '/A   1/,/OC2 ASP A 428/p' *.pdb > chainA.txt
sed -n '/P1  PMP C 901/,/H93 EST E 903/p' *.pdb > other.txt
cat chainA.txt ter 1.txt ter other.txt > mod.pdb
rm 1.txt chainA.txt other.txt ter
sh ../../../N_2.sh
#cd ..
#done < "$input2"

#cd ..
#done < "$input"
