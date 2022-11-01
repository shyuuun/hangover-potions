from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment

def index(request):
    comments = Comment.objects.all().values()
    template = loader.get_template('index1.html')
    context = {
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def addComment(request):
    name = request.GET['user']
    content = request.GET['content']
    comment = Comment(user=name, content=content)
    comment.save()
    return HttpResponseRedirect(reverse('index'))