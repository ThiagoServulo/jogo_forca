from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets


class Ui_tela_resultado(object):
    def setupUi(self, tela_resultado):
        if not tela_resultado.objectName():
            tela_resultado.setObjectName(u"tela_resultado")
        tela_resultado.resize(326, 240)
        tela_resultado.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(tela_resultado)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_resultado = QLabel(self.centralwidget)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setGeometry(QRect(40, 20, 251, 51))
        font = QFont()
        font.setPointSize(25)
        self.label_resultado.setFont(font)
        self.label_resultado.setAlignment(Qt.AlignCenter)
        self.label_palavra = QLabel(self.centralwidget)
        self.label_palavra.setObjectName(u"label_palavra")
        self.label_palavra.setGeometry(QRect(40, 100, 231, 31))
        self.label_palavra.setAlignment(Qt.AlignCenter)
        font1 = QFont()
        font1.setPointSize(12)
        self.label_palavra.setFont(font1)
        self.botao_novo_jogo = QPushButton(self.centralwidget)
        self.botao_novo_jogo.setObjectName(u"botao_novo_jogo")
        self.botao_novo_jogo.setGeometry(QRect(170, 160, 111, 41))
        self.botao_novo_jogo.setFont(font1)
        self.botao_sair = QPushButton(self.centralwidget)
        self.botao_sair.setObjectName(u"botao_sair")
        self.botao_sair.setGeometry(QRect(40, 160, 111, 41))
        self.botao_sair.setFont(font1)
        tela_resultado.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_resultado)

        QMetaObject.connectSlotsByName(tela_resultado)
    # setupUi

    def retranslateUi(self, tela_resultado):
        tela_resultado.setWindowTitle(QCoreApplication.translate("tela_resultado", u"Resultado", None))
        self.label_resultado.setText(QCoreApplication.translate("tela_resultado", u"", None))
        self.label_palavra.setText(QCoreApplication.translate("tela_resultado", u"", None))
        self.botao_novo_jogo.setText(QCoreApplication.translate("tela_resultado", u"Novo Jogo", None))
        self.botao_sair.setText(QCoreApplication.translate("tela_resultado", u"Sair", None))
    # retranslateUi


class CriarTelaResultado(QtWidgets.QMainWindow, Ui_tela_resultado):
    def __init__(self):
        super(CriarTelaResultado, self).__init__()
        self.setupUi(self)
