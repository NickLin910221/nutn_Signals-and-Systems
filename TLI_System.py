# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import wave
import datetime
import numpy as np
import scipy
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from scipy.io.wavfile import write
from scipy.signal import filtfilt


class Ui_MainWindow(object):
    def initUi(self, MainWindow):
        file_path1 = ""; file_name = ""

        MainWindow.setObjectName("TLI System")
        MainWindow.resize(1600, 1000)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## button0
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1480, 27, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.openFileNameDialog1)

        ## button1
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1480, 510, 100, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.play)
        
        ## button2
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1370, 510, 100, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.filt_bandpass)

        ## button3
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1260, 510, 100, 31))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.filt_bandstop)

        ## button4
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1150, 510, 100, 31))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.filt_highpass)

        ## button5
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1040, 510, 100, 31))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.filt_lowpass)

        #LineEdit with high cut
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(650, 510, 100, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("200")

        #LineEdit with low cut
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(900, 510, 100, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setText("400")

        ## vertical and horizontal line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 485, 1600, 20))
        self.line.setToolTip("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        ## Label 1 & 3
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(135, 20, 1000, 41))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 510, 100, 31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 510, 100, 31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # Widget
        self.widget = QtWidgets.QGraphicsView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 70, 1560, 410))
        self.widget.setObjectName("widget")

        self.widget3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 555, 1560, 410))
        self.widget3.setObjectName("widget3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def play(self):
        playsound('example.wav')
    
    def filt_bandpass(self):
        try:
            wave_data, time = self.read_wave_data(self.file_path1)
            result = self.filter(wave_data[0], "bandpass")
            plot2 = Figure_Canvas()
            plot2.test(time, result)
            graphicscene2 = QtWidgets.QGraphicsScene()
            graphicscene2.addWidget(plot2)
            self.widget3.setScene(graphicscene2)
            self.widget3.show()
        except TypeError:
            pass
        except AttributeError:
            pass

    def filt_bandstop(self):
        try:
            wave_data, time = self.read_wave_data(self.file_path1)
            result = self.filter(wave_data[0], "bandstop")
            plot2 = Figure_Canvas()
            plot2.test(time, result)
            graphicscene2 = QtWidgets.QGraphicsScene()
            graphicscene2.addWidget(plot2)
            self.widget3.setScene(graphicscene2)
            self.widget3.show()
        except TypeError:
            pass
        except AttributeError:
            pass

    def filt_highpass(self):
        try:
            wave_data, time = self.read_wave_data(self.file_path1)
            result = self.filter(wave_data[0], "highpass")
            plot2 = Figure_Canvas()
            plot2.test(time, result)
            graphicscene2 = QtWidgets.QGraphicsScene()
            graphicscene2.addWidget(plot2)
            self.widget3.setScene(graphicscene2)
            self.widget3.show()
        except TypeError:
            pass
        except AttributeError:
            pass

    def filt_lowpass(self):
        try:
            wave_data, time = self.read_wave_data(self.file_path1)
            result = self.filter(wave_data[0], "lowpass")
            plot2 = Figure_Canvas()
            plot2.test(time, result)
            graphicscene2 = QtWidgets.QGraphicsScene()
            graphicscene2.addWidget(plot2)
            self.widget3.setScene(graphicscene2)
            self.widget3.show()
        except TypeError:
            pass
        except AttributeError:
            pass

    def setlabel2name(self, table_name):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", table_name))
        self.file_path1 = table_name
        self.read_wave_data(self.file_path1)

    def openFileNameDialog1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Python Files (*.wav)", options=options)
        if fileName:
            self.setlabel2name(table_name = fileName)

    def filter(self, signal, filter):
        fs = 44100.0
        nyq = 0.5 * fs
        order = 9
        if filter == "bandpass":
            b, a = scipy.signal.butter(order, [int(self.lineEdit.text())/ nyq, int(self.lineEdit2.text())/ nyq], 'bandpass', analog = False)
        elif filter == "bandstop":
            b, a = scipy.signal.butter(order, [int(self.lineEdit.text())/ nyq, int(self.lineEdit2.text())/ nyq], 'bandstop', analog = False)
        elif filter == "lowpass":
            b, a = scipy.signal.butter(order, [int(self.lineEdit.text())/ nyq], 'lowpass', analog = False)
        elif filter == "highpass":
            b, a = scipy.signal.butter(order, [int(self.lineEdit2.text())/ nyq], 'highpass', analog = False)
        y = scipy.signal.filtfilt(b, a, signal, axis = 0)
        
        samplerate = 44100
        t = np.linspace(0., 1., samplerate)
        data = y
        write(f'example_{datetime.datetime.now():%Y%m%d %H%M%S}.wav', samplerate, data.astype(np.int16))
        return y

    def read_wave_data(self, file_path):
        #open a wave file, and return a Wave_read object
        f = wave.open(file_path,"rb")
        #read the wave's format infomation,and return a tuple
        params = f.getparams()
        #get the info
        nchannels, sampwidth, framerate, nframes = params[:4]
        #Reads and returns nframes of audio, as a string of bytes. 
        str_data = f.readframes(nframes)
        #close the stream
        f.close()
        #turn the wave's data to array
        wave_data = np.fromstring(str_data, dtype = np.short)
        #for the data is stereo,and format is LRLRLR...
        #shape the array to n*2(-1 means fit the y coordinate)
        wave_data.shape = -1, 2
        #transpose the data
        wave_data = wave_data.T
        #calculate the time bar
        time = np.arange(0, nframes) * (1.0/framerate)

        plot1 = Figure_Canvas()
        plot1.test(time, wave_data[0])
        graphicscene1 = QtWidgets.QGraphicsScene()
        graphicscene1.addWidget(plot1)
        self.widget.setScene(graphicscene1)
        self.widget.show()

        return wave_data, time

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "File Name :"))
        self.pushButton_1.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_3.setText(_translate("MainWindow", "BandPass"))
        self.pushButton_4.setText(_translate("MainWindow", "BandStop"))
        self.pushButton_5.setText(_translate("MainWindow", "HighPass"))
        self.pushButton_6.setText(_translate("MainWindow", "LowPass"))
        self.label_2.setText(_translate("MainWindow", "No File !"))
        self.label_3.setText(_translate("MainWindow", "LowCut : "))
        self.label_4.setText(_translate("MainWindow", "HighCut : "))

class Figure_Canvas(FigureCanvas):

    def __init__(self, parent=None, width=45, height=10, dpi=0):
        fig = Figure(figsize=(width, height), dpi=100)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(212)

    def test(self, x, y):
        x = x
        y = y
        self.axes.plot(x, y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.initUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())