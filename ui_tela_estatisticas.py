from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import ast

class Ui_tela_estatisticas(object):

    dict_resultados = {}

    def setupUi(self, tela_estatisticas):
        if not tela_estatisticas.objectName():
            tela_estatisticas.setObjectName(u"tela_estatisticas")
        icon = QIcon()
        icon.addFile(u"icone_forca.png", QSize(), QIcon.Normal, QIcon.Off)
        tela_estatisticas.setWindowIcon(icon)
        tela_estatisticas.resize(351, 252)
        tela_estatisticas.setMinimumSize(QSize(351, 252))
        tela_estatisticas.setMaximumSize(QSize(351, 252))
        self.centralwidget = QWidget(tela_estatisticas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 271, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_vitorias = QLabel(self.centralwidget)
        self.label_vitorias.setObjectName(u"label_vitorias")
        self.label_vitorias.setGeometry(QRect(70, 80, 171, 21))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.label_vitorias.setFont(font1)
        self.label_derrotas = QLabel(self.centralwidget)
        self.label_derrotas.setObjectName(u"label_derrotas")
        self.label_derrotas.setGeometry(QRect(70, 110, 171, 21))
        self.label_derrotas.setFont(font1)
        self.label_desistencias = QLabel(self.centralwidget)
        self.label_desistencias.setObjectName(u"label_desistencias")
        self.label_desistencias.setGeometry(QRect(70, 140, 171, 21))
        self.label_desistencias.setFont(font1)
        self.botao_zerar_estatisticas = QPushButton(self.centralwidget)
        self.botao_zerar_estatisticas.setObjectName(u"botao_zerar_estatisticas")
        self.botao_zerar_estatisticas.setGeometry(QRect(40, 190, 131, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.botao_zerar_estatisticas.setFont(font2)
        self.botao_sair = QPushButton(self.centralwidget)
        self.botao_sair.setObjectName(u"botao_sair")
        self.botao_sair.setGeometry(QRect(190, 190, 131, 41))
        self.botao_sair.setFont(font2)
        tela_estatisticas.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_estatisticas)

        QMetaObject.connectSlotsByName(tela_estatisticas)
    # setupUi

    def retranslateUi(self, tela_estatisticas):
        tela_estatisticas.setWindowTitle(QCoreApplication.translate("tela_estatisticas", u"Estatísticas", None))
        self.label.setText(QCoreApplication.translate("tela_estatisticas", u"Estatísticas do Jogo", None))
        self.label_vitorias.setText(QCoreApplication.translate("tela_estatisticas", u"Vitórias:", None))
        self.label_derrotas.setText(QCoreApplication.translate("tela_estatisticas", u"Derrotas", None))
        self.label_desistencias.setText(QCoreApplication.translate("tela_estatisticas", u"Desistências:", None))
        self.botao_zerar_estatisticas.setText(QCoreApplication.translate("tela_estatisticas", u"Zerar Estatíticas", None))
        self.botao_sair.setText(QCoreApplication.translate("tela_estatisticas", u"Sair", None))
    # retranslateUi

    def carregar_tela_resultados(self):
        self.label_vitorias.setText(f"Vitórias: {Ui_tela_estatisticas.dict_resultados['vitorias']}")
        self.label_derrotas.setText(f"Derrotas: {Ui_tela_estatisticas.dict_resultados['derrotas']}")
        self.label_desistencias.setText(f"Desistências: {Ui_tela_estatisticas.dict_resultados['desistencias']}")
        self.show()
    # carregar_tela_resultados

    def ler_arquivo_estatisticas(self):
        try:
            with open('resultados.txt', 'r') as arquivo:
                dado = arquivo.read()
                Ui_tela_estatisticas.dict_resultados = ast.literal_eval(dado)
        except:
            open('resultados.txt', 'w').close()
            Ui_tela_estatisticas.dict_resultados = {'vitorias': 0, 'derrotas': 0, 'desistencias': 0}
    # ler_arquivo_estatisticas

    def escrever_arquivo_estatisticas(self):
        try:
            with open('resultados.txt', 'w') as arquivo:
                arquivo.write(str(Ui_tela_estatisticas.dict_resultados))
        except FileNotFoundError:
            print('Erro ao salvar dados no arquivo')
    # escrever_arquivo_estatisticas

    def zerar_estatisticas(self):
        try:
            with open('resultados.txt', 'w') as arquivo:
                Ui_tela_estatisticas.dict_resultados = {'vitorias': 0, 'derrotas': 0, 'desistencias': 0}
                arquivo.write(str(Ui_tela_estatisticas.dict_resultados))
                self.label_vitorias.setText(f"Vitórias: {Ui_tela_estatisticas.dict_resultados['vitorias']}")
                self.label_derrotas.setText(f"Derrotas: {Ui_tela_estatisticas.dict_resultados['derrotas']}")
                self.label_desistencias.setText(f"Desistências: {Ui_tela_estatisticas.dict_resultados['desistencias']}")
        except FileNotFoundError:
            print('Erro ao zerar dados no arquivo')
    # zerar_estatisticas


class CriarTelaEstatisticas(QtWidgets.QMainWindow, Ui_tela_estatisticas):
    def __init__(self):
        super(CriarTelaEstatisticas, self).__init__()
        self.setupUi(self)
