from django.urls import path
from .import views

urlpatterns= [
   path('login/',views.login,name="login"),
   path('dashboard/', views.dashboard, name='dashboard'), 
   path('adminlogin/',views.adminlogin,name="adminlogin"),
   # ------------------------------- about us page ---------------------------------------
   path('about_us_new/',views.about_us_new,name="about_us_new"),
   path('about_us_update/',views.about_us_update,name="about_us_update"),
   path('about_us_review/', views.about_us_review, name='about_us_review'),
   path('client_review_insert/', views.client_review_insert, name='client_review_insert'),
   path('delete_review/<int:id>/', views.delete_review, name='delete_review'),
   path('adminheader', views.adminheader, name='adminheader'),

   path('aboutUsStaff/',views.aboutUsStaff,name='aboutUsStaff'),
   path('aboutUsmemeber/',views.aboutUsmemeber,name='aboutUsmemeber'),
   path('aboutUsTeam/',views.aboutUsTeam,name='aboutUsTeam'),
   path('updateMember/<int:team_id>/',views.updateMember,name='updateMember'),
   
 
   path('Add_view/', views.add_view, name='add_view'),
   path('addTeam/', views.add_team, name='addTeam'),
   path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),
   path('delete_Member/<int:team_id>/', views.delete_Member, name='delete_Member'),
#   ==================================  destination =========================================
   path('destination/', views.destination, name='destination'),
   path('des_insertfn/',views.des_insertfn,name='des_insertfn'),
   path('destination_edit/<int:team_id>',views.destination_edit,name='destination_edit'),
   path('destination_delete/<int:team_id>',views.destination_delete,name='destination_delete'),

   path('destination_cities/', views.destination_cities, name='destination_cities'),
   path('add_destination_city/', views.add_destination_city, name='add_destination_city'),
   path('edit_destination_city/<int:team_id>/', views.edit_destination_city, name='edit_destination_city'),
   path('delete_destination_city/<int:team_id>/', views.delete_destination_city, name='delete_destination_city'),


   path('destination_attraction/', views.destination_attraction, name='destination_attraction'),
   path('destination_attraction_insert/', views.destination_attraction_insert, name='destination_attraction_insert'),
   path('desti_add_deatils/', views.desti_add_deatils, name='desti_add_deatils'),
   path('edit_attraction_page/', views.edit_attraction_page, name='edit_attraction_page'),
   path('attraction_edit/', views.attraction_edit, name='attraction_edit'),
   path('delete_attraction/<int:team_id>', views.delete_attraction, name='delete_attraction'),

   # ==========================================  destination all page meta content ===========================

#   path('Destination_meta/',views.Destination_meta,name='Destination_meta'),

   # ============================================= home page ==============================

   path('Homepage_slider/',views.Homepage_slider,name='Homepage_slider'),
   path('Homepage_slider_add/',views.Homepage_slider_add,name='Homepage_slider_add'),
   path('Homepage_slider_Edit/<int:team_id>',views.Homepage_slider_Edit,name='Homepage_slider_Edit'),
   path('Homepage_slider_delete/<int:team_id>',views.Homepage_slider_delete,name='Homepage_slider_delete'),

   # ==================================== home international top destination ================================
   path('Homepage_topdestination/',views.Homepage_topdestination,name='Homepage_topdestination'),
   path('Homepage_topdestination_Edit/',views.Homepage_topdestination_Edit,name='Homepage_topdestination_Edit'),


      # ==================================== home domestic top destination ================================
   path('Homepage_domestic_topdestination/',views.Homepage_domestic_topdestination,name='Homepage_domestic_topdestination'),
   path('Homepage_domestic_topdestination_Edit/',views.Homepage_domestic_topdestination_Edit,name='Homepage_domestic_topdestination_Edit'),

   #  =========================================== destination categories ====================================
   path('categories_view/', views.categories_view, name='categories_view'),
   path('add_categories/', views.add_categories, name='add_categories'),
   path('edit_categories/<int:team_id>/', views.edit_categories, name='edit_categories'),

   # =============================================== categories based cities select function =======================
   path('categories_cities/',views.categories_cities,name='categories_cities'),
   path('add_categories_cities/',views.add_categories_cities,name='add_categories_cities'),
   path('edit_categories_cities/<int:team_id>',views.edit_categories_cities,name='edit_categories_cities'),
   path('delete_categories_cities/<int:team_id>',views.delete_categories_cities,name='delete_categories_cities'),

  




   path('submit_form_blogus/',views.submit_form_blogus,name='submit_form_blogus'),
   path('packagesmainadmin/',views.packagesmainadmin,name="packagesmainadmin"),
   path('packagesadmin/',views.packagesadmin,name="packagesadmin"),
   path('createpackages/',views.createpackages,name="createpackages"),
   path('deletepackages/',views.deletepackages,name="deletepackages"),
   path('updatepackages/',views.updatepackages,name="updatepackages"),
   path('addpackages/',views.addpackages,name="addpackages"),
   path('update_packages_hidden_state/',views.update_packages_hidden_state,name="update_packages_hidden_state"),
   path('update_packages_home_state/',views.update_packages_home_state,name="update_packages_home_state"),
   path('update_destination_category/', views.update_destination_category, name='update_destination_category'),
   

   path('contact_us_admin/',views.contact_us_admin,name="contact_us_admin"),
   path('submit_form_contact/',views.submit_form_contact,name="submit_form_contact"),
   path('adminlogout/',views.adminlogout,name="adminlogout"),
   path('blog_us_admin/',views.blog_us_admin,name="blog_us_admin"),
   path('addblogs/',views.addblogs,name="addblogs"),
   path('createblogs/',views.createblogs,name="createblogs"),
   path('updateblogs/', views.updateblogs, name='updateblogs'),
   path('deleteblogs/', views.deleteblogs, name='deleteblogs'),
   path('blogtag/', views.blogtag, name='blogtag'),  
   path('tags_list/', views.tags_list, name='tags_list'),
   path('update_blog_popular_state/', views.update_blog_popular_state, name='update_blog_popular_state'),
   path('update_blog_hidden_state/', views.update_blog_hidden_state, name='update_blog_hidden_state'),
   path('blogtagadd/', views.blogtagadd, name='blogtagadd'),
   path('blogupdatetags/', views.blogupdatetags, name='blogupdatetags'),
   path('deleteblogtitle/', views.deleteblogtitle, name='deleteblogtitle'), 
    
   path('update_packages_category_state/', views.update_packages_category_state, name='update_packages_category_state'),

   # ========Footer=============
   path('footeradmin/', views.footer, name='footer'),
   path('addheader/', views.addheaderfooter, name='addheader'),
   path('updateheader/', views.updateheader, name='updateheader'),
   path('addtitlefooter/', views.addtitlefooter, name='addtitlefooter'),
   path('deletefooterheader/', views.deletefooterheader, name='deletefooterheader'),
   path('updatetitlefooter/', views.updatetitlefooter, name='updatetitlefooter'),
   path('deletefootertitle/', views.deletefootertitle, name='deletefootertitle'),
   
   
   path('Continent_Metas/', views.Continent_Metas, name='Continent_Metas'),
   path('Continent_Metas_edit/<int:team_id>/', views.Continent_Metas_edit, name='Continent_Metas_edit'),
   
   path('destination_Metas/', views.destination_Metas, name='destination_Metas'),
   path('destination_Metas_edit/<int:team_id>/', views.destination_Metas_edit, name='destination_Metas_edit'),
   
   # Adduser
   path('adduser/', views.adduser, name='adduser'),
   path('add_user/', views.add_user, name='add_user'),
   path('edit_user/<int:team_id>/', views.edit_user, name='edit_user'),
   path('deleteuser/',views.deleteuser,name='deleteuser'),
   
]