from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("ui.kv")

class CalcGridLayout(GridLayout):
    def update_display(self, value):
        """Appends button text to the display."""
        self.ids.entry.text += value

    def clear_display(self):
        """Clears the display."""
        self.ids.entry.text = ""

    def calculate_result(self):
        """Evaluates the expression and updates the display."""
        try:
            expression = self.ids.entry.text
            self.ids.entry.text = str(eval(expression))
        except ZeroDivisionError:
            self.ids.entry.text = "Error"
        except Exception:
            self.ids.entry.text = "Invalid Input"

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

if __name__ == "__main__":
    CalculatorApp().run()
