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

    context = {'setting': setting,
                'category': category,
                'page':'home',
                'sliderdata':sliderdata}
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
