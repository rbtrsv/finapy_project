import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
        
#         # Check if a date is not in the past. 
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))

#         # Check if a date is in the allowed range (+4 weeks from today).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

#         # Remember to always return the cleaned data.
#         return data

# # OR

# from django.forms import ModelForm

# from catalog_app.models import BookInstance

# class RenewBookModelForm(ModelForm):
#     def clean_due_back(self):
#        data = self.cleaned_data['due_back']
       
#        # Check if a date is not in the past.
#        if data < datetime.date.today():
#            raise ValidationError(_('Invalid date - renewal in past'))

#        # Check if a date is in the allowed range (+4 weeks from today).
#        if data > datetime.date.today() + datetime.timedelta(weeks=4):
#            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

#        # Remember to always return the cleaned data.
#        return data

#     class Meta:
#         model = BookInstance
#         fields = ['due_back']
#         labels = {'due_back': _('New renewal date')}
#         help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')} 

from django.forms import ModelForm

from summary.models import Stock

class ChangeClientModelForm(ModelForm):
    def  clean_price_date(self):
        data = self.cleaned_data['price_date']

        if data > datetime.date.to():
            raise ValidationError(_('Invalid date - price date in the future'))

        return data

    # Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), or human-readable singular and plural names (verbose_name and verbose_name_plural).
    class Meta:
        model = Stock
        fields = ['price_date']
        labels = {'price_date': _('Check price date consistency')}
        help_texts = {'price_date': _('Check whether price date is not in the future')}