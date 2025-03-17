import sys
from PyQt6.QtWidgets import QApplication, QWidget #Esta madre es la clase padre

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('Mi primera ventana')
        self.show() #Muestra la ventana

if __name__ == '__main__':
    app = QApplication(sys.argv) #Crea la instancia de la aplicación
    ventana = VentanaVacia() #Crea la instancia de la ventana
    sys.exit(app.exec()) #Ejecuta la aplicación