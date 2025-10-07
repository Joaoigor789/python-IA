# 🤖 Assistente Virtual com Interface Gráfica em Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/Framework-PyQt5-green?logo=qt)](https://riverbankcomputing.com/software/pyqt/)
[![Edge TTS](https://img.shields.io/badge/Voice-EdgeTTS-purple)](https://pypi.org/project/edge-tts/)
[![License](https://img.shields.io/badge/License-CC--BY--NC--ND%204.0-orange)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)]()
[![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux-lightgrey)]()

---

## 📘 Sobre o Projeto

Um **assistente virtual inteligente** desenvolvido em **Python** com interface gráfica feita em **PyQt5**, integração com **Edge TTS (Text-To-Speech)** para voz natural, **gráficos dinâmicos em tempo real**, e **comandos personalizáveis**.

O objetivo é criar uma experiência de interação visual e auditiva com o usuário, unindo **automação**, **inteligência artificial leve** e **design intuitivo**.

---

## 🧠 Funcionalidades Principais

### 💬 Interação e Respostas
O assistente responde a perguntas pré-definidas, exibindo mensagens no chat e falando em voz natural.

### 🗣️ Voz Natural (Edge TTS)
- Utiliza a voz neural **`pt-BR-AntonioNeural`** da Microsoft.
- O áudio é salvo temporariamente em `C:\Temp` e reproduzido com **playsound**.

### 🌐 Pesquisa na Internet
- Use o comando:
  ```bash
  pesquisar <termo>

🎮 Abertura de Programas

Possui um comando dedicado para abrir o DayZ Launcher diretamente:

caminho_dayz = r"E:\SteamLibrary\steamapps\common\DayZ\DayZLauncher.exe"

⚙️ Diagnóstico de Voz

Exibe o status atual da voz e da escuta (ativa ou desativada).

🧩 Criação de Comandos Personalizados

O usuário pode criar novos comandos dinamicamente pela interface.

Exemplo:

Pergunta: qual seu criador?

Resposta: Fui desenvolvido por João Igor.

📈 Gráfico Dinâmico

Mostra um gráfico em tempo real utilizando pyqtgraph, simulando atividade do assistente.

🖥️ Interface Visual

A interface contém:

💬 Chat interativo entre usuário e assistente

⌨️ Campo de entrada de texto

🎛️ Botões de controle:

Ativar/Desativar Voz

Ativar/Desativar Escuta

Abrir DayZ

Diagnóstico

Apresentar InForsis

Pesquisar na Internet

Criar Novo Comando

A atualização do gráfico ocorre em tempo real, proporcionando um toque visual moderno.

⚙️ Estrutura do Código

O projeto utiliza as seguintes bibliotecas:

Biblioteca	Função
PyQt5	Interface gráfica
pyqtgraph	Gráficos dinâmicos
edge_tts	Conversão de texto em voz neural
playsound	Reprodução de áudio
numpy	Geração de dados aleatórios para o gráfico
Classe Principal: PainelAssistente(QWidget)

Responsável por:

Gerenciar a interface visual

Executar comandos e respostas

Criar novos comandos

Atualizar o gráfico dinâmico

Controlar voz e escuta

Funções Auxiliares
Função	Descrição
falar(texto)	Gera e reproduz fala com Edge TTS
abrir_dayz()	Abre o DayZ Launcher
pesquisar_internet(termo)	Abre o navegador com busca no Google
diagnosticar_voz()	Exibe o status do sistema de voz e escuta
🧠 Base de Conhecimento (Knowledge)

O dicionário inicial inclui respostas padrão:

knowledge = {
    "olá": "Olá! Como posso te ajudar?",
    "qual o seu nome": "Meu nome é Assistente Virtual.",
    "como você está": "Estou bem, obrigado por perguntar!",
    "quero saber o discord": "https://discord.gg/TJcBqdw9p2"
}


Você pode adicionar novos comandos diretamente pelo botão “Criar Novo Comando”.

🚀 Execução
🔧 Pré-requisitos

Instale as dependências:

pip install PyQt5 pyqtgraph edge-tts playsound numpy

▶️ Como Executar

Execute o script principal:

python assistente_virtual.py


A interface gráfica será exibida automaticamente.

📂 Estrutura de Pastas
📁 AssistenteVirtual
 ├── assistente_virtual.py
 ├── README.md
 └── C:\Temp\voz_temp.mp3  (gerado automaticamente)

🧑‍💻 Autor

João Igor Rodrigues Pereira da Silva
👨‍💻 Desenvolvedor e criador do projeto
🏢 Farmacia AppTech Technology
📅 2025

🔗 LinkedIn
 (adicione seu perfil aqui)
📧 (adicione seu e-mail profissional, opcional)

🧾 Licença

Licenciado sob Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

Uso permitido apenas para fins educacionais e não comerciais.

✨ Frase Final

“Transformar linhas de código em interação humana é o verdadeiro poder da programação.”

🌟 Se este projeto te inspirou

Dê uma ⭐ no repositório!

Compartilhe sua versão personalizada.

Publique sua experiência no LinkedIn com a hashtag #AssistenteVirtualPython.
