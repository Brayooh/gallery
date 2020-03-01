from django.shortcuts import render
from django.http import HttpResponse
from .models import image


def posted_images(request):

    pics = image.objects.all()

    return render(request, 'index.html', {"pics":pics})




# def copy_to_clipboard(request):
    
#     pyperclip.copy('The text to be copied to the clipboard.')
#     spam = pyperclip.paste()

#     return copy