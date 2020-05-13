from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from property.models import Category,Images,Property,Comment
from home.models import Setting, ContactFormu, ContactFormMessage
from home.forms import SearchForm
from django.contrib.auth import logout, authenticate, login


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
    category = Category.objects.all()
    context = {'setting': setting,'category':category}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'category':category}
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
    category = Category.objects.all()
    context={'setting':setting, 'form': form,'category':category}
    return render(request, 'iletisim.html', context)


def category_properties(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    properties = Property.objects.filter(category_id=id)
    context = {'properties': properties,
                'category': category,
                'categorydata': categorydata}
    return render(request,'properties.html',context)

def property_detail(request,id,slug):
    category = Category.objects.all()
    property = Property.objects.get(pk=id)
    images = Images.objects.filter(property_id=id)
    comments = Comment.objects.filter(property_id = id, status = 'True')
    context = { 'property':property,
                'category': category,
                'images':images,
                'comments': comments,
                }
    return render(request,'property_detail.html',context)

def property_search(request):
    if request.method == 'POST': # form post edildiyse
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query'] #formdan bilgiyi al
            properties = Property.objects.filter(title__icontains=query)
            context = {
                'properties': properties,
                'category': category,
            }
            return render(request, 'properties_search.html', context)
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatasi ! Kullanici Adi veya sifre yanlis")
            return HttpResponseRedirect ('/login')

    category = Category.objects.all()
    context = { 'category': category,}
    return render(request,'login.html',context)
