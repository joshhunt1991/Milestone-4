from django import forms
from .models import Order
from django.core.validators import validate_email


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        # Add placeholders and classes, remove default
        # labels and set autofocus on primary field
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        # this function is for validation

    def clean(self):

        # data from the form is fetched using super function
        super(OrderForm, self).clean()

        # extract the fields from the data
        full_name = self.cleaned_data.get('full_name')
        street_address1 = self.cleaned_data.get('street_address1')
        phone_number = self.cleaned_data.get('phone_number')

        # conditions to be met for the username length
        if len(full_name) < 5:
            self._errors['full_name'] = self.error_class([
                'Minimum 5 characters required'])

        # conditions to be met for the address line 1 length
        if len(street_address1) < 5:
            self._errors['street_address1'] = self.error_class([
                'Minimum 5 characters required'])

        # conditions to be met for phone number characters
        if not phone_number.isdecimal():
            self._errors['phone_number'] = self.error_class([
                'Phone number should only contain numbers'])

        # return any errors if found
        return self.cleaned_data
