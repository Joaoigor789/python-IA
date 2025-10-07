import sys
import os
import subprocess
import time
from threading import Thread
import asyncio
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
import pyqtgraph as pg
import numpy as np
import edge_tts
from playsound import playsound

voz_ativa = True
escuta_ativa = True

knowledge = {
    "olá": "Olá! Como posso te ajudar?",
    "qual o seu nome": "Meu nome é Assistente Virtual.",
    "como você está": "Estou bem, obrigado por perguntar!",
    "quero saber o discord": "https://discord.gg/TJcBqdw9p2"
}

async def falar_async(texto):
    if not voz_ativa:
        return
    try:
        pasta_temp = "C:\\Temp"
        if not os.path.exists(pasta_temp):
            os.makedirs(pasta_temp)
        caminho_voz = os.path.join(pasta_temp, "voz_temp.mp3")
        if os.path.exists(caminho_voz):
            try:
                os.remove(caminho_voz)
            except:
                pass
        communicate = edge_tts.Communicate(texto, voice="pt-BR-AntonioNeural")
        await communicate.save(caminho_voz)
        playsound(caminho_voz)
    except Exception as e:
        print(f"[ERRO] Falha na fala: {e}")

def falar(texto):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(falar_async(texto))

def buscar_resposta(pergunta):
    return knowledge.get(pergunta.lower(), None)

def abrir_dayz():
    caminho_dayz = r"E:\SteamLibrary\steamapps\common\DayZ\DayZLauncher.exe"
    if os.path.exists(caminho_dayz):
        subprocess.Popen(caminho_dayz)
        painel.adicionar_mensagem("DayZ aberto!")
        falar("DayZ aberto! Divirta-se jogando!")
    else:
        painel.adicionar_mensagem("Erro: DayZ não encontrado")
        falar("Não consegui encontrar o DayZ.")

def apresentar_inforsis():
    painel.adicionar_mensagem("Apresentando InForsis")
    falar("Olá InForsis, prazer! Sou o assistente virtual do sistema.")

def diagnosticar_voz():
    status = f"Voz ativa: {voz_ativa}\nEscuta ativa: {escuta_ativa}"
    painel.adicionar_mensagem(status)
    falar("Sistema de voz operacional")

def pesquisar_internet(termo):
    if termo.strip() == "":
        painel.adicionar_mensagem("[Assistente]: Nenhum termo fornecido para pesquisa")
        falar("Nenhum termo fornecido para pesquisa")
        return
    url = f"https://www.google.com/search?q={termo}"
    webbrowser.open(url)
    painel.adicionar_mensagem(f"[Assistente]: Pesquisando por '{termo}' na internet...")
    falar(f"Pesquisando por {termo} na internet")

class PainelAssistente(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painel do Assistente Virtual")
        self.setGeometry(200, 50, 700, 700)
        layout = QVBoxLayout()

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        layout.addWidget(self.chat)

        hbox = QHBoxLayout()
        self.input_cmd = QLineEdit()
        self.input_cmd.setPlaceholderText("Digite um comando...")
        self.input_cmd.returnPressed.connect(self.enviar_comando)
        hbox.addWidget(self.input_cmd)
        btn_enviar = QPushButton("Enviar")
        btn_enviar.clicked.connect(self.enviar_comando)
        hbox.addWidget(btn_enviar)
        layout.addLayout(hbox)

        btn_voz = QPushButton("Ativar/Desativar Voz")
        btn_voz.clicked.connect(self.toggle_voz)
        btn_escuta = QPushButton("Ativar/Desativar Escuta")
        btn_escuta.clicked.connect(self.toggle_escuta)
        btn_dayz = QPushButton("Abrir DayZ")
        btn_dayz.clicked.connect(abrir_dayz)
        btn_diagnostico = QPushButton("Diagnóstico")
        btn_diagnostico.clicked.connect(diagnosticar_voz)
        btn_inforsis = QPushButton("Apresentar InForsis")
        btn_inforsis.clicked.connect(apresentar_inforsis)
        btn_pesquisar = QPushButton("Pesquisar na Internet")
        btn_pesquisar.clicked.connect(self.botao_pesquisar)
        btn_novo_cmd = QPushButton("Criar Novo Comando")
        btn_novo_cmd.clicked.connect(self.criar_comando)

        layout.addWidget(btn_voz)
        layout.addWidget(btn_escuta)
        layout.addWidget(btn_dayz)
        layout.addWidget(btn_diagnostico)
        layout.addWidget(btn_inforsis)
        layout.addWidget(btn_pesquisar)
        layout.addWidget(btn_novo_cmd)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground(None)
        self.data = np.random.normal(size=100)
        self.curve = self.graphWidget.plot(self.data, pen=pg.mkPen('#00ffea', width=2))
        layout.addWidget(self.graphWidget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(50)

        self.setLayout(layout)

    def adicionar_mensagem(self, texto):
        self.chat.append(texto)

    def enviar_comando(self):
        cmd = self.input_cmd.text().strip()
        if not cmd:
            return
        self.adicionar_mensagem(f"[Você]: {cmd}")
        self.input_cmd.clear()
        if cmd.lower() in knowledge:
            resposta = knowledge[cmd.lower()]
            self.adicionar_mensagem(f"[Assistente]: {resposta}")
            falar(resposta)
        elif "abrir dayz" in cmd.lower():
            abrir_dayz()
        elif "apresentar inforsis" in cmd.lower() or "diga oi ao inforsis" in cmd.lower():
            apresentar_inforsis()
        elif "diagnóstico" in cmd.lower():
            diagnosticar_voz()
        elif cmd.lower().startswith("pesquisar "):
            termo = cmd[10:]
            pesquisar_internet(termo)
        else:
            self.adicionar_mensagem("[Assistente]: Comando não reconhecido")
            falar("Comando não reconhecido")

    def botao_pesquisar(self):
        termo = self.input_cmd.text().strip()
        if termo:
            pesquisar_internet(termo)
            self.input_cmd.clear()

    def toggle_voz(self):
        global voz_ativa
        voz_ativa = not voz_ativa
        self.adicionar_mensagem(f"Voz {'ativada' if voz_ativa else 'desativada'}")
        falar(f"Voz {'ativada' if voz_ativa else 'desativada'}")

    def toggle_escuta(self):
        global escuta_ativa
        escuta_ativa = not escuta_ativa
        self.adicionar_mensagem(f"Escuta {'ativada' if escuta_ativa else 'desativada'}")
        falar(f"Escuta {'ativada' if escuta_ativa else 'desativada'}")

    def criar_comando(self):
        pergunta, ok1 = QInputDialog.getText(self, "Novo Comando", "Digite a frase do comando:")
        if ok1 and pergunta.strip():
            resposta, ok2 = QInputDialog.getText(self, "Nova Resposta", f"Digite a resposta para '{pergunta}':")
            if ok2 and resposta.strip():
                knowledge[pergunta.lower()] = resposta
                self.adicionar_mensagem(f"[Assistente]: Novo comando '{pergunta}' adicionado!")
                falar(f"Comando '{pergunta}' criado com sucesso!")

    def update_graph(self):
        self.data = np.roll(self.data, -1)
        self.data[-1] = np.random.normal()
        self.curve.setData(self.data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    painel = PainelAssistente()
    painel.show()
    sys.exit(app.exec_())
