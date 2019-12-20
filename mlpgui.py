import sys
import os
from PyQt5 import QtWidgets
from mlpregressor import *

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.regresyon = MlpRegressor()
        self.buffer = []

    def init_ui(self):

        self.setWindowTitle("Deep Learning")
        self.dosyayolu = QtWidgets.QLabel()
        self.iterasyon = QtWidgets.QLabel("Iterasyon")
        self.iterasyon_text = QtWidgets.QLineEdit()
        self.testsize = QtWidgets.QLabel("Test Size")
        self.testsize_text = QtWidgets.QLineEdit()
        self.randomstate = QtWidgets.QLabel("Random State")
        self.randomstate_text = QtWidgets.QLineEdit()
        self.testtext = QtWidgets.QLabel("Test Result")
        self.egitimtext = QtWidgets.QLabel("Train Result")
        self.girdibas = QtWidgets.QLabel("Input Beginning")

        self.girdison = QtWidgets.QLabel("Input Last")
        self.ciktibas = QtWidgets.QLabel("Target Beginning")
        self.ciktison = QtWidgets.QLabel("Target Last")
        self.test = QtWidgets.QLabel()
        self.egitim = QtWidgets.QLabel()

        self.girdibas_text = QtWidgets.QComboBox()
        self.girdison_text = QtWidgets.QComboBox()

        self.ciktibas_text = QtWidgets.QComboBox()
        self.ciktison_text = QtWidgets.QComboBox()

        self.hidden = QtWidgets.QLabel("Hidden Layer\n(default 1)")
        self.hidden_text = QtWidgets.QLineEdit()

        self.activationtext = QtWidgets.QLabel("Activation F")
        self.activation = QtWidgets.QComboBox()
        self.analiz = QtWidgets.QPushButton("Analyze")
        self.ac = QtWidgets.QPushButton("File Reader")
        h_box2 = QtWidgets.QHBoxLayout()
        h_box = QtWidgets.QHBoxLayout()

        h_box6 = QtWidgets.QHBoxLayout()
        h_box7 = QtWidgets.QHBoxLayout()
        h_box4 = QtWidgets.QHBoxLayout()
        h_box5 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()                                         #gui
        h_box8 = QtWidgets.QHBoxLayout()
        h_box9 = QtWidgets.QHBoxLayout()
        self.h_box10 = QtWidgets.QHBoxLayout()
        h_box11 = QtWidgets.QHBoxLayout()
        h_box12 = QtWidgets.QHBoxLayout()
        h_box13 = QtWidgets.QHBoxLayout()
        h_box14 = QtWidgets.QHBoxLayout()
        h_box115 = QtWidgets.QHBoxLayout()
        h_boxactivation = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.girdibas)
        h_box.addStretch(21)
        h_box.addWidget(self.girdibas_text)
        h_box.addStretch(200)
        h_box2.addWidget(self.girdison)
        h_box2.addStretch(72)
        h_box2.addWidget(self.girdison_text)
        h_box2.addStretch(600)
        h_box3.addWidget(self.ciktibas)
        h_box3.addStretch(29)
        h_box3.addWidget(self.ciktibas_text)
        h_box3.addStretch(600)
        h_box4.addWidget(self.ciktison)
        h_box4.addStretch(64)
        h_box4.addWidget(self.ciktison_text)
        h_box4.addStretch(600)
        self.listwidget = QtWidgets.QListWidget()



        
        h_box5.addWidget(self.iterasyon)
        h_box5.addStretch(65)
        h_box5.addWidget(self.iterasyon_text)
        h_box5.addStretch(600)
        h_box6.addWidget(self.testsize)
        h_box6.addStretch(71)
        h_box6.addWidget(self.testsize_text)
        h_box6.addStretch(600)
        h_box7.addWidget(self.randomstate)
        h_box7.addStretch(33)
        h_box7.addWidget(self.randomstate_text)
        h_box7.addStretch(600)

        h_boxactivation.addWidget(self.activationtext)
        h_boxactivation.addStretch(63)
        h_boxactivation.addWidget(self.activation)
        h_boxactivation.addStretch(600)

        self.v_box = QtWidgets.QVBoxLayout()
        h_box11.addStretch(100)
        h_box115.addStretch()
        h_box115.addWidget(self.dosyayolu)
        h_box115.addStretch()

        h_box11.addWidget(self.listwidget)
        h_box11.addStretch(100)

        h_box13.addWidget(self.egitimtext)
        h_box13.addWidget(self.egitim)
        h_box13.addStretch()

        h_box13.addWidget(self.testtext)
        h_box13.addWidget(self.test)
        h_box13.addStretch()
        h_box.addWidget(self.ac)
        h_box.addSpacing(100)


        self.maetraintextdol = QtWidgets.QLabel()
        self.maetesttextdol = QtWidgets.QLabel()
        self.maetraintext = QtWidgets.QLabel("Mae Train")
        self.maetesttext = QtWidgets.QLabel("Mae Test")
        self.katmanalan = QtWidgets.QPushButton("Create Area")
        h_box9.addStretch(100)
        h_box9.addWidget(self.katmanalan)
        h_box9.addStretch(300)

        h_box14.addWidget(self.maetraintext)
        h_box14.addWidget(self.maetraintextdol)
        h_box14.addStretch(50)
        h_box14.addWidget(self.maetesttext)

        h_box14.addWidget(self.maetesttextdol)
        h_box14.addStretch(49)
        h_box8.addWidget(self.hidden)
        h_box8.addStretch(40)
        h_box8.addWidget(self.hidden_text)
        h_box8.addStretch(600)
        h_box8.addStretch()
        h_box12.addWidget(self.analiz)

        self.v_box.addLayout(h_box)
        self.v_box.addLayout(h_box2)

        self.v_box.addLayout(h_box3)

        self.v_box.addLayout(h_box4)

        self.v_box.addLayout(h_box5)

        self.v_box.addLayout(h_box6)
        self.v_box.addLayout(h_box7)
        self.v_box.addLayout(h_boxactivation)
        self.v_box.addLayout(h_box8)
        self.v_box.addLayout(h_box9)
        self.v_box.addLayout(self.h_box10)
        self.v_box.addLayout(h_box115)
        self.v_box.addLayout(h_box11)
        self.v_box.addLayout(h_box12)
        self.v_box.addLayout(h_box13)
        self.v_box.addLayout(h_box14)

        self.setGeometry(600, 200, 650, 550)

        self.setLayout(self.v_box)


        self.analiz.clicked.connect(self.analizEt)
        self.ac.clicked.connect(self.dosyaAc)
        self.katmanalan.clicked.connect(self.gizliKatman)

        self.ciktibas_text.currentIndexChanged.connect(self.selectionchange)
        self.show()

    def selectionchange(self,value):

        if value+1 == self.regresyon.columns():
            self.ciktison_text.setVisible(False)
            self.ciktison.setVisible(False)
        else:
            self.ciktison_text.setVisible(True)
            self.ciktison.setVisible(True)

        
    def hiddenFonk(self):
        if  len(self.hidden_text.text()) <= 0:
            return 0
        else:
            return int(self.hidden_text.text())                              #hidden layer fonk


    def gizliKatman(self):

        if len(self.buffer) > 0:
            for i in self.buffer:
                i.setVisible(False)
            self.buffer.clear()

        for i in range(self.hiddenFonk()):
            self.buffer.append(QtWidgets.QLineEdit())
            self.h_box10.addWidget(self.buffer[i])                                #button click up hidden layer



    def analizEt(self):
        control = self.hiddenFonk()

        if self.ciktison_text.isVisible():

            arr = self.regresyon.inpTar(int(self.girdibas_text.currentText()),int(self.girdison_text.currentText()),int(self.ciktibas_text.currentText()),int(self.ciktison_text.currentText()))
        else:
            arr = self.regresyon.inpTar(int(self.girdibas_text.currentText()), int(self.girdison_text.currentText()),int(self.ciktibas_text.currentText()), 0)
        data = self.regresyon.encoder(arr[0],arr[1])
                                                                                         #MLPRegressor interface
        if(control != 0):
            buff = []
            for i in range(len(self.buffer)):
                buff.append(int(self.buffer[i].text()))
            buff = tuple(buff)
            egitimdat = self.regresyon.egitim(data[0],data[1],int(self.iterasyon_text.text()),float(self.testsize_text.text()),int(self.randomstate_text.text()),buff,self.activation.currentText())
        else:
            egitimdat = self.regresyon.egitim(data[0],data[1], int(self.iterasyon_text.text()),
                                              float(self.testsize_text.text()), int(self.randomstate_text.text()),
                                              0,self.activation.currentText())
        self.egitim.setText(str(egitimdat[0]))
        self.test.setText(str(egitimdat[1]))

        mae = self.regresyon.mae()

        self.maetraintextdol.setText(str(mae[0]))
        self.maetesttextdol.setText(str(mae[1]))

      #  return self.liste

    def dataColumns(self):

        for i in range(len(self.file.columns)):                                                                     #data columns for listwidget
            self.listwidget.addItem("{} --------> {}".format(i+1,self.file.columns[i]))

    def dosyaAc(self):
        self.dosyaismi = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Ac", os.getenv("HOME"))                 #file upload
        print(self.dosyaismi)
        self.dosyayolu.setText(self.dosyaismi[0])

        self.file = self.regresyon.dataOku(self.dosyaismi[0])

        self.summ = self.regresyon.columns()
        self.comboColumns()
        self.dataColumns()
        self.activationFonk()

    def comboColumns(self):
        for i in range(1,self.summ+1):
            self.girdibas_text.addItem(str(i))
            self.girdison_text.addItem(str(i))													#for combobox columns
            self.ciktibas_text.addItem(str(i))
            if (self.ciktison_text.isVisible()):
                self.ciktison_text.addItem(str(i))

    def activationFonk(self):
        self.activation.addItem("relu")
        self.activation.addItem("identity")
        self.activation.addItem("logistic")
        self.activation.addItem("tanh")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    menu = Pencere()                                                                    #run
    sys.exit(app.exec_())
