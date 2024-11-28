from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTabWidget, QGroupBox, QLabel, QLineEdit, QDateEdit, QTimeEdit, QPlainTextEdit, QCheckBox, QPushButton, QWidget
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIcon
import sys

class Gestor_tareas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Gestor de Tareas")
        self.setFixedSize(700, 550)
        self.setWindowIcon(QIcon("task_icon.png"))  

        # Tab Widget
        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(25, 20, 650, 500)

        # Tab: Crear Tareas
        self.tab_create_task = QWidget()
        self.tabs.addTab(self.tab_create_task, "Crear Tarea")

        # Grupo: Formulario para Crear Tareas
        self.group_create_task = QGroupBox("CREAR TAREAS", self.tab_create_task)
        self.group_create_task.setGeometry(10, 10, 620, 460)

        # Campo: Título de la Tarea
        self.label_title = QLabel("Título Tarea:", self.group_create_task)
        self.label_title.setGeometry(40, 40, 120, 20)
        self.input_title = QLineEdit(self.group_create_task)
        self.input_title.setGeometry(40, 70, 300, 30)
        self.input_title.setPlaceholderText("Escribe el título de la tarea")

        # Campo: Fecha y Hora
        self.label_datetime = QLabel("Fecha y Hora:", self.group_create_task)
        self.label_datetime.setGeometry(40, 120, 120, 20)
        self.input_date = QDateEdit(self.group_create_task)
        self.input_date.setGeometry(40, 150, 120, 30)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDateTime(QDateTime.currentDateTime())

        self.input_time = QTimeEdit(self.group_create_task)
        self.input_time.setGeometry(180, 150, 100, 30)

        # Campo: Descripción
        self.label_description = QLabel("Descripción:", self.group_create_task)
        self.label_description.setGeometry(40, 200, 120, 20)
        self.input_description = QPlainTextEdit(self.group_create_task)
        self.input_description.setGeometry(40, 230, 310, 100)
        self.input_description.setPlaceholderText("Escribe la descripción de la tarea")

        # Checkbox: Repetir
        self.checkbox_repeat = QCheckBox("Repetir", self.group_create_task)
        self.checkbox_repeat.setGeometry(310, 150, 100, 30)

        # Botón: Crear Tarea
        self.btn_create_task = QPushButton("Crear", self.group_create_task)
        self.btn_create_task.setGeometry(520, 420, 75, 30)
        self.btn_create_task.clicked.connect(self.create_task)

        # Placeholder para otras pestañas (opcional)
        self.tab_tasks_list = QWidget()
        self.tabs.addTab(self.tab_tasks_list, "Lista de Tareas")

        self.tab_completed_tasks = QWidget()
        self.tabs.addTab(self.tab_completed_tasks, "Tareas Completadas")

    def create_task(self):
        """
        Valida los campos y crea una nueva tarea. Implementa lógica de guardado en base de datos aquí.
        """
        title = self.input_title.text().strip()
        date = self.input_date.date().toString("yyyy-MM-dd")
        time = self.input_time.time().toString("HH:mm")
        description = self.input_description.toPlainText().strip()
        repeat = self.checkbox_repeat.isChecked()

        if not title:
            QMessageBox.warning(self, "Error", "El título de la tarea no puede estar vacío.")
            return

        # Aquí puedes conectar con tu base de datos para guardar la tarea
        print(f"Tarea creada: {title}, Fecha: {date}, Hora: {time}, Repetir: {repeat}")
        QMessageBox.information(self, "Éxito", f"Tarea '{title}' creada exitosamente.")

        # Limpiar campos después de crear la tarea
        self.input_title.clear()
        self.input_description.clear()
        self.checkbox_repeat.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gestor_tareas()
    window.show()
    sys.exit(app.exec_())
