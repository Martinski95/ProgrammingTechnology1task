import urllib.request
import os
import re

class Site:
	urls = []
	
class Page:
	content = ''
	url = ''
	links = []
	
class Link:
	url = ''
	
def getUrls(url, num):
	c = urllib.request.urlopen(url).read()
	Pages[num].content = str(c)
	
	urlPat = re.compile(r'<a [^<>]*?href=("|\')([^<>"\']*?)("|\')')
	result = re.findall(urlPat, Pages[num].content)
	
	for item in result:
		link = item[1]
		if(link.startswith("http://")):
			if(link not in Pages[num].links):
				Pages[num].links.append(link)

def selectUrl(num):
	print("Enter the number of the link you want to follow")
	
	for i in range(0, len(Pages[num].links)):
		print(str(i) + " " + Pages[num].links[i])
	print("\n--------------------------------------------------------------\n")
		
	nextLinkId = input("Enter the number here: ")
	Site.urls.append(Pages[num].links[int(nextLinkId)])
	
	return Pages[num].links[int(nextLinkId)]
	
Pages = []
tempLink = input("Enter the link you would like to start from : ")
numberOfLinks = input("Enter the depth of the search : ")
for i in range(0, int(numberOfLinks)):
	inst = Page()
	inst.links = []
	Pages.append(inst)

i = 0
nextUrl = ''

while(i < int(numberOfLinks)):
	Pages.append(Page)
	if(i == 0):
		Site.urls.append(tempLink)
		Pages[0].url = Site.urls[0]
		getUrls(Pages[0].url, i)
		nextUrl = selectUrl(i)
		i += 1
	else:
		Pages[i].url = nextUrl
		getUrls(Pages[i].url, i)
		nextUrl = selectUrl(i)
		i += 1	
		
print("End of search")
os.system("PAUSE")