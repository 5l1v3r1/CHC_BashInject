from django import forms

class CMSForm(forms.Form):
    netid = forms.CharField(required=True)
    homework = forms.FileField(required=True)

    def clean(self):
        """Check if value consists only of valid emails."""
        super(CMSForm, self).clean()
        if not self.cleaned_data['homework'].name.endswith(".zip"):
            self.add_error("homework","File must be a zip file")