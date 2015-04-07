import urllib,urllib2
from bs4 import BeautifulSoup
import time
from pymongo import Connection
from pymongo import GEO2D

db=Connection().albuquerque
#db.drop_collection("bus") 
db.bus.create_index([("loc",GEO2D)])

def logBus():
    url = 'http://data.cabq.gov/transit/realtime/route/route766.kml'
    rawreply = urllib2.urlopen(url).read()
    soup=BeautifulSoup(rawreply)

    s1=soup.placemark
    p=soup.find_all('point')

    with open('766.txt.','a') as output:
        y=1
        i=2
        for x in p:
            exec("d=s"+str(y)+".find_all('td')")
            exec("xy=s"+str(y)+".coordinates.text")
            output.write(str(xy)+"\n")
            exec("s"+str(i)+"=s"+str(y)+".find_next_sibling('placemark')")
	    p=xy.split(",")
	    db.bus.insert({"loc":[float(p[1]),float(p[0])],"number":str(d[1].text),"speed":str(d[3].text),"time":str(d[5].text),"nextstop":str(d[7].text)})
            y+=1
            i+=1
        output.close()
    time.sleep(80)

while True:
    logBus()

