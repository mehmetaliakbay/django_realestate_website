from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from property.models import Property
from property.models import Category
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Property.objects.all()[:4]
    category = Category.objects.all()
    dayproperties= Property.objects.all()[:4]
    lastproperties = Property.objects.all().order_by('-id')[:4]
    randomproperties = Property.objects.all().order_by('?')[:9]
    context = {'setting': setting,
                'category': category,
                'page':'home',
                'sliderdata':sliderdata,
                'randomproperties':randomproperties,
                'lastproperties':lastproperties,
                'dayproperties':dayproperties}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    if request.method == 'POST': # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() # model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data[ 'message' ]
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() # verirabanına kaydet
            messages.success(request, "Mesajanız başarı ile gönderilmiştir. Teşekkür Ederiz ")
            return HttpResponseRedirect ('/iletisim')
         
       
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context={'setting':setting, 'form': form}
    return render(request, 'iletisim.html', context)


def category_properties(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    properties = Property.objects.filter(category_id=id)
    context = {'properties': properties,
                'category': category,
                'categorydata': categorydata}
    return render(request,'properties.html',context)
