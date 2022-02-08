from django import forms
from .models import Emp,Role



class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'

        labels = {'eid':'Emp ID','name':'Emp Name','email':'Email','mno':'Phone No'}

        widgets = {'eid':forms.NumberInput(attrs={'class':'form-control'}),
                   'name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'mno':forms.NumberInput(attrs={'class':'form-control'})}



class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

        labels = {'role':'Role'}

        widgets ={'role':forms.TextInput(attrs={'class':'form-control'})}




