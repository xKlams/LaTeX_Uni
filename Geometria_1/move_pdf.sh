#!/bin/bash
echo "inizio da $1 e finisco a $2"
for i in $(seq $1 1 $2)
do
	cp "$i"_lezione/main.pdf ./PDF_Lezioni/Lezione_$i.pdf
	echo "Sto copiando la lezione numero $i" 
done
