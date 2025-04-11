import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


def load_URL():
    url = url_bar.text()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # Add https:// if it's missing
    browser.setUrl(QUrl(url))  # Convert string to QUrl


def go_back():
    browser.back()  # Navigate backward


def go_forward():
    browser.forward()  # Navigate forward


def reload_page():
    browser.reload()  # Reload the current page


# Create the application
application = QApplication(sys.argv)

# Main window setup
window = QMainWindow()
window.setWindowTitle("Saddam Tech Browser")
window.setGeometry(100, 100, 1000, 600)

# Create the QWebEngineView browser object
browser = QWebEngineView()
browser.setUrl(QUrl("https://www.google.com"))  # Default to Google

# Set up the URL bar and buttons in a horizontal layout
url_bar = QLineEdit()
load_button = QPushButton("Load URL")
load_button.clicked.connect(load_URL)

# Horizontal layout for URL bar and load button
url_layout = QHBoxLayout()
url_layout.addWidget(url_bar)
url_layout.addWidget(load_button)

# Set up the back, forward, and reload buttons
back_button = QPushButton("Back")
back_button.clicked.connect(go_back)

forward_button = QPushButton("Forward")
forward_button.clicked.connect(go_forward)

reload_button = QPushButton("Reload")
reload_button.clicked.connect(reload_page)

# Horizontal layout for navigation buttons
nav_buttons_layout = QHBoxLayout()
nav_buttons_layout.addWidget(back_button)
nav_buttons_layout.addWidget(forward_button)
nav_buttons_layout.addWidget(reload_button)

# Create the main layout and add the widgets
main_layout = QVBoxLayout()
main_layout.addLayout(url_layout)  # Add URL bar and load button
main_layout.addLayout(nav_buttons_layout)  # Add navigation buttons
main_layout.addWidget(browser)  # Add the browser

# Set up the central widget with the main layout
central_widget = QWidget()
central_widget.setLayout(main_layout)
window.setCentralWidget(central_widget)

# Show the window
window.show()

# Execute the application
sys.exit(application.exec())