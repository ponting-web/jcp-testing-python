from django.shortcuts import render, render_to_response

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')

def main(request):
    return render(request, 'main.html')

def portfolio_details(request):
    return render(request, 'portfolio_details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

