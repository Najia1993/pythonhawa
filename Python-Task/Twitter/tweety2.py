import twitter, datetime, time
import urllib2
import BeautifulSoup
from BeautifulSoup import BeautifulSoup

while True:
    file = open("C:\Users\user\AppData\Local\Google\Chrome\User Data\Default\Current Session",'r')
    data = file.read()
    
    #Hawa Najihah Twitter
    user = 3096383277
    file = open("tweet.txt")
    cred = file.readline().strip().split(',')
    
    api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
                  access_token_key=cred[2],access_token_secret=cred[3]) 

    #Find URL
    startUrl = data.rfind("http")
    endUrl = data.find(chr(0), startUrl)
    url = data[startUrl:endUrl]
    print(url)

    #Get Title
    response = urllib2.urlopen(url)
    html = response.read()
    
    soup = BeautifulSoup(html)
    titleofurl = soup.html.head.title
    titlePage = soup.title
    titlePage = str(titlePage)
    titlePage = titlePage.replace("<title>","")
    titlePage = titlePage.replace("</title>","")
    titlePage = titlePage.strip()
    print("I love " + titlePage + " on " + url)

    #print titleofurl.contents
    #print soup.title


#-------------------------------------
    #titleofurl2 = titleofurl.contents
    #titleofurl2 = str(titleofurl2)
    #titleofurl2 = str(titleofurl2.strip())
    #print (titleofurl2)
#-------------------------------------

    #Post on Hawa Najihah's Twitter
    timestamp = datetime.datetime.utcnow()
    response = api.PostUpdate("I love " + titlePage + " on " + url)
    print("Status updated!")


    time.sleep(3600)
    



