from PySide2.QtCore import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from palavras import sortear_palavra
from ui_tela_resultado import CriarTelaResultado
from unicodedata import normalize


class Ui_MainWindow(object):

    chances_jogador = 6
    letras_advinhadas = 0

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 577)
        MainWindow.setMaximumSize(QSize(800, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.menu_novo_jogo = QAction(MainWindow)
        self.menu_novo_jogo.setObjectName(u"menu_novo_jogo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tela_resultado = CriarTelaResultado()
        self.forca = QLabel(self.centralwidget)
        self.forca.setObjectName(u"forca")
        self.forca.setGeometry(QRect(80, 80, 271, 341))
        self.forca.setPixmap(QPixmap(u"forca.jpg"))
        self.cabeca = QLabel(self.centralwidget)
        self.cabeca.setObjectName(u"cabeca")
        self.cabeca.setGeometry(QRect(250, 140, 71, 71))
        self.cabeca.setPixmap(QPixmap(u"cabeca.jpg"))
        self.corpo = QLabel(self.centralwidget)
        self.corpo.setObjectName(u"corpo")
        self.corpo.setGeometry(QRect(280, 210, 8, 141))
        self.corpo.setPixmap(QPixmap(u"corpo.jpg"))
        self.braco_esquerdo = QLabel(self.centralwidget)
        self.braco_esquerdo.setObjectName(u"braco_esquerdo")
        self.braco_esquerdo.setGeometry(QRect(286, 220, 47, 81))
        self.braco_esquerdo.setPixmap(QPixmap(u"braco_esquerdo.jpg"))
        self.perna_esquerda = QLabel(self.centralwidget)
        self.perna_esquerda.setObjectName(u"perna_esquerda")
        self.perna_esquerda.setGeometry(QRect(286, 323, 47, 81))
        self.perna_esquerda.setPixmap(QPixmap(u"braco_esquerdo.jpg"))
        self.braco_direito = QLabel(self.centralwidget)
        self.braco_direito.setObjectName(u"braco_direito")
        self.braco_direito.setGeometry(QRect(234, 233, 47, 61))
        self.braco_direito.setPixmap(QPixmap(u"braco_direito.jpg"))
        self.perna_direita = QLabel(self.centralwidget)
        self.perna_direita.setObjectName(u"perna_direita")
        self.perna_direita.setGeometry(QRect(234, 336, 47, 61))
        self.perna_direita.setPixmap(QPixmap(u"perna_direita.jpg"))
        self.palavra_group_box = QGroupBox(self.centralwidget)
        self.palavra_group_box.setObjectName(u"palavra_group_box")
        self.palavra_group_box.setGeometry(QRect(20, 460, 421, 80))
        font = QFont()
        font.setPointSize(12)
        self.palavra_group_box.setFont(font)
        self.letra_13 = QLabel(self.palavra_group_box)
        self.letra_13.setObjectName(u"letra_13")
        self.letra_13.setGeometry(QRect(380, 20, 21, 31))
        font1 = QFont()
        font1.setPointSize(22)
        self.letra_13.setFont(font1)
        self.letra_13.setAlignment(Qt.AlignCenter)
        self.traco_1 = QLabel(self.palavra_group_box)
        self.traco_1.setObjectName(u"traco_1")
        self.traco_1.setGeometry(QRect(20, 43, 21, 31))
        self.traco_1.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_12 = QLabel(self.palavra_group_box)
        self.letra_12.setObjectName(u"letra_12")
        self.letra_12.setGeometry(QRect(350, 20, 21, 31))
        self.letra_12.setFont(font1)
        self.letra_12.setAlignment(Qt.AlignCenter)
        self.traco_10 = QLabel(self.palavra_group_box)
        self.traco_10.setObjectName(u"traco_10")
        self.traco_10.setGeometry(QRect(290, 43, 21, 31))
        self.traco_10.setPixmap(QPixmap(u"traco.jpg"))
        self.traco_2 = QLabel(self.palavra_group_box)
        self.traco_2.setObjectName(u"traco_2")
        self.traco_2.setGeometry(QRect(50, 43, 21, 31))
        self.traco_2.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_2 = QLabel(self.palavra_group_box)
        self.letra_2.setObjectName(u"letra_2")
        self.letra_2.setGeometry(QRect(50, 20, 21, 31))
        self.letra_2.setFont(font1)
        self.letra_2.setAlignment(Qt.AlignCenter)
        self.letra_1 = QLabel(self.palavra_group_box)
        self.letra_1.setObjectName(u"letra_1")
        self.letra_1.setGeometry(QRect(20, 20, 21, 31))
        self.letra_1.setFont(font1)
        self.letra_1.setAlignment(Qt.AlignCenter)
        self.traco_13 = QLabel(self.palavra_group_box)
        self.traco_13.setObjectName(u"traco_13")
        self.traco_13.setGeometry(QRect(380, 43, 21, 31))
        self.traco_13.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_9 = QLabel(self.palavra_group_box)
        self.letra_9.setObjectName(u"letra_9")
        self.letra_9.setGeometry(QRect(260, 20, 21, 31))
        self.letra_9.setFont(font1)
        self.letra_9.setAlignment(Qt.AlignCenter)
        self.traco_9 = QLabel(self.palavra_group_box)
        self.traco_9.setObjectName(u"traco_9")
        self.traco_9.setGeometry(QRect(260, 43, 21, 31))
        self.traco_9.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_8 = QLabel(self.palavra_group_box)
        self.letra_8.setObjectName(u"letra_8")
        self.letra_8.setGeometry(QRect(230, 20, 21, 31))
        self.letra_8.setFont(font1)
        self.letra_8.setAlignment(Qt.AlignCenter)
        self.traco_5 = QLabel(self.palavra_group_box)
        self.traco_5.setObjectName(u"traco_5")
        self.traco_5.setGeometry(QRect(140, 43, 21, 31))
        self.traco_5.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_5 = QLabel(self.palavra_group_box)
        self.letra_5.setObjectName(u"letra_5")
        self.letra_5.setGeometry(QRect(140, 20, 21, 31))
        self.letra_5.setFont(font1)
        self.letra_5.setAlignment(Qt.AlignCenter)
        self.traco_7 = QLabel(self.palavra_group_box)
        self.traco_7.setObjectName(u"traco_7")
        self.traco_7.setGeometry(QRect(200, 43, 21, 31))
        self.traco_7.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_3 = QLabel(self.palavra_group_box)
        self.letra_3.setObjectName(u"letra_3")
        self.letra_3.setGeometry(QRect(80, 20, 21, 31))
        self.letra_3.setFont(font1)
        self.letra_3.setAlignment(Qt.AlignCenter)
        self.traco_3 = QLabel(self.palavra_group_box)
        self.traco_3.setObjectName(u"traco_3")
        self.traco_3.setGeometry(QRect(80, 43, 21, 31))
        self.traco_3.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_6 = QLabel(self.palavra_group_box)
        self.letra_6.setObjectName(u"letra_6")
        self.letra_6.setGeometry(QRect(170, 20, 21, 31))
        self.letra_6.setFont(font1)
        self.letra_6.setAlignment(Qt.AlignCenter)
        self.letra_7 = QLabel(self.palavra_group_box)
        self.letra_7.setObjectName(u"letra_7")
        self.letra_7.setGeometry(QRect(200, 20, 21, 31))
        self.letra_7.setFont(font1)
        self.letra_7.setAlignment(Qt.AlignCenter)
        self.traco_4 = QLabel(self.palavra_group_box)
        self.traco_4.setObjectName(u"traco_4")
        self.traco_4.setGeometry(QRect(110, 43, 21, 31))
        self.traco_4.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_4 = QLabel(self.palavra_group_box)
        self.letra_4.setObjectName(u"letra_4")
        self.letra_4.setGeometry(QRect(110, 20, 21, 31))
        self.letra_4.setFont(font1)
        self.letra_4.setAlignment(Qt.AlignCenter)
        self.traco_8 = QLabel(self.palavra_group_box)
        self.traco_8.setObjectName(u"traco_8")
        self.traco_8.setGeometry(QRect(230, 43, 21, 31))
        self.traco_8.setPixmap(QPixmap(u"traco.jpg"))
        self.traco_11 = QLabel(self.palavra_group_box)
        self.traco_11.setObjectName(u"traco_11")
        self.traco_11.setGeometry(QRect(320, 43, 21, 31))
        self.traco_11.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_10 = QLabel(self.palavra_group_box)
        self.letra_10.setObjectName(u"letra_10")
        self.letra_10.setGeometry(QRect(290, 20, 21, 31))
        self.letra_10.setFont(font1)
        self.letra_10.setAlignment(Qt.AlignCenter)
        self.traco_6 = QLabel(self.palavra_group_box)
        self.traco_6.setObjectName(u"traco_6")
        self.traco_6.setGeometry(QRect(170, 43, 21, 31))
        self.traco_6.setPixmap(QPixmap(u"traco.jpg"))
        self.traco_12 = QLabel(self.palavra_group_box)
        self.traco_12.setObjectName(u"traco_12")
        self.traco_12.setGeometry(QRect(350, 43, 21, 31))
        self.traco_12.setPixmap(QPixmap(u"traco.jpg"))
        self.letra_11 = QLabel(self.palavra_group_box)
        self.letra_11.setObjectName(u"letra_11")
        self.letra_11.setGeometry(QRect(320, 20, 21, 31))
        self.letra_11.setFont(font1)
        self.letra_11.setAlignment(Qt.AlignCenter)
        self.traco_1.raise_()
        self.traco_10.raise_()
        self.traco_2.raise_()
        self.letra_2.raise_()
        self.letra_1.raise_()
        self.traco_13.raise_()
        self.traco_9.raise_()
        self.traco_5.raise_()
        self.traco_7.raise_()
        self.traco_3.raise_()
        self.traco_4.raise_()
        self.traco_8.raise_()
        self.traco_11.raise_()
        self.letra_10.raise_()
        self.traco_6.raise_()
        self.traco_12.raise_()
        self.letra_11.raise_()
        self.letra_12.raise_()
        self.letra_8.raise_()
        self.letra_6.raise_()
        self.letra_9.raise_()
        self.letra_3.raise_()
        self.letra_5.raise_()
        self.letra_7.raise_()
        self.letra_13.raise_()
        self.letra_4.raise_()
        self.letras_group_box = QGroupBox(self.centralwidget)
        self.letras_group_box.setObjectName(u"letras_group_box")
        self.letras_group_box.setGeometry(QRect(470, 10, 271, 381))
        self.letras_group_box.setFont(font)
        self.botao_letra_a = QPushButton(self.letras_group_box)
        self.botao_letra_a.setObjectName(u"botao_letra_a")
        self.botao_letra_a.setEnabled(True)
        self.botao_letra_a.setGeometry(QRect(30, 30, 41, 31))
        font2 = QFont()
        font2.setPointSize(18)
        self.botao_letra_a.setFont(font2)
        self.botao_letra_b = QPushButton(self.letras_group_box)
        self.botao_letra_b.setObjectName(u"botao_letra_b")
        self.botao_letra_b.setGeometry(QRect(90, 30, 41, 31))
        self.botao_letra_b.setFont(font2)
        self.botao_letra_c = QPushButton(self.letras_group_box)
        self.botao_letra_c.setObjectName(u"botao_letra_c")
        self.botao_letra_c.setGeometry(QRect(150, 30, 41, 31))
        self.botao_letra_c.setFont(font2)
        self.botao_letra_d = QPushButton(self.letras_group_box)
        self.botao_letra_d.setObjectName(u"botao_letra_d")
        self.botao_letra_d.setGeometry(QRect(210, 30, 41, 31))
        self.botao_letra_d.setFont(font2)
        self.botao_letra_g = QPushButton(self.letras_group_box)
        self.botao_letra_g.setObjectName(u"botao_letra_g")
        self.botao_letra_g.setGeometry(QRect(150, 80, 41, 31))
        self.botao_letra_g.setFont(font2)
        self.botao_letra_e = QPushButton(self.letras_group_box)
        self.botao_letra_e.setObjectName(u"botao_letra_e")
        self.botao_letra_e.setGeometry(QRect(30, 80, 41, 31))
        self.botao_letra_e.setFont(font2)
        self.botao_letra_h = QPushButton(self.letras_group_box)
        self.botao_letra_h.setObjectName(u"botao_letra_h")
        self.botao_letra_h.setGeometry(QRect(210, 80, 41, 31))
        self.botao_letra_h.setFont(font2)
        self.botao_letra_f = QPushButton(self.letras_group_box)
        self.botao_letra_f.setObjectName(u"botao_letra_f")
        self.botao_letra_f.setGeometry(QRect(90, 80, 41, 31))
        self.botao_letra_f.setFont(font2)
        self.botao_letra_n = QPushButton(self.letras_group_box)
        self.botao_letra_n.setObjectName(u"botao_letra_n")
        self.botao_letra_n.setGeometry(QRect(90, 180, 41, 31))
        self.botao_letra_n.setFont(font2)
        self.botao_letra_k = QPushButton(self.letras_group_box)
        self.botao_letra_k.setObjectName(u"botao_letra_k")
        self.botao_letra_k.setGeometry(QRect(150, 130, 41, 31))
        self.botao_letra_k.setFont(font2)
        self.botao_letra_o = QPushButton(self.letras_group_box)
        self.botao_letra_o.setObjectName(u"botao_letra_o")
        self.botao_letra_o.setGeometry(QRect(150, 180, 41, 31))
        self.botao_letra_o.setFont(font2)
        self.botao_letra_i = QPushButton(self.letras_group_box)
        self.botao_letra_i.setObjectName(u"botao_letra_i")
        self.botao_letra_i.setGeometry(QRect(30, 130, 41, 31))
        self.botao_letra_i.setFont(font2)
        self.botao_letra_l = QPushButton(self.letras_group_box)
        self.botao_letra_l.setObjectName(u"botao_letra_l")
        self.botao_letra_l.setGeometry(QRect(210, 130, 41, 31))
        self.botao_letra_l.setFont(font2)
        self.botao_letra_j = QPushButton(self.letras_group_box)
        self.botao_letra_j.setObjectName(u"botao_letra_j")
        self.botao_letra_j.setGeometry(QRect(90, 130, 41, 31))
        self.botao_letra_j.setFont(font2)
        self.botao_letra_p = QPushButton(self.letras_group_box)
        self.botao_letra_p.setObjectName(u"botao_letra_p")
        self.botao_letra_p.setGeometry(QRect(210, 180, 41, 31))
        self.botao_letra_p.setFont(font2)
        self.botao_letra_m = QPushButton(self.letras_group_box)
        self.botao_letra_m.setObjectName(u"botao_letra_m")
        self.botao_letra_m.setGeometry(QRect(30, 180, 41, 31))
        self.botao_letra_m.setFont(font2)
        self.botao_letra_x = QPushButton(self.letras_group_box)
        self.botao_letra_x.setObjectName(u"botao_letra_x")
        self.botao_letra_x.setGeometry(QRect(150, 280, 41, 31))
        self.botao_letra_x.setFont(font2)
        self.botao_letra_q = QPushButton(self.letras_group_box)
        self.botao_letra_q.setObjectName(u"botao_letra_q")
        self.botao_letra_q.setGeometry(QRect(30, 230, 41, 31))
        self.botao_letra_q.setFont(font2)
        self.botao_letra_s = QPushButton(self.letras_group_box)
        self.botao_letra_s.setObjectName(u"botao_letra_s")
        self.botao_letra_s.setGeometry(QRect(150, 230, 41, 31))
        self.botao_letra_s.setFont(font2)
        self.botao_letra_t = QPushButton(self.letras_group_box)
        self.botao_letra_t.setObjectName(u"botao_letra_t")
        self.botao_letra_t.setGeometry(QRect(210, 230, 41, 31))
        self.botao_letra_t.setFont(font2)
        self.botao_letra_w = QPushButton(self.letras_group_box)
        self.botao_letra_w.setObjectName(u"botao_letra_w")
        self.botao_letra_w.setGeometry(QRect(210, 280, 41, 31))
        self.botao_letra_w.setFont(font2)
        self.botao_letra_u = QPushButton(self.letras_group_box)
        self.botao_letra_u.setObjectName(u"botao_letra_u")
        self.botao_letra_u.setGeometry(QRect(30, 280, 41, 31))
        self.botao_letra_u.setFont(font2)
        self.botao_letra_v = QPushButton(self.letras_group_box)
        self.botao_letra_v.setObjectName(u"botao_letra_v")
        self.botao_letra_v.setGeometry(QRect(90, 280, 41, 31))
        self.botao_letra_v.setFont(font2)
        self.botao_letra_r = QPushButton(self.letras_group_box)
        self.botao_letra_r.setObjectName(u"botao_letra_r")
        self.botao_letra_r.setGeometry(QRect(90, 230, 41, 31))
        self.botao_letra_r.setFont(font2)
        self.botao_letra_z = QPushButton(self.letras_group_box)
        self.botao_letra_z.setObjectName(u"botao_letra_z")
        self.botao_letra_z.setGeometry(QRect(150, 330, 41, 31))
        self.botao_letra_z.setFont(font2)
        self.botao_letra_y = QPushButton(self.letras_group_box)
        self.botao_letra_y.setObjectName(u"botao_letra_y")
        self.botao_letra_y.setGeometry(QRect(90, 330, 41, 31))
        self.botao_letra_y.setFont(font2)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(470, 410, 271, 131))
        self.groupBox.setFont(font)
        self.palavra_texto = QLineEdit(self.groupBox)
        self.palavra_texto.setObjectName(u"palavra_texto")
        self.palavra_texto.setGeometry(QRect(20, 40, 231, 21))
        self.palavra_texto.setFont(font)
        self.palavra_texto.setMaxLength(18)
        self.botao_arriscar = QPushButton(self.groupBox)
        self.botao_arriscar.setObjectName(u"botao_arriscar")
        self.botao_arriscar.setGeometry(QRect(90, 80, 91, 31))
        self.botao_arriscar.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 251, 41))
        font3 = QFont()
        font3.setFamily(u"Pristina")
        font3.setPointSize(25)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        self.label.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 765, 21))
        self.menu_jogo = QMenu(self.menuBar)
        self.menu_jogo.setObjectName(u"menu_jogo")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu_jogo.menuAction())
        self.menu_jogo.addAction(self.menu_novo_jogo)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.botao_letra_a.clicked.connect(self.letra_a)
        self.botao_letra_b.clicked.connect(self.letra_b)
        self.botao_letra_c.clicked.connect(self.letra_c)
        self.botao_letra_d.clicked.connect(self.letra_d)
        self.botao_letra_e.clicked.connect(self.letra_e)
        self.botao_letra_f.clicked.connect(self.letra_f)
        self.botao_letra_g.clicked.connect(self.letra_g)
        self.botao_letra_h.clicked.connect(self.letra_h)
        self.botao_letra_i.clicked.connect(self.letra_i)
        self.botao_letra_j.clicked.connect(self.letra_j)
        self.botao_letra_k.clicked.connect(self.letra_k)
        self.botao_letra_l.clicked.connect(self.letra_l)
        self.botao_letra_m.clicked.connect(self.letra_m)
        self.botao_letra_n.clicked.connect(self.letra_n)
        self.botao_letra_o.clicked.connect(self.letra_o)
        self.botao_letra_p.clicked.connect(self.letra_p)
        self.botao_letra_q.clicked.connect(self.letra_q)
        self.botao_letra_r.clicked.connect(self.letra_r)
        self.botao_letra_s.clicked.connect(self.letra_s)
        self.botao_letra_t.clicked.connect(self.letra_t)
        self.botao_letra_u.clicked.connect(self.letra_u)
        self.botao_letra_v.clicked.connect(self.letra_v)
        self.botao_letra_x.clicked.connect(self.letra_x)
        self.botao_letra_y.clicked.connect(self.letra_y)
        self.botao_letra_z.clicked.connect(self.letra_z)
        self.botao_letra_w.clicked.connect(self.letra_w)
        self.botao_arriscar.clicked.connect(self.arriscar_palavra)
        self.tela_resultado.botao_novo_jogo.clicked.connect(self.novo_jogo)
        self.menu_novo_jogo.triggered.connect(self.abondonar_jogo)

    # setupUi

    def closeEvent(self, event):
        print('aaa')


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_novo_jogo.setText(QCoreApplication.translate("MainWindow", u"Novo Jogo", None))
        self.forca.setText("")
        self.cabeca.setText("")
        self.corpo.setText("")
        self.braco_esquerdo.setText("")
        self.perna_esquerda.setText("")
        self.braco_direito.setText("")
        self.perna_direita.setText("")
        self.palavra_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Palavra", None))
        self.letra_13.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_1.setText("")
        self.letra_12.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_10.setText("")
        self.traco_2.setText("")
        self.letra_2.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.letra_1.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_13.setText("")
        self.letra_9.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_9.setText("")
        self.letra_8.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_5.setText("")
        self.letra_5.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_7.setText("")
        self.letra_3.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_3.setText("")
        self.letra_6.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.letra_7.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_4.setText("")
        self.letra_4.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_8.setText("")
        self.traco_11.setText("")
        self.letra_10.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.traco_6.setText("")
        self.traco_12.setText("")
        self.letra_11.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.letras_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Letras", None))
        self.botao_letra_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.botao_letra_b.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.botao_letra_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.botao_letra_d.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.botao_letra_g.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.botao_letra_e.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.botao_letra_h.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.botao_letra_f.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.botao_letra_n.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.botao_letra_k.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.botao_letra_o.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.botao_letra_i.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.botao_letra_l.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.botao_letra_j.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.botao_letra_p.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.botao_letra_m.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.botao_letra_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.botao_letra_q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.botao_letra_s.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.botao_letra_t.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.botao_letra_w.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.botao_letra_u.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.botao_letra_v.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.botao_letra_r.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.botao_letra_z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.botao_letra_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Arriscar palavra", None))
        self.botao_arriscar.setText(QCoreApplication.translate("MainWindow", u"Arriscar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Jogo da Forca", None))
        self.menu_jogo.setTitle(QCoreApplication.translate("MainWindow", u"Jogo", None))
    # retranslateUi

    def zerar_jogo(self):
        Ui_MainWindow.chances_jogador = 6
        Ui_MainWindow.letras_advinhadas = 0
        self.palavra_texto.setText('')
        self.cabeca.hide()
        self.perna_esquerda.hide()
        self.perna_direita.hide()
        self.braco_esquerdo.hide()
        self.braco_direito.hide()
        self.corpo.hide()
        self.letra_1.hide()
        self.letra_2.hide()
        self.letra_3.hide()
        self.letra_4.hide()
        self.letra_5.hide()
        self.letra_6.hide()
        self.letra_7.hide()
        self.letra_8.hide()
        self.letra_9.hide()
        self.letra_10.hide()
        self.letra_11.hide()
        self.letra_12.hide()
        self.letra_13.hide()
        self.botao_letra_a.setEnabled(True)
        self.botao_letra_b.setEnabled(True)
        self.botao_letra_c.setEnabled(True)
        self.botao_letra_d.setEnabled(True)
        self.botao_letra_e.setEnabled(True)
        self.botao_letra_f.setEnabled(True)
        self.botao_letra_g.setEnabled(True)
        self.botao_letra_h.setEnabled(True)
        self.botao_letra_i.setEnabled(True)
        self.botao_letra_j.setEnabled(True)
        self.botao_letra_k.setEnabled(True)
        self.botao_letra_l.setEnabled(True)
        self.botao_letra_m.setEnabled(True)
        self.botao_letra_n.setEnabled(True)
        self.botao_letra_o.setEnabled(True)
        self.botao_letra_p.setEnabled(True)
        self.botao_letra_q.setEnabled(True)
        self.botao_letra_r.setEnabled(True)
        self.botao_letra_s.setEnabled(True)
        self.botao_letra_t.setEnabled(True)
        self.botao_letra_u.setEnabled(True)
        self.botao_letra_v.setEnabled(True)
        self.botao_letra_x.setEnabled(True)
        self.botao_letra_w.setEnabled(True)
        self.botao_letra_y.setEnabled(True)
        self.botao_letra_z.setEnabled(True)
        self.traco_1.hide()
        self.traco_2.hide()
        self.traco_3.hide()
        self.traco_4.hide()
        self.traco_5.hide()
        self.traco_6.hide()
        self.traco_7.hide()
        self.traco_8.hide()
        self.traco_9.hide()
        self.traco_10.hide()
        self.traco_11.hide()
        self.traco_12.hide()
        self.traco_13.hide()

    def letra_a(self):
        self.botao_letra_a.setEnabled(False)
        self.verificar_letra('a')

    def letra_b(self):
        self.botao_letra_b.setEnabled(False)
        self.verificar_letra('b')

    def letra_c(self):
        self.botao_letra_c.setEnabled(False)
        self.verificar_letra('c')

    def letra_d(self):
        self.botao_letra_d.setEnabled(False)
        self.verificar_letra('d')

    def letra_e(self):
        self.botao_letra_e.setEnabled(False)
        self.verificar_letra('e')

    def letra_f(self):
        self.botao_letra_f.setEnabled(False)
        self.verificar_letra('f')

    def letra_g(self):
        self.botao_letra_g.setEnabled(False)
        self.verificar_letra('g')

    def letra_h(self):
        self.botao_letra_h.setEnabled(False)
        self.verificar_letra('h')

    def letra_i(self):
        self.botao_letra_i.setEnabled(False)
        self.verificar_letra('i')

    def letra_j(self):
        self.botao_letra_j.setEnabled(False)
        self.verificar_letra('j')

    def letra_k(self):
        self.botao_letra_k.setEnabled(False)
        self.verificar_letra('k')

    def letra_l(self):
        self.botao_letra_l.setEnabled(False)
        self.verificar_letra('l')

    def letra_m(self):
        self.botao_letra_m.setEnabled(False)
        self.verificar_letra('m')

    def letra_n(self):
        self.botao_letra_n.setEnabled(False)
        self.verificar_letra('n')

    def letra_o(self):
        self.botao_letra_o.setEnabled(False)
        self.verificar_letra('o')

    def letra_p(self):
        self.botao_letra_p.setEnabled(False)
        self.verificar_letra('p')

    def letra_q(self):
        self.botao_letra_q.setEnabled(False)
        self.verificar_letra('q')

    def letra_r(self):
        self.botao_letra_r.setEnabled(False)
        self.verificar_letra('r')

    def letra_s(self):
        self.botao_letra_s.setEnabled(False)
        self.verificar_letra('s')

    def letra_t(self):
        self.botao_letra_t.setEnabled(False)
        self.verificar_letra('t')

    def letra_u(self):
        self.botao_letra_u.setEnabled(False)
        self.verificar_letra('u')

    def letra_v(self):
        self.botao_letra_v.setEnabled(False)
        self.verificar_letra('v')

    def letra_x(self):
        self.botao_letra_x.setEnabled(False)
        self.verificar_letra('x')

    def letra_y(self):
        self.botao_letra_y.setEnabled(False)
        self.verificar_letra('y')

    def letra_w(self):
        self.botao_letra_w.setEnabled(False)
        self.verificar_letra('w')

    def letra_z(self):
        self.botao_letra_z.setEnabled(False)
        self.verificar_letra('z')

    def gerar_palavra(self):
        palavra_sorteada, palavra_normalizada = sortear_palavra()
        self.__palavra_sorteada = palavra_sorteada
        self.__palavra_normalizada = palavra_normalizada
        self.iniciar_tracos()
        print(self.__palavra_sorteada)

    def iniciar_tracos(self):
        quantidade = len(self.__palavra_sorteada)
        if quantidade >= 1:
            self.traco_1.show()
        if quantidade >= 2:
            self.traco_2.show()
        if quantidade >= 3:
            self.traco_3.show()
        if quantidade >= 4:
            self.traco_4.show()
        if quantidade >= 5:
            self.traco_5.show()
        if quantidade >= 6:
            self.traco_6.show()
        if quantidade >= 7:
            self.traco_7.show()
        if quantidade >= 8:
            self.traco_8.show()
        if quantidade >= 9:
            self.traco_9.show()
        if quantidade >= 10:
            self.traco_10.show()
        if quantidade >= 11:
            self.traco_11.show()
        if quantidade >= 12:
            self.traco_12.show()
        if quantidade >= 13:
            self.traco_13.show()

    def mostrar_letra(self, posicao, letra):
        if posicao == 1:
            self.letra_1.setText(letra)
            self.letra_1.show()
        elif posicao == 2:
            self.letra_2.setText(letra)
            self.letra_2.show()
        elif posicao == 3:
            self.letra_3.setText(letra)
            self.letra_3.show()
        elif posicao == 4:
            self.letra_4.setText(letra)
            self.letra_4.show()
        elif posicao == 5:
            self.letra_5.setText(letra)
            self.letra_5.show()
        elif posicao == 6:
            self.letra_6.setText(letra)
            self.letra_6.show()
        elif posicao == 7:
            self.letra_7.setText(letra)
            self.letra_7.show()
        elif posicao == 8:
            self.letra_8.setText(letra)
            self.letra_8.show()
        elif posicao == 9:
            self.letra_9.setText(letra)
            self.letra_9.show()
        elif posicao == 10:
            self.letra_10.setText(letra)
            self.letra_10.show()
        elif posicao == 11:
            self.letra_11.setText(letra)
            self.letra_11.show()
        elif posicao == 12:
            self.letra_12.setText(letra)
            self.letra_12.show()
        elif posicao == 13:
            self.letra_13.setText(letra)
            self.letra_13.show()

    def verificar_letra(self, letra):
        if letra in self.__palavra_normalizada:
            index = 0
            for caractere in self.__palavra_normalizada:
                if caractere == letra:
                    self.mostrar_letra(index + 1, self.__palavra_sorteada[index])
                    Ui_MainWindow.letras_advinhadas += 1
                    if Ui_MainWindow.letras_advinhadas == len(self.__palavra_normalizada):
                        self.mostra_tela_resultado('vitoria')
                index += 1
        else:
            self.adicionar_erro()

    def arriscar_palavra(self):
        if len(self.palavra_texto.text()) > 2:
            palavra_arriscada = self.palavra_texto.text()
            palavra_arriscada = normalize('NFKD', palavra_arriscada).encode('ASCII', 'ignore').decode('ASCII')
            palavra_arriscada = palavra_arriscada.lower()
            if palavra_arriscada == self.__palavra_normalizada:
                self.mostra_tela_resultado('vitoria')
            else:
                self.adicionar_erro()

    def adicionar_erro(self):
        if Ui_MainWindow.chances_jogador == 6:
            self.cabeca.show()
        elif Ui_MainWindow.chances_jogador == 5:
            self.corpo.show()
        elif Ui_MainWindow.chances_jogador == 4:
            self.braco_direito.show()
        elif Ui_MainWindow.chances_jogador == 3:
            self.braco_esquerdo.show()
        elif Ui_MainWindow.chances_jogador == 2:
            self.perna_direita.show()
        elif Ui_MainWindow.chances_jogador == 1:
            self.perna_esquerda.show()
            self.mostra_tela_resultado('derrota')
        Ui_MainWindow.chances_jogador -= 1

    def mostra_tela_resultado(self, resultado):
        if resultado == 'derrota':
            self.tela_resultado.label_resultado.setText('Você perdeu')
        elif resultado == 'vitoria':
            self.tela_resultado.label_resultado.setText('Você ganhou')
        elif resultado == 'desistencia':
            self.tela_resultado.label_resultado.setText('Você desistiu')
        self.tela_resultado.label_palavra.setText(f'A palavra era: {self.__palavra_sorteada}')
        self.tela_resultado.show()

    def novo_jogo(self):
        self.zerar_jogo()
        self.gerar_palavra()
        self.tela_resultado.close()

    def abondonar_jogo(self):
        self.mostra_tela_resultado('desistencia')


class CriarTelaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CriarTelaPrincipal, self).__init__()
        self.setupUi(self)
        self.zerar_jogo()
        self.gerar_palavra()
