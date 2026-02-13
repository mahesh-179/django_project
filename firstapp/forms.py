from django import forms
from django.core import validators
# def start_with_m(value):
#      if value[0].lower() != 'm':
#         raise forms.ValidationError("Name Should Start with M")

      
class StudentForm(forms.Form):
    ename=forms.CharField()
    add=forms.CharField()
    age=forms.IntegerField()
    gpa=forms.FloatField()
    college=forms.CharField()

    def clean(self):
        cleaned_data= super().clean()
        inputname = self.cleaned_data["ename"]
        if inputname[0].lower() != "m":
            raise forms.ValidationError("Name Must be start with M")
        inputadd=self.cleaned_data["add"]
        if inputadd.lower() != "kathmandu":
            raise forms.ValidationError("Address Should be kathmandu")
        inputage= self.cleaned_data["age"]
        if inputage<=18:
            raise forms.ValidationError("You are Underage! Age Must be greater than 18")
        

    # def start_with_m(value):
    #     value[0].lower() != 'm'
    #     raise forms.ValidationError("Name Should Start with M")
    # # def clean_ename(self):
    # #     inputname=self.cleaned_data["ename"]
    #     if len(inputname)<5:
    #         raise forms.ValidationError("Name is too short please enter long name")
    #     return inputname
    # def clean_age(self):
    #     inputage=self.cleaned_data["age"]
    #     if (inputage)<=18:
    #         raise forms.ValidationError("Age Should Be Greater or Equal than 18 ")
    #     return inputage