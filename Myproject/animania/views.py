from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User,Room,Message,Enquiry
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MyUserCreationForm,RoomForm,UserForm,EnquiryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    naruto_room = Room.objects.get(name='Naruto')  
    op_room = Room.objects.get(name='One Piece')  
    aot_room = Room.objects.get(name='Attack On Titan')  
    tg_room = Room.objects.get(name='Tokyo Ghoul')  
    bleach_room = Room.objects.get(name='Bleach')  
    dn_room = Room.objects.get(name='Death Note')  
    # act_cat = Category.objects.get(name='Action')  
    # adv_cat = Category.objects.get(name='Adventure')  
    # hen_cat = Category.objects.get(name='Hentai')  
    # fan_cat = Category.objects.get(name='Fantasy')  
    # com_cat = Category.objects.get(name='Comedy')  
    # da_cat = Category.objects.get(name='Dark')
    dbz_room = Room.objects.get(name='Dragon Ball Z')  
    boruto_room = Room.objects.get(name='Boruto')  
    jojo_room = Room.objects.get(name="Jojo's")  
    ber_room = Room.objects.get(name='Berserk')  
    mas_room = Room.objects.get(name='Mashle')  
    drs_room = Room.objects.get(name='Dr.Stone')  
    gin_room = Room.objects.get(name='Gintama')  
    jjk_room = Room.objects.get(name='Jujutsu Kaisen')  
    hxh_room = Room.objects.get(name='Hunter X Hunter')  
    dxd_room = Room.objects.get(name='High School DXD')  
    kak_room = Room.objects.get(name='Kakegurui')  
    sao_room = Room.objects.get(name='Sword Art Online')  
    context = {
        'naruto_room': naruto_room,
        'op_room': op_room,
        'aot_room': aot_room,
        'tg_room': tg_room,
        'dn_room': dn_room,
        'bleach_room': bleach_room,
        # 'act_cat':act_cat,
        # 'adv_cat':adv_cat,
        # 'hen_cat':hen_cat,
        # 'fan_cat':fan_cat,
        # 'com_cat':com_cat,
        # 'da_cat':da_cat,
        'dbz_room':dbz_room,
        'boruto_room':boruto_room,
        'jojo_room':jojo_room,
        'ber_room':ber_room,
        'mas_room':mas_room,
        'drs_room':drs_room,
        'gin_room':gin_room,
        'jjk_room':jjk_room,
        'hxh_room':hxh_room,
        'dxd_room':dxd_room,
        'kak_room':kak_room,
        'sao_room':sao_room,
    }
    return render(request, "anime.html", context)


def room(request, room_id):
    # Get the specific room or return 404 if not found
    room = get_object_or_404(Room, id=room_id)
    
    # Get all messages associated with this room
    room_messages = room.message_set.all()

    # Handle POST request for creating a new message
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        # Redirect to the same room after posting the message
        return redirect('room', room_id=room.id)

    # Pass the room and messages to the template context
    context = {'room': room, 'room_messages': room_messages}
    return render(request, "room.html", context)

def adventure(request):
    op_room = Room.objects.get(name='One Piece')  
    boruto_room = Room.objects.get(name='Boruto')  
    jojo_room = Room.objects.get(name="Jojo's") 
    context={'op_room': op_room,
    'boruto_room':boruto_room,
    'jojo_room':jojo_room,}
    return render(request,"adventure.html",context)

def action(request):
    dbz_room = Room.objects.get(name='Dragon Ball Z')
    naruto_room = Room.objects.get(name='Naruto')
    bleach_room = Room.objects.get(name='Bleach')
    context={'naruto_room': naruto_room,
    'bleach_room': bleach_room,
    'dbz_room':dbz_room,}
    return render(request,"action.html",context)

def hentai(request):
    dxd_room = Room.objects.get(name='High School DXD')  
    kak_room = Room.objects.get(name='Kakegurui')  
    sao_room = Room.objects.get(name='Sword Art Online')
    context={
    'dxd_room':dxd_room,
    'kak_room':kak_room,
    'sao_room':sao_room,
    }
    return render(request,"hentai.html",context)

def comedy(request):
    mas_room = Room.objects.get(name='Mashle')  
    drs_room = Room.objects.get(name='Dr.Stone')  
    gin_room = Room.objects.get(name='Gintama') 
    context={
    'mas_room':mas_room,
    'drs_room':drs_room,
    'gin_room':gin_room,
    }
    return render(request,"comedy.html",context)

def fantasy(request):
    dn_room = Room.objects.get(name='Death Note')    
    jjk_room = Room.objects.get(name='Jujutsu Kaisen')  
    hxh_room = Room.objects.get(name='Hunter X Hunter')  
    context={
    'dn_room': dn_room,
    'jjk_room':jjk_room,
    'hxh_room':hxh_room,
    }
    return render(request,"fantasy.html",context)

def dark(request):
    aot_room = Room.objects.get(name='Attack On Titan')  
    tg_room = Room.objects.get(name='Tokyo Ghoul')  
    ber_room = Room.objects.get(name='Berserk')  
    context={
    'aot_room': aot_room,
    'tg_room': tg_room,
    'ber_room':ber_room,
    }
    return render(request,"dark.html",context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        email = request.POST.get('email')  
        password = request.POST.get('password')

        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.") 

    context = {'page': page}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')
        else:
            # Iterate through each field's error and add a message
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    context = {'form': form, 'page': 'register'}
    return render(request, 'login.html', context)

@login_required(login_url = '/login')
def deleteMessage(request,room_id):
    message = Message.objects.get(id=room_id)
    if request.user!=message.user:
        return HttpResponse("You are not allowed here")
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request,'delete.html',{'obj':message})

@login_required(login_url='/login')
def updateUser(request):
    user = request.user
    form  = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'form':form})

def enquiry(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request,'home',{'form':form})
            