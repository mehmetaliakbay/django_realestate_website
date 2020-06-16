from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from home.models import UserProfile
from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderProperty
from property.models import Category, Property


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



@login_required(login_url='/login')
def orderproperty(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.myproperty.price * rs.quantity

    if request.method == 'POST':    #if there is a post
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']   #get property quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            # Move shopcart items to Order Products items
            shopcart = ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcart:
                detail = OrderProperty()
                detail.order_id = data.id
                detail.property_id = rs.myproperty_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                # ***Reduce quantity of sold property from Amount of Product
                property = Property.objects.get(id=rs.myproperty_id)
                property.amount -= rs.quantity
                property.save()
                #******************************
                detail.price = rs.myproperty.price
                detail.amount = rs.amount
                detail.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()   #clear & delete shopcart
            request.session['shopcart_items'] = 0
            messages.success(request, "Your Order has been completed. Thank you")
            return render(request, 'order_completed.html',{'ordercode':ordercode, 'category':category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/order/orderproperty')

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'order_form.html', context)