from flask import Flask, jsonify, render_template, redirect, url_for
import json, requests
import urllib.request
from flask import request
import random
import tracking as track

app = Flask(__name__)

host = "https://apexcapitallogistics.com"

@app.route('/')
def index():
    # url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=d943744688aa41d8aae0d7b8af1f5a14'
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0b2230af525a418496207e4f6e3a2be0'
    news_data = {}
    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        with open('news.json', 'w') as outfile:
            json.dump(data, outfile)
        with open('news.json', 'r') as outfile:
            news_data = json.load(outfile)
    except:
        with open('news.json', 'r') as outfile:
            news_data = json.load(outfile)
    articles = news_data['articles']
    random.shuffle(articles)
    return render_template('index.html', data=articles[:3], recent=news_data['articles'][:2])

@app.route('/fe7d1bfc-2751-49dd-823a-6cea6887d8fe')
def sample():
    url = f"{host}/9108443e3e2b035c0e167594a63ff2fde9c9cea9"
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'tracking':'ST948508TZ892'}

    session = requests.Session()
    page = session.post(url,headers=headers,data=payload).text
    return page

#tracking : 9611941b-5145-4161-87ef-3c7669a7704c
@app.route('/9611941b-5145-4161-87ef-3c7669a7704c')
def custom_tracking():
    url = f"{host}/9108443e3e2b035c0e167594a63ff2fde9c9cea9"
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'tracking':'TR344053A77D4'}

    session = requests.Session()
    page = session.post(url,headers=headers,data=payload).text
    return page

@app.route('/9611941b-5145-4161-87ef-167594a63ff2')
def custom_tracking_uae():
    url = f"{host}/9108443e3e2b035c0e167594a63ff2fde9c9cea9"
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'tracking':'TR8711DA61099'}

    session = requests.Session()
    page = session.post(url,headers=headers,data=payload).text
    return page

@app.route('/privacy')
def privacy():
    return render_template('privacypolicy.html')

@app.route('/9108443e3e2b035c0e167594a63ff2fde9c9cea9', methods=['GET', 'POST'])
def track_id():
    try:
        data = request.form['tracking']
        if data.lower() == "7e8443e3e2b07d".lower():
            return redirect(url_for('app.storage_220'))
        if "ST".lower() in data.lower():
            items = {
                    'ST948508TZ892':
                    {'id': data, 'co':'PALUKU NATHANAEL','name': 'COOMIBEL','ind':'Company','type': 'Precious Metal (AU)', 'storage_date': '28 Apr 2023 11:30', 'location': 'Kampala, Uganda',
                               'quantity': '500 kg [1102.31 lbs]', 'cid':'3e2b035c0e167594a63f', 'description': '500 kg Dore Bars\n 97% Purity', 'image': f'{host}/static/profile.jpg'},
                    'ST711DA610991':
                    {'id': data, 'co':'PALUKU NATHANAEL','name': 'COOMIBEL','ind':'Company','type': 'Precious Metal (AU)', 'storage_date': '12 Jun 2023 14:30', 'location': 'Kampala, Uganda',
                               'quantity': '5000 kg [11023.11 lbs]', 'cid':'3e2b035c0e167594a63f', 'description': '5000 kg Dore Bars\n 97% Purity', 'image': f'{host}/static/profile.jpg'},
                    }
            keys = list(items.keys())
            if data.lower() in [i.lower() for i in keys]:
                return render_template('storage.html', id=data, details=items[data])
        elif "TR" in data and data == 'TR344053A77D4':
            return track.uganda_new_mexico()
        elif "TR" in data and data == 'TR8711DA61099':
            return track.uganda_uae()
        else:
            return redirect(url_for('index'))
    except Exception as e:
        print(e)
        return redirect(url_for('index'))


@app.route('/tracking/7dcf5bc2d51ebc4d9a9c<id>9108443e3e2b035c0e167594a63ff2fde9a9cea98')
def tracking(id):
    if id == "f5bc2d51ebc4d":
        id = id[::-1]
        details = {'id': id,'name': '-','type': 'Export', 'shipped_date': '11 Nov 2020 03:30 AM', 'location': 'Entebbe International Airport',
                   'dest': 'Singapore', 'status': 'Delivered', 'Exp': '10 Dec 2020'}
        data = [
            {
                'date':'11 Nov 2020 ',
                'time': '15:30 PM',
                'location': 'Entebbe',
                'status': 'Delivered'
            }
        ]
        return render_template('tracking.html', id=id, details=details, data=data)
    else:
        return redirect(url_for('index'))

@app.route('/storage/9108443e3e2b035c0e167594a63ff2fde9a9cea98<id>7dcf5bc2d51ebc4d9a9c')
def storage(id):
    if id == "f5bc2d51ebc4d":
        id = id[::-1]
        details = {'id': id,'name': 'Wasim Hamed','ind':'Individual','type': 'Parcel', 'storage_date': '26 Sept 2020 15:30 PM', 'location': 'N/A',
                   'quantity': '12 (twelve)', 'cid':'3e2b035c0e167594a63f', 'description': '12 (twelve) parcel bags', 'image': 'https://finalance.com/images/401e4bff-ecbf-4a54-9b9b-ac75dd0f89a7.jpg'}


        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))

@app.route('/storage/9108443e3e2b035c0e167594a63ff2fde9a9cea9<id>7dcf5bc2d51ebc4d9a9c')
def storagecompany(id):
    if id == "f5bc2d51ebc4d":
        id = id[::-1]
        details = {'id': id,'name': 'Krystalflux','ind':'Company','type': 'Precious Metal (AU)', 'storage_date': '16 Nov 2020 07:25 AM', 'location': 'N/A',
                   'quantity': '2,575 kg', 'cid':'xxxxxxxxxxxxx4a63f', 'description': '103 AU boxes (25kg each)\n 96% Purity', 'email':'info@krystalflux.com',
                   'sign':'Rash Ceasor','image': 'https://krystalflux.com/assets/images/Directors/Rash-ceasor.jpg'}


        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))

@app.route('/storage/9108443e3e2b035c0e167594a63ff2fde9c9cea9<id>7dcf5bc2d51ebc4d9a9c')
def storage_company(id):
    uri = "/storage/9108443e3e2b035c0e167594a63ff2fde9c9cea99108443e3e2b07dcf5bc2d51ebc4d9a9c"
    if id == "9108443e3e2b0":
        id = id[::-1]
        details = {'id': id,'name': 'Krystalflux','ind':'Company','type': 'Precious Metal (AU)', 'storage_date': '11 Nov 2020 09:25 AM', 'location': 'N/A',
                   'quantity': '2,500 kg', 'cid':'xxxxxxxxxxxxx94a63', 'description': '100 AU boxes (25kg each)\n 96% Purity', 'email':'info@krystalflux.com',
                   'sign':'Li Chen-Wei','image': 'https://krystalflux.com/assets/images/Directors/Li-chen-wei.jpg', 'ceo':'WILLIAM KENWELL'}


        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))

@app.route('/storage/9108443e3e2b035c0f167594a63ff2fde9c9cea9<id>7dcf5bc2d51ebc4d9a9c')
def storage_kenwell(id):
    uri = "/storage/9108443e3e2b035c0f167594a63ff2fde9c9cea9108443e3e2b07d7dcf5bc2d51ebc4d9a9c"
    if id == "108443e3e2b07d":
        id = id[::-1]
        details = {'id': id,'name': 'KENWELL WILLIAM','ind':'Individual','type': 'Precious Metal (AU)', 'storage_date': '25 Nov 2020 08:30 AM', 'location': 'N/A',
                   'quantity': '20,000 kg', 'cid':'xxxxxxxxxxxxx7d8fd', 'description': '800 AU boxes (25kg each)\n 96% Purity', 'email':'info@krystalflux.com',
                   'sign':'Li Chen-Wei','image': 'https://finalance.com/images/401e4bff-ecbf-4a54-9b9b-ac75dd0f89a7.jpg', 'ceo':'WILLIAM KENWELL'}


        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))

@app.route('/storage/858443e3e2b035c0f167594a63ff2fde9c9cea9<id>7dcf5bc2d51ebc4d9a9c')
def storage_mark (id):
    uri = "/storage/858443e3e2b035c0f167594a63ff2fde9c9cea97e8443e3e2b07d7dcf5bc2d51ebc4d9a9c"
    if id == "7e8443e3e2b07d":
        id = id[::-1]
        details = {'id': id,'name': 'MARK SAEROYI','ind':'Individual','type': 'Precious Metal (AU)', 'storage_date': '24 Nov 2020 08:30 AM', 'location': 'DUBAI ⇒ Transit',
                   'quantity': '478 kg', 'cid':'xxxxxxxxxxxxx7d8fd', 'description': '478 kg Dore Bars\n 96% Purity', 'email':'info@krystalflux.com',
                   'sign':'Li Chen-Wei','image': 'https://i.stack.imgur.com/l60Hf.png', 'ceo':'WILLIAM KENWELL'}

        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))

@app.route('/storage/858443e3e2b035c0f167594a63fd2fde9c9cea9<id>7dcf5bc2d51ebc4d9a9c')
def storage_wasswa (id):
    uri = "/storage/858443e3e2b035c0f167594a63fd2fde9c9cea97e8443e3e2b07d7dcf5bc2d51ebc4d9a9c"
    if id == "7e8443e3e2b07d":
        id = id[::-1]
        details = {'id': id,'name': 'WASWA ROGERS','ind':'Individual','type': 'PARCELS', 'storage_date': '4 Dec 2020 08:30 AM', 'location': '⇒ Transit',
                   'quantity': '50', 'cid':'xxxxxxxxxxxxx7d8fd', 'description': 'Religious Books', 'email':'info@krystalflux.com',
                   'sign':'Li Chen-Wei','image': 'https://i.stack.imgur.com/l60Hf.png', 'ceo':'WILLIAM KENWELL'}

        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))

@app.route('/storage/858443e3e2b035c0f167594a63fd2fde9c9<id>7dcf5bc2d51ebc4d9a9c')
def storage_220 (id):
    uri = "/storage/858443e3e2b035c0f167594a63fd2fde9c97e8443e3e2b07d7dcf5bc2d51ebc4d9a9c"
    if id == "7e8443e3e2b07d":
        #id = id[::-1]
        details = {'id': id,'name': 'Kenwell William','ind':'Individual','type': 'PARCELS', 'storage_date': '26 Sep 2020 08:30 AM', 'location': '⇒ Transit',
                   'quantity': '220', 'cid':'xxxxxxxxxxxxx7d8fd', 'description': 'Boxes containing Scholastic Material (Religious Books)', 'email':'info@krystalflux.com',
                   'sign':'Li Chen-Wei','image': 'https://i.stack.imgur.com/l60Hf.png', 'ceo':'Dr WILLIAM'}

        return render_template('storage.html', id=id, details=details)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
