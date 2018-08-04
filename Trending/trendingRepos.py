import requests
from bs4 import BeautifulSoup 

def getPageContent(url):
	r = requests.get(url)
	if not r.status_code==200:
		print("Problem accessing page data.")
		return -1
	return r.text

def getRepoNames(url):
	content = getPageContent(url)
	soup = BeautifulSoup(content, 'html.parser')
	allAs = soup.find_all('a')
	names = []
	for As in allAs:
		hrefValue = str(As.attrs['href'])
		slashCount = 0
		for x in hrefValue:
			if x=='/':
				slashCount+=1
		if len(hrefValue)==0:
			continue
		if not('trending' in hrefValue) and not('github' in hrefValue) and (hrefValue[0]=='/') and (slashCount==2):
			names.append(hrefValue)
	names = names[:-6]
	return names

def main():
	URL = 'https://github.com/trending'
	names = getRepoNames(URL)
	print(names)
	return names