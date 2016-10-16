from django import forms

class CMSForm(forms.Form):
    netid = forms.CharField(required=True)
    homework = forms.FileField(required=True)