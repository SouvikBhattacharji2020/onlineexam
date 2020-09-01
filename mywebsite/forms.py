from django import forms  
from mywebsite.models import login 
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = myprojectdata  
        fields = "__all__"  