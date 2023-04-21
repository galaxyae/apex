from flask import Flask, jsonify, render_template, redirect, url_for
import json, requests
import urllib.request
from flask import request
import random
import icons

class Tracking():
    def __init__(self):
        pass

def uganda_new_mexico():
    locations = [{
            'country': 'Entebbe',
            'code': 'UG',
            'airport': 'EBB'
        },{
            'country': 'Dubai',
            'code': 'AE',
            'airport': 'DXB'
        },{
            'country': 'San Francisco',
            'code': 'US',
            'airport': 'SFO'
        },{
            'country': 'Arizona City',
            'code': 'US',
            'airport': 'PHX'
        }]

    map = []
    checkpoints = [i['airport'].upper() for i in locations]

    f = open('cities.json',)
    cities = json.load(f)

    origins = []

    for i in locations:
        for j in cities:
            if j['name'].lower() == i['country'].lower() and j['country'].lower() == i['code'].lower():
                map.append(
                    {
                        "svgPath": "targetSVG",
                        "title": j['name'].title(),
                        "name":j['name'].lower(),
                        "latitude": float(j['lat']),
                        "longitude": float(j['lng'])
                    }
                )

    unique = list({ each['name'] : each for each in map }.values())

    lines = []
    for i in range(len(unique)):
        if i+1 <= len(unique) -1:
            lines.append(
                {
                    "latitudes": [unique[i]['latitude'], unique[i+1]['latitude']],
                    "longitudes": [unique[i]['longitude'], unique[i+1]['longitude']]
                  }
            )
    print(lines)
    sender = {
        'name':'ELIJAH',
        'address':"""
                    PLOT 1, KATALINA CRESCENT LOWER \n
                    NAGURU - UGANDA
                """,
        'contact':'info@newcrest.com'
    }


    product = {
        'name':'Precious Minerals',
        'content':[
            {'item': '2 Boxe(s) of GOLD AU BARS [100 KGs]'},
        ]
    }

    transit = [
        {
            'current':'Entebbe, Entebbe International Airport [EBB] - Dubai, Dubai International Airport [DXB]'.upper(),#' - Dubai International Airport [DXB]',
            'departure':'Emirates, EK 0730 → Entebbe, Entebbe International Airport [EBB] - Dubai, Dubai International Airport [DXB] 30-12-2021 22:40 [ Duration 5h15m ]',
            'arrival':'Emirates, EK 0730 → ETA Dubai, Dubai International Airport [DXB] 30-12-2021 22:40',
            'comment': 'The shipment queried and discharged, shipper notification forwarded for follow up'
        },
        # {
        #     'current':'Dubai, Dubai International Airport [DXB] - San Francisco International Airport [SFO]'.upper(),#' - Dubai International Airport [DXB]',
        #     'departure':'Emirates, EK 0225 → Dubai, Dubai International Airport [DXB] - San Francisco International Airport [SFO] 02-01-2022 08:45 [ Duration 14h15m ]',
        #     'arrival':'Emirates, EK 0225 → ETA San Francisco International Airport [SFO] 02-01-2022 23:00',
        #     'comment': 'The shipment queried and discharged, shipper notification forwarded for follow up'
        # },
        # {
        #     'current':'San Francisco International Airport [SFO] - Phoenix Sky Harbor International Airport [PHX]'.upper(),#' - Dubai International Airport [DXB]',
        #     'departure':'Emirates, QJ 1728 → San Francisco International Airport [SFO] - Phoenix Sky Harbor International Airport [PHX] 03-01-2022 12:45 [ Duration 45h15m ]',
        #     'arrival':'Emirates, QJ 1728 → ETA Phoenix Sky Harbor International Airport [PHX] 05-01-2022 10:00',
        #     'comment': 'The shipment queried and discharged, shipper notification forwarded for follow up'
        # },
    ]

    reciever = {
        'name':'Client Name',
        'address':"""Client Address""".upper(),
        'contact':'Client Contact'
    }
    # Harry Reid International Airport (LAS)
    flight_progress = [
        {
            'time':'16:25',
            'date':'30-12-2021 16:25',
            'airport':'Entebbe, Entebbe International Airport [EBB]'.upper(),
            'is_error': False,
            'status':'🛫 EK 0730 - Departure',
            'color':'green'
        },
        #5h 10m
        {
            'time':'22:40',
            'date':'30-12-2021 22:40',
            'airport':'Dubai, Dubai International Airport [DXB]'.upper(),
            'is_error': False,
            'status':'🛬 EK 0730 - Arrival',
            'color':'green'
        },
        {
            'time':'10:00',
            'date':'31-12-2021 10:00',
            'airport':'Error occurred processing shipment',
            'is_error': True,
            'status':'Action Required',
            'color':'orange'
        },
        {
            'time':'08:45',
            'date':'02-01-2022 08:45',
            'airport':'Dubai, Dubai International Airport [DXB]'.upper(),
            'is_error': False,
            'status':'🛫 EK 0225 - Departure',
            'color':'default'
        },
        #1h 10m
        {
            'time':'12:45',
            'date':'02-01-2022 12:45',
            'airport':'San Francisco International Airport [SFO]'.upper(),
            'is_error': False,
            'status':'🛬 EK 0225 - Arrival',
            'color':'default'
        },
        {
            'time':'23:00',
            'date':'03-01-2022 23:00',
            'airport':'San Francisco International Airport [SFO]'.upper(),
            'is_error': False,
            'status':'🚚 Departure → [Ground Shipping]',
            'color':'default'
        },
        {
            'time':'10:00',
            'date':'05-01-2022 10:00',
            'airport':'Phoenix Sky Harbor International Airport [PHX]'.upper(),
            'is_error': False,
            'status':'🚚 Arrival → [Ground Shipping]',
            'color':'default'
        },
    ]

    has_shipped = True
    has_arrived = True


    has_arrived_message = [
        {
            'title':"Dubai International Airport [DXB]".upper(),
            'message': 'We are pleased to inform you that the items arrived successfully. Items awaiting review to be discharged to next destination.',
            'color':'#32CD32',
            'icon':'false',
            'class':'',
        },
        {
            'title':icons.warning,
            'message': """Caution: As per the description of the goods being shipped, you are informed to contact the consignee
                        or consignee representative to sign the documents provided by the Dubai Customs to ensure further shipment of the goods.
            """,
            'color':'orange',
            'icon':'true',
            'class':'warning',
        },
    ]


    shipping_message = {}
    if not has_shipped:
        shipping_message['message'] = "Item under review for discharge"

    error = {
    'error_message':'Please review your consignment within 24hrs before 02-DEC-2022 08:00 to enure proper shipping.'
    }

    shipment_error = True

    arrival_time = "Estimated time of arrival → 05 DEC 2022 [Emirates]"

    # check
    increment = 100 / len(checkpoints)
    progress = .85
    return render_template('track.html', item="", ui="", shipment=product, has_arrived=has_arrived, has_arrived_message=has_arrived_message, sender=sender, has_shipped=has_shipped, shipping_message=shipping_message, product=transit, receiver=reciever, amount=len(transit), map = unique, lines = lines, source = locations[0]['country'].title(), checkpoints=checkpoints, checkpoints_length=len(checkpoints), increment=increment, progress=progress, error=error, flight_progress=flight_progress, arrival_time=arrival_time, shipment_error=shipment_error)
