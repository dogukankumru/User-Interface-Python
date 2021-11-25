import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.radio_yazisi=QtWidgets.QLabel("Hangi dili en çok seviyorsun")

        self.java=QtWidgets.QRadioButton("Java")
        self.python = QtWidgets.QRadioButton("Python")
        self.php = QtWidgets.QRadioButton("Php")

        self.yazi_alani=QtWidgets.QLabel("")
        self.buton=QtWidgets.QPushButton("Gönder")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("RadioButton Uygulaması")

        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))    # Click fonksiyonu çağrılırken içine parametreler alacağı için bu kısmı lambda kullanarak tamamlıyoruz.
                                                                                                                                               # isChecked fonksiyonu da radiobutonuna basılıp basılmadığını kontrol eden fonksiyon. Duruma göre true ya ad false döndürür.
        self.show()

    def click(self,python,java,php,yazi_alani):

        if python:
            yazi_alani.setText("Python Seçildi")

        if java:
            yazi_alani.setText("Java Seçildi")

        if php:
            yazi_alani.setText("PHP Seçildi")





app = QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())