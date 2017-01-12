from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

from .forms import NameForm, AddressForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        name_form = NameForm(request.POST)
        address_form = AddressForm(request.POST)

        context={}
        # check whether it's valid:
        if name_form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = name_form.cleaned_data['first_name']
            last_name = name_form.cleaned_data['last_name']

            context["first_name"] = name_form.cleaned_data["first_name"]
            context["last_name"] = name_form.cleaned_data["last_name"]

        if address_form.is_valid():
            # process the data in form.cleaned_data as required
            address = address_form.cleaned_data['address']

            context["address"] = address_form.cleaned_data["address"]

        return HttpResponseRedirect(reverse('myforms:thanks'))

    # if a GET (or any other method) we'll create a blank form
    else:
        name_form = NameForm()
        address_form = AddressForm()

    return render(request, 'name.html', {'name_form': name_form, 'address_form':address_form})


def thanks(request):
    return render(request, 'thanks.html')
