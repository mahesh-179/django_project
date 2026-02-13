from django import forms
class StudentForm(forms.Form):
    ename=forms.CharField()
    add=forms.CharField()
    age=forms.IntegerField()
    gpa=forms.FloatField()
    college=forms.CharField()

    
    def clean_ename(self):
        inputname=self.cleaned_data["ename"]
        if len(inputname)<5:
            raise forms.ValidationError("Name is too short please enter long name")
        return inputname
    def clean_age(self):
        inputage=self.cleaned_data["age"]
        if (inputage)<=18:
            raise forms.ValidationError("Age Should Be Greater or Equal than 18 ")
        return inputage