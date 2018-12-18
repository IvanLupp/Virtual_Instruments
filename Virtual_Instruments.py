import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Instuments import Ui_Dialog
import pygame


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Виртуальные инструменты')
        self.instr.setText("АЛЬТ")
        self.vpe.clicked.connect(self.run)
        self.naz.clicked.connect(self.run1)
        self.A.clicked.connect(self.vrun2)
        self.AD.clicked.connect(self.vrun3)
        self.B.clicked.connect(self.vrun4)
        self.C.clicked.connect(self.vrun5)
        self.CD.clicked.connect(self.vrun6)
        self.D.clicked.connect(self.vrun7)
        self.DD.clicked.connect(self.vrun8)
        self.E.clicked.connect(self.vrun9)
        self.F.clicked.connect(self.vrun10)
        self.FD.clicked.connect(self.vrun11)
        self.G.clicked.connect(self.vrun12)
        self.GD.clicked.connect(self.vrun13)

    def run(self):
        self.instr.setText("ГИТАРА")
        self.A.clicked.connect(self.run2)
        self.AD.clicked.connect(self.run3)
        self.B.clicked.connect(self.run4)
        self.C.clicked.connect(self.run5)
        self.CD.clicked.connect(self.run6)
        self.D.clicked.connect(self.run7)
        self.DD.clicked.connect(self.run8)
        self.E.clicked.connect(self.run9)
        self.F.clicked.connect(self.run10)
        self.FD.clicked.connect(self.run11)
        self.G.clicked.connect(self.run12)
        self.GD.clicked.connect(self.run13)

    def run2(self):
        pygame.mixer.init()
        pygame.mixer.music.load('A.mp3')
        pygame.mixer.music.play()

    def run3(self):
        pygame.mixer.init()
        pygame.mixer.music.load('A#.mp3')
        pygame.mixer.music.play()

    def run4(self):
        pygame.mixer.init()
        pygame.mixer.music.load('B.mp3')
        pygame.mixer.music.play()

    def run5(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C.mp3')
        pygame.mixer.music.play()

    def run6(self):
        pygame.mixer.init()
        pygame.mixer.music.load('C#.mp3')
        pygame.mixer.music.play()

    def run7(self):
        pygame.mixer.init()
        pygame.mixer.music.load('D.mp3')
        pygame.mixer.music.play()

    def run8(self):
        pygame.mixer.init()
        pygame.mixer.music.load('D#.mp3')
        pygame.mixer.music.play()

    def run9(self):
        pygame.mixer.init()
        pygame.mixer.music.load('E.mp3')
        pygame.mixer.music.play()

    def run10(self):
        pygame.mixer.init()
        pygame.mixer.music.load('F.mp3')
        pygame.mixer.music.play()

    def run11(self):
        pygame.mixer.init()
        pygame.mixer.music.load('F#.mp3')
        pygame.mixer.music.play()

    def run12(self):
        pygame.mixer.init()
        pygame.mixer.music.load('G.mp3')
        pygame.mixer.music.play()

    def run13(self):
        pygame.mixer.init()
        pygame.mixer.music.load('G#.mp3')
        pygame.mixer.music.play()

    def run1(self):
        self.instr.setText("АЛЬТ")
        self.A.clicked.connect(self.vrun2)
        self.AD.clicked.connect(self.vrun3)
        self.B.clicked.connect(self.vrun4)
        self.C.clicked.connect(self.vrun5)
        self.CD.clicked.connect(self.vrun6)
        self.D.clicked.connect(self.vrun7)
        self.DD.clicked.connect(self.vrun8)
        self.E.clicked.connect(self.vrun9)
        self.F.clicked.connect(self.vrun10)
        self.FD.clicked.connect(self.vrun11)
        self.G.clicked.connect(self.vrun12)
        self.GD.clicked.connect(self.vrun13)

    def vrun2(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VA.mp3')
        pygame.mixer.music.play()

    def vrun3(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VA#.mp3')
        pygame.mixer.music.play()

    def vrun4(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VB.mp3')
        pygame.mixer.music.play()

    def vrun5(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VC.mp3')
        pygame.mixer.music.play()

    def vrun6(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VC#.mp3')
        pygame.mixer.music.play()

    def vrun7(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VD.mp3')
        pygame.mixer.music.play()

    def vrun8(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VD#.mp3')
        pygame.mixer.music.play()

    def vrun9(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VE.mp3')
        pygame.mixer.music.play()

    def vrun10(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VF.mp3')
        pygame.mixer.music.play()

    def vrun11(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VF#.mp3')
        pygame.mixer.music.play()

    def vrun12(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VG.mp3')
        pygame.mixer.music.play()

    def vrun13(self):
        pygame.mixer.init()
        pygame.mixer.music.load('VG#.mp3')
        pygame.mixer.music.play()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
