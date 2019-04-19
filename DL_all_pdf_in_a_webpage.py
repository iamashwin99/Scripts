import urlparse
import urllib2
import os
import sys
 
try:
        from bs4 import BeautifulSoup
except ImportError:
        print "[*] Please download and install Beautiful Soup first!"
        sys.exit(0)
 
url = raw_input("[+] Enter the url: ")
download_path = raw_input("[+] Enter the download path in full: ")
 
try:
        #to make it look legit for the url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
 
        i = 0
 
        request = urllib2.Request(url, None, headers)
        html = urllib2.urlopen(request)
        soup = BeautifulSoup(html.read()) #to parse the website
 
        for tag in soup.findAll('a', href=True): #find <a> tags with href in it so you know it is for urls
                #so that if it doesn't contain the full url it can the url itself to it for the download
                tag['href'] = urlparse.urljoin(url, tag['href'])
 
                #this is pretty easy we are getting the extension (splitext) from the last name of the full url(basename)
                #the spiltext splits it into the filename and the extension so the [1] is for the second part(the extension)
                if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
                        current = urllib2.urlopen(tag['href'])
                        print "\n[*] Downloading: %s" %(os.path.basename(tag['href']))
 
                        f = open(download_path + "\\" +os.path.basename(tag['href'], "wb"))
                        f.write(current.read())
                        f.close()
                        i+=1
 
        print "\n[*] Downloaded %d files" %(i+1)
        raw_input("[+] Press any key to exit...")
 
except KeyboardInterrupt:
        print "[*] Exiting..."
        sys.exit(1)
 
except URLError as e:
        print "[*] Could not get information from server!!"
        sys.exit(2)
 
except:
        print "I don't know the problem but sorry!!"
        sys.exit(3)
