import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui_MainWindow import Ui_MainWindow  # Import the generated design.py file

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin"

# Conversion rates (as provided in the tkinter example)
conversion_rates = {
    "GEL": {"GEL": 1.0, "USD": 0.37, "EUR": 0.34, "GBP": 0.28},
    "USD": {"GEL": 2.69, "USD": 1.0, "EUR": 0.91, "GBP": 0.76},
    "EUR": {"GEL": 2.97, "USD": 1.1, "EUR": 1.0, "GBP": 0.84},
    "GBP": {"GEL": 3.53, "USD": 1.31, "EUR": 1.19, "GBP": 1.0}
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Connect buttons to functions
        self.loginButton.clicked.connect(self.handle_login)
        self.convertButton.clicked.connect(self.convert_currency)
        self.clearButton.clicked.connect(self.clear)
        self.logoutButton.clicked.connect(self.logout)

        # Connect the show password checkbox
        # self.showPasswordCheckBox.stateChanged.connect(self.toggle_password_visibility)

        # Set initial page
        self.stackedWidget.setCurrentIndex(0)

    def handle_login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()

        if username == USERNAME and password == PASSWORD:
            self.stackedWidget.setCurrentIndex(1)  # Go to the next page
        else:
            QMessageBox.warning(self, "Error", "Incorrect username or password.")

    def convert_currency(self):
        from_currency = self.fromCurrencyCombo.currentText()
        to_currency = self.toCurrencyCombo.currentText()
        amount = self.amountInput.text()

        if not amount:
            self.resultLabel.setText("Please enter an amount.")
            return

        try:
            amount = float(amount)
            converted_amount = amount * conversion_rates[from_currency][to_currency]
            self.resultLabel.setText(f"{converted_amount:.2f} {to_currency}")
        except ValueError:
            self.resultLabel.setText("Invalid input. Please enter a numeric value.")

    def clear(self):
        self.amountInput.clear()
        self.resultLabel.clear()
        self.fromCurrencyCombo.setCurrentIndex(0)
        self.toCurrencyCombo.setCurrentIndex(0)

    def logout(self):
        self.usernameInput.clear()
        self.passwordInput.clear()
        self.clear()
        self.stackedWidget.setCurrentIndex(0)  # Go back to the login page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
