from django.shortcuts import render

# Create your views here.
def map(request):
    return render(
        request,
        'sub_page/map.html',
    )