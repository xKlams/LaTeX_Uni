#!/bin/bash
date=$(date +%d/%m)
echo "inizio da $1 e finisco a $2"
for i in $(seq $1 1 $2)
do
	if [ "$i" -le "9" ]; then
		cp LaTeX_Lezioni/Lezione_0"$i"/main.pdf ./PDF_Lezioni/Lezione_0"$i".pdf
		echo "Sto copiando la lezione numero $i" 
	else
		cp LaTeX_Lezioni/Lezione_"$i"/main.pdf ./PDF_Lezioni/Lezione_"$i".pdf
		echo "Sto copiando la lezione numero $i" 
	fi
done
python3 merge_pdfs.py $1 $2
git add -A
git commit -m "Update $date"
git push
