from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Booking

@csrf_exempt  # Temporarily disable CSRF protection for simplicity (not recommended for production)
def save_booking(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            booking = Booking.objects.create(
                staff=data['staff'],
                service=data['service'],
                date=data['date'],
                start_time=data['startTime'],
                end_time=data['endTime'],
                payment_method=data['paymentMethod'],
                card_number=data.get('cardNumber', ''),
                expiry_date=data.get('expiryDate', ''),
                cvv=data.get('cvv', ''),
                bank_name=data.get('bankName', ''),
                account_number=data.get('accountNumber', ''),
                additional_notes=data.get('additionalNotes', '')
            )
            return JsonResponse({"status": "success", "message": "Booking saved!", "booking_id": booking.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

def admin_bookings(request):
    bookings = Booking.objects.all()
    print(bookings)  # Check if the queryset is being fetched
    return render(request, 'admin-bookings.html', {'bookings': bookings})

# views.py
from django.shortcuts import render, redirect
from .models import Staff
from .form import StaffForm

def manage_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_staff')
    else:
        form = StaffForm()
    staff_list = Staff.objects.all()
    return render(request, 'admin/manage_staff.html', {'form': form, 'staff_list': staff_list})


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