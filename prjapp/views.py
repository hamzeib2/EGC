from django.http import JsonResponse
from django.shortcuts import render,redirect , HttpResponse
from django.contrib.auth.models import Group,User,auth
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .functions import Rezer_Gold,Apples,Nintendo_Or_Uber,Amzon_us,Amzon_Uk_or_De,Convert_List_to_Text,Convert_List,most_redundant_element,append_sort_codes_am_us,get_code_from_text_file_am_us,append_sort_codes_apple,get_code_from_text_file_apple,append_sort_codes_am_uk_de,get_code_from_text_file_am_uk_de,append_sort_codes_nin,get_code_from_text_file_nin
import json
import time
import datetime
import random
import requests
from . util import cartData , guestOrder,update_user_order,is_admin,append_order_into_text_file,get_orders_from_text_file,create_map,append_prefer_in_file,get_prefer_from_file,create_map_current_location_only,append_order_category_into_text_file , get_trend_from_file
from django.conf import settings
from .association_rules import process_association,process_association_categories
from .decorators import unauth_user,allowed_users,auth_user , admins,time_restrict
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# bot_name = settings.TELEGRAM_BOT_NAME
# bot_token = settings.TELEGRAM_BOT_TOKEN
# redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

# Create your views here.

#####################  Const Variable
user_bills={'hh': [] ,'tt':['Amazon_us_5*1']}


@unauth_user
def register_user(request):
    if request.method=='POST':
        uname = request.POST['username']    
        password = request.POST['password']
        password2 = request.POST['password2']
        try:
            if password == password2:
                my_user = User.objects.create_user(uname , '' , password)
                print(uname , password)
                my_user.save()
                my_group = Group.objects.get(name='customers')
                my_group.user_set.add(my_user)
                
                customer = Customer.objects.create(user = my_user , name = uname , password = password)
                user = authenticate(request , username = uname , password = password)
                login(request , user)
                update_user_order(request)
                
                return redirect ('store')
            else:
                messages.success(request , (" There Is Error In Your Password..!!"))
                return redirect ('sign_up')
        except:
            messages.success(request , (" This Email is Used..!!"))
            return redirect ('sign_up')
    else:
        return render(request , 'auth/signup.html')
#####################################################################    
@unauth_user
def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password  = request.POST['password']
        try:
            customer = Customer.objects.get(name = email )
            user = authenticate(request , username = email , password = password)
            if user is not None:
                if customer.suspand == True:
                    messages.success(request , ("Your Account Has Been Suspended...!!!"))
                    return redirect('login')
                
                login(request , user)
                return redirect('store')
            else:
                messages.success(request , ("Email or Password is Wrong...!!!"))
                
                return redirect('login')
        except:
            messages.success(request , ("This Email Does Not Exist...!!!"))
                
            return redirect('login')
    else:
        return render(request , 'auth/login.html')

#################################################################
@auth_user
def logout_user(request):
    logout(request)
    
    return redirect ('login')
#################################



###################################
# @time_restrict
@auth_user
def store(request):
    bool = is_admin(request)
    print(bool)
    # messages.success(request , ("SomeThing Went Wrong Please Try Again Later...!!!"))
    cust = request.user.customer
    cu = Customer.objects.get(name = cust)
    if cu.suspand == True:
        logout(request)
        return redirect ('login')
    # if cu.name not in user_bills:
    #     messages.success(request , ("Who Are You, What you Want Here ...!!!"))
    #     cu.suspand = True
    #     logout(request)
    #     return redirect ('login')
    ################################

    products = Product.objects.all()
    try:
        custprd = CustomerProduct.objects.get(customer = cust)
    except:
        custprd = ''
    context = {'cu':cu,'bool':bool,'custprd':custprd,'products':products , 'cust':cust}
    return render(request,'store/index.html',context)

#################################
@auth_user
@allowed_users(allowed_roles=['admins'])
def Search_code(request):
    cust = request.user.customer
    search = Cards_search.objects.get(name = 4)


    context = {'cust':cust ,'search':search}
    return render(request,'store/search_code.html',context)

#############################

def accept_user(request):
    custs = []
    sort_customers_id = []
    
    customers = Customer.objects.all()
    for i in customers:
        sort_customers_id.append(i.id)

    sort_customers = sorted(sort_customers_id, reverse=True)
    for i in sort_customers:
        for j in customers:
            if i == j.id:
                custs.append(j)


    context = {'custs':custs,'customers':customers}
    return render(request,'store/accept_user.html',context)



#########################################################customer_id
def suspended(request , customer_id):
    this_cust = Customer.objects.get(id = customer_id)
    print(this_cust)
    if this_cust.suspand == False:
        this_cust.suspand = True
        this_cust.save()
   
    
    return HttpResponse("Success!")

#######################################################################
def notsuspended(request , customer_id):
    this_cust = Customer.objects.get(id = customer_id)
    print(this_cust)
    if this_cust.suspand == True:
        this_cust.suspand = False
        this_cust.save()
    
    return HttpResponse("Success!")

#######################################################################
def verified(request , customer_id):
    this_cust = Customer.objects.get(id = customer_id)
    print(this_cust)
    if this_cust.verified == False:
        this_cust.verified = True
        this_cust.save()
    
    return HttpResponse("Success!")

#######################################################################
def notverified(request , customer_id):
    this_cust = Customer.objects.get(id = customer_id)
    print(this_cust)
    if this_cust.verified == True:
        this_cust.verified = False
        this_cust.save()
    
    return HttpResponse("Success!")

#######################################################################
def delete_user(request,customer_id):
    this_cust = Customer.objects.get(id = customer_id)
    cust = User.objects.get(username = this_cust.email)
    print(this_cust)
    cust.delete()
    return HttpResponse("Success!")

###############################
@auth_user
@allowed_users(allowed_roles=['admins'])
def Search_for_code(request):
    cust = request.user.customer
    data = json.loads(request.body)
    code = data['code']
    # print(code)
    Names =[]
    for i in user_bills:
        custprd = CustomerProduct.objects.get(who = i)
        if code in custprd.all_codes:
            Names.append(i)
        
    # searc = Cards_search.objects.get_or_create(name = 'hh')
    search = Cards_search.objects.get(name = 4)
    cod = Convert_List(Names)
    search.type = cod

    search.save()
  





    return JsonResponse('item was added',safe=False)  
######################################
@auth_user
@allowed_users(allowed_roles=['admins'])
def get_invoice(request):
    cust = request.user.customer
    bills = []
    for i in user_bills:
        if user_bills[i] != []:
            bills.append(i)
            

    context = {'bills':bills,'cust':cust}
    return render(request,'store/get_an_invoice.html',context)


########################
@auth_user
@allowed_users(allowed_roles=['admins'])
def draw_cards(request):
    cust = request.user.customer
    bills = []
    for i in user_bills:
        if user_bills[i] != []:
            bills.append(i)
            

    context = {'bills':bills,'cust':cust}
    return render(request,'store/draw_cards.html',context)
###################################
def Reset_Draw_Cards(request):
    data = json.loads(request.body)
    user = data['user']
    custprd= CustomerProduct.objects.get(who = user)
    custprd.Amazon_us_5 = ''
    custprd.Amazon_us_10 = ''
    custprd.Amazon_us_15 = ''
    custprd.Amazon_us_20 = ''
    custprd.Amazon_us_25 = ''
    custprd.Amazon_us_30 = ''
    custprd.Amazon_us_50 = ''
    custprd.Amazon_us_100 = ''
    #################
    custprd.Amazon_uk_5 = ''
    custprd.Amazon_uk_10 = ''
    custprd.Amazon_uk_15 = ''
    custprd.Amazon_uk_20 = ''
    custprd.Amazon_uk_25 = ''
    custprd.Amazon_uk_30 = ''
    custprd.Amazon_uk_50 = ''
    custprd.Amazon_uk_100 = ''
    ################
    custprd.Amazon_de_5 = ''
    custprd.Amazon_de_10 = ''
    custprd.Amazon_de_15 = ''
    custprd.Amazon_de_20 = ''
    custprd.Amazon_de_25 = ''
    custprd.Amazon_de_30 = ''
    custprd.Amazon_de_50 = ''
    custprd.Amazon_de_100 = ''
    ################
    custprd.Apple_5 = ''
    custprd.Apple_10 = ''
    custprd.Apple_15 = ''
    custprd.Apple_20 = ''
    custprd.Apple_25 = ''
    custprd.Apple_30 = ''
    custprd.Apple_50 = ''
    custprd.Apple_100 = ''
    ###############
    custprd.Nintendo_10 = ''
    #################
    custprd.Razer_5 = ''
    custprd.Razer_10 = ''
    custprd.Razer_15 = ''
    custprd.Razer_20 = ''
    custprd.Razer_25 = ''
    custprd.Razer_30 = ''
    custprd.Razer_50 = ''
    custprd.Razer_100 = ''
    #########################
    custprd.save()


    return JsonResponse('item was added',safe=False)



#################################
@auth_user
@allowed_users(allowed_roles=['admins'])
def draw_card(request , user):
    cust = request.user.customer
    custprd = CustomerProduct.objects.get(who = user)
    help_bill = []
    for i in user_bills:
        if i == user:
            for j in user_bills[i]:
                help_bill.append(j)

    skip=''
    all_bill = []
    for i in help_bill:
        for j in i:
            if j == '*':
                all_bill.append(skip)
                skip=''
                break
            skip+=j

########################################
    current_url = request.path
    
    parts = current_url.split('draw_card/')
    print(parts)
    print(current_url)
    if len(parts) > 1:
        what_comes_after = parts[1]

        # do something with what_comes_after
        print(what_comes_after)  # prints "hh" in your example
    else:
        print("No part after draw_card/")
    # custprd = CustomerProduct.objects.get(who = user)
    

    context = {'what_comes_after':what_comes_after,'all_bill':all_bill,'custprd':custprd , 'cust':cust}
    return render(request,'store/draw_card.html',context)



##########################
@csrf_exempt
@auth_user
@allowed_users(allowed_roles=['admins'])
def getuserinvoice(request):
    bills = []
    data = json.loads(request.body)
    customer = data['user']
    cu = CustomerProduct.objects.get(who = customer)
    # for i in user_bills:
    #     if i == customer:
    #         bills = user_bills[i]
    #         bill = Convert_List(bills)
    #         cu.get_invoice = bill
    #         cu.save()



    return JsonResponse('item was added',safe=False)   
#################################


# def go_to_get_invoice(request , customer):
#     cust = CustomerProduct.objects.get(who = customer)
#     return 


@auth_user
@csrf_exempt
def Process_cards(request):
    cust = request.user.customer
    data = json.loads(request.body)
    prdid = data['prdid']
    cards = data['cards']
    values = data['value']
    cod = []
    error = []
    product = Product.objects.get(id = prdid)
    custpr = CustomerProduct.objects.get_or_create(customer = cust)
    custprd = CustomerProduct.objects.get(customer = cust)
    #####################################if codes in Erorrs:
    if product.name == 'Amazon us':
        cod ,error =  Amzon_us(cards)
    if product.name == 'Apple':
        cod ,error =  Apples(cards)
    if product.name == 'Amazon uk':
        cod ,error =  Amzon_Uk_or_De(cards)
    if product.name == 'Amazon de':
        cod ,error =  Amzon_Uk_or_De(cards)
    if product.name == 'Nintendo':
        cod ,error =  Nintendo_Or_Uber(cards)
    if product.name == 'Razer Gold':
        cod , error = Rezer_Gold(cards)

    co , err = Convert_List_to_Text(cod , error)
    custprd.name = product.sname
    custprd.codes = co
    custprd.error_codes = err
    sct = Customer.objects.get(name = cust).name
    custprd.who = sct
    custprd.save()
    ##############################if Codes is Redundant
    redun = []
    redunn = []
    redun = most_redundant_element(cod)
    for i in redun:
        if i in redunn:
            continue
        else:
            redunn.append(i)
        
    redundant = Convert_List(redunn)
    custprd.redundant_codes = redundant
    custprd.save()
   
    ###########################codes After delete Redundant
    for i in redun:
        cod.remove(i)
    num_codes = len(cod)
    co = Convert_List(cod)
    custprd.codes = co
    custprd.num_codes = num_codes
    custprd.save()
    ################################Append codes in All codes and thier Category:
    if custprd.all_codes == '':
        custprd.all_codes = co +'\n'
    else:    
        custprd.all_codes += co +'\n'
    types = custprd.name+'_'+ str(values)
   #############################################Append codes for thier Category:
   ###################### Amazon us 
    if types == 'Amazon_us_5':
        if custprd.Amazon_us_5 ==None:
            custprd.Amazon_us_5 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_5 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_10':
        if custprd.Amazon_us_10 ==None:
            custprd.Amazon_us_10 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_10 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_15':
        if custprd.Amazon_us_15 ==None:
            custprd.Amazon_us_15 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_15 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_20':
        if custprd.Amazon_us_20 ==None:
            custprd.Amazon_us_20 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_20 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_25':
        if custprd.Amazon_us_25 ==None:
            custprd.Amazon_us_25 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_25 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_30':
        if custprd.Amazon_us_30 ==None:
            custprd.Amazon_us_30 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_30 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_50':
        if custprd.Amazon_us_50 ==None:
            custprd.Amazon_us_50 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_50 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_us_100':
        if custprd.Amazon_us_100 ==None:
            custprd.Amazon_us_100 = custprd.codes +'\n'
        else:
            custprd.Amazon_us_100 += custprd.codes +'\n'
        custprd.save()
    ################################################ Apple 
    if types == 'Apple_5':
        if custprd.Apple_5 ==None:
            custprd.Apple_5 = custprd.codes +'\n'
        else:
            custprd.Apple_5 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_10':
        if custprd.Apple_10 ==None:
            custprd.Apple_10 = custprd.codes +'\n'
        else:
            custprd.Apple_10 += custprd.codes +'\n'
        custprd.save()
    
    if types == 'Apple_15':
        if custprd.Apple_15 ==None:
            custprd.Apple_15 = custprd.codes +'\n'
        else:
            custprd.Apple_15 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_20':
        if custprd.Apple_20 ==None:
            custprd.Apple_20 = custprd.codes +'\n'
        else:
            custprd.Apple_20 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_25':
        if custprd.Apple_25 ==None:
            custprd.Apple_25 = custprd.codes +'\n'
        else:
            custprd.Apple_25 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_30':
        if custprd.Apple_30 ==None:
            custprd.Apple_30 = custprd.codes +'\n'
        else:
            custprd.Apple_30 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_40':
        if custprd.Apple_40 ==None:
            custprd.Apple_40 = custprd.codes +'\n'
        else:
            custprd.Apple_40 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_50':
        if custprd.Apple_50 ==None:
            custprd.Apple_50 = custprd.codes +'\n'
        else:
            custprd.Apple_50 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_60':
        if custprd.Apple_60 ==None:
            custprd.Apple_60 = custprd.codes +'\n'
        else:
            custprd.Apple_60 += custprd.codes +'\n'
        custprd.save()

    if types == 'Apple_100':
        if custprd.Apple_100 ==None:
            custprd.Apple_100 = custprd.codes +'\n'
        else:
            custprd.Apple_100 += custprd.codes +'\n'
        custprd.save()
    ###################################################### Amazon uk
    if types == 'Amazon_uk_5':
        if custprd.Amazon_uk_5 ==None:
            custprd.Amazon_uk_5 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_5 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_uk_10':
        if custprd.Amazon_uk_10 ==None:
            custprd.Amazon_uk_10 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_10 += custprd.codes +'\n'
        custprd.save()
    if types == 'Amazon_uk_15':
        if custprd.Amazon_uk_15 ==None:
            custprd.Amazon_uk_15 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_15 += custprd.codes +'\n'
        custprd.save()
    if types == 'Amazon_uk_20':
        if custprd.Amazon_uk_20 ==None:
            custprd.Amazon_uk_20 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_20 += custprd.codes +'\n'
        custprd.save()
    if types == 'Amazon_uk_25':
        if custprd.Amazon_uk_25 ==None:
            custprd.Amazon_uk_25 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_25 += custprd.codes +'\n'
        custprd.save()
    if types == 'Amazon_uk_30':
        if custprd.Amazon_uk_30 ==None:
            custprd.Amazon_uk_30 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_30 += custprd.codes +'\n'
        custprd.save()
    if types == 'Amazon_uk_50':
        if custprd.Amazon_uk_50 ==None:
            custprd.Amazon_uk_50 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_50 += custprd.codes +'\n'
        custprd.save()
    if types == 'Amazon_uk_100':
        if custprd.Amazon_uk_100 ==None:
            custprd.Amazon_uk_100 = custprd.codes +'\n'
        else:
            custprd.Amazon_uk_100 += custprd.codes +'\n'
        custprd.save()
    ###################################Amzon de
    if types == 'Amazon_de_5':
        if custprd.Amazon_de_5 ==None:
            custprd.Amazon_de_5 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_5 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_10':
        if custprd.Amazon_de_10 ==None:
            custprd.Amazon_de_10 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_10 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_15':
        if custprd.Amazon_de_15 ==None:
            custprd.Amazon_de_15 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_15 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_20':
        if custprd.Amazon_de_20 ==None:
            custprd.Amazon_de_20 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_20 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_25':
        if custprd.Amazon_de_25 ==None:
            custprd.Amazon_de_25 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_25 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_30':
        if custprd.Amazon_de_30 ==None:
            custprd.Amazon_de_30 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_30 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_50':
        if custprd.Amazon_de_50 ==None:
            custprd.Amazon_de_50 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_50 += custprd.codes +'\n'
        custprd.save()

    if types == 'Amazon_de_100':
        if custprd.Amazon_de_100 ==None:
            custprd.Amazon_de_100 = custprd.codes +'\n'
        else:
            custprd.Amazon_de_100 += custprd.codes +'\n'
        custprd.save()

    #################################Nido
    if types == 'Nintendo_10':
        if custprd.Nintendo_10 ==None:
            custprd.Nintendo_10 = custprd.codes +'\n'
        else:
            custprd.Nintendo_10 += custprd.codes +'\n'
        custprd.save()



    ##############################################Rezar Gold
    if types == 'Razer_5':
        if custprd.Razer_5 ==None:
            custprd.Razer_5 = custprd.codes +'\n'
        else:
            custprd.Razer_5 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_10':
        if custprd.Razer_10 ==None:
            custprd.Razer_10 = custprd.codes +'\n'
        else:
            custprd.Razer_10 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_15':
        if custprd.Razer_15 ==None:
            custprd.Razer_15 = custprd.codes +'\n'
        else:
            custprd.Razer_15 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_20':
        if custprd.Razer_20 ==None:
            custprd.Razer_20 = custprd.codes +'\n'
        else:
            custprd.Razer_20 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_25':
        if custprd.Razer_25 ==None:
            custprd.Razer_25 = custprd.codes +'\n'
        else:
            custprd.Razer_25 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_30':
        if custprd.Razer_30 ==None:
            custprd.Razer_30 = custprd.codes +'\n'
        else:
            custprd.Razer_30 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_50':
        if custprd.Razer_50 ==None:
            custprd.Razer_50 = custprd.codes +'\n'
        else:
            custprd.Razer_50 += custprd.codes +'\n'
        custprd.save()
    if types == 'Razer_100':
        if custprd.Razer_100 ==None:
            custprd.Razer_100 = custprd.codes +'\n'
        else:
            custprd.Razer_100 += custprd.codes +'\n'
        custprd.save()

    ####################################################




    #####################################add bill to customer
    bell = str(types)+'*'+ str(len(cod))

    user_n = Customer.objects.get(name = cust).name
    user_bills[user_n].append(bell)

    # Create a dictionary to store the merged quantities
    merged_quantities = {}

    for item in user_bills[user_n]:
        name, quantity = item.rsplit('*', 1)
        quantity = int(quantity)
        if name in merged_quantities:
            merged_quantities[name] += quantity
        else:
            merged_quantities[name] = quantity

    # Reconstruct the 'tt' list with the merged quantities
    user_bills[user_n] = [f"{name}*{quantity}" for name, quantity in merged_quantities.items()]


    # print(user_bills)
    for i in user_bills:
        if i == custprd.who:
            bills = user_bills[i]
            bill = Convert_List(bills)
            custprd.get_invoice = bill
            custprd.save()






    return JsonResponse('item was added',safe=False)




###########################################
@csrf_exempt
@auth_user
def Reset_cards(request):
    cust =  request.user.customer
    data = json.loads(request.body)
    prdid = data['prdid']
    try:
        product = Product.objects.get(id=prdid)
        custprd = CustomerProduct.objects.get(customer = cust )
        custprd.codes = ''
        custprd.error_codes = ''
        custprd.redundant_codes = ''
        custprd.save()
    except:
        pass

    return JsonResponse('item was added',safe=False)
######################################
@csrf_exempt
@auth_user
@allowed_users(allowed_roles=['admins'])
def Reset_bill(request):
    data = json.loads(request.body)
    user = data['user']
    for i in user_bills:
        if i == user:
            user_bills[i] = []

    print(user_bills)
    return JsonResponse('item was added',safe=False)
############################
@auth_user
@allowed_users(allowed_roles=['admins'])
def getproducts(request):
    products= Product.objects.all()
    return JsonResponse({"products":list(products.values())})

#####################################
@auth_user
@allowed_users(allowed_roles=['admins'])
def goto_invoice(request):
    customer = CustomerProduct.objects.all()
    return JsonResponse({"customer":list(customer.values())})

@auth_user
@allowed_users(allowed_roles=['admins'])
def add_to_category(request,types):
    cust =  request.user.customer
    custpr = CustomerProduct.objects.get(customer = cust)
    rangee = ''
    if types == 'Apple_5':
        rangee = 'it!A1'
    if types == 'Apple_10':
        rangee = 'it!B1'
    if types == 'Apple_15':
        rangee = 'it!C1'
    if types == 'Apple_20':
        rangee = 'it!D1'
    if types == 'Apple_25':
        rangee = 'it!E1'
    if types == 'Apple_30':
        rangee = 'it!F1'
    if types == 'Apple_50':
        rangee = 'it!G1'
    if types == 'Apple_100':
        rangee = 'it!H1'
    
        #######Amazon US#####

    if types == 'Amazon_us_5':
        print('true')
        custpr.Amazon_us_5 += custpr.codes +'\n'
        custpr.save()
    if types == 'Amazon_us_10':
        rangee = 'am!B1'
    if types == 'Amazon_us_15':
        rangee = 'am!C1'
    if types == 'Amazon_us_20':
        rangee = 'am!D1'
    if types == 'Amazon_us_25':
        rangee = 'am!E1'
    if types == 'Amazon_us_30':
        rangee = 'am!F1'
    if types == 'Amazon_us_50':
        rangee = 'am!G1'
    if types == 'Amazon_us_100':
        rangee = 'am!H1'
    if types == 'Amazon_us_1':
        rangee = 'am!I1'
    if types == 'Amazon_us_2':
        rangee = 'am!J1'
    if types == 'Amazon_us_3':
        rangee = 'am!K1'

        #######Amazon UK#####

    if types == 'Amazon_uk_5':
        rangee = 'uk!A1'
    if types == 'Amazon_uk_10':
        rangee = 'uk!B1'
    if types == 'Amazon_uk_15':
        rangee = 'uk!C1'
    if types == 'Amazon_uk_20':
        rangee = 'uk!D1'
    if types == 'Amazon_uk_25':
        rangee = 'uk!E1'
    if types == 'Amazon_uk_30':
        rangee = 'it!F1'
    if types == 'Amazon_uk_50':
        rangee = 'uk!G1'
    
        #######Amazon DE#####

    if types == 'Amazon_german_5':
        rangee = 'uk!M1'
    if types == 'Amazon_german_10':
        rangee = 'uk!N1'
    if types == 'Amazon_german_15':
        rangee = 'uk!O1'
    if types == 'Amazon_german_20':
        rangee = 'uk!P1'
    if types == 'Amazon_german_25':
        rangee = 'uk!Q1'
    if types == 'Amazon_german_30':
        rangee = 'uk!R1'
    if types == 'Amazon_german_50':
        rangee = 'uk!S1'

        #######Razer#####

    if types == 'razer_5':
        rangee = 'it!A1'
    if types == 'razer_10':
        rangee = 'it!B1'
    if types == 'razer_15':
        rangee = 'it!C1'
    if types == 'razer_20':
        rangee = 'it!D1'
    if types == 'razer_25':
        rangee = 'it!E1'

        #######Nintendo#####
    
    if types == 'Nintendo_10':
        rangee = 'ni!P1'
    
        #######Walmart##### 
    
    if types == 'walmart_5':
        rangee = 'it!A1'
    if types == 'walmart_10':
        rangee = 'it!B1'
    if types == 'walmart_15':
        rangee = 'it!C1'
    if types == 'walmart_20':
        rangee = 'it!D1'
    if types == 'walmart_25':
        rangee = 'it!E1'
    
        #######Uber#####

    if types == 'uber_10':
        rangee = 'ni!H1'
    if types == 'uber_15':
        rangee = 'ni!J1'

        
    else:
        print('false')
    
    # return rangee



###########################