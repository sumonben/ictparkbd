from django.http import HttpResponse
from django.shortcuts import render
from .models import Payment
from accounts.models import CustomUser
from .forms import PaymentCreateForm
from django.contrib.auth.models import User
# Create your views he

def CreatePayment(request):
 if request.user.is_authenticated:
    user = request.user
    form = PaymentCreateForm(request.POST, request.FILES)
    users=CustomUser.objects.all()
    if request.method == 'POST':
        for user in users:
          print(request.POST['email'])
          payment = Payment(email=user.email, user_id=user.pk,phone=user.phone,month=request.POST['month'], amount=request.POST['amount'], status=request.POST['status'],start_date=request.POST['start_date'],end_date=request.POST['end_date'],deadline=request.POST['deadline'])
          payment.save()
        
    #return HttpResponse("Succesfull")
    return render(request, 'payments/createpayment.html', {'form': form})
    