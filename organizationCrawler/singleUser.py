import requests
from bs4 import BeautifulSoup 

def getPageContent(url):
	r = requests.get(url)
	if not r.status_code==200:
		print("Problem accessing page data.")
		return -1
	return r.text

def getRepositoryCount(content):
    soup = BeautifulSoup(content, 'html.parser')
    allLinks = soup.find_all('span')
    repoCount = [x for x in allLinks if "Counter" in str(x)]
    return repoCount[0].text.strip()


def mainFunc(username):
	url = 'https://github.com'+ username
	content = getPageContent(url)
	return getRepositoryCount(content)
