#!/bin/bash
date=$(date +%d/%m)
echo "inizio da $1 e finisco a $2"
for i in $(seq $1 1 $2)
do
	if [ "$i" -le "9" ]; then
		latexmk -pdf LaTeX_Lezioni/0"$i"_lezione/main.tex
		latexmk -c
		cp LaTeX_Lezioni/0"$i"_lezione/main.pdf ./PDF_Lezioni/0"$i"_Lezione.pdf
		echo "Sto copiando la lezione numero $i" 
	else
		latexmk -pdf LaTeX_Lezioni/"$i"_lezione/main.tex
		latexmk -c
		cp LaTeX_Lezioni/"$i"_lezione/main.pdf ./PDF_Lezioni/"$i"_Lezione.pdf
		echo "Sto copiando la lezione numero $i" 
	fi
done
python3 merge_pdfs.py $1 $2
git add -A
git commit -m "Update $date"
git push
