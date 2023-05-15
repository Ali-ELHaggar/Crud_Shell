from django import forms
from .models import Student

# creating a form
class InputForm(forms.Form):

    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
    help_text = "Enter 6 digit roll number"
    )
    password = forms.CharField(widget = forms.PasswordInput())


    # import form class from django
# import StudentModel from models.py
# create a ModelForm
class StudentForm(forms.ModelForm):
# specify the name of model to use
    class Meta:
        model = Student
        fields = "__all__"