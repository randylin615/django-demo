from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#def index(request): ## ed.1
#    now = datetime.now()

    
#    #html_content = "<html><head><title>Hello, Django</title></head><body>"
#    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    #html_content += "</body></html>"
#    #return HttpResponse(html_content)

#    return render(
#        request,
#        "HelloDjangoApp/index.html",
#        {
#            'content':"<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#        }
#    )

def index(request): ## ed.2
    now = datetime.now()
    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title': "Hello Django",
            'message': "Demo, Hello Django! ",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )
