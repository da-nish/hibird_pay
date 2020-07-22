from django.shortcuts import render,HttpResponse
from .models import *
from django.http import HttpResponseRedirect
import razorpay
from datetime import datetime

# Create your views here.


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def profile(request):
	user = request.user
	try:
		profile = Profile.objects.get(user=user)
	except:
		return HttpResponseRedirect('/login/')
	transaction = TransactionDetail.objects.filter(user=user).order_by('-date')
	last_payment = transaction.first()
	if last_payment:
		if datetime.today().strftime("%B")==last_payment.payment_month and last_payment.success:
			return render(request,'profile.html',{'user':user,'profile':profile,'transaction':transaction,'paid':False})

	return render(request,'profile.html',{'user':user,'profile':profile,'transaction':transaction,'paid':True})

def payment(request):
	if request.method=='GET':
		user  = request.user
		try:
			profile = Profile.objects.get(user=user)
		except:
			return HttpResponseRedirect('/login/')
		try:
			transaction = TransactionDetail.objects.filter(user=user).order_by('date')
			last_payment = transaction.first()
			if last_payment:
				if datetime.today().strftime("%B")==last_payment.payment_month and last_payment.success:
					return HttpResponseRedirect('/profile/')
		except:
			pass

		DATA = {
		'amount':profile.plan_amount*100,
		'currency':'INR',
		'receipt':profile.user.username
		}
		client = razorpay.Client(auth=('rzp_test_WkaeFjgesty0qO','vTK0qIRRURVRzhBfGEqsvNh0'))
		dic = client.order.create(data=DATA)
		try:
			transaction = TransactionDetail.objects.get(user=user,success=False,payment_month=str(datetime.today().strftime("%B")))
			transaction.order_id = dic['id']
			transaction.save()
		except:
			transaction = TransactionDetail(user=user,order_id=dic['id'],payment_month=datetime.today().strftime("%B"))
			transaction.save()
		return render(request,'payment.html',{'order':dic['id'],'amount':dic['amount'],'user':profile,'key':'rzp_test_WkaeFjgesty0qO','transaction':transaction})

	else:
		# client.utility.verify_payment_signature({'razorpay_order_id':})
		data = request.POST
		transaction = TransactionDetail.objects.get(id=request.POST['tran'])
		transaction.date=datetime.now()
		transaction.payment_id = data['razorpay_payment_id']
		client = razorpay.Client(auth=('rzp_test_WkaeFjgesty0qO','vTK0qIRRURVRzhBfGEqsvNh0'))
		try:
			client.utility.verify_payment_signature({'razorpay_order_id':transaction.order_id,'razorpay_payment_id':data['razorpay_payment_id'],'razorpay_signature':data['razorpay_signature']})
			transaction.success	=True
			transaction.save()
			return HttpResponseRedirect('/profile/')
		except:
			return HttpResponse('Transaction Failed')


# order_amount = 50000
# order_currency = 'INR'
# order_receipt = 'order_rcptid_11'
# notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL

# client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0')