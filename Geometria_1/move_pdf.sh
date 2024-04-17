#!/bin/bash
date=$(date '+%Y-%m-%d')
echo "inizio da $1 e finisco a $2"
for i in $(seq $1 1 $2)
do
	if [ "$i" -le "9" ]; then
		cp 0"$i"_lezione/main.pdf ./PDF_Lezioni/0"$i"_Lezione.pdf
		echo "Sto copiando la lezione numero $i" 
	else
		cp "$i"_lezione/main.pdf ./PDF_Lezioni/"$i"_Lezione.pdf
		echo "Sto copiando la lezione numero $i" 
	fi
done
python3 merge_pdfs.py $1 $2
git add -A
git commit -m "update $date fino a lezione $2"
git push
