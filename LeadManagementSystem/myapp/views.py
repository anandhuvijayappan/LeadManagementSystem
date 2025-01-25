from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import LeadForm

from myapp.models import Lead

from django.db.models import Count

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

            print(data)

            Lead.objects.create(**data)

            print("Added")

            return redirect("create_lead")

        return render(request,"create_lead.html",{"form":form_instance})
    
class LeadDeleteView(View):

    def get(self,request,*args,**kargs):

        id=kargs.get("pk")

        Lead.objects.get(id=id).delete()

        return redirect("create_lead")
    
class LeadUpdateView(View):

    def get(self,request,*args,**kargs):

        id=kargs.get("pk")

        l_obj=Lead.objects.get(id=id)

        print("*********************************",l_obj)

        form_instance=LeadForm(instance=l_obj)

        return render(request,"edit.html",{"form":form_instance,"data":l_obj})
    
    def post(self,request,*args,**kargs):

        id=kargs.get("pk")

        l_obj=Lead.objects.get(id=id)

        data_instance=request.POST

        form_instance=LeadForm(data_instance,instance=l_obj)

        if form_instance.is_valid():

            form_instance.save()

            print("data updated successfuly")

            return redirect("create_lead")
        
        print("failed to update data")

        return render(request,"edit.html",{"form":form_instance,"data":l_obj})
    
class IndexView(View):

    def get(self,request,*args,**kargs):

        count=Lead.objects.count()

        status_summery=Lead.objects.all().values("status").annotate(count=Count("status"))

        source_summery=Lead.objects.all().values("source").annotate(count=Count("source"))

        condext={
            "count":count,
            "status_summery":status_summery,
            "source_summery":source_summery
        }

        return render(request,"index.html",condext)
        