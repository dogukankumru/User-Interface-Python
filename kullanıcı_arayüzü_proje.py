import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()
        self.init_ui()


    def baglanti_olustur(self):         #Sql veritabanı oluşturduğumuz fonksiyon.

        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS üyeler (kullanıcı_adı TEXT, parola TEXT)")
        baglanti.commit()

        self.cursor.execute("INSERT INTO üyeler VALUES('Doğukan Kumru','123456')")
        baglanti.commit()


    def init_ui(self):

        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)              #Parola kısmına yazarken yazdığımız yazı gözükmeyecek gerçek hayattaki gibi
        self.giris=QtWidgets.QPushButton("Giriş Yap")
        self.kayit_ol=QtWidgets.QPushButton("Kayıt Ol")

        self.yazi_alani=QtWidgets.QLabel("")                               #Burayı şimdilik boş bırakıyoruz, eğer kullanıcı girişi hatalı ya da doğru yapılırsa ona göre burdaki yazının akıbeti belli olacak


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit_ol)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.giris.clicked.connect(self.login)
        self.kayit_ol.clicked.connect(self.kaydol)
        self.show()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()



        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))

        data=self.cursor.fetchall()

        if len(data)==0:

            self.yazi_alani.setText("Kullanıcı Bulunmamaktadır.")

        else:
            self.yazi_alani.setText("Hoşgeldin "+adi)


    def kaydol(self):

        kullan = self.kullanici_adi.text()
        parol = self.parola.text()

        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("Select * From üyeler where kullanıcı_adı=?", (kullan,))
        date = self.cursor.fetchall()

        if len(date) == 0:
            self.yazi_alani.setText("Bilgileriniz Kaydedildi.")
            self.cursor.execute("Insert Into üyeler Values (?,?)", (kullan, parol))
            baglanti.commit()

        else:

            self.yazi_alani.setText("Kullanıcı Adı Alınmış.")




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
