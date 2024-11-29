#ARCHIVO PRINCIPAL PARA INICIAR EL PROYECTO

from interfaz import Gestor_tareas
from PySide6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
ventana = Gestor_tareas()
ventana.show()
sys.exit(app.exec_())
