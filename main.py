import sys
from PySide2 import QtCore, QtGui, QtWidgets
from ui_tela_do_jogo import CriarTelaPrincipal


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_login = CriarTelaPrincipal()
    window_login.show()
    sys.exit(app.exec_())
