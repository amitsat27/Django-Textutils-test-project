#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , "index.html")

def analyze(request):
    texts = request.POST.get("text","Default")
    checkpun = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremove",'off')
    spaceremover = request.POST.get("spaceremove",'off')
    puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if checkpun=="on":
        analyzed = ""
        for char in texts:
            if char not in puncs:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        texts = analyzed
    if(fullcaps  == "on"):
        analyzed = ""
        for char in texts:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalize Text', 'analyzed_text': analyzed}
        texts = analyzed
    if(spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(texts):
            if char == texts[-1]:
                if not (texts[index] == " "):
                    analyzed = analyzed + char
            elif not(texts[index]==" " and texts[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        texts = analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in texts:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'NewLine Remover', 'analyzed_text': analyzed}

    if (checkpun != "on" and newlineremover != "on" and spaceremover != "on" and fullcaps != "on" ):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
