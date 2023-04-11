from django.shortcuts import render
from django.http import HttpResponse
from .forms import ChatMessageForm
from .models import *
# Create your views here.

def index(request):
    user = request.user.frofile
    friends = Friend.objects.all()
    context = {'users': user, 'friends': friends}
    return render(request, "mychatapp/index.html", context)

def detail(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    form = ChatMessageForm()
    user = request.user.frofile
    profile = Frofile.objects.get(id=friend.profile.id)
    chat = ChatMessage.objects.all()
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
    context = {'friend': friend, 'form': form, 'chats': chat, 'user': user, 'profile': profile}
    return render(request, 'mychatapp/detail.html', context)

