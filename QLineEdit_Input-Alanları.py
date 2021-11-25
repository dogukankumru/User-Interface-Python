import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()  # QtWidget'ın init fonksiyonunu kullanacak ve ekstra olarak aşağıdaki işlemi yapacak Pencere classı ile obje oluşturulduğu zaman

        self.init_ui()

    def init_ui(self):

        self.yazı_alanı = QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")             #Butonların ve yazı alanının oluşturulduğu bölge
        self.yazdır=QtWidgets.QPushButton("Yazdır")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)                          #Yazıların ve butonların ekranda düzgün bir şekilde gözükmesi için
        v_box.addWidget(self.temizle)                             #yazdığımız vertical boxlar
        v_box.addWidget(self.yazdır)
        v_box.addStretch()
        self.setLayout(v_box)


        self.temizle.clicked.connect(self.click)                  #Butonlara basıldığında bizi click fonksiyonuna yönlendirecek
        self.yazdır.clicked.connect(self.click)

        self.show()

    def click(self):

        sender = self.sender()                            #Hangi butona basıldığını anlamamıza yardımcı olan fonksiyon

        if sender.text() == "Temizle":

            self.yazı_alanı.clear()                       #Eğer Temizle adlı butona basıldıysa, yazı alanındaki yazıları silecek

        else:
            print(self.yazı_alanı.text())                 #Else durumunda yani diğer butona basıldıysa, yazı alanındaki yazıları yazdıracak



app = QtWidgets.QApplication(sys.argv)

pencere= Pencere()

sys.exit(app.exec_())