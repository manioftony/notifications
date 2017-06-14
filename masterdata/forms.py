from django import forms
from masterdata.models import Student

class AddStudent(forms.ModelForm):
    class Meta:

        model = Student
        fields = ('name',)