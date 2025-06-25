from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from ml import predict_grades

class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(
            text="Hours Studied:",
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.75}
        ))
        self.hours_studied = TextInput(
            multiline=False,
            size_hint=(0.6, 0.1),
            pos_hint={'x': 0.35, 'y': 0.75}
        )
        self.add_widget(self.hours_studied)

        self.add_widget(Label(
            text="Attendance Rate:",
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.6}
        ))
        self.attendance_rate = TextInput(
            multiline=False,
            size_hint=(0.6, 0.1),
            pos_hint={'x': 0.35, 'y': 0.6}
        )
        self.add_widget(self.attendance_rate)

        self.add_widget(Label(
            text="Output Completion Rate:",
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.45}
        ))
        self.completion_rate = TextInput(
            multiline=False,
            size_hint=(0.6, 0.1),
            pos_hint={'x': 0.35, 'y': 0.45}
        )
        self.add_widget(self.completion_rate)

        self.predict_button = Button(
            text="Predict Grades",
            size_hint=(0.4, 0.1),
            pos_hint={'x': 0.3, 'y': 0.28}
        )
        self.predict_button.bind(on_press=self.predict_grades_function)
        self.add_widget(self.predict_button)

        self.result_label = Label(
            text="",
            size_hint=(1, 0.2),
            pos_hint={'x': 0, 'y': 0.1}
        )
        self.add_widget(self.result_label)

    def predict_grades_function(self, instance):
        try:
            hours_studied = float(self.hours_studied.text)

            attendance_rate_text = self.attendance_rate.text.strip('%')
            if not attendance_rate_text:
                raise ValueError("Attendance rate cannot be empty.")
            attendance_rate = float(attendance_rate_text) / 100

            completion_rate_text = self.completion_rate.text.strip('%')
            if not completion_rate_text:
                raise ValueError("Completion rate cannot be empty.")
            completion_rate = float(completion_rate_text) / 100

            predicted_grade = predict_grades(hours_studied, attendance_rate, completion_rate)
            self.result_label.text = f"Predicted Grade: {predicted_grade:.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers."
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

class GradePredictorApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    GradePredictorApp().run()
