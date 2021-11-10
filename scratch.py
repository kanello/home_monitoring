from hashlib import new
from time import sleep
import speedtest
import csv
from datetime import date, datetime
import psycopg2



def run():
    test = speedtest.Speedtest()

    #outputing the test results like this first, then will add to a csv
    # command_line_output = ("D:", test.download(), "\nU:", test.upload(), "\nP:", test.get_best_server()['latency'])

    #the original download and upload outputs are in bits
    download = round(test.download()/1000000, 2)
    upload = round(test.upload()/1000000, 2)
    ping = round(test.get_best_server()['latency'], 2)

    #parse the time format here rather than leave it up to whatever program we use later
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%d-%m-%Y %H:%M:%S")

    to_csv = (timestamp, download, upload, ping)

    with open('speedtest.csv', 'a', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(to_csv)

    return to_csv

def to_postgres():

    conn = psycopg2.connect("host=localhost dbname=anthony user=postgres")
    cur = conn.cursor()
    insert_query = ("""INSERT INTO internet_speed VALUES {};""").format(run())
    cur.execute(insert_query)
    conn.commit()


if __name__ == '__main__':
   to_postgres()

    

        
