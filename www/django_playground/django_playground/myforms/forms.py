from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Your name', max_length=100, initial='here nigga...')


class AddressForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea, help_text="enter your address here")
    how_many = forms.IntegerField(max_value=100,
                                  min_value=0,
                                  required=True,
                                  error_messages={'required': 'Please fucking enter your name'},
                                  label='how much man!',
                                  label_suffix='?',
                                  initial=5)
    date_field = forms.DateField(widget=forms.SelectDateWidget)
    date_input = forms.DateInput()
    date_time_field = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    date = forms.DateTimeInput()

    error_css_class = 'error'
    required_css_class = 'required'
    prefix = 'person'
