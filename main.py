from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def welcome_employee(self, worker_id, worker_pass):
        if worker_id.text == "jovie" and worker_pass.text == "123":
            self.manager.current = "welcome_employee"
            print(worker_id.text, worker_pass.text)

    def welcome_admin(self, worker_id, worker_pass):
        if worker_id.text == "jovie" and worker_pass.text == "123":
            self.manager.current = "welcome_admin"
            print(worker_id.text, worker_pass.text)

class RootWidget(ScreenManager):
    pass

class WelcomeEmployee(Screen):
    pass

class WelcomeAdmin(Screen):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
