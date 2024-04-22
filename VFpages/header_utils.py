from .models import Destination,FooterHeader,FooterTitle,Category
import requests

def header_fn(request):
    all_destinations = Destination.objects.all()
    destinations_list = []
    hidden_email = request.session.get('hidden_email','')
    hidden_phone_number = request.session.get('hidden_phone_number','')
    hidden_first_name = request.session.get('hidden_first_name','')
    hidden_last_name = request.session.get('hidden_last_name','')
    

    for destination in all_destinations:
        destination_dict = {
            'id': destination.id,
            'destination_category': destination.destination_category,
            'destination_name': destination.destination_name,
            'destination_slug': destination.destination_slug,
            'destination_image': destination.destination_image.split("/")[-1]
        }
        destinations_list.append(destination_dict)
        
   

    grouped_destinations = {}
    grouped_destinations = {
        'hidden_email': hidden_email,
        'hidden_phone_number': hidden_phone_number,
        'hidden_first_name': hidden_first_name,
        'hidden_last_name': hidden_last_name,
    }

    for destination in destinations_list:
        category = destination['destination_category']
        if category in grouped_destinations:
            grouped_destinations[category].append(destination)
        else:
            grouped_destinations[category] = [destination]
            
    all_categories = Category.objects.all()

    return grouped_destinations , all_categories

# header
def adminheader(request):
        username = request.session.get('username')
        role = request.session.get('role')

        userdetails = {"username":username,"role":role}

        # Authentication successful, redirect to dashboard
        return userdetails

def homefooter():
    footer_header = FooterHeader.objects.all()
    footer_title = FooterTitle.objects.all()

    footer = {"footer_header":footer_header,"footer_title":footer_title}

    return footer
