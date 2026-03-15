<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=003366&height=200&section=header&text=🌍%20FlagsGame&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Teste%20seus%20conhecimentos%20sobre%20as%20bandeiras%20do%20mundo!&descAlignY=58&descSize=18" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Kivy](https://img.shields.io/badge/Kivy-Framework-brightgreen?style=for-the-badge&logo=kivy&logoColor=white)
![Plataforma](https://img.shields.io/badge/Plataforma-Desktop%20%7C%20Android-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Países](https://img.shields.io/badge/Países-40%2B-red?style=for-the-badge&logo=googlemaps&logoColor=white)

</div>

---

## 🗺️ Sobre o Projeto

**FlagsGame** é um jogo interativo de adivinhação de bandeiras desenvolvido em **Python com Kivy**, criado como projeto acadêmico. O jogador visualiza uma bandeira e deve identificar o país correto entre quatro opções — com três níveis de dificuldade e um sistema de dicas.

> 🎓 *Desenvolvido como trabalho escolar no IFCE — Instituto Federal do Ceará.*

---

## 🎮 Como Funciona

```
1. Escolha a dificuldade: Fácil, Médio ou Difícil
2. Uma bandeira aparece na tela
3. Selecione o país correto entre as 4 opções
4. Use a dica 💡 se travar (só vale uma por rodada!)
5. Responda 10 perguntas e veja sua pontuação final
```

---

## 🌐 Países Disponíveis

O jogo conta com **40+ países** distribuídos por todos os continentes:

| Continente | Exemplos |
|---|---|
| 🌎 América do Sul | Brasil, Argentina, Chile, Peru, Colômbia |
| 🌍 Europa | França, Alemanha, Itália, Portugal, Noruega |
| 🌏 Ásia | Japão, China, Coreia do Sul, Emirados Árabes |
| 🌍 África | Marrocos, Egito, Nigéria, África do Sul |
| 🌏 Oceania | Austrália, Nova Zelândia |
| 🌎 América do Norte | EUA, Canadá, México |

---

## ⚔️ Níveis de Dificuldade

| Nível | Países | Descrição |
|---|---|---|
| 🟢 **Fácil** | Brasil, França, EUA, Alemanha... | Bandeiras mundialmente reconhecidas |
| 🟡 **Médio** | México, Japão, Argentina, Austrália... | Países populares, mas menos óbvios |
| 🔴 **Difícil** | Chipre, Albânia, Omã, Iêmen... | Para os verdadeiros especialistas |

---

## 💡 Sistema de Dicas

Cada rodada permite **uma dica gratuita** sobre o país misterioso. As dicas incluem:

- 🏛️ Capital do país
- 🌍 Continente
- 🗣️ Idioma oficial
- 👥 População aproximada

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Uso |
|---|---|
| **Python 3.10+** | Linguagem principal |
| **Kivy** | Interface gráfica multiplataforma |
| **Buildozer** | Empacotamento para Android |
| **PyInstaller** | Empacotamento para Desktop |

</div>

---

## 🚀 Como Rodar

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/dhiogoFrutuoso/FlagsGame.git
cd FlagsGame

# Instale as dependências
pip install kivy

# Execute o jogo
python main.py
```

### Para Android (com Buildozer)

```bash
pip install buildozer
buildozer android debug deploy run
```

---

## 📁 Estrutura do Projeto

```
FlagsGame/
├── main.py              # Código principal do jogo
├── buildozer.spec       # Configuração do build Android
├── bandeiras/           # Imagens das bandeiras (PNG)
│   ├── brasil.png
│   ├── franca.png
│   └── ...
├── imagens/             # Assets de interface
│   └── dica.png
└── README.md
```

---

## 👨‍💻 Autor

<div align="center">

**Dhiogo Frutuoso**
Dev Full-Stack | Ciência da Computação — IFCE

[![GitHub](https://img.shields.io/badge/GitHub-dhiogoFrutuoso-181717?style=for-the-badge&logo=github)](https://github.com/dhiogoFrutuoso)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=003366&height=100&section=footer" />

*"A geografia do mundo, na palma da sua mão."* 🌍

</div>