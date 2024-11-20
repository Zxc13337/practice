import sys
from PyQt5.QtWidgets import QApplication
from image_info_module import ImageInfoModule

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageInfoModule()
    window.show()
    sys.exit(app.exec_())
