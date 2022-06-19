from django.shortcuts import render

def studentHome(request):
    return render(request, 'studentHome.html')
