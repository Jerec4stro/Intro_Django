from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kargs):
        context={


        }
        
        return render(request, "index.html",context)