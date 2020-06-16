from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from home.models import UserProfile
from property.models import Category, Comment, Property, PropertyForm
from user.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url="/login")
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)


@login_required(login_url="/login")
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user session data
        # "instance.request.user.userprofile" comes from "userprofile" model -> OneTOOneField relation
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user  # Access User Session information
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


@login_required(login_url="/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
        'form': form,'category': category
    })

@login_required(login_url="/login")
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url="/login")
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request,'Comment deleted')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')     # Check login
def addproperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Property()   # model ile baglantl kur
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.price = form.cleaned_data['price']
            data.floor = form.cleaned_data['floor']
            data.room = form.cleaned_data['room']
            data.rate = form.cleaned_data['rate']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.address = form.cleaned_data['address']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save() # verirabanlna kagdet
            messages.success(request, 'Your Content Insterted Successfuly')
            return HttpResponseRedirect('/user/properties')
        else:
            messages.success(request, 'Property Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/addproperty')
    else:
        category = Category.objects.all()
        form = PropertyForm()
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'user_addproperty.html', context)


@login_required(login_url='llogin') # Check login
def propertyedit(request,id):
    property = Property.objects.get(id=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Content Updated Successfuly')
            return HttpResponseRedirect('/user/properties')
        else:
            messages.success(request, 'Content Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/propertyedit/'+str(id))
    else:
        category = Category.objects.all()
        form = PropertyForm(instance=property)
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'user_addproperty.html', context)


@login_required(login_url="/login")
def properties(request):
    category = Category.objects.all()
    current_user = request.user
    properties = Property.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'properties': properties,
    }
    return render(request, 'user_properties.html', context)


@login_required(login_url='/login') # Check login
def propertydelete(request, id):
    current_user = request.user
    Property.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Property deleted...')
    return HttpResponseRedirect('/user/properties')