# from amazon.models import LoginForm
# from amazon.models import clothe
# from amazon.models import footware
# from amazon.models import accessories
from amazon.models import RegisterForm
from django.shortcuts import render,redirect 
# from django.urls import path,include
from django.http import HttpResponse
from django.core.mail import send_mail
# from django.http import HttpResponse
# from django.template import loader

# Create your views here.


def sendSimpleEmail(request):
   res = send_mail("love", "i love you jay", "khyatikansara23996@gmail.com", ["jayupadhyay11192@gmail.com"])
   return HttpResponse("Success")

def insert_data(request):
   #Creating an entry
   
	womenshops = [{
					'type':'Clothes',
					'value':[
							{
								'Product':'Shirt',
				   				'Price':500
			   				},
			   				{
				   				'Product':'Jeans',
				   				'Price':800
			   				},
			   				{
				   				'Product':'Dress',
				   				'Price':1000
			   				}]
			   		},
			   	{
		   			'type':'Footware',
		   			'value':[
		   					{
			   					'Product':'Sandals',
				   				'Price':200
		   					},
		   					{
			   					'Product':'Shoes',
				   				'Price':300
		   					},
		   					{
				   				'Product':'Casual shoes',
				   				'Price':1000
			   				}]
		   		},
			   	{
		   			'type':'Accessories',
		   			'value':[
		   					{
		   						'Product':'Ring',
				   				'Price':1000
		   					},
		   					{
		   						'Product':'watch',
				   				'Price':500
		   					},
		   					{
				   				'Product':'Bracelet',
				   				'Price':400
			   				}
			   				]
		   		}]

	# for i in womenshops:
	# 	print(i)
	# 	for k,v in i.items():
	# 		print(k,v)
	# 		l = len(v)
	
	# if womenshops[0]['type'] == "Clothes":	
	for data in womenshops[0]['value']:
		print(data['Product'])
		print(data['Price'])
			# d['Product'] = data['Product']
			# d['Price'] = data['Price']
	# print(len(d))

	# for le in range(len(d)):
		c = clothe.objects.create(Product = data['Product'],Price = data['Price'])

		# Read ALL entries
		c1 = clothe.objects.all()
		res ='Printing all clothe entries in the DB : <br>'
		for elt in c1:
			res += elt.Product+"<br>"
	# elif womenshops[1]['type'] == "Footware":
	for data1 in womenshops[1]['value']:
		# 	print(data1['Product'])
		# 	print(data1['Price'])
		f = footware.objects.create(Product = data1['Product'],Price = data1['Price'])
		
		#Read ALL entries
		f1 = footware.objects.all()
		res ='Printing all Dreamreal entries in the DB : <br>'

		for elt in f1:
			res += elt.Product+"<br>"
		
		# Delete an entry
		res += '<br> Deleting an entry <br>'
		f1.delete()
		f2 = data1(Product = "Sandals", Price = 800)
		res += 'Updating entry<br>'
		f3 = footware.objects.get(Product = 'Sandals')
		print(data1)
		f3.Product = 'bellies'
	   
	   # dreamreal.save()

	   # dreamreal.save()
	# elif womenshops[2]['type'] == "Accessories":
	for data2 in womenshops[2]['value']:
		# 	print(data2['Product'])
		# 	print(data2['Price'])
		a = accessories.objects.create(Product = data2['Product'],Price = data2['Price'])
		#Read ALL entries
		# a1 = accessories.objects.all()
		# res ='Printing all footware entries in the DB : <br>'
		# for elt in a1:
		# 	res += elt.Product+"<br>"
	else:
		print("no data found")
	# return HttpResponse(res)
	return render(request, "amazon/view.html",{"wo":womenshops})

def register(request):
	# empl = employee_de.objects.filter()
# 	print("hiiiii")
# 	# print(empl)
	return render(request, "register.html",{})

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']

   else:
      MyLoginForm = LoginForm()

   # return HttpResponse("Success")
   return render(request, "login.html", {})

 
# def login(request):
# 	username = "not logged in"

# 	if request.method == "POST":
# 		MyLoginForm = LoginForm(request.POST)
# 		if MyLoginForm.is_valid():
# 			username = MyLoginForm.cleaned_data['username']
# 	else:
#    		MyLoginForm = Loginform()

# 	return render(request, 'login.html', {"username" : username})
	# return render(request, "login.html",{"username" : username})
	# return redirect(register)
# def amazon(request):	 
#     clothes = [{
#                 'type': 'women',
#                 'values': [
#                     {
#                         'pname': 'Jeans',
#                         'quan': 80,
#                         'price': 1000
#                     },
#                     {
#                         'pname': 'Shirt',
#                         'quan': 20,
#                         'price': 500
#                     },
#                     {
#                         'pname': 'Dress',
#                         'quan': 50,
#                         'price': 2000
#                     }
#                 ]
#             },
#             {
#                 'type': 'men',
#                 'values': [
#                     {
#                         'pname': 'Jeans',
#                         'quan': 30,
#                         'price': 800
#                     },
#                     {
#                         'pname': 'Shirt',
#                         'quan': 40,
#                         'price': 500
#                     }
#                 ]
#             }]

#     footware = [{
#                 'type': 'women',
#                 'values': [
#                     {
#                         'pname': 'Sandals',
#                         'quan': 80,
#                         'price': 1000
#                     },
#                     {
#                         'pname': 'shoes',
#                         'quan': 20,
#                         'price': 500
#                     }
#                 ]
#             },
#             {
#                 'type': 'men',
#                 'values': [
#                     {
#                         'pname': 'Sandals',
#                         'quan': 30,
#                         'price': 800
#                     },
#                     {
#                         'pname': 'shoes',
#                         'quan': 40,
#                         'price': 500
#                     }
#                 ]
#             }]


	# return HttpResponse(template.render(context,request))	
# def hello(request):
#    return render(request, "myapp/template/hello.html", {})