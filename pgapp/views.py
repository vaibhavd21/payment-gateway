from os import name
from django.shortcuts import render
from django.http import HttpResponse
from payment_gateway.settings import *
from django.views.decorators.csrf import csrf_exempt
from time import time
import math
import razorpay
# Create your views here.
from .models import payment 


order = None
# amount = 1
# email = ""
# msg = ""
# name = ""
# currency = "INR"
# receipt = f"payvrd-{int(time())}"
# notes = {"email":email,"name":name} 
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

def home(request):
    #action = request.GET.get('action')


    # if action == 'create_payment':
    #     #global amount
    #     # global email
    #     # global msg
    #     # global name
    #     #global currency
    #     #global receipt
    #     #global notes
    #     # DATA = {'receipt':receipt,'notes' : notes,'amount' : amount,'currency' : currency}
    #     # order = client.order.create(data=DATA)
    #     return render(request,'index.html',{'create_order':True,'order':order})
    if request.method == 'POST':
        # global email
        # global msg
        # global name
        # global amount
        # global currency
        # global receipt
        # global notes
        name = request.POST['name']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        amount = math.floor(amount * 100)
        msg = request.POST['message']
        print(name)
        print(email)
        print(amount)
        print(msg)
        receipt = f"payvrd-{int(time())}"
        notes = {"email":email,"name":name,"message":msg} 
        DATA = {'receipt':receipt,'notes' : notes,'amount' : amount,'currency' : 'INR'}
        order = client.order.create(data=DATA)
        paym = payment()
        paym.name = name
        paym.email = email
        paym.amount = amount
        paym.order_id = order.get('id')
        paym.save()
        
        return render(request,'index.html',{'successful_submit':True,'order':order})

    
    
    if request.method == 'GET':
        return render(request,'index.html')

@csrf_exempt
def success(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment_obj = payment.objects.get(order_id = razorpay_order_id)
            payment_obj.payment_id = razorpay_payment_id
            payment_obj.status = True
            payment_obj.save()

            return render(request,'success.html')
        except:
            return HttpResponse("Invalid")