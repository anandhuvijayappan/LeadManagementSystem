from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import LeadForm

from myapp.models import Lead

# Create your views here.

class CreateLeadView(View):

    def get(self,request,*args,**kargs):

        form_instance=LeadForm()

        eq=Lead.objects.all()

        return render(request,"create_lead.html",{"form":form_instance,"data":eq})
    
    def post(self,request,*args,**kargs):

        data_instance=request.POST

        form_instance=LeadForm(data_instance)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Lead.objects.create(**data)

            return redirect("create_lead")

        return render(request,"create_lead.html",{"form":form_instance})