from django import forms

class CMSForm(forms.Form):
    form_netid = forms.CharField(required=True)
    form_file = forms.FileField(required=True)