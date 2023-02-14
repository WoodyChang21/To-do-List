from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}),required=False, initial=True)
