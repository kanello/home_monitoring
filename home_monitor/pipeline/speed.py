import speedtest
from datetime import datetime

def get_speeds():
    tester=speedtest.Speedtest(secure=True) # If you don't have secure=True enabled, you'll get a 403 error
    tester.get_best_server()
    now = datetime.now()
    results = {
        "time":now.strftime("%d/%m/%Y %H:%M:%S"),
        "ping": tester.results.ping,
        "upload": round(tester.upload() / 1000 / 1000, 1),
        "download": round(tester.download() / 1000 / 1000, 1)
        }


    return results

if __name__ == "__main__":
    a = get_speeds()
    print(a)


