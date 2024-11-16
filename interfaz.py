from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget

class Gestor_tareas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestor de Tareas')
        self.setGeometry(100,100,600,400)
        self.inicializar_ui()

    def inicializar_ui(self):
        layout = QVBoxLayout()
        self.lista_tareas = QListWidget()
        layout.addWidget(self.lista_tareas)
        self.boton_agregar = QPushButton('Agregar Tarea')
        layout.addWidget(self.boton_agregar)
        self.boton_agregar.clicked.connect(self.mostrar_dialogoAgregar)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_dialogoAgregar(self):
        pass

    
