from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import TinyMessageForm
from .models import TinyMessage


def index(request):
    context = {'title': 'Página Inicial', 'app_name': 'TinyApp'}

    return render(request, 'tinyapp/index.html', context)


def messages(request):
    form = TinyMessageForm()
    messages = TinyMessage.objects.all()

    context = {'title': 'Mensagens', 'form': form, 'messages': messages}

    return render(request, 'tinyapp/messages.html', context)


def new_message(request):
    content = request.POST['content']

    new_message = TinyMessage(content=content)
    new_message.save()

    return redirect(reverse('tinyapp:messages'))


def about(request):
    context = {
        'title': 'Sobre',
        'app_name': 'TinyApp',
        'authors': [
            'Giovani Candido',
            'Luiz Fernando Merli de Oliveira Sementille'
        ],
    }

    return render(request, 'tinyapp/about.html', context)
