import cherrypy
import urllib,urllib2
from bs4 import BeautifulSoup

	  
class route766(object):
    def index(self):
        url = 'http://data.cabq.gov/transit/realtime/route/route766.kml'
        rawreply = urllib2.urlopen(url).read()
        soup=BeautifulSoup(rawreply)

        s1=soup.placemark
        p=soup.find_all('point')
        y=1
        i=2
        rest=[]
        for x in p:
            exec("d=s"+str(y)+".find_all('td')")
            exec("xy=s"+str(y)+".coordinates.text")
            exec("s"+str(i)+"=s"+str(y)+".find_next_sibling('placemark')")
	    p=xy.split(",")
	    y+=1
            i+=1
            rest.append('{"loc":['+p[1]+','+p[0]+'],"number":'+str(d[1].text)+',"speed":'+str(d[3].text)+',"time":'+str(d[5].text)+',"nextstop":'+str(d[7].text)+'},') 
        return rest
    index.exposed = True



cherrypy.config.update(
    {'server.socket_host': '0.0.0.0'} )
cherrypy.quickstart(route766())