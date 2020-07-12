#!/bin/bash
#read a file with

input="/home/projects/qz1903/TAIC/Umbella_sampling_windows_US4/ES3/screening/mutation_list.txt"
while read -r line
do

cat frame*/$line/energy_2.txt > energy2_all.txt

grep Coul-SR:Protein-EST energy2_all.txt > Coul_Protein-EST
grep LJ-SR:Protein-EST energy2_all.txt > LJ_Protein-EST 

awk -v line=2 'BEGIN{s=0;}{s=s+$line;}END{print s/NR;}' Coul_Protein-EST > col_avg_2.txt
awk -v line=2 '{delta = $line - avg; avg += delta / NR; mean2 += delta * ($line - avg); } END { print sqrt(mean2 / (NR-1)); }' Coul_Protein-EST > col_std_2.txt

awk -v line=2 'BEGIN{s=0;}{s=s+$line;}END{print s/NR;}' LJ_Protein-EST > lj_avg_2.txt
awk -v line=2 '{delta = $line - avg; avg += delta / NR; mean2 += delta * ($line - avg); } END { print sqrt(mean2 / (NR-1)); }' LJ_Protein-EST > lj_std_2.txt

echo $line > name
echo "col" > col.txt
paste col.txt col_avg_2.txt col_std_2.txt > W1_WT_col.txt

echo "lj" > lj.txt
paste lj.txt lj_avg_2.txt lj_std_2.txt > W1_WT_lj.txt

echo "Protein-EST" > Protein-EST
paste  Protein-EST name W1_WT_col.txt  W1_WT_lj.txt > 1

rm Coul_Protein-EST LJ_Protein-EST col_avg_2.txt col_std_2.txt lj_avg_2.txt  lj_std_2.txt 
rm W1_WT_col.txt  W1_WT_lj.txt col.txt lj.txt energy2_all.txt

#......................energy 2................
cat frame*/$line/energy.txt > energy2_all.txt

grep Coul-SR:Protein_PMP-EST energy2_all.txt > Coul_Protein-EST_2
grep LJ-SR:Protein_PMP-EST energy2_all.txt > LJ_Protein-EST_2

awk -v line=2 'BEGIN{s=0;}{s=s+$line;}END{print s/NR;}' Coul_Protein-EST_2 > col_avg_2.txt
awk -v line=2 '{delta = $line - avg; avg += delta / NR; mean2 += delta * ($line - avg); } END { print sqrt(mean2 / (NR-1)); }' Coul_Protein-EST_2 > col_std_2.txt

awk -v line=2 'BEGIN{s=0;}{s=s+$line;}END{print s/NR;}' LJ_Protein-EST_2 > lj_avg_2.txt
awk -v line=2 '{delta = $line - avg; avg += delta / NR; mean2 += delta * ($line - avg); } END { print sqrt(mean2 / (NR-1)); }' LJ_Protein-EST_2 > lj_std_2.txt

echo "col" > col.txt
paste col.txt col_avg_2.txt col_std_2.txt > W1_WT_col2.txt

echo "lj" > lj.txt
paste lj.txt lj_avg_2.txt lj_std_2.txt > W1_WT_lj2.txt

echo "Protein_PMP-EST" > Protein_PMP-EST
paste Protein_PMP-EST name W1_WT_col2.txt  W1_WT_lj2.txt > 2

cat 1 2 > $line

rm Coul_Protein-EST_2 LJ_Protein-EST_2 col_avg_2.txt col_std_2.txt lj_avg_2.txt  lj_std_2.txt
rm W1_WT_col2.txt  W1_WT_lj2.txt col.txt lj.txt energy2_all.txt name 1 2 

done < "$input"

cat *Asp_*Asp > last_Mut.txt

grep "Protein-EST" last_Mut.txt > Asp_Protein-EST
grep "Protein_PMP-EST" last_Mut.txt > Asp_Potein_PMP-EST

rm *Asp*Asp Protein-EST Protein_PMP-EST
