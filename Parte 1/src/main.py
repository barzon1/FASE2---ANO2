import csv

caminho_txt = r'C:\Users\lucas\Documents\FIAP ANO 2\FASE2 - ANO2\ATIVIDADE 1\Parte 1\dados\frases.txt'
caminho_csv = r'C:\Users\lucas\Documents\FIAP ANO 2\FASE2 - ANO2\ATIVIDADE 1\Parte 1\dados\mapa_conhecimento.csv'

with open(caminho_txt, 'r', encoding='utf-8') as arquivo_txt:
    frases = arquivo_txt.readlines()
with open(caminho_csv, 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    mapa = list(leitor)

for relato in frases:
    relato_minusculo = relato.lower()    
    if relato.strip() == "":
        continue    
    
    diagnostico_encontrado = False

    for causa in mapa:
        gatilho_1 = causa[0].lower().strip()
        gatilho_2 = causa[1].lower().strip()
        causa_raiz = causa[2].lower().strip()

        if (gatilho_1 in relato_minusculo) and (gatilho_2 in relato_minusculo):
            print("--- NOVO CHAMADO ANALISADO ---")
            print(f"Relato do cliente: {relato.strip()}")
            print(f"Diagnóstico Automático: {causa_raiz}")
            print("------------------------------\n")
            # Levanta a bandeira dizendo que achamos o problema
            diagnostico_encontrado = True
            
            # O comando 'break' interrompe o loop interno. Se já achamos a doença, 
            # não precisamos testar o resto do CSV para esta mesma frase.
            break
    if diagnostico_encontrado == False:
        print("--- NOVO PACIENTE ANALISADO ---")
        print(f"Relato: {relato.strip()}")
        print("Diagnóstico Automático: Nenhum padrão mapeado foi encontrado.")
        print("------------------------------\n")    