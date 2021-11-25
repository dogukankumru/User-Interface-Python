import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()  # QtWidget'ın init fonksiyonunu kullanacak ve ekstra olarak aşağıdaki işlemi yapacak Pencere classı ile obje oluşturulduğu zaman

        self.init_ui()

    def init_ui(self):

        self.yazı = QtWidgets.QLabel("Bana henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("Bana Tıkla")
        self.tıklama_sayısı = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı)    #Dikey olarak yazıyı oluşturduk. Buton ve yazıyı yukarı yapışık olacak şekilde ayarladık
        v_box.addStretch()


        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)         #Yazımızı ve butonumuzu ortaya sıkıştırmış olduk
        h_box.addStretch()

        self.setLayout(h_box)
        self.setGeometry(800,300,500,500)


        self.buton.clicked.connect(self.click)   # Butona tıkladığımızda connect ile içine belirttiğimiz fonksiyona bağlanacak
        self.show()

    def click(self):

        self.tıklama_sayısı = self.tıklama_sayısı+1
        self.yazı.setText("Bana " + str(self.tıklama_sayısı) + " defa tıklandı")


app = QtWidgets.QApplication(sys.argv)

pencere= Pencere()

sys.exit(app.exec_())
