import os
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap

class ImageInfoModule(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Info Module")
        
        self.image_path = ""
        
        layout = QVBoxLayout()
        
        self.image_label = QLabel("Выберите изображение")
        layout.addWidget(self.image_label)
        
        self.image_button = QPushButton("Выбрать изображение")
        self.image_button.clicked.connect(self.open_image)
        layout.addWidget(self.image_button)
        
        self.info_label = QLabel("")
        layout.addWidget(self.info_label)
        
        self.rename_button = QPushButton("Переименовать изображение")
        self.rename_button.clicked.connect(self.rename_image)
        layout.addWidget(self.rename_button)
        
        self.setLayout(layout)
        
    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Изображения (*.jpg *.png *.bmp)", options=options)
        
        if self.image_path:  # Проверяем, что путь не пуст
            pixmap = QPixmap(self.image_path)
            if pixmap.isNull():  # Проверяем, удалось ли загрузить изображение
                self.info_label.setText("Ошибка загрузки изображения.")
                return
            
            self.image_label.setPixmap(pixmap.scaled(300, 300, aspectRatioMode=1))  # Масштабируем для корректного отображения
            
            image_info = f"Размер: {os.path.getsize(self.image_path)} байт\n"
            image_info += f"Разрешение: {pixmap.width()}x{pixmap.height()}\n"
            image_info += f"Дата создания: {os.path.getctime(self.image_path)}"
            
            self.info_label.setText(image_info)
        else:
            self.info_label.setText("Файл не выбран.")
        
    def rename_image(self):
        if self.image_path:
            new_name, _ = QFileDialog.getSaveFileName(self, "Выберите новое имя для изображения", "", "Изображения (*.jpg *.png *.bmp)")
            if new_name:
                try:
                    os.rename(self.image_path, new_name)
                    self.image_path = new_name
                    self.info_label.setText("Изображение успешно переименовано.")
                except Exception as e:
                    self.info_label.setText(f"Ошибка переименования: {e}")
        else:
            self.info_label.setText("Выберите изображение перед переименованием.")
