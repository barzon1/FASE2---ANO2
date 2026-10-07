# CardioIA - Sistema de Triagem Cardiológica Automática

Este repositório contém a entrega da **Fase 2** do projeto **CardioIA**, desenvolvido para a FIAP. O objetivo principal é construir algoritmos capazes de ler relatos de pacientes e automatizar a triagem clínica, simulando o raciocínio de sistemas médicos reais.

O projeto foi dividido em duas abordagens de arquitetura de software: um **Motor Baseado em Regras** (Determinístico) e um **Classificador de Inteligência Artificial** (Machine Learning).

---

## 📺 Apresentação em Vídeo
> **Assista aqui à demonstração completa do projeto:**
> [[🔗 https://youtu.be/lNxuFrSl8Zc ]]

---

## 📁 Estrutura do Repositório

```text
📦 CardioIA-Triagem-Fase2
├── 📁 Parte 1/
│   ├── 📁 dados/
│   │   ├── frases.txt (10 relatos simulados de pacientes)
│   │   └── mapa_conhecimento.csv (Ontologia clínica com sintomas e doenças)
│   └── 📁 src/
│       └── main.py (Script de inferência lógica)
│
├── 📁 Parte 2/
│   ├── base_simulada.csv (50 relatos classificados por nível de risco)
│   └── decision_tree.ipynb (Notebook com a análise exploratória e treinamento do modelo)
│
└── README.md

🛠️ Parte 1: Motor de Inferência (Sistema Baseado em Regras)
Na primeira fase do projeto, construímos um sistema determinístico clássico. O algoritmo funciona como uma linha de montagem de processamento de texto.

Como funciona:

O script main.py faz a ingestão das narrativas informais dos pacientes a partir do frases.txt.

O sistema varre uma matriz estruturada (mapa_conhecimento.csv) contendo regras clínicas.

Através de um laço de repetição aninhado e Lógica Booleana (AND), o código verifica se o "Sintoma 1" E o "Sintoma 2" estão presentes na mesma frase.

Quando a condição é atendida, o sistema imprime automaticamente a doença associada no terminal.

Para executar localmente:
Navegue até a pasta src e execute o script no terminal:
python main.py

🧠 Parte 2: Classificador de Texto (Machine Learning)
Enquanto a Parte 1 utiliza regras fixas, a Parte 2 avança para o aprendizado de máquina supervisionado, onde a IA aprende a classificar a gravidade clínica de novos pacientes com base em exemplos passados.

O Fluxo de Processamento:

Ingestão: Lemos uma base maior e mais complexa (base_simulada.csv), contendo 50 relatos rotulados como Alto Risco, Médio Risco e Baixo Risco.

Tradução Matemática (TF-IDF): Como máquinas não leem português, aplicamos a vetorização TfidfVectorizer (Term Frequency - Inverse Document Frequency). Esse algoritmo mapeia a relevância de cada palavra, atribuindo pesos maiores para termos clínicos específicos (ex: "suor", "irradia") e pesos menores para palavras comuns.

O Cérebro (Decision Tree): Utilizamos o DecisionTreeClassifier da biblioteca scikit-learn. Treinamos a IA com 80% dos dados, reservando 20% para o teste cego.

Avaliação e Vieses do Modelo:
Ao analisar a Matriz de Confusão gerada no Notebook, identificamos um padrão interessante: o modelo desenvolveu um viés conservador. Ele teve facilidade em classificar os extremos (alto e baixo risco), mas tendeu a classificar os pacientes de "Médio Risco" como sendo de "Alto Risco". Em um contexto de triagem hospitalar (como o Protocolo de Manchester), este é um comportamento defensivo aceitável, pois o algoritmo prefere errar por excesso de zelo a enviar um paciente potencialmente grave para a sala de espera comum.

👨‍💻 Autor
Lucas Rodrigues Barzon - RM567914

FIAP - Ano 2
