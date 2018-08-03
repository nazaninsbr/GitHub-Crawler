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
	allDivs = soup.find_all('div')
	allDivsWithClass = [x for x in allDivs if 'class="d-inline-block col-9 mb-1"' in str(x)]
	allAs = []
	print(allDivsWithClass)
	for item in allDivsWithClass:
		children = item.findChildren("a" , recursive=True)
		allAs.append(children)
	names = []
	for As in allAs:
		print(As[0])
		names.append(As.attrs['href'])
	return names

def main():
	URL = 'https://github.com/trending'
	names = getRepoNames(URL)