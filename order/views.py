from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from order.models import ShopCart, ShopCartForm
from property.models import Category


def index(request):
    return HttpResponse("Order App")


@login_required(login_url='/login')  # Check Login
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    checkproperty = ShopCart.objects.filter(myproperty_id = id)  #Ürün sepette var mı sorgusu
    if checkproperty:
        control = 1  # Ürün sepette var
    else:
        control = 0  # Ürün sepette yok

    if request.method == 'POST':  # form post edildiyse urun detay saufasinda
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:  # ürün varsa güncelle
                data = ShopCart.objects.get(myproperty_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # veritananina kaydet
            else :  #ürün yoksa ekle
                data = ShopCart()  # model ile bağlantı kur
                data.user_id = current_user.id
                data.myproperty_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
                request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Ev başarı ile sepete eklenmiştir. Teşekkür ederiz ")
            return HttpResponseRedirect(url)
    else:  # Ürün direk sepete ekle butonuna basıldıysa
        if control ==1:
            data = ShopCart.objects.get(myproperty_id=id)
            data.quantity += 1
            data.save()  # veritananina kaydet
        else:
            data = ShopCart()   # model ile bağlantı kur
            data.user_id = current_user.id
            data.myproperty_id = id
            data.quantity = 1
            data.save()     # veritabanina kaydet
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, "Ev başarı ile sepete eklenmiştir. Teşekkür Ederiz ")
        return HttpResponseRedirect(url)

    messages.success(request, "Ev sepete etmede hata oluştu! Lütfen kontrol ediniz ")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')     # Check login
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    total=0
    for rs in shopcart:
        total += rs.myproperty.price * rs.quantity

    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               }
    return render(request, 'shopcart_properties.html', context)


@login_required(login_url='/login')    # Check login
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Ev Satin alma islemi Silinmiştir.")
    return HttpResponseRedirect("/shopcart")