from django.shortcuts import render


def error404(request, exception=None):
    return render(request, '404.html', status=404)

def error500(request):
    return render(request, '500.html', status=500)