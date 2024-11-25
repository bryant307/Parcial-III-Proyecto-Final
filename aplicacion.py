#ARCHIVO PRINCIPAL PARA INICIAR EL PROYECTO

from interfaz import Gestor_tareas
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
ventana = Gestor_tareas()
ventana.show()
sys.exit(app.exec_())