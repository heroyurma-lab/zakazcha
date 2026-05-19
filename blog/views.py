from django.shortcuts import render

def home_page_view(request):
    # Bu funksiya 'home.html' faylini brauzerga yuboradi
    return render(request, 'home.html')