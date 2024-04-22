from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
from .models import CcustomerDetails,BlogUs,Tags,Destination,InternationalCity,InternationalAttraction,HomepageSlider,CategoriesDestination,Category,Lead,LeadDayInfo,Hotel,LeadDaySightSee,Place,HotelsDetails,DestinationMeta,ContinentMetas
from .models import CcustomerDetails,BlogUs,Tags,Packages,Userdetails
from .models import CcustomerDetails,BlogUs,Tags,Destination,InternationalCity,InternationalAttraction,HomepageSlider
from .models import CcustomerDetails,BlogUs,Tags,Packages,FooterHeader,FooterTitle
from datetime import datetime
from .models import PagesTable,UserReviews,Member
from .models import PagesTable,UserReviews
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import hashlib
from django.db.models import F, ExpressionWrapper, fields
from django.utils import timezone
import re
from .header_utils import header_fn,homefooter
from django.db.models import Q
from django.conf import settings
from email.mime.text import MIMEText
from django.core.exceptions import ObjectDoesNotExist
import smtplib
import random
from django.contrib.auth import logout
from django.urls import reverse
from django.core.mail import EmailMessage



def home_page(request):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
    destinationSlider = HomepageSlider.objects.all()
    packages_top = Packages.objects.filter(homepage=False)
    print("top")
    print(packages_top)
    # destination_id = destinationSlider
    user_reviews_list = UserReviews.objects.all()
    all_content = []
    for user_review in user_reviews_list:
        all_content.append(user_review.content)

    
    Packages_details = Packages.objects.all()
    about_page = PagesTable.objects.filter(pagesname='about_us').first()
    if about_page:
        description = about_page.description.get('aboutus_details')
    else:
        description = None

   

    categories =  Category.objects.all()
    last_seven_entries = BlogUs.objects.order_by('-id')[:7]
    
    homepage_meta = DestinationMeta.objects.filter(pagename='Home_page').first()

    if homepage_meta:
        mew_details =homepage_meta.meta_details
    else:
        print("No meta details found for the Home page.")
    

    domestict_page_top = PagesTable.objects.filter(pagesname='domestic_top_destination').first()
    international_page_top = PagesTable.objects.filter(pagesname='international_top_destination').first()
    
    C_package = []
    for categoriespackage in Packages_details:
        package={
            "id":categoriespackage.id,
            "description":categoriespackage.description,
            "destination_category":categoriespackage.destination_category,
            "itinaries_id":categoriespackage.itinaries_id,
            "category_boolen":categoriespackage.category_button

        }
        C_package.append(package)
    print(C_package)
    
    news = []
    for i in categories:
        news.append(i.categeory_slug)

    days_activities = {category: [] for category in news}

    # List to hold activities that meet both conditions
    filtered_activities = []
    
    for activity in C_package:
        category = activity['destination_category']
        
        # If category not in days_activities, add it
        if category not in days_activities:
            days_activities[category] = []
    
        # Check if both conditions are met
        if activity['category_boolen'] == 0:
            days_activities[category].append(activity)
            filtered_activities.append(activity)



    # return render(request, "home/Home_page.html",{"destinations": destinations_data,"destinationSlider":destinationSlider,"Packages_details":Packages_details,"footer_header":footer_header,"footer_title":footer_title,"packages_top":packages_top,"domestict_page_top":domestict_page_top,"international_page_top":international_page_top})

    return render(request, "home/Home_page.html",{"destinations": destinations_data,'description': description,"user_reviews":all_content,"destinationSlider":destinationSlider,"Packages_details":Packages_details,"categories":days_activities,"footer_header":footer_header,"footer_title":footer_title,"packages_top":packages_top,"domestict_page_top":domestict_page_top,"international_page_top":international_page_top,"last_seven_entries":last_seven_entries,"homepage_meta":mew_details,"all_categories":all_categories})
    # return render(request, "home/Home_page.html",{"destinations": destinations_data,"destinationSlider":destinationSlider,"Packages_details":Packages_details,"footer_header":footer_header,"footer_title":footer_title,"packages_top":packages_top})


def contact_us(request):
        destinations_data,all_categories = header_fn(request)
        footers = homefooter()
        footer_header = footers["footer_header"]
        footer_title = footers["footer_title"]
        meta = PagesTable.objects.filter(pagesname='contact us').first()
        data = meta.description
        print(data)
        return render(request, "home/contact_us.html",{'meta':data,"destinations": destinations_data,"footer_header":footer_header,"footer_title":footer_title,"all_categories":all_categories})

def footer(request):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]

    

    return render(request, "home/footer.html",{"destinations": destinations_data,"footer_header":footer_header,"footer_title":footer_title,"all_categories":all_categories})

def insert_customer_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        destination = request.POST.get('destination')

        footers = homefooter()
        footer_header = footers.footer_header
        footer_title = footers.footer_title
        
        # Create an instance of CcustomerDetails
        customer = CcustomerDetails(
            name=name,
            email=email,
            phone=phone,
            destination=destination,
            created_at=datetime.now()  # Assuming you want to set the current datetime
        )
        
        # Save the instance to the database
        customer.save()
        
        # Return a success response
        return JsonResponse({'success': True})
    
    # Return an error response if the request method is not POST
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def about_us(request):
    # user review details
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
    user_reviews_list = UserReviews.objects.all()
    all_content = []
    for user_review in user_reviews_list:
        all_content.append(user_review.content)

    # about us comman details
    about_page = PagesTable.objects.filter(pagesname='about_us').first()
    if about_page:
        description = about_page.description.get('aboutus_details')
    else:
        description = None
    print(all_content)

    # team memebers details
    Member_list = Member.objects.all()
    all_description = []
    for member in Member_list:
       all_description.append(member.description)
    
    team_details = {}

    # Iterate over all_description
    for entry in all_description:
        team_id = entry['team_id']
        ordernumber = entry['Ordernumber']
        
        # If team_id is not in team_details, add it with an empty list
        if team_id not in team_details:
            team_details[team_id] = []
        
        # Append the entry to the team_details list for the corresponding team_id
        team_details[team_id].append(entry)

    # Sort entries within each team based on Ordernumber
    for team_id, entries in team_details.items():
        sorted_entries = sorted(entries, key=lambda x: int(x['Ordernumber']))
        team_details[team_id] = sorted_entries

    # print(team_details)
    allteam = {"salse_team":team_details.get('Sales Team', []),
               "digital_development_team":team_details.get('Digital & development Team', []),
               "HR_Accounts_team":team_details.get('HR & Accounts', []),
               "Operation":team_details.get('Operation', []),}
    print(allteam)
    print(all_description)
     
    return render(request, "home/about.html",{'description': description,'user_reviews': all_content,'teams':allteam,"destinations": destinations_data,"footer_header":footer_header,"footer_title":footer_title,"all_categories":all_categories})


def main_Destination(request):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
    
    international_meta = DestinationMeta.objects.filter(pagename='international_page').first()

    if international_meta:
        new_details =international_meta.meta_details
        print(new_details)
    else:
        print("No meta details found for the Home page.")
    return render(request, "home/destinationshome.html",{"destinations": destinations_data,"footer_header":footer_header,"footer_title":footer_title,"new_details":new_details,"all_categories":all_categories})


def domestic_city(request):
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
    destinations_data,all_categories = header_fn(request)
    
    domestic__meta = DestinationMeta.objects.filter(pagename='domestic_page').first()

    if domestic__meta:
        new_details =domestic__meta.meta_details
        print(new_details)
    else:
        print("No meta details found for the Home page.")
    return render(request, "home/domestic_city.html",{"destinations": destinations_data,"footer_header":footer_header,"footer_title":footer_title,"new_details":new_details,"all_categories":all_categories})

def main_DestinationCity(request,continent_name):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
  
    
    all_destinations = Destination.objects.filter(destination_category=continent_name)
    destinations_list = []

    for destination in all_destinations:
        destination_dict = {
            'id': destination.id,
            'category': destination.category,
            'destination_category': destination.destination_category,
            'destination_name': destination.destination_name,
            'destination_slug': destination.destination_slug,
            'destination_image': destination.destination_image.split("/")[-1],
            'destination_title': destination.destination_title,
            'destination_title_slug': destination.destination_title_slug,
            # 'destination_cost': destination.destination_cost,
            # 'destination_duration': destination.destination_duration,
            # 'destination_season': destination.destination_season,
            # 'destination_live_guide': destination.destination_live_guide,
            # 'destination_max_group': destination.destination_max_group,
            'created_at': destination.created_at,
            'updated_at': destination.updated_at,
            # 'show_text': destination.show_text,
        }
        destinations_list.append(destination_dict)
        
    domestic__meta = ContinentMetas.objects.filter(continent_name=continent_name).first()

    if domestic__meta:
        new_details =domestic__meta.description_son
        print(new_details)
    else:
        print("No meta details found for the Home page.")

    # print(destinations_list)
    return render(request, "home/destinationCities.html",{'Cities_list':destinations_list,"destinations": destinations_data,"footer_header":footer_header,"footer_title":footer_title,"new_details":new_details,"all_categories":all_categories})

def main_DestinationAttraction(request,city_name):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
    # continent = request.GET.get('continent')
 
    # img = request.GET.get('img')
    # city = request.GET.get('city')
    # name = request.GET.get('name')
    # continent_new = request.session.get('continent')
    # request.session['img'] = img
    
    print(city_name)
    # print("what is this new",continent)
    all_destinations = Destination.objects.filter(destination_slug=city_name)

    # Iterate over each destination and print its ID
    for destination in all_destinations:
        new =destination.id
        image =destination.destination_image.split("/")[-1]
        destination_category = destination.destination_category
        destination_name = destination.destination_name
        destination_metakeyword = destination.metakeyword
        destination_metadestination = destination.metadestination
        destination_metatitle = destination.metatitle
    
    all_city = InternationalCity.objects.filter(destination_id=new)
    city_list = []

    for destination in all_city:
        destination_dict = {
            'id': destination.id,
            'international_city_name': destination.international_city_name,
            'international_city_slug': destination.international_city_slug,
            'international_city_name':destination.international_city_name
        }
        city_list.append(destination_dict)
    # print(city_list)

    ids = [city['id'] for city in city_list]

    # print(ids)
    attraction_dict = {}

    # Loop through each city_id
    for city_id in ids:
        # Query InternationalAttraction objects with the current city_id
        attractions_for_city = InternationalAttraction.objects.filter(international_city_id=city_id)
        
        # Store the attractions for the current city_id in a list
        attractions_list = []
        for attraction in attractions_for_city:
            attractions_list.append(
                {"id":attraction.id,
                 "tour_spot_name":attraction.tour_spot_name,
                 "tour_spot_slug":attraction.tour_spot_slug,
                 "highlights_content":attraction.highlights_content,
                 "highlights_image":attraction.highlights_image.split("/")[-1],
                 "includes_content":attraction.includes_content,
                 "includes_image":attraction.includes_image.split("/")[-1],
                 "tour_spot_slug":attraction.tour_spot_slug,
                })  
        
        # Store the list of attractions in the dictionary with the city_id as the key
        attraction_dict[str(city_id)] = attractions_list
    print(attraction_dict)

    packages_entry = Packages.objects.filter(packages_id=new)
    other_city = Destination.objects.filter(destination_slug=city_name)
    
    if other_city.exists():
        destination_category = other_city.first().destination_category
        all_other = Destination.objects.filter(destination_category=destination_category)
        all_other_city = []
        for all in all_other:
            all_other_city.append({"destination_image":all.destination_image.split("/")[-1],
                                   "destination_category" :all.destination_category,
                                   "destination_name" : all.destination_name,
                                    "destination_slug" : all.destination_slug,
                                    "category" : all.category,
                                   })

    else:
        all_other_city = None
    
    return render(request, "home/destinations.html",{'city_list':city_list,'attraction_place':attraction_dict,"destinations": destinations_data,"image":image,"destination_category":destination_category,"all_categories":all_categories,"all_other_city":all_other_city,"city_name":city_name,
    "packages_entry":packages_entry,"destination_name":destination_name,"footer_header":footer_header,"footer_title":footer_title,"destination_metakeyword":destination_metakeyword,"destination_metadestination":destination_metadestination,"destination_metatitle":destination_metatitle})

def destination_menu(request):
    footers = homefooter()
    footer_header = footers["footer_header"]
    print(footer_header)
    footer_title = footers["footer_title"]
    print(footer_title)
    

    return render(request, "home/destinations.html",{"footer_header":footer_header,"footer_title":footer_title})
     
    
def gridblogus(request):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    print(footer_header)
    footer_title = footers["footer_title"]
    print(footer_title)
    search_query = request.GET.get('search_query','')
    tag_id = request.POST.get('tag_id')
    tag_name = request.POST.get('tag_name')

    # Split the tagIds string into a list of integers
    blog_entries = BlogUs.objects.filter(hidden=0).order_by('-id')
    print(tag_id)
    if tag_id:
         blog_entries = BlogUs.objects.filter(tags__contains=tag_id)
    # split_values = tagIds[0].split(',')

    # blog_entries = BlogUs.objects.filter(hidden=0)



    # Iterate through tag IDs and add Q objects for each
    # for tag_id in tagIds:
    #     # print(tag_id)
    #     # ttr = blog_entries.tags
    #     # print(ttr)

    #     blog_entries = blog_entries.filter(tags__contains=str(tag_id))
    
    count_of_entries = blog_entries.count()
    # selected_tags_str = request.GET.get('tags','')  # Retrieve selected tag IDs as a list
    # selected_tags = selected_tags_str.split(',') if selected_tags_str else []  # Convert string to list
    
    print(blog_entries)

    # Retrieve the description JSON data
    # description_data = blog_entries.description
        
        
    print("Start")
    # print(filtered_blogs)
    # selected_tags = []
    # Assign values from tagIds to selected_tags if tagIds has any value
    # if tagIds:
    #     selected_tags = tagIds
    
    meta = PagesTable.objects.filter(pagesname='blog_us').first()
    data = meta.description

    # if selected_tags:
    #     # Filter blog entries based on selected tags
    #     blog_entries = blog_entries.filter(description__tags__tag_name__in=selected_tags)

    if search_query:
        blog_entries = blog_entries.filter(description__title__icontains=search_query)

    paginator = Paginator(blog_entries, 5)  # Show 5 blog entries per page

    page = request.GET.get('page')
    try:
        blog_entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_entries = paginator.page(paginator.num_pages)

    
    # Filter popular blog entries
    popular_entries = BlogUs.objects.filter(popular=False)[:5]

    
     # Get the last 7 entries
    last_seven_entries = BlogUs.objects.order_by('-id')[:5]

    tags = Tags.objects.all()


     
    return render(request, "home/gridblog.html" , {'blog_entries': blog_entries,'popular_entries':popular_entries,'last_seven_entries':last_seven_entries,'tags':tags,'search_query': search_query,'meta':data,"destinations": destinations_data,"blog_entries_count": count_of_entries,"footer_header":footer_header,"footer_title":footer_title,"tag_name":tag_name,"tag_id":tag_id,"all_categories":all_categories})

def blogsdetails(request, blog_url):
     if request.method == 'GET':
        destinations_data,all_categories = header_fn(request)
        footers = homefooter()
        footer_header = footers["footer_header"]
        footer_title = footers["footer_title"]
        # blog_id = request.POST.get('id','')
        print(blog_url)
        # Get the BlogUs instance with the provided ID
        blog_entry = BlogUs.objects.get(url=blog_url)
        # Filter popular blog entries
        popular_entries = BlogUs.objects.filter(popular=False)[:5]
        # print(popular_entries)
        
        # Get the last 7 entries
        last_seven_entries = BlogUs.objects.order_by('-id')[:5]
        html_string = blog_entry.description['jump_link_titles']
        print(html_string)
        print(type(html_string))
        # Remove the string containing "data-doc-id" attribute
        jump_link_titles = re.sub(r'<p[^>]*?data-doc-id="[^"]*"[^>]*>.*?</p>', '', html_string)

        html_string_1 = blog_entry.description['richtextarea']

        richtextarea = re.sub(r'<p[^>]*?data-doc-id="[^"]*"[^>]*>.*?</p>', '', html_string_1)

        # Process the data as needed

        return render(request, "home/blogsview.html" , {'blog_entry':blog_entry,'jump_link_titles':jump_link_titles,'richtextarea':richtextarea,"destinations": destinations_data,'popular_entries':popular_entries,'last_seven_entries':last_seven_entries,"footer_header":footer_header,"footer_title":footer_title,"all_categories":all_categories})  # Return a JSON response indicating success

     return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
     





# import os
# import urllib.request
# import string
# import random
# from django.conf import settings
# from .models import InternationalAttraction  # Import your model

# def generate_random_filename(image_url):
#     """Generate a random filename."""
#     image = image_url.split("/")
  

#     return( image[len(image) - 1])



#     # letters = string.ascii_lowercase
#     # return ''.join(random.choice(letters) for _ in range(length))

# def download_image(image_url):
#     folder_path = os.path.join(settings.BASE_DIR, 'VFpages', 'static', 'destination', 'Attraction_image')

#     # Check if the folder exists, if not, create it
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     if image_url:
#         # Generate a random filename for each image
#         random_filename = generate_random_filename(image_url)
#         file_path = os.path.join(folder_path, random_filename)

#         # Download the image and save it with the generated filename
#         urllib.request.urlretrieve(image_url, file_path)

#         return file_path

#     return None

# def download_images(request):
#     attractions_for_city = InternationalAttraction.objects.all()

#     image_urls = [attraction.includes_image for attraction in attractions_for_city if attraction.includes_image]

#     downloaded_images = []

#     for image_url in image_urls:
#         file_path = download_image(image_url)
#         if file_path:
#             downloaded_images.append(file_path)

#     return HttpResponse("Images downloaded successfully.")


def lead_itinerary(request,lead):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]

    packages_t0_lead = Packages.objects.filter(description__Url_in_lead=lead).first()
  


    new = packages_t0_lead.itinaries_id
    all_package = packages_t0_lead.packages_id 
    package_city = packages_t0_lead.description
    Lead_details = Lead.objects.using('second_database').filter(id=new)
    
    in_ex = []
    for lead in Lead_details:
        city_ids = lead.cities_ids
       
        lead_val ={
            "include": json.loads(lead.pack_includs),
            "exclude": json.loads(lead.pack_excluds),
            "payment_police" :json.loads(lead.payment_poly),
            "refound_police" : json.loads(lead.refound_poly),
            "cancle_police" :  json.loads(lead.cancle_poly),
        }
        in_ex.append(lead_val)

    # for package in in_ex:
    #     package['include'] = json.loads(package['include'])
    #     package['exclude'] = json.loads(package['exclude'])
    #     package['payment_police'] = json.loads(package['payment_police'])
    #     package['refound_police'] = json.loads(package['refound_police'])
    #     package['cancle_police'] = json.loads(package['cancle_police'])
        

    days = LeadDayInfo.objects.using('second_database').filter(lead_id=new)
    day_activity = []

    for activity in days:
        place = Place.objects.using('second_database').get(id=activity.place_id)
        activity_data = LeadDaySightSee.objects.using('second_database').filter(lead_day_id=activity.id)
        
        activities = []
        for act in activity_data:
            activities.append({
                "id": act.id,
                "data": json.loads(act.data)
            })

        activity_info = {
            "id": activity.id,
            "lead_id": activity.lead_id,
            "days": activity.day,
            "Transfers": activity.transfers,
            "break": activity.breakfast,
            "lunch": activity.lunch,
            "dinner": activity.dinner,
            "Tickets": activity.tickets,
            "notes": activity.notes,
            "placeName": place.place_name,
            "Activity": activities,
        }
        day_activity.append(activity_info)

    # print(day_activity)

    days_activities = {}

    for activity in day_activity:
        day = activity['days']
        if day not in days_activities:
            days_activities[day] = []
        days_activities[day].append(activity)

    # print(days_activities)
        
    hotel_all = []

    hotel_list = HotelsDetails.objects.using('second_database').filter(lead_id=new)

    for hotel in hotel_list:
        # Fetching hotel data based on hotel ID
        hoteldata = Hotel.objects.using('second_database').get(id=hotel.hotel_id)
        
        # Creating a dictionary with correct key-value pairs
        hotel_details = {
            "hotel_id": hotel.hotel_id,
            "hotel_room_type": hotel.hotal_room_type,  # Corrected typo in key name
            "star_ratings": hotel.star_ratings,
            "hotel_night": hotel.hotal_night,  # Corrected typo in key name
            "lead_id": hotel.lead_id,
            "hotel_image": hoteldata.image,  # Corrected key name and accessing hoteldata.image
            "hotel_name": hoteldata.name,  # Corrected accessing hoteldata.name
            "location": hoteldata.location,
        }
        
        hotel_all.append(hotel_details)

    # print(hotel_all)
    packages_view = Packages.objects.filter(packages_id=all_package)
    
    return render(request, "home/lead_itinerary.html",{"footer_header":footer_header,"footer_title":footer_title,"destinations": destinations_data,"Lead_details":Lead_details,"packages":in_ex,"packages_lead":packages_t0_lead,"data":days_activities,"hotel_all":hotel_all,"all_categories":all_categories,"package_city":package_city,"packages_view":packages_view})

def catagories_city(request,city_name):
    destinations_data,all_categories = header_fn(request)
    footers = homefooter()
    footer_header = footers["footer_header"]
    footer_title = footers["footer_title"]
    # categories=city_name
    categories_destination = CategoriesDestination.objects.filter(categeory_slug = city_name)
    # categories_destination = CategoriesDestination.objects.filter(categeory_slug = city_name)
    if categories_destination:


        for destination in categories_destination:
            description = destination.city_id  # Retrieve the description dictionary
            categories= destination.category
            meata_image=destination.all_description
    

        
        all_destinations = Destination.objects.filter(id__in=description)  # Filter based on IDs in the 'new' list

        # List to store details of each destination
        destination_list = []

        # Iterate over each destination and store its details in a dictionary
        for destination in all_destinations:
            id = destination.id
            image = destination.destination_image.split("/")[-1]
            destination_category = destination.destination_category
            destination_name = destination.destination_name
            destination_slug = destination.destination_slug
            
            # Create a dictionary for each destination
            destination_dict = {
                "id": id,
                "image": image,
                "destination_category": destination_category,
                "destination_name": destination_name,
                "destination_slug":destination_slug
            }
            
            # Append the dictionary to the destination_list
            destination_list.append(destination_dict)

        print(destination_list)


                    


        return render(request, "home/catagories_cities.html",{"categories_City":destination_list,"city_name":categories,"footer_header":footer_header,"footer_title":footer_title,"destinations": destinations_data,"all_categories":all_categories,"meata_image":meata_image})
    
    return JsonResponse({'status': 'error', 'message': 'values not insert'}, status=405)
    
    
    # Signup
def signups(request):
    error_message = None
      # Initialize error message variable
    if request.method == 'POST':
        # Get form data
        user_name = request.POST.get('user_name')
        lastuserName = request.POST.get('lastuserName')
        date = request.POST.get('date')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        second_phone_number = request.POST.get('second_phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(user_name)

        if not user_name or not lastuserName or not email or not date or not second_phone_number or not phone_number or not password or not confirm_password:
            error_number = 1
            error_message = 'All fields are required.'

        # Generate and send OTP to the user's phone number
        # Check if user with provided email or phone number already exists
        elif Userdetails.objects.filter(email=email).exists() or Userdetails.objects.filter(whatsapp_number=phone_number).exists() or Userdetails.objects.filter(phone_number=second_phone_number).exists():
            error_number = 2
            error_message = 'User with this email or phone number already exists.'
        
        elif password != confirm_password:
            error_number = 3
            error_message = 'Passwords do not match'

        else:
            # Encrypt the password using MD5 hashing
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            print(hashed_password)

            # Create and save the user with encrypted password
            user = Userdetails(
                first_name=user_name,
                last_name=lastuserName,
                dateofbirth=date,
                email=email,
                whatsapp_number=phone_number,
                phone_number=second_phone_number,
                password=hashed_password,
                wallet_balance=0
            )
            print(user)
            user.save()

            # Redirect to a success page or login page
            return JsonResponse({'success': True, 'success_message': 'Signup successful'})

    return JsonResponse({'success': False,'error_number':error_number ,'error_message': error_message})


def send_email(otp,recipient_email):
    try:
        email_subject = "Vacation Feast OTP"
        email_message = f"Your OTP: {otp}"
        # Create an SMTP session
        # s = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        # s.starttls()  # Start TLS for security
        # s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)  # Authentication

        # # Construct the email message
        # msg = MIMEText(email_message)
        # msg['Subject'] = email_subject
        # msg['From'] = "bookings@vacationfeast.com"
        # msg['To'] = recipient_email

        # # Send the email
        # s.sendmail("bookings@vacationfeast.com", recipient_email, msg.as_string())
        
        # # Close the SMTP session
        # s.quit()
        
        email_from = "bookings@vacationfeast.com"
        recipient_list = recipient_email
        email = EmailMessage(
        subject=email_subject,
        body=email_message,
        from_email=settings.EMAIL_HOST,
        to=recipient_list,
        )
        email.send()
        # send_mail( email_subject, email_message, email_from, recipient_list )

        return True
    except Exception as e:
        print("Error:", e)
        return False
    
def send_otp_forgot(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        
        if not phone_number:
            return JsonResponse({'success': False, 'message': 'Phone number is required'})

        otp = str(random.randint(1000, 9999))
        expiration_time = timezone.now() + timezone.timedelta(seconds=180)  # Set expiration time (180 seconds)
        request.session['otp'] = {
            'value': otp,
            'created_at': str(datetime.now())
        }

        email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        phone_pattern = r'^\d{10}$'
        
        if re.match(email_pattern, phone_number):
            try:
                user = Userdetails.objects.get(email=phone_number)
                recipient_email = phone_number
                email_sent = send_email(otp, recipient_email)
                print("Valid email address")
            except ObjectDoesNotExist:
                return JsonResponse({'success': False, 'message': 'User not found'})
            
        elif re.match(phone_pattern, phone_number):
            try:
                user = Userdetails.objects.get(whatsapp_number=phone_number)
                Users = 'Customer'
                whatsapp_response = send_whatsapp_message(Users, phone_number, otp)
                print("Valid phone number")
            except ObjectDoesNotExist:
                return JsonResponse({'success': False, 'message': 'User not found'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid phone number or email address'})

        if otp:
            return JsonResponse({'success': True, 'message': 'OTP sent successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to send OTP'})
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'})
    
def send_otp(request):
    # phone_number = request.POST.get('phone_number')
    # print(phone_number)
    """
    Function to send OTP to the provided phone number
    (You may need to use a third-party service for sending OTP via SMS)
    """
    # Generate a 4-digit OTP
   
    # Code to send OTP to the user's phone number (e.g., via SMS)
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        
        # Generate OTP and send it to the provided phone number (implement this logic)
        otp = str(random.randint(1000, 9999)) 
        request.session['otp'] = {
            'value': otp,
            'created_at': str(datetime.now())  # Convert datetime object to string
        }
        print(otp)

        recipient_email = email
        
        # Sending OTP via email
        # email_sent = send_email(otp,recipient_email)
        
        whatsapp_response = send_whatsapp_message(user_name,phone_number,otp)

        # Assuming OTP sending is successful, return a JSON response
        if otp:
            return JsonResponse({'success': True, 'message': 'OTP sent successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to send OTP'})
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'})
def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        saved_otp = request.session.get('otp')
        print(otp_entered)
        print(saved_otp)
        if saved_otp and 'value' in saved_otp:
            otp_value = saved_otp['value']
            otp_created_at = datetime.strptime(saved_otp['created_at'], '%Y-%m-%d %H:%M:%S.%f')  # Convert string to datetime object
            current_time = datetime.now()
            time_difference = current_time - otp_created_at
            
            if otp_entered == otp_value and time_difference.total_seconds() <= 180:  # 180 seconds = 3 minutes
                # OTP is valid
                return JsonResponse({'success': True, 'message': 'OTP verified successfully'})
        
        # OTP is either invalid or expired
        return JsonResponse({'success': False, 'message': 'Invalid or expired OTP'})
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'})
    
def send_whatsapp_message(user_name,phone_number,otp):
    gallabox_api_key = settings.GALLABOX_API_KEY
    gallabox_api_secret = settings.GALLABOX_API_SECRET
    gallabox_Channelid = settings.GALLABOX_CHANNELID
    url = "https://server.gallabox.com/devapi/messages/whatsapp"

    payload = json.dumps({
      "channelId": gallabox_Channelid,  # Replace with your channelId
      "channelType": "whatsapp",
      "recipient": {
        "name": user_name,
        "phone": f"91{phone_number}"  # Recipient's phone number
      },
      "whatsapp": {
        "type": "template",
        "template": {
          "templateName": "registration_website",
          "bodyValues": {
            "Name": user_name,
            "variable_2": otp
          }
        }
      }
    })
    headers = {
      'apiSecret': gallabox_api_secret,  # Replace with your apiSecret
      'apiKey': gallabox_api_key,        # Replace with your apiKey
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

# def send_email(otp,recipient_email):
#     try:
#         email_subject = "Vacation Feast OTP"
#         email_message = f"Your OTP: {otp}"
#         # Create an SMTP session
#         s = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
#         s.starttls()  # Start TLS for security
#         s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)  # Authentication

#         # Construct the email message
#         msg = MIMEText(email_message)
#         msg['Subject'] = email_subject
#         msg['From'] = "bookings@vacationfeast.com"
#         msg['To'] = recipient_email

#         # Send the email
#         s.sendmail("bookings@vacationfeast.com", recipient_email, msg.as_string())
        
#         # Close the SMTP session
#         s.quit()

#         return True
#     except Exception as e:
#         print("Error:", e)
#         return False

def login_views(request):
    error = None
    if request.method == 'POST':
        email_or_phone = request.POST.get('email_or_phone')
        password = request.POST.get('password')
        print(email_or_phone)
        # Check if email_or_phone or password is empty
        if not email_or_phone or not password:
           error_message = 'Email/Phone and Password fields cannot be empty.'

        # Check if the user exists with the given email or phone number
        user = Userdetails.objects.filter(Q(email=email_or_phone) | Q(whatsapp_number=email_or_phone)).first()

        if user:
            # Hash the provided password using MD5 hashing for comparison
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            # Check if the hashed password matches the one stored in the database
            if user.password == hashed_password:
                print(user.email)
                print(user.password)
                print(request.session)
                request.session['hidden_email'] = user.email
                request.session['hidden_phone_number'] = user.whatsapp_number
                request.session['hidden_first_name'] = user.first_name
                request.session['hidden_last_name'] = user.last_name
                email = user.email
                phone_number = user.phone_number
                username = user.first_name
               
                return JsonResponse({'success': True, 'email': email,'phone_number':phone_number,'username':username})
            else:
                # Password doesn't match, render login page with error message
                 error_message = 'Invalid email/phone number or password.'

        else:
            # User not found, render login page with error message
           error_message = 'User not found.'

    # If the request method is not POST, render the login page
    return JsonResponse({'success': False, 'error_message': error_message})
# Function to get or refresh token

def logout_view(request):
    try:
        del request.session['hidden_email']
        del request.session['hidden_phone_number']
        del request.session['hidden_first_name']
        del request.session['hidden_last_name']
    except KeyError:
        pass  

    logout(request)

    return redirect(reverse('home_page'))

def change_password(request):
    error_message = None

    if request.method == 'POST':
        # Get form data
        email_or_phone = request.POST.get('user_name')
        new_password = request.POST.get('password')
        confirm_new_password = request.POST.get('confirm_password')

        # Retrieve user based on email or phone number
        user = Userdetails.objects.filter(email=email_or_phone).first() or \
               Userdetails.objects.filter(phone_number=email_or_phone).first()

        if not user:
            error_message = 'User not found.'
        else:
            # Retrieve user's current password from the database
            current_password = user.password

            # Check if new password is the same as the old password
            if hashlib.md5(new_password.encode()).hexdigest() == current_password:
                error_message = 'New password cannot be the same as the old password.'
            elif new_password != confirm_new_password:
                error_message = 'New passwords do not match.'
            else:
                # Encrypt the new password using MD5 hashing
                hashed_new_password = hashlib.md5(new_password.encode()).hexdigest()

                # Update the user's password
                user.password = hashed_new_password
                user.save()

                return JsonResponse({'success': True, 'success_message': 'Password changed successfully.'})

    return JsonResponse({'success': False, 'error_message': error_message})

def portalhome(request):
    hidden_email = request.session.get('hidden_email', '')
    hidden_phone_number = request.session.get('hidden_phone_number', '')
    hidden_username = request.session.get('hidden_username', '')

    user = Userdetails.objects.filter(Q(email=hidden_email) | Q(whatsapp_number=hidden_phone_number)).first()
    
    return render(request, 'home/portalhome.html',{'hidden_username': hidden_username,'user':user})
    




