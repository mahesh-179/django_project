from django import forms
class StudentForm(forms.Form):
    ename=forms.CharField()
    add=forms.CharField()
    age=forms.IntegerField()
    college=forms.CharField()

    