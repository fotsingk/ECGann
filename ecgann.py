# This Python file uses the following encoding: utf-8
# import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget
from PySide6.QtGui import QIcon
import pandas as pd
import os


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_ECGann
from ui_dialog import Ui_Dialog
import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use("QtAgg")

basedir = os.path.dirname(__file__)
filedir = os.path.expanduser('~\Documents\BioSigAnnotator Files\Database')
backdir = os.path.expanduser('~\Documents\BioSigAnnotator Files\Backup')
maxToSave = 100
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('samples')
        self.axes.set_ylabel("amplitudes")
        self.axes.set_title(" No DATA")
        super(MplCanvas, self).__init__(fig)


class ECGann(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # --------- Data and variables inside the GUI -----
        self.data = []
        self.signalNumber = 0       # actual signal plotted
        self.nextSigAnn = 0         #Next signal number to annotate
        self.numberOfSignals = 0    #The total of signals
        self.fileName = ""
        self.annCountForBck = 0
        self.isSavedWork = False

        # --------- The GUI ---------
        self.ui = Ui_ECGann()
        self.setWindowIcon(QIcon(os.path.join(basedir, r"img\ecgScorerIcon.png")))
        self.ui.setupUi(self)
        self.ui.figCanvas = MplCanvas(self.ui.centralwidget)
        self.ui.figCanvas.setObjectName(u"figure")
        self.ui.gridLayout.addWidget(self.ui.figCanvas, 1, 0, 1, 1)
        self.ui.labelGroupBox.setEnabled(False)
        self.ui.plotControlGroup.setEnabled(False)
        #@ ------ Radio Button ------------#
        self.ui.exploRadioButton.toggled.connect(self.explo_or_lab_mode)

        # ---- Button interraction ------- #
        # Load Button and continue button
        self.ui.loadButton.clicked.connect(self.test_load_data)
        self.ui.continuButton.clicked.connect(self.continu_annotation)
        # save and exit Button
        self.ui.saveButton.clicked.connect(self.save_data)
        #check button
        self.ui.checkButton.clicked.connect(self.check_labelization)

        # next Button
        self.ui.nextButton.clicked.connect(self.next_signal)

        # previous Button
        self.ui.prevButton.clicked.connect(self.prev_signal)

        # good Button
        self.ui.goodButton.clicked.connect(self.annot_as_good)
        # bad Button
        self.ui.badButton.clicked.connect(self.annot_as_bad)
        # unknown Button
        self.ui.unknownButton.clicked.connect(self.annot_as_unknown)

    # radio button function
    def explo_or_lab_mode(self, selected):
        if self.fileName == "":
            self.messageDialog(f'''
            *****************
            Load signal First 
            or Continue Previous Work
            **************************''')
        else: 
            if selected: # exploration mode selected
                self.ui.labelGroupBox.setEnabled(False)
                self.ui.nextButton.setEnabled(True)
                self.ui.labelGroupBox.setStyleSheet(
                u"background-color: rgba(43, 43, 43, 10);")
            else: #labelization mode
                self.ui.labelGroupBox.setEnabled(True)
                self.ui.nextButton.setEnabled(False)
                self.ui.labelGroupBox.setStyleSheet(
                u"background-color: rgb(243, 243, 243);")
                self.signalNumber = self.nextSigAnn
                self.update_plot()

    # Load data with loadButton
    def test_load_data(self):
        if self.fileName == '': #Nothing is Loaded
            self.load_data()
        else:
            self.get_labelization_info()
            if (self.remainToLabel == self.numberOfSignals) | (self.remainToLabel == 0) | (self.isSavedWork==True):
                self.load_data()
            else:
                dlog = Ui_Dialog(self)
                if dlog.exec():
                    self.load_data()
                else:
                    pass

    def load_data(self):
        path = filedir
        fileNamePath, _ = QFileDialog.getOpenFileName(self,
                        "Select Database File", path, "Text Files (*.txt *.csv)")
        if fileNamePath:
            self.data = []
            self.signalNumber = 0       # actual signal plotted
            self.nextSigAnn = 0         #Next signal number to annotate
            self.numberOfSignals = 0    #The total of signals
            self.fileName = ""
            self.annCountForBck = 0
            self.isSavedWork = False

            self.ui.plotControlGroup.setEnabled(True)
            self.ui.labelGroupBox.setEnabled(False)
                        #raw_data = open(fileNamePath, mode='rb')
                        #self.data = loadtxt(raw_data, delimiter=',')
            self.data = pd.read_csv(fileNamePath, header=None)
            self.data = self.data.values
            self.numberOfSignals = self.data.shape[1]
                        # initialize variable for annotation
            fileName = fileNamePath[fileNamePath.rfind('/')+1 : -4] #♥recupère le nom du fichier
            self.fileNamePath = fileNamePath
            self.fileName = fileName
            self.annotationFileName = fileName+"_annotation.txt"
                        #"index":list(range(self.numberOfSignals)),
            self.sigAnnMat = pd.DataFrame({"label":list(range(self.numberOfSignals))})
            self.sigAnnMat["label"] = self.sigAnnMat["label"].astype(str)
                        #print(self.sigAnnMat)
            self.update_plot()
            self.explo_or_lab_mode(self.ui.exploRadioButton.isChecked())

    def test_continue_annotation(self):
        if self.fileName == '': #Nothing is Loaded
            self.continu_annotation()
        else:
            self.get_labelization_info()
            if (self.remainToLabel == self.numberOfSignals) | (self.remainToLabel == 0) | (self.isSavedWork==True):
                self.continu_annotation()
            else:
                dlog = Ui_Dialog(self)
                if dlog.exec():
                    self.continu_annotation()
                else:
                    pass
    
    def continu_annotation(self):
        path = backdir
        infoFileNamePath, _ = QFileDialog.getOpenFileName(self,
            "Select File to continue your work", path, "Text Files (*.dat)")
        if infoFileNamePath != "":
            # load information
            self.infoFile = pd.read_csv(infoFileNamePath)
            fileNamePath = self.infoFile["fileNamePath"].values
            fileNamePath = fileNamePath[0]
            #print(fileNamePath)
            self.data = pd.read_csv(fileNamePath, header=None)
            self.data = self.data.values
            self.numberOfSignals = self.data.shape[1]
            self.remainToLabel = self.infoFile.remainToLabel[0]
            self.nextSigAnn = self.infoFile['nextSigAnn'][0]
            print(self.nextSigAnn)
            # initialize variable for annotation
            fileName = fileNamePath[fileNamePath.rfind('/')+1 : -4]
            self.fileNamePath = fileNamePath
            self.fileName = fileName
            self.annotationFileName = "annotation_"+fileName+".txt"

            self.sigAnnMat = pd.read_csv(self.infoFile.sigAnnMat[0], index_col=0)
            #print(self.sigAnnMat)
            self.ui.labelGroupBox.setDisabled(False)
            self.ui.plotControlGroup.setDisabled(False)

            if self.remainToLabel == 0:
                self.messageDialog(f'''
                -------------------------------------------
                | This DataSet had been labelled already  |
                -------------------------------------------
                ''')
                self.nextSigAnn = self.nextSigAnn - 1
                self.ui.exploRadioButton.setChecked(True)
            else:
                self.messageDialog(f'''
                *--------- Welcome Back !!! ---------*
                *    Database and annotation file loaded succesfully   *
                * --------       INFO    -------------*
                DataBase Name : {self.fileName}
                Total Number of Signals : {self.numberOfSignals}
                already labelled : { self.numberOfSignals - self.remainToLabel }
                remain to label : {self.remainToLabel}
                *--------------------------------------*
                ''')
                self.ui.labRadioButton.setChecked(True)
            self.signalNumber = self.nextSigAnn
            self.explo_or_lab_mode(self.ui.exploRadioButton.isChecked())
            self.update_plot()

    # Save Button
    def save_data(self):
        if self.fileName =="":
            self.messageDialog(f'''
            *******************
            Nothing to save
            Load signal First
            *******************''')
        else:
            self.get_labelization_info()
            if  self.remainToLabel<=10 & self.remainToLabel>0:
                self.messageDialog(f'''Just Complete The labelization
                its remain only {self.remainToLabel} signal(s)''')
            elif self.remainToLabel == self.numberOfSignals:
                self.messageDialog(f'''Nothing to save
                None signal have been labelled''')
            else:
                self.call_save(folder = QFileDialog.getExistingDirectory())

    def call_save(self, folder=backdir):
        #folder = QFileDialog.getExistingDirectory()
        if folder:
            annName = folder+"/"+self.annotationFileName
            self.sigAnnMat.to_csv(annName) #Ann file
            infoName = folder+"/"+self.fileName+"_info.dat"
            #update file infoFile
            self.infoFile = pd.DataFrame(self.infoFile, index=range(1))
            self.infoFile['sigAnnMat'] = annName
            self.infoFile.to_csv(infoName)
            #self.close()
            self.messageDialog("The work has been saved")
            self.isSavedWork=True
        else:
            self.messageDialog("The work is unsaved")

    def auto_save(self, folder=backdir):
        #folder = QFileDialog.getExistingDirectory()
        self.get_labelization_info()
        annName = folder+"/"+self.annotationFileName
        self.sigAnnMat.to_csv(annName) #Ann file
        infoName = folder+"/"+self.fileName+"_ibck.dat"
        #update file infoFile
        self.infoFile = pd.DataFrame(self.infoFile, index=range(1))
        self.infoFile['sigAnnMat'] = annName
        self.infoFile.to_csv(infoName)
        #self.close()
    


    # check button function
    def get_labelization_info(self):

        condition = (self.sigAnnMat["label"]=='good')| (self.sigAnnMat["label"]=='bad') | (self.sigAnnMat["label"]=='unknown')
        self.remainToLabel = self.sigAnnMat[~condition].shape[0]
        self.infoMessage = f'''
            *---------------- INFO ----------------*
             DataBase Name : {self.fileName}
             Total Number of Signals : {self.numberOfSignals}
             already labelled : { self.numberOfSignals - self.remainToLabel }
             remain to label : {self.remainToLabel}
            *--------------------------------------*
                '''
        if self.remainToLabel==0:
            self.labelizationStatus = "completed"
        else:
            self.labelizationStatus = "uncompleted"

        self.infoFile = {
        'fileNamePath': self.fileNamePath,
        'status':self.labelizationStatus,
        'remainToLabel': self.remainToLabel,
        'nextSigAnn': self.nextSigAnn}


    def check_labelization(self):
        if self.fileName =="":
            self.messageDialog(f'''
            *******************
            No Information
            Load signal First
            *******************''')
        else:
            self.get_labelization_info()
            self.messageDialog(self.infoMessage)


    def update_plot(self):
        self.ui.figCanvas.axes.cla()
        self.ui.figCanvas.axes.plot(self.data[:, self.signalNumber], linewidth=1)
        self.ui.figCanvas.axes.set_xlabel('samples')
        self.ui.figCanvas.axes.set_ylabel('amplitudes')
        self.ui.figCanvas.axes.set_title(f"DATABASE Name : { self.fileName } ")
        self.ui.figCanvas.draw()
        #update the label
        self.ui.sigNumber.setText(" signal "+str(self.signalNumber+1)+" over "+str(self.numberOfSignals))

    # Next Buton
    def next_signal(self):
        if self.signalNumber == self.numberOfSignals - 1:
            self.messageDialog("End of the List, No More Signals")
        else:
            self.signalNumber += 1
            self.update_plot()

    # Previous Button
    def prev_signal(self):
        if self.signalNumber == 0:
            self.messageDialog("Begining of the List, No previous Signals")
        else:
            self.signalNumber -= 1
            self.update_plot()


    # Annotation function
    def annot_as_good(self):
        self.sigAnnMat.iloc[self.signalNumber] = 'good'
        self.nextSigAnn += 1
        self.annCountForBck += 1
        #print(self.annCountForBck)
        if self.annCountForBck == maxToSave:
            self.auto_save()
            self.annCountForBck = 0

        self.next_signal()

    def annot_as_bad(self):
        self.sigAnnMat.iloc[self.signalNumber] = 'bad'
        self.nextSigAnn += 1
        self.annCountForBck += 1
        #print(self.annCountForBck)
        if self.annCountForBck == maxToSave:
            self.auto_save()
            self.annCountForBck = 0

        self.next_signal()

    def annot_as_unknown(self):
        self.sigAnnMat.iloc[self.signalNumber] = 'unknown'
        self.nextSigAnn += 1
        self.annCountForBck += 1
        #print(self.annCountForBck)
        if self.annCountForBck == maxToSave:
            self.auto_save()
            self.annCountForBck = 0

        self.next_signal()

 #--------- utilities -----------------
    def messageDialog(self, messageText):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Message")
        dlg.setStyleSheet(u"text-align: center")
        dlg.setText(messageText)
        dlg.show()
        

if __name__ == "__main__":
    app = QApplication([])
    widget = ECGann()
    widget.setWindowTitle("BioSig Annotator")
    widget.show()
    app.exec()
