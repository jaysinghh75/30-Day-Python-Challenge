# remember to install kivy in a virtual env coz kivy has multiple dependencies

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Set background color of the window
Window.clearcolor = (0.95, 0.95, 1, 1)  # Light blue background

class TempConverterApp(App):
    def build(self):
        self.unit = 'F'  # Default is Celsius to Fahrenheit

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Title Label
        title = Label(text="🌡️ Temperature Converter", font_size=28, size_hint=(1, 0.2), color=(0.2, 0.2, 0.5, 1))
        main_layout.add_widget(title)

        # Input field
        self.input_temp = TextInput(
            hint_text="Enter temperature",
            multiline=False,
            input_filter='float',
            font_size=22,
            size_hint=(1, 0.15),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0.2, 0.4, 0.6, 1)
        )
        main_layout.add_widget(self.input_temp)

        # CheckBox layout for unit selection
        unit_layout = BoxLayout(size_hint=(1, 0.15), spacing=40, padding=[50, 0])

        # Celsius Checkbox
        self.celsius_cb = CheckBox(group='unit', active=False)
        celsius_label = Label(text='Celsius (°C)', font_size=18, color=(0.1, 0.3, 0.6, 1))
        celsius_box = BoxLayout(orientation='horizontal', spacing=10)
        celsius_box.add_widget(self.celsius_cb)
        celsius_box.add_widget(celsius_label)
        unit_layout.add_widget(celsius_box)

        # Fahrenheit Checkbox
        self.fahrenheit_cb = CheckBox(group='unit', active=True)
        fahrenheit_label = Label(text='Fahrenheit (°F)', font_size=18, color=(0.6, 0.2, 0.2, 1))
        fahrenheit_box = BoxLayout(orientation='horizontal', spacing=10)
        fahrenheit_box.add_widget(self.fahrenheit_cb)
        fahrenheit_box.add_widget(fahrenheit_label)
        unit_layout.add_widget(fahrenheit_box)

        # Bind checkbox toggle
        self.celsius_cb.bind(active=self.on_celsius_checked)
        self.fahrenheit_cb.bind(active=self.on_fahrenheit_checked)

        main_layout.add_widget(unit_layout)

        # Convert button
        convert_btn = Button(
            text="🔁 Convert",
            font_size=22,
            size_hint=(1, 0.15),
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        convert_btn.bind(on_press=self.convert_temp)
        main_layout.add_widget(convert_btn)

        # Result label
        self.result_label = Label(text="", font_size=20, size_hint=(1, 0.15), color=(0.1, 0.4, 0.2, 1))
        main_layout.add_widget(self.result_label)

        return main_layout

    def on_celsius_checked(self, checkbox, value):
        if value:
            self.unit = 'C'

    def on_fahrenheit_checked(self, checkbox, value):
        if value:
            self.unit = 'F'

    def convert_temp(self, instance):
        temp_text = self.input_temp.text.strip()

        if not temp_text:
            self.result_label.text = "⚠️ Please enter a temperature!"
            return

        try:
            temp = float(temp_text)
            if self.unit == 'F':
                converted = (temp * 9/5) + 32
                self.result_label.text = f"{temp:.1f}°C = {converted:.1f}°F"
            else:
                converted = (temp - 32) * 5/9
                self.result_label.text = f"{temp:.1f}°F = {converted:.1f}°C"
        except ValueError:
            self.result_label.text = "❌ Invalid temperature entered."


if __name__ == "__main__":
    TempConverterApp().run()
