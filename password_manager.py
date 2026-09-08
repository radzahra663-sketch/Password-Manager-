#password manager 

import os
import json
import sys

from PyQt5.QtWidgets import (  
      QApplication, QWidget, QPushButton, QLabel,
      QLineEdit, QVBoxLayout,QMessageBox,QStackedWidget
)
from PyQt5.QtCore import Qt




filename = "password_docs.json"


if os.path.exists(filename):

    with open(filename, "r") as file:
        infos = json.load(file)

else:
    infos = []


def save():
    with open(filename, "w") as file:
        json.dump(infos, file, indent=4)



class PasswordManager(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Password Manager")
        self.setGeometry(500, 200, 400, 500)

       

        self.stack = QStackedWidget()

        # Create pages
        self.main_page = QWidget()
        self.signup_page = QWidget()
        self.login_page = QWidget()
        self.change_password_page = QWidget()
        self.delete_account_page = QWidget()

        # Add pagess
        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.signup_page)
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.change_password_page)
        self.stack.addWidget(self.delete_account_page)

       

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)

       

        self.create_main_page()
        self.create_signup_page()
        self.create_login_page()
        self.create_change_password_page()
        self.create_delete_account_page()

        # Start from main page
        self.stack.setCurrentWidget(self.main_page)

        
        
        self.setStyleSheet("""
         QPushButton{
         font-family: arial;
         font-size : 20px;
         background-color: #df97f0;
         border-radius: 10px;
         padding: 10px;
         }
         QLineEdit{
         font-size: 20px
         background-color: #e1c3e8;
         }
         QLabel{
         font-size:30px;
         }
         
       """)
        

   

    def create_main_page(self) :

        layout = QVBoxLayout()

        title = QLabel("welcome to \nPassword Manager")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 50px; font-weight: bold; color:#6f1f70;")

        



        signup_button = QPushButton("Sign Up")

        login_button = QPushButton("Log In")

        change_password_button = QPushButton("Change Password")

        delete_account_button = QPushButton("Delete Account")

        exit_button = QPushButton("Exit")


        

        signup_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.signup_page)
        )

        login_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.login_page)
        )

        change_password_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.change_password_page
            )
        )

        delete_account_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.delete_account_page
            )
        )

        exit_button.clicked.connect(self.close)


        

        layout.addWidget(title)
        

        layout.addSpacing(20)

        layout.addWidget(signup_button)
        layout.addWidget(login_button)
        layout.addWidget(change_password_button)
        layout.addWidget(delete_account_button)

        layout.addSpacing(20)

        layout.addWidget(exit_button)


        self.main_page.setLayout(layout)



    

    def create_signup_page(self)  :

        layout = QVBoxLayout()


        title = QLabel("CREATE ACCOUNT")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 50px; font-weight: bold; color:#6f1f70;")


        

        self.signup_name = QLineEdit()
        self.signup_name.setPlaceholderText("Enter your name")


        

        self.signup_age = QLineEdit()
        self.signup_age.setPlaceholderText("Enter your age")


        

        self.signup_password = QLineEdit()
        self.signup_password.setPlaceholderText(
            "Choose a password"
        )

        self.signup_password.setEchoMode(
            QLineEdit.Password
        )


        

        create_button = QPushButton("Create Account")

        back_button = QPushButton("Back")


        

        create_button.clicked.connect(
            self.create_account
        )

        back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.main_page
            )
        )


        

        layout.addWidget(title)

        layout.addSpacing(20)

        layout.addWidget(self.signup_name)
        layout.addWidget(self.signup_age)
        layout.addWidget(self.signup_password)

        layout.addSpacing(20)

        layout.addWidget(create_button)
        layout.addWidget(back_button)


        self.signup_page.setLayout(layout)



    

    def create_account(self):

        name = self.signup_name.text().strip()

        age = self.signup_age.text().strip()

        password = self.signup_password.text()


        

        if not name or not age or not password:

            QMessageBox.warning(
                self,
                "Error",
                "Please fill in all fields!"
            )

            return


        

        if not age.isdigit():

            QMessageBox.warning(
                self,
                "Error",
                "Age must be a number!"
            )

            return


        age = int(age)


        

        for user in infos :

            if user["name"] == name :

                QMessageBox.warning(
                    self,
                    "Error",
                    "This name already exists!"
                )

                return


        

        user = {
            "name": name,
            "age": age,
            "password": password
        }


        infos.append(user)

        save()


        QMessageBox.information(
            self,
            "Success",
            "Account created successfully! 🎉"
        )


        

        self.signup_name.clear()
        self.signup_age.clear()
        self.signup_password.clear()


        

        self.stack.setCurrentWidget(
            self.main_page
        )



    

    def create_login_page(self) :

        layout = QVBoxLayout()


        title = QLabel("LOG IN")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 50px; font-weight: bold; color:#6f1f70;")


        

        self.login_name = QLineEdit()

        self.login_name.setPlaceholderText(
            "Enter your name"
        )


        

        self.login_password = QLineEdit()

        self.login_password.setPlaceholderText(
            "Enter your password"
        )

        self.login_password.setEchoMode(
            QLineEdit.Password
        )


        

        login_button = QPushButton("Log In")

        back_button = QPushButton("Back")


        

        login_button.clicked.connect(
            self.check_login
        )

        back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.main_page
            )
        )


        

        layout.addWidget(title)

        layout.addSpacing(20)

        layout.addWidget(self.login_name)
        layout.addWidget(self.login_password)

        layout.addSpacing(20)

        layout.addWidget(login_button)
        layout.addWidget(back_button)


        self.login_page.setLayout(layout)


   

    def check_login(self):

        username = self.login_name.text().strip()

        password = self.login_password.text()


        if not username or not password:

            QMessageBox.warning(
                self,
                "Error",
                "Please fill in all fields!"
            )

            return


        

        for user in infos:

            if user["name"] == username:

                if user["password"] == password:

                    QMessageBox.information(
                        self,
                        "Success",
                        f"Welcome {username}! 🎉"
                    )


                    self.login_name.clear()
                    self.login_password.clear()


                    self.stack.setCurrentWidget(
                        self.main_page
                    )

                    return

                else:

                    QMessageBox.warning(
                        self,
                        "Error",
                        "The password is incorrect!"
                    )

                    return


        

        QMessageBox.warning(
            self,
            "Error",
            "There is no such account!"
        )





    def create_change_password_page(self):

        layout = QVBoxLayout()


        title = QLabel("CHANGE PASSWORD")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 50px; font-weight: bold; color:#6f1f70;")


        

        self.change_name = QLineEdit()

        self.change_name.setPlaceholderText(
            "Enter your name"
        )


        

        self.old_password = QLineEdit()

        self.old_password.setPlaceholderText(
            "Enter old password"
        )

        self.old_password.setEchoMode(
            QLineEdit.Password
        )


        

        self.new_password = QLineEdit()

        self.new_password.setPlaceholderText(
            "Enter new password"
        )

        self.new_password.setEchoMode(
            QLineEdit.Password
        )


        

        change_button = QPushButton(
            "Change Password"
        )

        back_button = QPushButton("Back")


        

        change_button.clicked.connect(
            self.update_password
        )

        back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.main_page
            )
        )


        

        layout.addWidget(title)

        layout.addSpacing(20)

        layout.addWidget(self.change_name)
        layout.addWidget(self.old_password)
        layout.addWidget(self.new_password)

        layout.addSpacing(20)

        layout.addWidget(change_button)
        layout.addWidget(back_button)


        self.change_password_page.setLayout(
            layout
        )


   

    def update_password(self):

        username = self.change_name.text().strip()

        old_password = self.old_password.text()

        new_password = self.new_password.text()


        if not username or not old_password or not new_password:

            QMessageBox.warning(
                self,
                "Error",
                "Please fill in all fields!"
            )

            return


        

        for user in infos:

            if user["name"] == username:

                

                if user["password"] == old_password:

                    user["password"] = new_password

                    save()


                    QMessageBox.information(
                        self,
                        "Success",
                        "Password changed successfully! ✅"
                    )


                    self.change_name.clear()
                    self.old_password.clear()
                    self.new_password.clear()


                    self.stack.setCurrentWidget(
                        self.main_page
                    )

                    return

                else:

                    QMessageBox.warning(
                        self,
                        "Error",
                        "The old password is incorrect!"
                    )

                    return


        QMessageBox.warning(
            self,
            "Error",
            "There is no such account!"
        )



    def create_delete_account_page(self):

        layout = QVBoxLayout()


        title = QLabel("DELETE ACCOUNT")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 50px; font-weight: bold; color:#6f1f70;")


        
        self.delete_name = QLineEdit()

        self.delete_name.setPlaceholderText(
            "Enter your name"
        )


        

        self.delete_password = QLineEdit()

        self.delete_password.setPlaceholderText(
            "Enter your password"
        )

        self.delete_password.setEchoMode(
            QLineEdit.Password
        )


        

        delete_button = QPushButton(
            "Delete Account"
        )

        back_button = QPushButton("Back")


        

        delete_button.clicked.connect(
            self.remove_account
        )

        back_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.main_page
            )
        )


        

        layout.addWidget(title)

        layout.addSpacing(20)

        layout.addWidget(self.delete_name)
        layout.addWidget(self.delete_password)

        layout.addSpacing(20)

        layout.addWidget(delete_button)
        layout.addWidget(back_button)


        self.delete_account_page.setLayout(
            layout
        )


    

    def remove_account(self):

        username = self.delete_name.text().strip()

        password = self.delete_password.text()


        if not username or not password:

            QMessageBox.warning(
                self,
                "Error",
                "Please fill in all fields!"
            )

            return


        

        for user in infos:

            if user["name"] == username:

                
                if user["password"] == password:

                    answer = QMessageBox.question(
                        self,
                        "Delete Account",
                        "Are you sure you want to delete this account?",
                        QMessageBox.Yes | QMessageBox.No
                    )


                    if answer == QMessageBox.Yes:

                        infos.remove(user)

                        save()


                        QMessageBox.information(
                            self,
                            "Success",
                            "Account deleted successfully! 🗑️"
                        )


                        self.delete_name.clear()
                        self.delete_password.clear()


                        self.stack.setCurrentWidget(
                            self.main_page
                        )

                    return

                else:

                    QMessageBox.warning(
                        self,
                        "Error",
                        "The password is incorrect!"
                    )

                    return


        QMessageBox.warning(
            self,
            "Error",
            "There is no such account!"
        )






if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = PasswordManager()

    window.show()

    sys.exit(app.exec_())