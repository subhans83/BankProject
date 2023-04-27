from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Div, Row, Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from django.http import request

from bankingapp.models import Register, Branch
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date


class Row(Div):
    css_class = 'row g-3'


class MemberCreationForm(forms.ModelForm):
    MATERIAL_CHOICES = (
        ('debitcard', 'Debit Card'),
        ('creditcard', 'Credit Card'),
        ('chequebook', 'Cheque Book')
    )
    material_choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=MATERIAL_CHOICES)
    birthdate = forms.DateField(
        # widget=forms.TextInput(
        #     attrs={'type': 'date'}
        # )
    )

    class Meta:
        model = Register
        fields = ['name', 'birthdate', 'age', 'gender', 'phone', 'email', 'address', 'district', 'branch', 'account',
                  'material_choices']
        labels = {
                  'birthdate': 'Date of Birth',
                  'phone': 'Phone Number',
                  'account': 'Account Type',
                  'material_choices': 'Materials Provided'}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(

            Div(
                Field('name',wrapper_class='col-md-13')
            ),
            Div(
                Field('birthdate', wrapper_class='col-md-3'),
                Field('age', wrapper_class='col-md-9'),
                css_class='form-row'),

            Div(
                Field('gender', wrapper_class='col-md-13')
            ),
            Div(
                Field('phone', wrapper_class='col-md-13')
            ),
            Div(
                Field('email', wrapper_class='col-md-13')
            ),
            Div(
                Field('address', wrapper_class='col-md-13')
            ),
            Div(
                Field('district', wrapper_class='col-md-3'),
                Field('branch', wrapper_class='col-md-9'),
                css_class='form-row'),

            Div(
                Field('account', wrapper_class='col-md-13')
            ),
            Div(
                Field('material_choices', wrapper_class='col-md-12')
            ),
            Div(
                Submit('submit', 'Submit')
            ),
        )
        self.fields['branch'].queryset = Branch.objects.none()
        self.fields['age'].widget.attrs['readonly'] = True

        

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Branch queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'