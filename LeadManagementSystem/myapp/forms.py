from django import forms

from myapp.models import Lead


class LeadForm(forms.ModelForm):

    class Meta:

        model=Lead

        fields="__all__"

        widgets={

            "source":forms.Select(attrs={"class":"form-control"}),
            "status":forms.Select(attrs={"class":"form-control"})
        }