from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
import json, time

#Import the Python-Instagram API
from zFeed.utilities.instagram import *

instagramAccessToken = '1644590945.1677ed0.a0c774fb4d5849fbae27dcc3dcb19388'


def home(request):

	return render_to_response('index.html')

def getHomePosts(request):

	api = InstagramAPI(access_token=instagramAccessToken)

	venues = [ 
				{'name':"Egg Slut", 'locationID': 558818418, 'xCoord': 34.070232, 'yCoord': -118.250272},
				{'name':"Wurstkuche", 'locationID': 15668, 'xCoord': 34.070232, 'yCoord': -118.250272},
				{'name':"Guisados", 'locationID': 590880110, 'xCoord': 34.070232, 'yCoord': -118.250272},
				{'name':"Salt & Straw", 'locationID': 508201822, 'xCoord': 34.050655, 'yCoord': -118.248795},
				{'name':"Sqirl", 'locationID': 7904974, 'xCoord': 34.084277, 'yCoord': -118.286640},
				{'name':"Daily Dose", 'locationID': 656219, 'xCoord': 34.035567, 'yCoord': -118.233778},
				{'name':"Yardhouse", 'locationID': 26752584, 'xCoord': 34.044938, 'yCoord': -118.265498},
				{'name':"Pizzanista", 'locationID': 3693307, 'xCoord': 34.034833, 'yCoord': -118.231605},
				{'name':"Urth Cafe", 'locationID': 523792, 'xCoord': 34.041974, 'yCoord': -118.235426},
				{'name':"Donut Friend", 'locationID': 141569971, 'xCoord': 34.121238, 'yCoord': -118.204405},
				{'name':"Stumptown Coffee", 'locationID': 139524136, 'xCoord': 34.033257, 'yCoord': -118.229876},
				{'name':"Frying Fish Restaruant", 'locationID': 1912238, 'xCoord': 34.033257, 'yCoord': -118.229876},
				{'name':"Caffe Primo", 'locationID': 4400068, 'xCoord': 34.033257, 'yCoord': -118.229876},
				{'name':"Sprinkles Cafe", 'locationID': 72627321, 'xCoord': 34.033257, 'yCoord': -118.229876},
				{'name':"Food Haus", 'locationID': 220251370, 'xCoord': 34.033257, 'yCoord': -118.229876}

			]

	homeStream = []

	for venue in venues:

		locationID = venue['locationID']
		venueName = venue['name']
		xCoord = venue['xCoord']
		yCoord = venue['yCoord']

		recent_media, next = api.location_recent_media(location_id=locationID)
		
		venueData = {'venueName': venueName, 'locationID': locationID, 'xCoord': xCoord, 'yCoord': yCoord, 'latestUrl': ''}
		latestUrl = recent_media[0].images['standard_resolution'].url

		venueData['latestUrl'] = latestUrl
		homeStream.append(venueData)	

	return HttpResponse(json.dumps(homeStream), content_type="application/json")

def getVenuePosts(request):

	venueName = request.GET.get('venueName')
	locationID = request.GET.get('locationID')

	api = InstagramAPI(access_token=instagramAccessToken)

	venues = [ 
				{'name':"Egg Slut", 'locationID': 558818418, 'xCoord': 34.070232, 'yCoord': -118.250272},
				{'name':"Wurstkuche", 'locationID': 15668, 'xCoord': 34.070232, 'yCoord': -118.250272},
				{'name':"Guisados", 'locationID': 590880110, 'xCoord': 34.070232, 'yCoord': -118.250272},
				{'name':"Salt & Straw", 'locationID': 508201822, 'xCoord': 34.050655, 'yCoord': -118.248795},
				{'name':"Sqirl", 'locationID': 7904974, 'xCoord': 34.084277, 'yCoord': -118.286640},
				{'name':"Daily Dose", 'locationID': 656219, 'xCoord': 34.035567, 'yCoord': -118.233778},
				{'name':"Yardhouse", 'locationID': 26752584, 'xCoord': 34.044938, 'yCoord': -118.265498},
				{'name':"Pizzanista", 'locationID': 3693307, 'xCoord': 34.034833, 'yCoord': -118.231605},
				{'name':"Urth Cafe", 'locationID': 523792, 'xCoord': 34.041974, 'yCoord': -118.235426},
				{'name':"Donut Friend", 'locationID': 141569971, 'xCoord': 34.121238, 'yCoord': -118.204405},
				{'name':"Stumptown Coffee", 'locationID': 139524136, 'xCoord': 34.033257, 'yCoord': -118.229876}
			]

	venueStream = {'venueName': venueName, 'locationID' : locationID, 'posts': []}

	recent_media, next = api.location_recent_media(location_id=locationID)

	for media in recent_media:
	    mediaUrl = media.images['standard_resolution'].url
	    captionText = media.caption.text if media.caption is not None else ''
	    numLikes = media.like_count
	    numComments = media.comment_count
	    timestamp = time.mktime(media.created_time.timetuple())	#Convert to unix timestamp
	    venueStream['posts'].append({'mediaUrl' : mediaUrl, 'captionText': captionText , 'numLikes': numLikes, 'numComments': numComments, 'timestamp' : timestamp})

		#print ("Url %s caption %s Likes %s numComments %s created at %s") % (mediaUrl, captionText, numLikes, numComments, timestamp)
		

	return HttpResponse(json.dumps(venueStream), content_type="application/json")



