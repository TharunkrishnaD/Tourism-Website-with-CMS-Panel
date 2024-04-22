from django.db import models

# Create your models here.
class PagesTable(models.Model):
    pagesname = models.CharField(max_length=255)
    description = models.JSONField()
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages_table'


class UserReviews(models.Model):
    content = models.JSONField()

    class Meta:
        managed = False
        db_table = 'user_reviews'

class TeamName(models.Model):
    Teamname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'team_name'
        
class Member(models.Model):
    role = models.CharField(max_length=255)
    Team_Name = models.CharField(max_length=255)
    description = models.JSONField()

    class Meta:
        managed = False
        db_table = 'members'


class UserTable(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_table'
        
class Userdetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    wallet_balance = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_details'

class CcustomerDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    destination = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ccustomer_details'

class BlogUs(models.Model):
    hidden = models.BooleanField(default=False)
    popular = models.BooleanField(default=True)
    description = models.JSONField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_us'

class FooterHeader(models.Model):
    header = models.JSONField(db_column='Header', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'footer_header'

class FooterTitle(models.Model):
    header_id = models.IntegerField(db_column='Header_id', blank=True, null=True)  # Field name made lowercase.
    description = models.JSONField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'footer_title'

class Packages(models.Model):
    hidden = models.BooleanField(default=False) 
    packages_id = models.CharField(db_column='Packages_id', max_length=255)  # Field name made lowercase.
    description = models.JSONField(blank=True, null=True)
    homepage = models.BooleanField(default=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)
    destination_category = models.CharField(max_length=200, blank=True, null=True)
    itinaries_id = models.IntegerField()
    category_button = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'packages'



class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tags'

class Destination(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True)
    destination_category = models.CharField(max_length=255)
    destination_name = models.CharField(max_length=255)
    destination_slug = models.CharField(max_length=255) 
    # destination_slug = models.CharField(max_length=255)
    destination_title = models.CharField(max_length=255)
    destination_title_slug = models.CharField(max_length=255)
    # destination_cost = models.CharField(max_length=255)
    # destination_duration = models.CharField(max_length=255)
    # destination_season = models.CharField(max_length=255)
    # destination_live_guide = models.CharField(max_length=255)
    # destination_max_group = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # show_text = models.IntegerField(default=0)
    destination_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    # show_text = models.IntegerField(blank=True, null=True)
    # destination_image = models.JSONField(blank=True, null=True)
    metakeyword = models.CharField(max_length=500)
    metatitle = models.CharField(max_length=500)
    metadestination = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'destinations'

class InternationalCity(models.Model):
    destination_id = models.IntegerField()
    international_city_name = models.CharField(max_length=255)
    international_city_slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'international_cities'

class InternationalAttraction(models.Model):
    international_city_id = models.IntegerField()
    tour_spot_name = models.CharField(max_length=255)
    tour_spot_slug = models.CharField(max_length=255)
    highlights_content = models.TextField()
    highlights_image = models.TextField()
    includes_content = models.TextField()
    includes_image = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    # metakeyword = models.CharField(max_length=500)
    # metatitle = models.CharField(max_length=500)
    # metadestination = models.CharField(max_length=500)


    class Meta:
        managed = False
        db_table = 'international_attractions'

class InternationalCities(models.Model):
    
    destination_id = models.IntegerField(blank=True, null=True)
    international_city_name = models.TextField(blank=True, null=True)
    international_city_slug = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'international_cities'

class HomepageSlider(models.Model):
    description = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homepage_slider'


class Category(models.Model):
    categoriesname = models.CharField(max_length=255)
    categeory_slug = models.CharField(max_length=255)
    updatedate = models.DateTimeField(null=True, blank=True)
    createdate = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'destination_categories'

class CategoriesDestination(models.Model):
   
    category = models.CharField(max_length=50)
    categeory_slug = models.CharField(max_length=50)
    city_id = models.JSONField()
    update_date = models.DateField()
    create_date = models.DateField()
    all_description = models.JSONField()


    class Meta:
        managed = False
        db_table = 'categoriesbasedcities'
        
class DestinationMeta(models.Model):
    pagename = models.CharField(max_length=255)
    meta_details = models.JSONField()
    update_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        managed = False
        db_table = 'destination_meta'
        
class ContinentMetas(models.Model):
    continent_name = models.CharField(max_length=255)
    description_son = models.JSONField()
    Update_at = models.DateTimeField(null=True, blank=True)
   

    class Meta:
        managed = False
        db_table = 'continent_metas'
        
class Lead(models.Model):

    leadNumber = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255)
    packageName = models.CharField(max_length=255)
    placeToVisit = models.CharField(max_length=255)
    itDate = models.DateField()
    itValidDate = models.DateField()
    departureDate = models.DateField()
    numOfNights = models.CharField(max_length=255)
    roomType = models.CharField(max_length=255)
    flight_id = models.CharField(max_length=255)
    costingNotes = models.CharField(max_length=255, null=True, blank=True)
    routeMap = models.CharField(max_length=255, null=True, blank=True)
    termsType = models.CharField(max_length=255, null=True, blank=True)
    vehicleType = models.CharField(max_length=255, null=True, blank=True)
    pack_includs = models.TextField()
    pack_excluds = models.TextField()
    payment_poly = models.TextField()
    refound_poly = models.TextField()
    cancle_poly = models.TextField()
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   
    pdf_name = models.CharField(max_length=255, null=True, blank=True)
    lead_json = models.TextField()
    no_need_flight = models.BooleanField(default=False)
    state_id = models.IntegerField(null=True, blank=True)
    cities_ids = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'leads'
        
        
class LeadDaySightSee(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_day_id = models.IntegerField()
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lead_day_sight_sees'


class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    place_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'places'
        
class LeadDayInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_id = models.IntegerField()
    day = models.TextField()
    country_state_id = models.TextField()
    city_id = models.TextField()
    place_id = models.TextField()
    activities = models.TextField()
    transfers = models.TextField()
    tickets = models.TextField()
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()
    notes = models.TextField(blank=True, null=True)
    sorting_order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lead_day_infos'




class Hotel(models.Model):
    id = models.BigAutoField(primary_key=True)
    state_id = models.IntegerField()
    city_id = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    

    class Meta:
        managed = False
        db_table = 'hotel_data'

class HotelsDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_id = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    hotel_id = models.CharField(max_length=255)
    HotelOptionNumber = models.CharField(max_length=255)
    hotal_room_type = models.CharField(max_length=255, null=True, blank=True)
    star_ratings = models.CharField(max_length=255, null=True, blank=True)
    hotal_night = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hotals_deatils'
