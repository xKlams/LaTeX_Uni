import os
import sys

def combina_lezioni(corsi):
    """
    Combina i file main.tex delle lezioni di diversi corsi universitari in un unico file.
    La compilazione LaTeX è stata rimossa.

    Args:
        corsi: Una lista di stringhe, ognuna rappresentante il nome di un corso universitario.
    """

    for corso in corsi:
        print(f"Elaborazione del corso: {corso}")
        corso_dir = corso
        latex_lezioni_dir = os.path.join(corso_dir, "LaTeX_Lezioni")

        if not os.path.exists(latex_lezioni_dir):
            print(f"  Directory 'LaTeX_Lezioni' non trovata per il corso '{corso}'. Salto questo corso.")
            continue

        pdf_completo_dir = os.path.join(latex_lezioni_dir, "pdf_completo") # Define pdf_completo directory path
        if not os.path.exists(pdf_completo_dir):
            print(f"  Directory 'pdf_completo' non trovata in '{latex_lezioni_dir}'. Creazione della directory...")
            try:
                os.makedirs(pdf_completo_dir, exist_ok=True) # Create directory if it doesn't exist, exist_ok=True prevents error if it exists
                print(f"  Directory 'pdf_completo' creata con successo in '{latex_lezioni_dir}'.")
            except OSError as e:
                print(f"  Errore durante la creazione della directory 'pdf_completo' in '{latex_lezioni_dir}': {e}. Salto questo corso.")
                continue # Skip to the next course if directory creation fails

        all_lectures_file = os.path.join(pdf_completo_dir, "all_lectures.tex") # Corrected path to pdf_completo
        combined_content = ""

        lezione_numero = 1
        while True:
            lezione_dir_nome = f"Lezione_{lezione_numero:02d}" # Formatta il numero della lezione con due cifre (es. 01, 02, ...)
            lezione_dir_path = os.path.join(latex_lezioni_dir, lezione_dir_nome)
            main_tex_path = os.path.join(lezione_dir_path, "main.tex")

            if not os.path.exists(lezione_dir_path) or not os.path.isdir(lezione_dir_path):
                print(f"  Directory '{lezione_dir_nome}' non trovata. Fine lezioni per questo corso.")
                break  # Esci dal loop se la directory della lezione non esiste

            if not os.path.exists(main_tex_path) or not os.path.isfile(main_tex_path):
                print(f"  File 'main.tex' non trovato in '{lezione_dir_nome}'. Fine lezioni per questo corso.")
                break  # Esci dal loop se main.tex non esiste

            print(f"  Trovato file: {main_tex_path}")

            try:
                with open(main_tex_path, 'r', encoding='utf-8') as f:
                    tex_content = f.read()

                start_document = tex_content.find(r'\begin{document}')
                end_document = tex_content.find(r'\end{document}')

                if start_document != -1 and end_document != -1:
                    lezione_content = tex_content[start_document + len(r'\begin{document}'):end_document]
                    combined_content += lezione_content.strip() + "\n\n% -------------------- Fine Lezione {} --------------------\n\n".format(lezione_numero)
                else:
                    print(f"  Marcatori '\\begin{{document}}' o '\\end{{document}}' non trovati in {main_tex_path}. Il contenuto della lezione potrebbe non essere estratto correttamente.")
                    combined_content += tex_content  # Includi tutto il contenuto se i marcatori non sono trovati, per evitare di perdere dati

            except Exception as e:
                print(f"  Errore durante la lettura del file {main_tex_path}: {e}")

            lezione_numero += 1

        if combined_content:
            try:
                with open(all_lectures_file, 'w', encoding='utf-8') as outfile:
                    outfile.write(r"\documentclass{article}" + "\n") # Aggiunge un preambolo minimo
                    outfile.write(r"\usepackage[utf8]{inputenc}" + "\n") # Gestione caratteri speciali
                    outfile.write(r"\usepackage{amsmath, amssymb}" + "\n") # Pacchetti matematici comuni
                    outfile.write(r"\title{Compendio Lezioni del Corso: " + corso + "}" + "\n") # Titolo del documento
                    outfile.write(r"\date{\today}" + "\n") # Data odierna
                    outfile.write(r"\author{Federico De Sisti}" + "\n")
                    outfile.write(r"\include{../../../setup.tex}" + "\n")
                    outfile.write(r"\begin{document}" + "\n") # Inizio del documento
                    outfile.write(r"\maketitle" + "\n") # Stampa il titolo
                    outfile.write(combined_content)
                    outfile.write(r"\end{document}" + "\n") # Fine del documento
                print(f"  File '{all_lectures_file}' creato con successo in '{latex_lezioni_dir}'.")

                # Rimossa la sezione di compilazione LaTeX
                # print(f"  Compilazione del file '{all_lectures_file}'...")
                # try:
                #     process = subprocess.run(['pdflatex', all_lectures_file], cwd=pdf_completo_dir, capture_output=True, text=True)
                #     if process.returncode == 0:
                #         print(f"  File PDF compilato con successo in '{pdf_completo_dir}'.")
                #     else:
                #         print(f"  Errore durante la compilazione del file '{all_lectures_file}'.")
                #         print("  Output di pdflatex (stderr):\n", process.stderr) # Mostra l'errore di LaTeX
                # except FileNotFoundError:
                #     print("  Errore: 'pdflatex' non trovato. Assicurati che LaTeX sia installato e nel PATH.")
                # except Exception as e:
                #     print(f"  Errore durante l'esecuzione di pdflatex: {e}")


            except Exception as e:
                print(f"  Errore durante la scrittura del file '{all_lectures_file}': {e}")
        else:
            print(f"  Nessun contenuto di lezione trovato per il corso '{corso}'. File 'all_lectures.tex' non creato.")
        print("-" * 30)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        corsi = [corso.strip() for corso in sys.argv[1:]] # Usa gli argomenti dalla linea di comando, rimuovi spazi bianchi
    else:
        corsi_input = input("Inserisci i nomi dei corsi universitari separati da uno spazio: ").split(' ')
        corsi = [corso.strip() for corso in corsi_input] # Rimuovi spazi bianchi superflui
        if not corsi or not corsi[0]: # Check if input is empty
            print("Nessun corso inserito. Uscita.")
            sys.exit()

    combina_lezioni(corsi)
    print("Processo completato.")
