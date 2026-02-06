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

        # Laske-painiketta painetaa
        self.ui.calculatePushButton.clicked.connect(self.calculateResistance)
        
        # Jännitesäätimen arvo muuttuu
        self.ui.voltageDial.valueChanged.connect(self.setSupplyVoltage)
        # Syöttöjännitteen arvo muuttuu
        self.ui.supplyVoltage.valueChanged.connect(self.checkSanity)

        # LED:n kynnysjännite muuttuu
        self.ui.forwardVoltage.valueChanged.connect(self.checkSanity)

        # LED:n virta muuttuu
        self.ui.forwardCurrent.valueChanged.connect(self.checkSanity)

    # SLOTIT
    # ------

    def setSupplyVoltage(self):
     self.ui.supplyVoltage.setValue(self.ui.voltageDial.value())

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
        print(resistance)
        
        resistanceString = str(round(resistance,1))
        print(resistanceString)
        digit1 = resistanceString[0]
        digit2 = resistanceString[1]
        multiplier4stripe = 10**(len(resistanceString)-4)
        print(multiplier4stripe)
        multiplienr5stripe = 10**(len(resistanceString)-5)
        digitValueString = digit1 + "." + digit2
        digitValue = float(digitValueString)
        resistorStandardValues = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7,
                                  3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5,
                                   8.2, 9.1]
        chosenValue = 0

        for value in resistorStandardValues:
            if value >= digitValue:
                chosenValue = value
                break
            
        print(chosenValue)
        chosenDigitValueString = str(chosenValue)
        stripeDigit1 = chosenDigitValueString[0]
        stripeDigit2 = chosenDigitValueString[2]

        stripeColors = {"0": "black",
                        "1": "brown",
                        "2": "red",
                        "3": "orange",
                        "4": "yellow",
                        "5": "green",
                        "6": "blue",
                        "7": "violet",
                        "8": "grey",
                        "9": "white"
                        }
        
        stripe1 = stripeColors[stripeDigit1]
        stripe2 = stripeColors[stripeDigit2]
        print(stripe1)
        print(stripe2)

        multiplierStripeColors = {
                        1: "black",
                        10: "brown",
                        100: "red",
                        1000: "orange",
                        10000: "yellow",
                        100000: "green",
                        1000000: "blue",
                        10000000: "violet"
        }
        multiplierStripe = multiplierStripeColors[multiplier4stripe]
        print(multiplierStripe)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()