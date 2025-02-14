#!/usr/bin/env python3
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(500, 500, 700, 700)
        self.setWindowTitle("Soil Plasticity Constitutive Models Testing")
        layout = QGridLayout()
        self.setLayout(layout)

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "General Information")
        tabwidget.addTab(SecondTab(), "Material Constants")
        tabwidget.addTab(ThirdTab(), "Water Retention Model")
        tabwidget.addTab(FourthTab(), "Initial Conditions")
        tabwidget.addTab(FifthTab(), "Test")
        tabwidget.addTab(SixthTab(), "Export")
        layout.addWidget(tabwidget, 0, 0)

    #def update(self):
     #   self.label.adjustSize()

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()

        self.information = QLabel("This program is to be used in conjuction with the FORTRAN program developed in Siterenios 2016.")
        self.information2 = QLabel("\n\nPlease fill in the appropriate data fields in each tab.")
        self.information3 = QLabel("\n\n\n\nWhen you have filled out all necessary information navigate to the export tab and click export.")
        self.information4 = QLabel("\n\n\n\n\n\nAn ASCII text file will be produced that can be used to perform the soils analysis.")
        self.information5 = QLabel("\n\n\n\n\n\n\n\nPlease ensure that you have filled out all fields, any empty fields will default to 0.")

        self.nameNT = QLabel("NT: ")
        self.nameNT.setToolTip("stress space dimension, 4 for single point and 2D, 6 only for 3D-Abaqus")
        self.nameEditNT = QLineEdit()
        self.nameEditNT.editingFinished.connect(self.updatevariable)

#add objects to layout
        layout = QGridLayout()

        layout.addWidget(self.information, 0, 0, 1, 0)
        layout.addWidget(self.information2, 0, 0, 1, 0)
        layout.addWidget(self.information3, 0, 0, 1, 0)
        layout.addWidget(self.information4, 0, 0, 1, 0)
        layout.addWidget(self.information5, 0, 0, 1, 0)

        layout.addWidget(self.nameNT, 6, 0)
        layout.addWidget(self.nameEditNT, 6, 1)

        self.setLayout(layout)

    def updatevariable(self):
        global NT

        if self.nameEditNT.text() == '':
            NT = 0
        else:
            NT = self.nameEditNT.text()


class SecondTab(QWidget):
    def __init__(self):
        super().__init__()

#IMODE1, IMODE2 IMODE3, IMODE4, DDE, RATIO, IDIR, IREV, PEAK, NPRINT, MAXLOOP, NCYCL label and LineEdit boxes

        self.nameIMODE1 = QLabel("IMODE(1): ")
        self.nameIMODE1.setToolTip("1 - Undrained, 2 - Drained")
        self.comboboxIMODE1 = QComboBox()
        self.comboboxIMODE1.addItem("Undrained")
        self.comboboxIMODE1.addItem("Drained")
        self.comboboxIMODE1.currentTextChanged.connect(self.update_combobox_IMODE1)

        self.nameIMODE2 = QLabel("IMODE(2): ")
        self.nameIMODE2.setToolTip("1 – Triaxial, 2- Plane Strain, 3 – DSS, 4 – Proportional TRX, 5 – Isotropic, 6 – constant p, 7 – 1D")
        self.comboboxIMODE2 = QComboBox()
        self.comboboxIMODE2.addItem("Triaxial")
        self.comboboxIMODE2.addItem("Plane Strain")
        self.comboboxIMODE2.addItem("DSS")
        self.comboboxIMODE2.addItem("Proportional Triaxial")
        self.comboboxIMODE2.addItem("Isotropic")
        self.comboboxIMODE2.addItem("Constant p")
        self.comboboxIMODE2.addItem("1D Consolidation")
        self.comboboxIMODE2.currentTextChanged.connect(self.update_combobox_IMODE2)

        self.nameIMODE3 = QLabel("IMODE(3): ")
        self.nameIMODE3.setToolTip("1 – stress controlled, 2- strain controlled")
        self.comboboxIMODE3 = QComboBox()
        self.comboboxIMODE3.addItem("Stress Controlled")
        self.comboboxIMODE3.addItem("Strain Controlled")
        self.comboboxIMODE3.currentTextChanged.connect(self.update_combobox_IMODE3)

        self.nameIMODE4 = QLabel("IMODE(4): ")
        self.nameIMODE4.setToolTip("1 - constant suction, 2- Wetting/Drying")
        self.comboboxIMODE4 = QComboBox()
        self.comboboxIMODE4.addItem("Constant Suction")
        self.comboboxIMODE4.addItem("Wetting/Drying")
        self.comboboxIMODE4.currentTextChanged.connect(self.update_combobox_IMODE4)

        self.nameDDE = QLabel("DDE: ")
        self.nameDDE.setToolTip("infinitesimal increment")
        self.nameEditDDE = QLineEdit()
        self.nameEditDDE.editingFinished.connect(self.updatevariable)

        self.nameRATIO = QLabel("RATIO: ")
        self.nameRATIO.setToolTip("stress ratio (for proportional TRX)")
        self.nameEditRATIO = QLineEdit()
        self.nameEditRATIO.editingFinished.connect(self.updatevariable)

        self.nameIDIR = QLabel("IDIR: ")
        self.nameIDIR.setToolTip("direction for loading (+1 loading, -1 unloading)")
        self.nameEditIDIR = QLineEdit()
        self.nameEditIDIR.editingFinished.connect(self.updatevariable)

        self.nameIREV = QLabel("IREV: ")
        self.nameIREV.setToolTip("")
        self.nameEditIREV = QLineEdit()
        self.nameEditIREV.editingFinished.connect(self.updatevariable)

        self.namePEAK = QLabel("PEAK: ")
        self.namePEAK.setToolTip("maximum stress or strain level to be reached")
        self.nameEditPEAK = QLineEdit()
        self.nameEditPEAK.editingFinished.connect(self.updatevariable)

        self.nameNPRINT = QLabel("NPRINT: ")
        self.nameNPRINT.setToolTip("number of outputs")
        self.nameEditNPRINT = QLineEdit()
        self.nameEditNPRINT.editingFinished.connect(self.updatevariable)

        self.nameMAXLOOP = QLabel("MAXLOOP: ")
        self.nameMAXLOOP.setToolTip("maximum increment applied")
        self.nameEditMAXLOOP = QLineEdit()
        self.nameEditMAXLOOP.editingFinished.connect(self.updatevariable)

        self.nameNCYCL = QLabel("NCYCL: ")
        self.nameNCYCL.setToolTip("number of tests")
        self.nameEditNCYCL = QLineEdit()
        self.nameEditNCYCL.editingFinished.connect(self.updatevariable)

#add objects to layout
        layout = QGridLayout()

        layout.addWidget(self.nameIMODE1, 1, 1)
        layout.addWidget(self.comboboxIMODE1, 1, 2)
        layout.addWidget(self.nameIMODE2, 2, 1)
        layout.addWidget(self.comboboxIMODE2, 2, 2)
        layout.addWidget(self.nameIMODE3, 3, 1)
        layout.addWidget(self.comboboxIMODE3, 3, 2)
        layout.addWidget(self.nameIMODE4, 4, 1)
        layout.addWidget(self.comboboxIMODE4, 4, 2)
        layout.addWidget(self.nameDDE, 5, 1)
        layout.addWidget(self.nameEditDDE, 5, 2)
        layout.addWidget(self.nameRATIO, 6, 1)
        layout.addWidget(self.nameEditRATIO, 6, 2)
        layout.addWidget(self.nameIDIR, 7, 1)
        layout.addWidget(self.nameEditIDIR, 7, 2)
        layout.addWidget(self.nameIREV, 8, 1)
        layout.addWidget(self.nameEditIREV, 8, 2)
        layout.addWidget(self.namePEAK, 9, 1)
        layout.addWidget(self.nameEditPEAK, 9, 2)
        layout.addWidget(self.nameNPRINT, 10, 1)
        layout.addWidget(self.nameEditNPRINT, 10, 2)
        layout.addWidget(self.nameMAXLOOP, 11, 1)
        layout.addWidget(self.nameEditMAXLOOP, 11, 2)
        layout.addWidget(self.nameNCYCL, 12, 1)
        layout.addWidget(self.nameEditNCYCL, 12, 2)

        self.setLayout(layout)

#updates to variables via combobox menus
    def update_combobox_IMODE1(self):
        global IMODE1
        if self.comboboxIMODE1.currentText() == "Undrained":
            IMODE1 = 1
        elif self.comboboxIMODE1.currentText() == "Drained":
            IMODE1 = 2

    def update_combobox_IMODE2(self):
        global IMODE2
        if self.comboboxIMODE2.currentText() == "Triaxial":
            IMODE2 = 1
        elif self.comboboxIMODE2.currentText() == "Plane Strain":
            IMODE2 = 2
        elif self.comboboxIMODE2.currentText() == "DSS":
            IMODE2 = 3
        elif self.comboboxIMODE2.currentText() == "Proportional Triaxial":
            IMODE2 = 4
        elif self.comboboxIMODE2.currentText() == "Isotropic":
            IMODE2 = 5
        elif self.comboboxIMODE2.currentText() == "Constant p":
            IMODE2 = 6
        elif self.comboboxIMODE2.currentText() == "1D Consolidation":
            IMODE2 = 7

    def update_combobox_IMODE3(self):
        global IMODE3
        if self.comboboxIMODE3.currentText() == "Stress Controlled":
            IMODE3 = 1
        elif self.comboboxIMODE3.currentText() == "Strain Controlled":
            IMODE3 = 2

    def update_combobox_IMODE4(self):
        global IMODE4
        if self.comboboxIMODE4.currentText() == "Constant Suction":
            IMODE4 = 1
        elif self.comboboxIMODE4.currentText() == "Wetting/Drying":
            IMODE4 = 2

#set up updates to global variables    
    def updatevariable(self):
        global DDE, RATIO, IDIR, IREV, PEAK, NPRINT, MAXLOOP, NCYCL

        if self.nameEditDDE.text() == '':
            DDE = 0
        else:
            DDE = self.nameEditDDE.text()
    
        if self.nameEditRATIO.text() == '':
            RATIO = 0
        else:
            RATIO = self.nameEditRATIO.text()
        
        if self.nameEditIDIR.text() == '':
            IDIR = 0
        else:
            IDIR = self.nameEditIDIR.text()

        if self.nameEditIREV.text() == '':
            IREV = 0
        else:
            IREV = self.nameEditIREV.text()

        if self.nameEditPEAK.text() == '':
            PEAK = 0
        else:
            PEAK = self.nameEditPEAK.text()

        if self.nameEditNPRINT.text() == '':
            NPRINT = 0
        else:
            NPRINT = self.nameEditNPRINT.text()            

        if self.nameEditMAXLOOP.text() == '':
            MAXLOOP = 0
        else:
            MAXLOOP = self.nameEditMAXLOOP.text()

        if self.nameEditNCYCL.text() == '':
            NCYCL = 0
        else:
            NCYCL = self.nameEditNCYCL.text()


class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

#PAR1 - PAR17, PAR21 - PAR26 Label and LineEdit boxes
        self.namePAR1 = QLabel("2G/K = PAR(1): ")
        self.namePAR1.setToolTip("elasticity parameter (controls shear modulus)")
        self.nameEditPAR1 = QLineEdit()
        self.nameEditPAR1.editingFinished.connect(self.updatevariable)

        self.namePAR2 = QLabel("\u03BB(0) = PAR(2): ")
        self.namePAR2.setToolTip("saturated compressibility")
        self.nameEditPAR2 = QLineEdit()
        self.nameEditPAR2.editingFinished.connect(self.updatevariable)

        self.namePAR3 = QLabel("\u03BA = PAR(3): ")
        self.namePAR3.setToolTip("elasticity parameter (controls bulk modulus)")
        self.nameEditPAR3 = QLineEdit()
        self.nameEditPAR3.editingFinished.connect(self.updatevariable)

        self.namePAR4 = QLabel("\u03B2 = PAR(4): ")
        self.namePAR4.setToolTip("unsaturated compressibility")
        self.nameEditPAR4 = QLineEdit()
        self.nameEditPAR4.editingFinished.connect(self.updatevariable)

        self.namePAR5 = QLabel("r = PAR(5): ")
        self.namePAR5.setToolTip("unsaturated compressibility")
        self.nameEditPAR5 = QLineEdit()
        self.nameEditPAR5.editingFinished.connect(self.updatevariable)

        self.namePAR6 = QLabel("\u03B3 = PAR(6): ")
        self.namePAR6.setToolTip("unsaturated compressibility")
        self.nameEditPAR6 = QLineEdit()
        self.nameEditPAR6.editingFinished.connect(self.updatevariable)

        self.namePAR7 = QLabel("Pc = PAR(7): ")
        self.namePAR7.setToolTip("reference pressure")
        self.nameEditPAR7 = QLineEdit()
        self.nameEditPAR7.editingFinished.connect(self.updatevariable)

        self.namePAR8 = QLabel("Niso = PAR(8): ")
        self.namePAR8.setToolTip("position of the NCL")
        self.nameEditPAR8 = QLineEdit()
        self.nameEditPAR8.editingFinished.connect(self.updatevariable)

        self.namePAR9 = QLabel("\u0393 = PAR(9): ")
        self.namePAR9.setToolTip("position of the CSL")
        self.nameEditPAR9 = QLineEdit()
        self.nameEditPAR9.editingFinished.connect(self.updatevariable)

        self.namePAR10 = QLabel("rb = PAR(10): ")
        self.namePAR10.setToolTip("compressibility framework parameter")
        self.nameEditPAR10 = QLineEdit()
        self.nameEditPAR10.editingFinished.connect(self.updatevariable)

        self.namePAR11 = QLabel("X = PAR(11): ")
        self.namePAR11.setToolTip("flow rule (controls dilatancy)")
        self.nameEditPAR11 = QLineEdit()
        self.nameEditPAR11.editingFinished.connect(self.updatevariable)

        self.namePAR12 = QLabel("\u03A8 = PAR(12): ")
        self.namePAR12.setToolTip("hardening rule")
        self.nameEditPAR12 = QLineEdit()
        self.nameEditPAR12.editingFinished.connect(self.updatevariable)

        self.namePAR13 = QLabel("nevp = PAR(13): ")
        self.namePAR13.setToolTip("void – not used, default 0")
        self.nameEditPAR13 = QLineEdit()
        self.nameEditPAR13.editingFinished.connect(self.updatevariable)

        self.namePAR14 = QLabel("neqp = PAR(14): ")
        self.namePAR14.setToolTip("hardening rule parameter")
        self.nameEditPAR14 = QLineEdit()
        self.nameEditPAR14.editingFinished.connect(self.updatevariable)

        self.namePAR15 = QLabel("nv exp = PAR(15): ")
        self.namePAR15.setToolTip("void – not used, default 0")
        self.nameEditPAR15 = QLineEdit()
        self.nameEditPAR15.editingFinished.connect(self.updatevariable)

        self.namePAR16 = QLabel("nv exp = PAR(16): ")
        self.namePAR16.setToolTip("void – not used, default 0")
        self.nameEditPAR16 = QLineEdit()
        self.nameEditPAR16.editingFinished.connect(self.updatevariable)

        self.namePAR17 = QLabel("PAR(17): ")
        self.namePAR17.setToolTip("void – not used, default 0")
        self.nameEditPAR17 = QLineEdit()
        self.nameEditPAR17.editingFinished.connect(self.updatevariable)

        self.namePAR21 = QLabel("PAR(21): ")
        self.namePAR21.setToolTip("YS aspect ratio; 1st deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditPAR21 = QLineEdit()
        self.nameEditPAR21.editingFinished.connect(self.updatevariable)

        self.namePAR22 = QLabel("PAR(22): ")
        self.namePAR22.setToolTip("YS aspect ratio; 2nd deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditPAR22 = QLineEdit()
        self.nameEditPAR22.editingFinished.connect(self.updatevariable)

        self.namePAR23 = QLabel("PAR(23): ")
        self.namePAR23.setToolTip("YS aspect ratio; 3rd deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditPAR23 = QLineEdit()
        self.nameEditPAR23.editingFinished.connect(self.updatevariable)

        self.namePAR24 = QLabel("PAR(24): ")
        self.namePAR24.setToolTip("PPS aspect ratio; 1st deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditPAR24 = QLineEdit()
        self.nameEditPAR24.editingFinished.connect(self.updatevariable)

        self.namePAR25 = QLabel("PAR(25): ")
        self.namePAR25.setToolTip("YS aspect ratio; 2nd deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditPAR25 = QLineEdit()
        self.nameEditPAR25.editingFinished.connect(self.updatevariable)

        self.namePAR26 = QLabel("PAR(26): ")
        self.namePAR26.setToolTip("YS aspect ratio; 3rd deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditPAR26 = QLineEdit()
        self.nameEditPAR26.editingFinished.connect(self.updatevariable)


#add objects to layout
        layout = QGridLayout()

        layout.addWidget(self.namePAR1, 1, 1)
        layout.addWidget(self.nameEditPAR1, 1, 2)
        layout.addWidget(self.namePAR2, 2, 1)
        layout.addWidget(self.nameEditPAR2, 2, 2)
        layout.addWidget(self.namePAR3, 3, 1)
        layout.addWidget(self.nameEditPAR3, 3, 2)
        layout.addWidget(self.namePAR4, 4, 1)
        layout.addWidget(self.nameEditPAR4, 4, 2)
        layout.addWidget(self.namePAR5, 5, 1)
        layout.addWidget(self.nameEditPAR5, 5, 2)
        layout.addWidget(self.namePAR6, 6, 1)
        layout.addWidget(self.nameEditPAR6, 6, 2)
        layout.addWidget(self.namePAR7, 7, 1)
        layout.addWidget(self.nameEditPAR7, 7, 2)
        layout.addWidget(self.namePAR8, 8, 1)
        layout.addWidget(self.nameEditPAR8, 8, 2)
        layout.addWidget(self.namePAR9, 9, 1)
        layout.addWidget(self.nameEditPAR9, 9, 2)
        layout.addWidget(self.namePAR10, 10, 1)
        layout.addWidget(self.nameEditPAR10, 10, 2)
        layout.addWidget(self.namePAR11, 11, 1)
        layout.addWidget(self.nameEditPAR11, 11, 2)
        layout.addWidget(self.namePAR12, 12, 1)
        layout.addWidget(self.nameEditPAR12, 12, 2)
        layout.addWidget(self.namePAR13, 13, 1)
        layout.addWidget(self.nameEditPAR13, 13, 2)
        layout.addWidget(self.namePAR14, 14, 1)
        layout.addWidget(self.nameEditPAR14, 14, 2)
        layout.addWidget(self.namePAR15, 15, 1)
        layout.addWidget(self.nameEditPAR15, 15, 2)
        layout.addWidget(self.namePAR16, 16, 1)
        layout.addWidget(self.nameEditPAR16, 16, 2)
        layout.addWidget(self.namePAR17, 17, 1)
        layout.addWidget(self.nameEditPAR17, 17, 2)
        layout.addWidget(self.namePAR21, 21, 1)
        layout.addWidget(self.nameEditPAR21, 21, 2)
        layout.addWidget(self.namePAR22, 22, 1)
        layout.addWidget(self.nameEditPAR22, 22, 2)
        layout.addWidget(self.namePAR23, 23, 1)
        layout.addWidget(self.nameEditPAR23, 23, 2)
        layout.addWidget(self.namePAR24, 24, 1)
        layout.addWidget(self.nameEditPAR24, 24, 2)
        layout.addWidget(self.namePAR25, 25, 1)
        layout.addWidget(self.nameEditPAR25, 25, 2)
        layout.addWidget(self.namePAR26, 26, 1)
        layout.addWidget(self.nameEditPAR26, 26, 2)


        self.setLayout(layout)

#set up updates to global variables    
    def updatevariable(self):
        global PAR1, PAR2, PAR3, PAR4, PAR5, PAR6, PAR7, PAR8, PAR9, PAR10, PAR11, PAR12, PAR13, PAR14, PAR15, PAR16, PAR17, PAR21, PAR22, PAR23, PAR24, PAR25, PAR26 

        if self.nameEditPAR1.text() == '':
            PAR1 = 0
        else:
            PAR1 = self.nameEditPAR1.text()

        if self.nameEditPAR2.text() == '':
            PAR2 = 0
        else:
            PAR2 = self.nameEditPAR2.text()

        if self.nameEditPAR3.text() == '':
            PAR3 = 0
        else:
            PAR3 = self.nameEditPAR3.text()

        if self.nameEditPAR4.text() == '':
            PAR4 = 0
        else:
            PAR4 = self.nameEditPAR4.text()

        if self.nameEditPAR5.text() == '':
            PAR5 = 0
        else:
            PAR5 = self.nameEditPAR5.text()

        if self.nameEditPAR6.text() == '':
            PAR6 = 0
        else:
            PAR6 = self.nameEditPAR6.text()

        if self.nameEditPAR7.text() == '':
            PAR7 = 0
        else:
            PAR7 = self.nameEditPAR7.text()

        if self.nameEditPAR8.text() == '':
            PAR8 = 0
        else:
            PAR8 = self.nameEditPAR8.text()

        if self.nameEditPAR9.text() == '':
            PAR9 = 0
        else:
            PAR9 = self.nameEditPAR9.text()

        if self.nameEditPAR10.text() == '':
            PAR10 = 0
        else:
            PAR10 = self.nameEditPAR10.text()

        if self.nameEditPAR11.text() == '':
            PAR11 = 0
        else:
            PAR11 = self.nameEditPAR11.text()

        if self.nameEditPAR12.text() == '':
            PAR12 = 0
        else:
            PAR12 = self.nameEditPAR12.text()

        if self.nameEditPAR13.text() == '':
            PAR13 = 0
        else:
            PAR13 = self.nameEditPAR13.text()

        if self.nameEditPAR14.text() == '':
            PAR14 = 0
        else:
            PAR14 = self.nameEditPAR14.text()

        if self.nameEditPAR15.text() == '':
            PAR15 = 0
        else:
            PAR15 = self.nameEditPAR15.text()

        if self.nameEditPAR16.text() == '':
            PAR16 = 0
        else:
            PAR16 = self.nameEditPAR16.text()

        if self.nameEditPAR17.text() == '':
            PAR17 = 0
        else:
            PAR17 = self.nameEditPAR17.text()

        if self.nameEditPAR21.text() == '':
            PAR21 = 0
        else:
            PAR21 = self.nameEditPAR21.text()

        if self.nameEditPAR22.text() == '':
            PAR22 = 0
        else:
            PAR22 = self.nameEditPAR22.text()

        if self.nameEditPAR23.text() == '':
            PAR23 = 0
        else:
            PAR23 = self.nameEditPAR23.text()

        if self.nameEditPAR24.text() == '':
            PAR24 = 0
        else:
            PAR24 = self.nameEditPAR24.text()
        
        if self.nameEditPAR25.text() == '':
            PAR25 = 0
        else:
            PAR25 = self.nameEditPAR25.text()

        if self.nameEditPAR26.text() == '':
            PAR26 = 0
        else:
            PAR26 = self.nameEditPAR26.text()

class FourthTab(QWidget):
    def __init__(self):
        super().__init__()

        #SWCCPAR1 - 5 label and LineEdit boxes
        self.nameSWCCPAR1 = QLabel("N = SWCCPAR(1): ")
        self.nameSWCCPAR1.setToolTip("Effective Sr parameter")
        self.nameEditSWCCPAR1 = QLineEdit()
        self.nameEditSWCCPAR1.editingFinished.connect(self.updatevariable)

        self.nameSWCCPAR2 = QLabel("\u03C6 = SWCCPAR(2): ")
        self.nameSWCCPAR2.setToolTip("Gallipoli WRC parameter")
        self.nameEditSWCCPAR2 = QLineEdit()
        self.nameEditSWCCPAR2.editingFinished.connect(self.updatevariable)

        self.nameSWCCPAR3 = QLabel("n = SWCCPAR(3): ")
        self.nameSWCCPAR3.setToolTip("Gallipoli WRC parameter")
        self.nameEditSWCCPAR3 = QLineEdit()
        self.nameEditSWCCPAR3.editingFinished.connect(self.updatevariable)

        self.nameSWCCPAR4 = QLabel("m = SWCCPAR(4): ")
        self.nameSWCCPAR4.setToolTip("Gallipoli WRC parameter")
        self.nameEditSWCCPAR4 = QLineEdit()
        self.nameEditSWCCPAR4.editingFinished.connect(self.updatevariable)

        self.nameSWCCPAR5 = QLabel("\u03C8 = SWCCPAR(5): ")
        self.nameSWCCPAR5.setToolTip("Gallipoli WRC parameter")
        self.nameEditSWCCPAR5 = QLineEdit()
        self.nameEditSWCCPAR5.editingFinished.connect(self.updatevariable)                

#add objects to layout
        layout = QGridLayout()

        layout.addWidget(self.nameSWCCPAR1, 0, 1)
        layout.addWidget(self.nameEditSWCCPAR1, 0, 2)
        layout.addWidget(self.nameSWCCPAR2, 1, 1)
        layout.addWidget(self.nameEditSWCCPAR2, 1, 2)
        layout.addWidget(self.nameSWCCPAR3, 2, 1)
        layout.addWidget(self.nameEditSWCCPAR3, 2, 2)
        layout.addWidget(self.nameSWCCPAR4, 3, 1)
        layout.addWidget(self.nameEditSWCCPAR4, 3, 2)
        layout.addWidget(self.nameSWCCPAR5, 4, 1)
        layout.addWidget(self.nameEditSWCCPAR5, 4, 2)

        self.setLayout(layout)

#set up updates to global variables    
    def updatevariable(self):
        global SWCCPAR1, SWCCPAR2, SWCCPAR3, SWCCPAR4, SWCCPAR5

        if self.nameEditSWCCPAR1.text() == '':
            SWCCPAR1 = 0
        else:
            SWCCPAR1 = self.nameEditSWCCPAR1.text()

        if self.nameEditSWCCPAR2.text() == '':
            SWCCPAR2 = 0
        else:
            SWCCPAR2 = self.nameEditSWCCPAR2.text()

        if self.nameEditSWCCPAR3.text() == '':
            SWCCPAR3 = 0
        else:
            SWCCPAR3 = self.nameEditSWCCPAR3.text()

        if self.nameEditSWCCPAR4.text() == '':
            SWCCPAR4 = 0
        else:
            SWCCPAR4 = self.nameEditSWCCPAR4.text()

        if self.nameEditSWCCPAR5.text() == '':
            SWCCPAR5 = 0
        else:
            SWCCPAR5 = self.nameEditSWCCPAR5.text()

class FifthTab(QWidget):
    def __init__(self):
        super().__init__()

        #QH1 - 6_3 S, S1 - 3, SUC label and LineEdit boxes
        self.nameQH1 = QLabel("QH(1): ")
        self.nameQH1.setToolTip("a, isotropic hardening")
        self.nameEditQH1 = QLineEdit()
        self.nameEditQH1.editingFinished.connect(self.updatevariable)

        self.nameQH2 = QLabel("v(s) = QH(2): ")
        self.nameQH2.setToolTip("specific volume")
        self.nameEditQH2 = QLineEdit()
        self.nameEditQH2.editingFinished.connect(self.updatevariable)

        self.nameQH3 = QLabel("NSURF = QH(3): ")
        self.nameQH3.setToolTip("flag identifier; 0 - elastic state, 1 - plastic state")
        self.nameEditQH3 = QLineEdit()
        self.nameEditQH3.editingFinished.connect(self.updatevariable)

        self.nameQH4 = QLabel("Evp = QH(4): ")
        self.nameQH4.setToolTip("accumulated plastic volumetric strains")
        self.nameEditQH4 = QLineEdit()
        self.nameEditQH4.editingFinished.connect(self.updatevariable)

        self.nameQH5 = QLabel("Evq = QH(5): ")
        self.nameQH5.setToolTip("accumulated plastic deviatoric strains")
        self.nameEditQH5 = QLineEdit()
        self.nameEditQH5.editingFinished.connect(self.updatevariable)

        self.nameQH6_1 = QLabel("b1 = QH(6): ")
        self.nameQH6_1.setToolTip("anisotropy tensor; 1st deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditQH6_1 = QLineEdit()
        self.nameEditQH6_1.editingFinished.connect(self.updatevariable)

        self.nameQH6_2 = QLabel("b2 = QH(6): ")
        self.nameQH6_2.setToolTip("anisotropy tensor; 2nd deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditQH6_2 = QLineEdit()
        self.nameEditQH6_2.editingFinished.connect(self.updatevariable)

        self.nameQH6_3 = QLabel("b3 = QH(6): ")
        self.nameQH6_3.setToolTip("anisotropy tensor; 3rd deviatoric plane of the Transformed Stress Space (TSS)")
        self.nameEditQH6_3 = QLineEdit()
        self.nameEditQH6_3.editingFinished.connect(self.updatevariable)

        self.nameS = QLabel("S: ")
        self.nameS.setToolTip("mean stress")
        self.nameEditS = QLineEdit()
        self.nameEditS.editingFinished.connect(self.updatevariable)

        self.nameS1 = QLabel("S(1): ")
        self.nameS1.setToolTip("1st deviatoric stress component in TSS")
        self.nameEditS1 = QLineEdit()
        self.nameEditS1.editingFinished.connect(self.updatevariable)

        self.nameS2 = QLabel("S(2): ")
        self.nameS2.setToolTip("2nd deviatoric stress component in TSS")
        self.nameEditS2 = QLineEdit()
        self.nameEditS2.editingFinished.connect(self.updatevariable)

        self.nameS3 = QLabel("S(3): ")
        self.nameS3.setToolTip("3rd deviatoric stress component in TSS")
        self.nameEditS3 = QLineEdit()
        self.nameEditS3.editingFinished.connect(self.updatevariable)

        self.nameSUC = QLabel("SUC: ")
        self.nameSUC.setToolTip("Suction Value")
        self.nameEditSUC = QLineEdit()
        self.nameEditSUC.editingFinished.connect(self.updatevariable)   

#add objects to layout
        layout = QGridLayout()

        layout.addWidget(self.nameQH1, 0, 1)
        layout.addWidget(self.nameEditQH1, 0, 2)
        layout.addWidget(self.nameQH2, 1, 1)
        layout.addWidget(self.nameEditQH2, 1, 2)
        layout.addWidget(self.nameQH3, 2, 1)
        layout.addWidget(self.nameEditQH3, 2, 2)
        layout.addWidget(self.nameQH4, 3, 1)
        layout.addWidget(self.nameEditQH4, 3, 2)
        layout.addWidget(self.nameQH5, 4, 1)
        layout.addWidget(self.nameEditQH5, 4, 2)
        layout.addWidget(self.nameQH6_1, 5, 1)
        layout.addWidget(self.nameEditQH6_1, 5, 2)
        layout.addWidget(self.nameQH6_2, 6, 1)
        layout.addWidget(self.nameEditQH6_2, 6, 2)
        layout.addWidget(self.nameQH6_3, 7, 1)
        layout.addWidget(self.nameEditQH6_3, 7, 2)
        layout.addWidget(self.nameS, 8, 1)
        layout.addWidget(self.nameEditS, 8, 2)
        layout.addWidget(self.nameS1, 9, 1)
        layout.addWidget(self.nameEditS1, 9, 2)
        layout.addWidget(self.nameS2, 10, 1)
        layout.addWidget(self.nameEditS2, 10, 2)
        layout.addWidget(self.nameS3, 11, 1)
        layout.addWidget(self.nameEditS3, 11, 2)
        layout.addWidget(self.nameSUC, 12, 1)
        layout.addWidget(self.nameEditSUC, 12, 2)

        self.setLayout(layout)

#set up updates to global variables    
    def updatevariable(self):
        global QH1, QH2, QH3, QH4, QH5, QH6_1, QH6_2, QH6_3, S, S1, S2, S3, SUC

        if self.nameEditQH1.text() == '':
            QH1 = 0
        else:
            QH1 = self.nameEditQH1.text()

        if self.nameEditQH2.text() == '':
            QH2 = 0
        else:
            QH2 = self.nameEditQH2.text()

        if self.nameEditQH3.text() == '':
            QH3 = 0
        else:
            QH3 = self.nameEditQH3.text()

        if self.nameEditQH4.text() == '':
            QH4 = 0
        else:
            QH4 = self.nameEditQH4.text()

        if self.nameEditQH5.text() == '':
            QH5 = 0
        else:
            QH5 = self.nameEditQH5.text()

        if self.nameEditQH6_1.text() == '':
            QH6_1 = 0
        else:
            QH6_1 = self.nameEditQH6_1.text()

        if self.nameEditQH6_2.text() == '':
            QH6_2 = 0
        else:
            QH6_2 = self.nameEditQH6_2.text()

        if self.nameEditQH6_3.text() == '':
            QH6_3 = 0
        else:
            QH6_3 = self.nameEditQH6_3.text()

        if self.nameEditS.text() == '':
            S = 0
        else:
            S = self.nameEditS.text()

        if self.nameEditS1.text() == '':
            S1 = 0
        else:
            S1 = self.nameEditS1.text()

        if self.nameEditS2.text() == '':
            S2 = 0
        else:
            S2 = self.nameEditS2.text()

        if self.nameEditS3.text() == '':
            S3 = 0
        else:
            S3 = self.nameEditS3.text()

        if self.nameEditSUC.text() == '':
            SUC = 0
        else:
            SUC = self.nameEditSUC.text()

class SixthTab(QWidget):
    def __init__(self):
        super().__init__()

#export button
        self.exportButton = QtWidgets.QPushButton(self)
        self.exportButton.setText("Export as txt")
        self.exportButton.clicked.connect(self.write_txt)

#add objects to layout
        layout = QGridLayout()
        layout.addWidget(self.exportButton, 1, 1)
        self.setLayout(layout)

#write to txt file    
    def write_txt(self):
        with open('export.txt', 'w') as f:
            f.writelines(str(NT) + "\n")
            f.writelines(str(PAR1) +" "+ str(PAR2) +" "+ str(PAR3)+ "\n")
            f.writelines(str(PAR4) +" "+ str(PAR5) +" "+ str(PAR6) + "\n")
            f.writelines(str(PAR7) + "\n")
            f.writelines(str(PAR8) +" "+ str(PAR9) +" "+ str(PAR10) + "\n")
            f.writelines(str(PAR11) + "\n")
            f.writelines(str(PAR12) +" "+ str(PAR14) + "\n")
            f.writelines(str(PAR21) +" "+ str(PAR22) +" "+ str(PAR23) + "\n")
            f.writelines(str(PAR24) +" "+ str(PAR25) +" "+ str(PAR26) + "\n")
            f.writelines(str(SWCCPAR1) + "\n")
            f.writelines(str(SWCCPAR2) +" "+ str(SWCCPAR3) +" "+ str(SWCCPAR4) +" "+ str(SWCCPAR5) + "\n")
            f.writelines(str(QH1) + "\n")
            f.writelines(str(QH2) + "\n")
            f.writelines(str(QH3) + "\n")
            f.writelines(str(QH4) +" "+ str(QH5) + "\n")
            f.writelines(str(QH6_1) +" "+ str(QH6_2) +" "+ str(QH6_3) + "\n")
            f.writelines(str(S) +" "+ str(S1) +" "+ str(S2) +" "+ str(S3) + "\n")
            f.writelines(str(SUC) + "\n")
            f.writelines(str(MAXLOOP) + "\n")
            f.writelines(str(NCYCL) + "\n")
            f.writelines(str(IMODE1) +" "+ str(IMODE2) +" "+ str(IMODE3) +" "+ str(IMODE4) +" "+ str(DDE) +" "+ str(RATIO) +" "+ str(IDIR) +" "+ str(IREV) +" "+ str(PEAK) +" "+ str(NPRINT) + "\n")


#VARIABLES
NT = 0

IMODE1, IMODE2, IMODE3, IMODE4, DDE, RATIO, IDIR, IREV, PEAK, NPRINT, MAXLOOP, NCYCL = 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0

PAR1, PAR2, PAR3, PAR4, PAR5, PAR6, PAR7, PAR8, PAR9, PAR10, PAR11, PAR12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 
PAR13, PAR14, PAR15, PAR16, PAR17, PAR21,PAR22, PAR23, PAR24, PAR25, PAR26 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

SWCCPAR1, SWCCPAR2, SWCCPAR3, SWCCPAR4, SWCCPAR5 = 0, 0, 0, 0, 0

QH1, QH2, QH3, QH4, QH5, QH6_1, QH6_2, QH6_3 = 0, 0, 0, 0, 0, 0, 0, 0

S, S1, S2, S3, SUC = 0, 0, 0, 0, 0

#window loop
def window():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())

window()
