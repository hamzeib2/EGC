from os import name
from django.urls import path

from . import views


urlpatterns = [
    path('store/' , views.store , name= 'store'),
    path('getinvoice/' , views.get_invoice , name= 'getinvoice'),
    path('draw_cards/' , views.draw_cards , name='draw_cards'),
    path('draw_card/<str:user>', views.draw_card , name= 'draw_card'), 
    path('search_code/' , views.Search_code , name='search_code'),
    path('getsearchcode/' , views.Search_for_code , name='getsearchcode'),
    path('accept_user/' , views.accept_user , name='accept_user'),

    path('' , views.register_user , name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    

    path('verified/<str:customer_id>', views.verified , name= 'verified'),
    path('notverified/<str:customer_id>', views.notverified , name= 'notverified'),
    path('delete_user/<str:customer_id>', views.delete_user , name= 'delete_user'), 
    path('suspended/<str:customer_id>', views.suspended , name= 'suspended'), 
    path('notsuspended/<str:customer_id>', views.notsuspended , name= 'notsuspended'), 
    path('getuserinvoice/' , views.getuserinvoice , name='getuserinvoice'),
    path('Reset_Draw_Cards/' , views.Reset_Draw_Cards , name='Reset_Draw_Cards'),
    path('Process_cards/' , views.Process_cards , name='Process_cards'),
    path('Reset_cards/' , views.Reset_cards , name='Reset_cards'),
    path('Reset_bill/' , views.Reset_bill , name='Reset_bill'),
    path('getproduct/' , views.getproducts , name='getproducts'),
    path('goto_invoice/' , views.goto_invoice , name='goto_invoice'),
]