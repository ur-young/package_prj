from django.shortcuts import render

# Create your views here.
def fileupload(request):
    return render(
        request,
        'file_page/fileupload.html',
    )
