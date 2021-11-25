import sys
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.kime=QtWidgets.QLabel("Kime")
        self.kime_alani=QtWidgets.QLineEdit()

        self.konu=QtWidgets.QLabel("Konu")
        self.konu_alani=QtWidgets.QLineEdit()

        self.mesajj=QtWidgets.QTextEdit()

        self.gonder=QtWidgets.QPushButton("Gönder")
        self.gonderildimi=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kime)
        v_box.addWidget(self.kime_alani)
        v_box.addWidget(self.konu)
        v_box.addWidget(self.konu_alani)
        v_box.addWidget(self.mesajj)
        v_box.addStretch()
        v_box.addWidget(self.gonderildimi)
        v_box.addWidget(self.gonder)

        self.setLayout(v_box)


        self.gonder.clicked.connect(self.login)

        self.show()


    def login(self):

        self.mesaj = MIMEMultipart()
        self.mesaj["From"] = "dgkkumru@gmail.com"
        self.mesaj["To"] = self.kime_alani.text()
        self.mesaj["Subject"] = self.konu_alani.text()
        self.mesaj_govdesi = MIMEText(self.mesajj.toPlainText(),"plain")  # Mesaj alanına yazılan tüm yazıları almış oluyoruz böylece
        self.mesaj.attach(self.mesaj_govdesi)

        try:
            self.mail=smtplib.SMTP("smtp.gmail.com",587)
            self.mail.ehlo()
            self.mail.starttls()
            self.mail.login("Enter your e-mail here","Enter password here")
            self.mail.sendmail(self.mesaj["From"],self.mesaj["To"],self.mesaj.as_string())

            self.gonderildimi.setText("Mesajınız Gönderildi.")
            self.mail.close()

        except:
            self.gonderildimi.setText("Hata Tespit Edildi")





app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())