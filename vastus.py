# SOVELLUS LED-KOMPONENTTIEN ETUVASTUSTEN ARVON LASKENTAAN
# ========================================================

# KIRJASTOT JA MODUULIT
# ---------------------

# Vakiokirjastot käyttöjärjestelmälle ja käynnistysparametreille
import os
import sys

# Qt-vimpaimet
from PySide6 import QtWidgets

# Käyttöliittymätiedosto
from vastus_ui import Ui_MainWindow

# LUOKAT
# ------

# Pääikkunan luokka
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Luodaan pääikkuna konvertoidun ui-tiedoston perusteella
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculatePushButton.setEnabled(False)
        

        # SIGNAALIT
        # ---------

        # Laske-painike
        self.ui.calculatePushButton.clicked.connect(self.calculateResistance)
        
        # Syöttöjännite
        self.ui.supplyVoltage.valueChanged.connect(self.checkSanity)

    # SLOTIT
    # ------
    def checkSanity(self):
        self.sanity = True
        if self.ui.supplyVoltage.value() == 0:
          self.sanity = False

        if self.ui.forwardVoltage.value() == 0:
          self.sanity = False

        if self.ui.forwardCurrent.value() == 0:
           self.sanity = False

        self.ui.calculatePushButton.setEnabled(self.sanity)
        
    def calculateResistance(self):
        supplyVoltage = self.ui.supplyVoltage.value()
        ledForwardCurrent = self.ui.forwardCurrent.value()/1000
        ledForwardVoltage = self.ui.forwardVoltage.value()

        resistance = (supplyVoltage - ledForwardVoltage)/ledForwardCurrent
        self.ui.resistanceLcd.display(resistance)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()