from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime as dt
from backend import Database

database = Database("Bundy_clock.db")

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def welcome_employee(self, worker_id, worker_pass):
        if worker_id.text == "jovie" and worker_pass.text == "123":
            self.manager.current = "welcome_employee"
            print(worker_id.text, worker_pass.text)
            print(dt.now())

    def welcome_admin(self, worker_id, worker_pass):
        if worker_id.text == "jovie" and worker_pass.text == "123":
            self.manager.current = "welcome_admin"
            print(worker_id.text, worker_pass.text)
            print(dt.now().date())
            print(dt.now().strftime("%I:%M:%S %p"))

class RootWidget(ScreenManager):
    pass

class WelcomeEmployee(Screen):
    pass

class WelcomeAdmin(Screen):
    def add_employee(self):
        self.manager.current = "add_employee"

class AddEmployee(Screen):
    def employee_add_success(self, employee_name, employee_pass):
        self.manager.current = "employee_add_success"

class EmployeeAddSuccess(Screen):
    def login_screen(self):
        self.manager.current = "login_screen"

    def welcome_admin(self):
        self.manager.current = "welcome_admin"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
