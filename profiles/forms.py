from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        # Add placeholders and classes, remove default
        # labels and set autofocus on primary field
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black\
                 rounded-0 profile-form-input'
            self.fields[field].label = False

        # this function is for validation

    def clean(self):

        # data from the form is fetched using super function
        super(UserProfileForm, self).clean()

        # extract the fields from the data
        default_street_address1 = self.cleaned_data.get('street_address1')
        default_phone_number = self.cleaned_data.get('default_phone_number')

        # conditions to be met for the address line 1 length
        if len(default_street_address1) < 5:
            self._errors['default_street_address1'] = self.error_class([
                'Minimum 5 characters required'])

        # conditions to be met for phone number characters
        if not default_phone_number.isdecimal():
            self._errors['phone_number'] = self.error_class([
                'Phone number should only contain numbers'])

        # return any errors if found
        return self.cleaned_data
