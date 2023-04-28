from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import ChatMessageForm
from django.core.serializers import serialize
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
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()

    context = {'friend': friend, 'form': form, 'chats': chat, 'user': user, 'profile': profile}
    return render(request, 'mychatapp/detail.html', context)

def sent_chat(request, pk):
    new_chat = request.POST.get('msg')
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.frofile
    profile = Frofile.objects.get(id=friend.profile.id)
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen = False)
    serialized_data = serialize('json', [new_chat_message])
    return JsonResponse({"result": new_chat}, safe=False)

