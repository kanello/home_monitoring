#!/Users/anthony/opt/anaconda3/bin/python

from hashlib import new
from time import sleep
import speedtest
import csv
from datetime import date, datetime
import psycopg2
from geopy import geocoders
import geocoder



def run():


    test = speedtest.Speedtest()

    #the original download and upload outputs are in bits
    download = round(test.download()/1000000, 2)
    upload = round(test.upload()/1000000, 2)
    
    #couldn't find where else to get ping speed from, except for this dictionary
    ping = round(test.get_best_server()['latency'], 2)

    #parse the time format here rather than leave it up to whatever program we use later
    timestamp = datetime.now()

    #this format helps postgresql
    timestamp = timestamp.strftime("%d-%m-%Y %H:%M:%S")

    #so I can tell if this was captured at home
    
    # calling the nominatim tool
    geoLoc = geocoders.Nominatim(user_agent="GetLoc")
    geo = geocoder.ip('me')
    locname = geoLoc.reverse(geo.latlng)


    to_csv = (timestamp, download, upload, ping, geo.ip, geo.latlng[0],geo.latlng[1] , locname.address)

    #we can probably kill this part for the mac monitoring. Will need it for the rasbpi probably though
    with open('speedtest.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(to_csv)

    return to_csv

def to_postgres():
    """Sends data from this file into postgres
    """

    conn = psycopg2.connect("host=localhost dbname=anthony user=postgres")
    cur = conn.cursor()
    insert_query = ("""INSERT INTO internet_speed VALUES {};""").format(run())
    cur.execute(insert_query)
    conn.commit()


if __name__ == '__main__':

    
    run()
    

   

    

        
