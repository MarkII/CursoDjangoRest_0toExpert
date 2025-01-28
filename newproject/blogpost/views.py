from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render

# Create your views here.


class HelloWorld(View):
    def get(self, request):
        # return HttpResponse(content="Hola mundo")
        # Creacion de Django Template:
        
        data = {
            'name':'el pishita',
            'surname':'53',
            'languaje': ['python','c++','c','java'],
        }
        
        return render(request,'creacionhtml.html',context=data, 
        )



