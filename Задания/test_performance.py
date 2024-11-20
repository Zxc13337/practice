import time
import os
import sys
from PyQt5.QtWidgets import QApplication
from image_info_module import ImageInfoModule
from utils import get_file_creation_time, format_file_size

# Функции замеров
def time_function_call(func, *args, **kwargs):
    start_time = time.time()  # Время начала
    result = func(*args, **kwargs)
    end_time = time.time()  # Время окончания
    execution_time = end_time - start_time
    return result, execution_time

def test_get_file_creation_time():
    file_path = "test_image.jpg"  # Укажите путь к тестовому файлу
    _, execution_time = time_function_call(get_file_creation_time, file_path)
    print(f"Время выполнения get_file_creation_time: {execution_time:.6f} секунд")

def test_format_file_size():
    file_size = 1024 * 1024 * 5  # 5MB
    _, execution_time = time_function_call(format_file_size, file_size)
    print(f"Время выполнения format_file_size: {execution_time:.6f} секунд")

def test_open_image():
    app = QApplication(sys.argv)
    window = ImageInfoModule()
    window.image_path = "test_image.jpg"  # Укажите путь к изображению для теста
    _, execution_time = time_function_call(window.open_image)
    print(f"Время выполнения open_image: {execution_time:.6f} секунд")
    return app  # Чтобы приложение не завершилось сразу

def test_rename_image():
    app = QApplication(sys.argv)
    window = ImageInfoModule()
    window.image_path = "test_image.jpg"  # Укажите путь к изображению для теста
    window.rename_image()  # Это вызовет переименование
    _, execution_time = time_function_call(window.rename_image)
    print(f"Время выполнения rename_image: {execution_time:.6f} секунд")

def test_full_application():
    start_time = time.time()

    # Инициализация приложения
    app = QApplication(sys.argv)
    
    # Создание и запуск окна с выбором изображения
    window = ImageInfoModule()
    window.image_path = "test_image.jpg"  # Укажите путь к изображению для теста
    window.show()
    
    # Запуск интерфейса
    sys.exit(app.exec_())
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Общее время выполнения программы: {total_time:.6f} секунд")

# Запуск тестов
if __name__ == "__main__":
    print("Тестируем функцию get_file_creation_time...")
    test_get_file_creation_time()

    print("\nТестируем функцию format_file_size...")
    test_format_file_size()

    print("\nТестируем функцию open_image...")
    test_open_image()

    print("\nТестируем функцию rename_image...")
    test_rename_image()

    print("\nТестируем полную программу...")
    test_full_application()
