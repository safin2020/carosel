from django.shortcuts import render
from .models import Feature,CaroselModel

# Create your views here.
def carosel(request):
    carosel = CaroselModel.objects.all()
    features = Feature.objects.all()[:3]


    context = {
        'features':features,
        'carosel': carosel
    }
    return render(request, 'carousel/index.html',context)