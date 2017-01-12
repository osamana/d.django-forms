from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Your name', max_length=100)

class AddressForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)



