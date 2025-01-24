from django import forms

from myapp.models import Lead


class LeadForm(forms.ModelForm):

    class Meta:

        model=Lead

        fields="__all__"