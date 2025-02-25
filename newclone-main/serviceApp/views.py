from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request,'service.html')

def review(request):
    return render(request,'review.html')

def booking1(request):
    return render(request,'booking1.html')

def account(request):
    return render(request,'account.html')

def a_booking(request):
    return render(request,'admin-bookings.html')

def a_dashboard(request):
    return render(request,'ad.html')

def a_emp(request):
    return render(request,'admin-employees.html')

def a_playment(request):
    return render(request,'admin-payments.html')

def a_review(request):
    return render(request,'admin-reviews.html')

def a_service(request):
    return render(request,'admin-services.html')

def a_users(request):
    return render(request,'admin-users.html')
