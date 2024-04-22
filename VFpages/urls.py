from django.urls import path
from .import views

urlpatterns= [
   path('',views.home_page,name="home_page"),
   path('contact-us/', views.contact_us, name='contact_us'),
   path('insert_customer_details/',views.insert_customer_details,name='insert_customer_details'),
   path('about-us/', views.about_us, name='about-us'),
   path('header_fn/', views.header_fn, name='header_fn'),
   path('footer/', views.footer, name='footer'),

   
  
   path('international-tour/', views.main_Destination, name='international-tour'),
   path('international-tour-package/<str:continent_name>/', views.main_DestinationCity, name='international-tour-package'),
   path('domestic-package/<str:continent_name>/', views.main_DestinationCity, name='domestic-package'),
   path('international-tour-packages/<str:city_name>/', views.main_DestinationAttraction, name='international-tour-packages'),
   path('main_DestinationAttraction/<str:city_name>/', views.main_DestinationAttraction, name='main_DestinationAttraction'),
   path('domestic-tour/', views.domestic_city, name='domestic-tour'),
   
   path('catagories_city/<str:city_name>/', views.catagories_city, name='catagories_city'),


   path('blog/', views.gridblogus, name='gridblogus'),
   # path('bloglist/', views.bloglist, name='bloglist'),
   path('blogs/<str:blog_url>/', views.blogsdetails, name='blogsdetails'),
   # path('download_images/', views.download_images, name='download_images'),
   
   path('lead_itinerary/<str:lead>', views.lead_itinerary, name='lead_itinerary'),
   
   # Login
   path('send_otp/',views.send_otp,name='send_otp'),
   path('verify-otp/', views.verify_otp, name='verify_otp'),
   path('signups/', views.signups, name='signups'),
   path('login_views/',views.login_views,name='login_views'),
   path('logout_view/',views.logout_view,name='logout_view'),
   path('send_otp_forgot/',views.send_otp_forgot,name='send_otp_forgot'),
   path('change_password/', views.change_password, name='change_password'),
   path('portalhome/',views.portalhome,name='portalhome'),
   


]

