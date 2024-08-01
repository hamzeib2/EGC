from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)# كل زبون واحد مرتبط بحساب واحد فقط وممكن نكون فاضي هي الخانة
    verify_code = models.CharField(max_length=200,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    user_image = models.ImageField(null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    telegram_username=models.CharField(max_length=200,null=True,blank=True)
    suspand =models.BooleanField(default=False)
    verified =models.BooleanField(default=False)
    password = models.CharField(max_length=200,null=True,blank=True)
    age_range = (
        ('under 15','under 15'),
        ('from 15 to 20' , 'from 15 to 20'),
        ('from 21 to 25' , 'from 21 to 25'),
        ('from 26 to 32' , 'from 26 to 32'),
        ('from 33 to 36' , 'from 33 to 36'),
        ('from 37 to 42' , 'from 37 to 42'),
        ('from 43 to 47' , 'from 43 to 47'),
        ('more than 48' , 'more than 48'),
        )

    age=models.CharField(max_length=200,null=True ,blank=True,choices=age_range)
    study_field= (
        ('school_student', (
            ('elementry school', 'elemebtary school'),
            ('high school', 'high school'),
            ('other','other')
        )),
        ('college_student', (('medical colleges','medical colleges'),
                            ('engineering colleges','engineering colleges'),
                            ('literary colleges','litrary colleges'),
                            ('science colleges','science colleges'),
                            ('other','other'),)

        ))
    study=models.CharField(max_length=200,null=True,blank=True,choices=study_field)
    sex=(('male','male'),('female','female'))
    gender=models.CharField(max_length=200,null=True,blank=True,choices=sex)
    work= (
        ('governmental employee', (
            ('work in government department', 'work in government department'),
            ('teacher', 'teacher'),
            ('other','other')
        )),
        ('free_work',  (('clothes dealer','clothes dealer'),
                        ('electronics dealer','electronics dealer'),
                        ('librarian','librarian'),
                        ('not_working','not_working'),)

        ),
        ('other','other')
        )
    work_field=models.CharField(max_length=200,null=True ,blank=True,choices=work)
    info_updated = models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return str(self.name)#القيمة يلي رح يرجعها منل عنوان بالجداول التابع متل باني للكلاس
    
    @property 
    def imageURL(self):#اذا ما عنا صورة رح يعطينا خطا لهيك عملنا تابع مشان يشوف اذا في صورة بيحط الرابط واذا لا بيخلي الرابط فاضي
        try:
            url = self.user_image.url
        except:
            url=''
        return url
    

########################################

class CustomerProduct(models.Model):
   
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    name=models.CharField(max_length=200,null=True)
    who =  models.CharField(max_length=200,null=True)
    all_codes= models.TextField(blank=True,null=True)
    num_codes = models.CharField(max_length=200,null=True)
    codes = models.TextField(blank=True,null=True)
    error_codes = models.TextField(blank=True,null=True)
    redundant_codes = models.TextField(blank=True,null=True)
    get_invoice = models.TextField(blank=True,null=True)
    date_upload = models.DateTimeField(auto_now_add=True , null=True)
 
    ################## Amazon us
    Amazon_us_5 = models.TextField(blank=True,null=True)
    Amazon_us_10 = models.TextField(blank=True,null=True)
    Amazon_us_15 = models.TextField(blank=True,null=True)
    Amazon_us_20 = models.TextField(blank=True,null=True)
    Amazon_us_25 = models.TextField(blank=True,null=True)
    Amazon_us_30 = models.TextField(blank=True,null=True)
    Amazon_us_50 = models.TextField(blank=True,null=True)
    Amazon_us_100 = models.TextField(blank=True,null=True)
    ############################## Apple
    Apple_5 = models.TextField(blank=True,null=True)
    Apple_10 = models.TextField(blank=True,null=True)
    Apple_15 = models.TextField(blank=True,null=True)
    Apple_20 = models.TextField(blank=True,null=True)
    Apple_25 = models.TextField(blank=True,null=True)
    Apple_30 = models.TextField(blank=True,null=True)
    Apple_40 = models.TextField(blank=True,null=True)
    Apple_50 = models.TextField(blank=True,null=True)
    Apple_60 = models.TextField(blank=True,null=True)
    Apple_100 = models.TextField(blank=True,null=True)
    ########################### Amzon uk
    Amazon_uk_5 = models.TextField(blank=True,null=True)
    Amazon_uk_10 = models.TextField(blank=True,null=True)
    Amazon_uk_15 = models.TextField(blank=True,null=True)
    Amazon_uk_20 = models.TextField(blank=True,null=True)
    Amazon_uk_25 = models.TextField(blank=True,null=True)
    Amazon_uk_30 = models.TextField(blank=True,null=True)
    Amazon_uk_50 = models.TextField(blank=True,null=True)
    Amazon_uk_100 = models.TextField(blank=True,null=True)
    ################################## Amazon de
    Amazon_de_5 = models.TextField(blank=True,null=True)
    Amazon_de_10 = models.TextField(blank=True,null=True)
    Amazon_de_15 = models.TextField(blank=True,null=True)
    Amazon_de_20 = models.TextField(blank=True,null=True)
    Amazon_de_25 = models.TextField(blank=True,null=True)
    Amazon_de_30 = models.TextField(blank=True,null=True)
    Amazon_de_50 = models.TextField(blank=True,null=True)
    Amazon_de_100 = models.TextField(blank=True,null=True)
    ################################ nido
    Nintendo_10 = models.TextField(blank=True,null=True)
    ###########################Rezer
    Razer_5 = models.TextField(blank=True,null=True)
    Razer_10 = models.TextField(blank=True,null=True)
    Razer_15 = models.TextField(blank=True,null=True)
    Razer_20 = models.TextField(blank=True,null=True)
    Razer_25 = models.TextField(blank=True,null=True)
    Razer_30 = models.TextField(blank=True,null=True)
    Razer_50 = models.TextField(blank=True,null=True)
    Razer_100 = models.TextField(blank=True,null=True)
    
  
    def __str__(self):
        return str(self.customer) 
############################################################
class Cards_search(models.Model):
    name = models.ForeignKey(CustomerProduct,on_delete=models.CASCADE,null=True)
    type = models.TextField(blank=True,null=True)
    cards = models.TextField(blank=True,null=True)

    if name is not None:
        def __str__(self):
            return self.name.who+" "+"id:"+" "+str(self.name.id)


##############################################

class Product(models.Model):
    CATEGORY = (
        ('Amazon' , 'Amazon'),
        ('Amazon-UK' , 'Amazon-UK'),
        ('Amazon-German','Amazon-German'),
        ('Itunes' , 'Itunes'),
        ('Razer-Gold' , 'Razer-Gold'),
        ('Razer-Gold-Global' , 'Razer-Gold-Global'),
        ('Master-Card' , 'Master-Card'),
        ('Wolmart' , 'Wolmart'),
        ('Nintendo','Nintendo'),
        ('Uber' , 'Uber'),
        ('XBOX' , 'XBOX'),
        ('FreeFire&Pubg','FreeFire&Pubg'),
        ('clothes','clothes'),
        ('other','other')
    )
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    name=models.CharField(max_length=200,null=True)
    sname=models.CharField(max_length=200,null=True)
    price=models.IntegerField(default=0,null=True,blank=True)
    offer=models.FloatField()
    revenue = models.IntegerField(default=0,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    digital=models.BooleanField(default=False,null=True,blank=True)#قيمة بتدل على انو المنتج رقمي ولا لا مشان النقل بعدين
    category = models.CharField(max_length=200 , choices=CATEGORY,blank=True)
    short_desc = models.TextField(blank=True)
    tall_desc = models.TextField(blank=True)
    num_views = models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    extra_photo = models.ImageField(null=True,blank=True)
    extra_img = models.ImageField(null=True,blank=True)
    date_upload = models.DateTimeField(auto_now_add=True , null=True,blank=True)

    def __str__(self):
        return self.name +" "+"id:"+" "+str(self.id)

    @property 
    def imageURL(self):#اذا ما عنا صورة رح يعطينا خطا لهيك عملنا تابع مشان يشوف اذا في صورة بيحط الرابط واذا لا بيخلي الرابط فاضي
        try:
            url = self.image.url
        except:
            url=''
        return url
    

    @property
    def image_extra(self):
        try:
            url= self.extra_photo.url
        except:
            url=''
        return url
    
    @property
    def image_extra_p(self):
        try:
            url= self.extra_img.url
        except:
            url=''
        return url


###########################################################################################
class Order(models.Model):
    CATEGORY = (
        ('Rejected' , 'Rejected'),
        ('Processing' , 'Processing'),
        ('Complate' , 'Complate'),
        
    )
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)# كل زبون ممكن بكون عندو اكنر من طلبية علاقة ميني تو ميني واذا انحذف اليوزر رح تصير الطلبية نول
    date_orderd=models.DateTimeField(auto_now=True)#حفظ زمن الطلبية
    complete=models.BooleanField(default=False) #مشان نشوف البطاقة اذا مكتملة ولا لا
    delevered=models.BooleanField(default=False)#مشان نشوف البطاقة اذا مكتملة ولا لا
    rejected=models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100 , null =True)#معلومات اضافية عن الطلبية
    state =  models.CharField(max_length=200 , choices=CATEGORY,blank=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping


    @property
    def get_state(self):
        if self.complete == True:
            state = 'Processing'
        if self.complete and self.delevered == True:
            state = 'Complete'
        return state



    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()#هي الطريقة يلي منجيب فيها الابناء كلن
        try:
            total = sum([item.get_price for item in orderitems])
        except:
            total = None
        return total
    
    @property
    def get_cart_quantity(self):
        orderitems=self.orderitem_set.all()#هي الطريقة يلي منجيب فيها الابناء كلن
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_revenue(self):
        orderitems=self.orderitem_set.all()#هي الطريقة يلي منجيب فيها الابناء كلن
        try:
            total = sum([(item.get_item_revenue) for item in orderitems])
        except:
            total = None
        return total

#######################################################################################################################

class Orderitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)#بالكارت ممكن يكون اكتر طلبية للمنتج نفسو
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)#وبالكارت ممكن بكون من اورد ايتم للطلبية نفسها
    #orderitem is a child for both order and product
    #الطلبية ممكن يكون الا اكتر من اوردر ايتم والاورد ايتم يحتوي منتج
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        try:
            total=self.product.price * self.quantity#we want the total is price of product from parent product that attach to it * the quantity from here
        except:
            total = None
        return total

    @property
    def get_price_offer(self):
        try:
            total=self.product.price * ((100 - self.product.offer) / 100) #we want the total is price of product from parent product that attach to it * the quantity from here
            to = str(total)
            t = to[0:5]
            tt = float(t)
        except:
            total = None
            tt = total
        return tt

    @property
    def get_price(self):
        try:
            total=self.product.price * ((100 - self.product.offer) / 100) * self.quantity #we want the total is price of product from parent product that attach to it * the quantity from here
            to = str(total)
            t = to[0:5]
            tt = float(t)
        except:
            total = None
            tt = total
        return tt
    
    @property
    def get_item_revenue(self):
        try:
            total=self.product.price * (( self.product.revenue) / 100) * self.quantity #we want the total is price of product from parent product that attach to it * the quantity from here
            to = str(total)
            t = to[0:5]
            tt = float(t)
        except:
            total = None
            tt = total
        return tt
    
#########################################################################################################################

class Shippingadd(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)#null can not be false beacuse there must be an order
    coupon=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=200,null=False)
    state=models.CharField(max_length=200,null=False)
    zipcode=models.CharField(max_length=200,null=False)
    total_price = models.FloatField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address




