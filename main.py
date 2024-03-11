
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout,QPushButton,QAction,QMainWindow,QLabel



import socket
import threading
import alias

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.user = alias.dialogue()
        
        self.terminate=f"{self.user} has left the chat\n"
        self.users = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.begin()
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('Chat Window')
        self.setGeometry(100, 100, 500, 500)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.txt = QLabel("Howdy!Welcome to the chatroom")
        self.layout.addWidget(self.txt)

        self.txt1 = QTextEdit()

        self.txt1.setReadOnly(True)
        self.layout.addWidget(self.txt1)
        
 

        self.tplace = QTextEdit()
        self.tplace.setFixedHeight(70)
        self.layout.addWidget(self.tplace)

        self.sendButton = QPushButton('Send')
        self.sendButton.clicked.connect(self.send)
        self.sendButton.setFixedSize(45,45)
        self.layout.addWidget(self.sendButton)

        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('File')
        endChatAction = QAction('End Chat', self)
        endChatAction.triggered.connect(self.end_chat)
        fileMenu.addAction(endChatAction)
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

    def send(self):
        user_input = self.tplace.toPlainText().strip()
        if not user_input:
            return
        letter = f"{self.user}: {user_input}\n"
        self.txt1.append(letter)
        self.users.send(letter.encode('utf-8'))
        self.tplace.clear()

    def end_chat(self):
        
        self.users.send(self.terminate.encode('utf-8'))
        self.txt1.setReadOnly(True)
        try:
          self.users.close()
        except Exception as e:
            self.txt1.append(self.terminate)

    def user_receive(self):
        while True:
            try:
                message = self.users.recv(1024).decode('utf-8')
                self.txt1.insertPlainText(message)
            except:
                self.txt1.insertPlainText(self.terminate)
                self.end_chat()
                break

    def begin(self):
        self.address = input("Enter the server address: ")
        self.users.connect((self.address, 59000))
        print(f"Connected to {self.address}")
        data = f'{self.user} has joined the chat\n'
        rec_thread = threading.Thread(target=self.user_receive)
        rec_thread.start()
        self.users.send(data.encode('utf-8'))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
#programmed by Oliver
