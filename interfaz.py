from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox, QTabWidget, QGroupBox, QLabel, QLineEdit, QDateEdit, QTimeEdit, QPlainTextEdit, QCheckBox, QPushButton, QComboBox, QListView, QCalendarWidget, QCommandLinkButton
from PySide6.QtCore import QDateTime, Qt, QUrl
from PySide6.QtGui import QIcon, QDesktopServices, QStandardItemModel, QStandardItem
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
        self.group_crear_tarea = QGroupBox("CREAR TAREAS", self.tab_create_task)
        self.group_crear_tarea.setGeometry(10, 10, 620, 460)

        # Campo: Título de la Tarea
        self.label_title = QLabel("Título Tarea:", self.group_crear_tarea)
        self.label_title.setGeometry(40, 40, 120, 20)
        self.input_title = QLineEdit(self.group_crear_tarea)
        self.input_title.setGeometry(40, 70, 300, 30)
        self.input_title.setPlaceholderText("Escribe el título de la tarea")

        # Campo: Fecha y Hora
        self.label_datetime = QLabel("Fecha y Hora:", self.group_crear_tarea)
        self.label_datetime.setGeometry(40, 120, 120, 20)
        self.input_date = QDateEdit(self.group_crear_tarea)
        self.input_date.setGeometry(40, 150, 120, 30)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDateTime(QDateTime.currentDateTime())

        self.input_time = QTimeEdit(self.group_crear_tarea)
        self.input_time.setGeometry(180, 150, 100, 30)

        # Campo: Descripción
        self.label_description = QLabel("Descripción:", self.group_crear_tarea)
        self.label_description.setGeometry(40, 200, 120, 20)
        self.input_description = QPlainTextEdit(self.group_crear_tarea)
        self.input_description.setGeometry(40, 230, 310, 100)
        self.input_description.setPlaceholderText("Escribe la descripción de la tarea")

        # Checkbox: Repetir
        self.checkbox_repeat = QCheckBox("Repetir", self.group_crear_tarea)
        self.checkbox_repeat.setGeometry(310, 150, 100, 30)

        # Combobox: Prioridad de la tarea
        self.label_priority = QLabel("Prioridad:", self.group_crear_tarea)
        self.label_priority.setGeometry(40, 340, 100, 20)
        self.combo_priority = QComboBox(self.group_crear_tarea)
        self.combo_priority.setGeometry(120, 340, 100, 30)
        self.combo_priority.addItems(["Alta", "Media", "Baja"])

        # Botón: Crear Tarea
        self.btn_create_task = QPushButton("Crear", self.group_crear_tarea)
        self.btn_create_task.setGeometry(520, 420, 75, 30)
        self.btn_create_task.clicked.connect(self.create_task)

        # Modelo para las tareas
        self.tasks_model = QStandardItemModel()

        # Tab: Lista de Tareas
        self.tab_tasks_list = QWidget()
        self.tabs.addTab(self.tab_tasks_list, "Lista de Tareas")

        self.listview = QListView(self.tab_tasks_list)
        self.listview.setGeometry(20, 20, 600, 400)
        self.listview.setModel(self.tasks_model)

        # Botones en la pestaña Lista de Tareas
        self.btn_complete_task = QPushButton("Marcar Completada", self.tab_tasks_list)
        self.btn_complete_task.setGeometry(20, 440, 150, 30)
        self.btn_complete_task.clicked.connect(self.marcar_tarea_completada)

        self.btn_delete_task = QPushButton("Eliminar Tarea", self.tab_tasks_list)
        self.btn_delete_task.setGeometry(180, 440, 150, 30)
        self.btn_delete_task.clicked.connect(self.eliminar_tarea)

        # Tab: Tareas Completadas
        self.tab_list_complet = QWidget()
        self.tabs.addTab(self.tab_list_complet, "Tareas Completadas")

        self.completed_tasks_model = QStandardItemModel()
        self.completed_listview = QListView(self.tab_list_complet)
        self.completed_listview.setGeometry(20, 20, 600, 400)
        self.completed_listview.setModel(self.completed_tasks_model)

        # Tab: Calendario
        self.tab_calendar = QWidget()
        self.tabs.addTab(self.tab_calendar, "Calendario")
        self.calendar_widget = QCalendarWidget(self.tab_calendar)
        self.calendar_widget.setGeometry(20, 20, 300, 300)

        self.command_link_button = QCommandLinkButton("Repositorio del Proyecto", self.tab_calendar)
        self.command_link_button.setGeometry(340, 250, 220, 40)
        self.command_link_button.clicked.connect(self.abrir_repo)

    def abrir_repo(self):
        url = QUrl('https://github.com/bryant307/Parcial-III-Proyecto-Final')
        QDesktopServices.openUrl(url)

    def create_task(self):
        title = self.input_title.text().strip()
        date = self.input_date.date().toString("yyyy-MM-dd")
        time = self.input_time.time().toString("HH:mm")
        description = self.input_description.toPlainText().strip()
        repeat = self.checkbox_repeat.isChecked()
        priority = self.combo_priority.currentText()

        if not title:
            QMessageBox.warning(self, "Error", "El título de la tarea no puede estar vacío.")
            return

        # Crear elemento para la tarea
        task_item = QStandardItem(f"{title} - {date} {time} - {priority}")
        self.tasks_model.appendRow(task_item)

        QMessageBox.information(self, "Éxito", f"Tarea '{title}' creada exitosamente.")
        self.input_title.clear()
        self.input_description.clear()
        self.checkbox_repeat.setChecked(False)
        self.combo_priority.setCurrentIndex(0)

    def marcar_tarea_completada(self):
        selected_indexes = self.listview.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una tarea para marcar como completada.")
            return

        for index in selected_indexes:
            task_item = self.tasks_model.takeRow(index.row())[0]
            self.completed_tasks_model.appendRow(task_item)

        QMessageBox.information(self, "Éxito", "Tarea marcada como completada.")

    def eliminar_tarea(self):
        selected_indexes = self.listview.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una tarea para eliminar.")
            return

        for index in selected_indexes:
            self.tasks_model.removeRow(index.row())

        QMessageBox.information(self, "Éxito", "Tarea eliminada.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gestor_tareas()
    window.show()
    sys.exit(app.exec())
