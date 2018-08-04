import requests
from bs4 import BeautifulSoup 

MAIN_URL = 'https://github.com/search?'
RESULT_TYPE = '&type=Repositories'
PAGE = 'p='
SEARCH = 'q='

def getPageContent(url):
	r = requests.get(url)
	if not r.status_code==200:
		print("Problem accessing page data.")
		return -1
	return r.text

def getNames(content):
	soup = BeautifulSoup(content, 'html.parser')
	allAs = soup.find_all('a')
	nameAs = [x for x in allAs if 'class="v-align-middle"' in str(x)]
	allHrefs = [x['href'] for x in nameAs]
	print(allHrefs)
	return allHrefs


def writeToFile(fileName, result):
	thefile = open(fileName, 'a')
	for item in result:
		thefile.write(item+'\n')
	thefile.close()

def getSearchResult(searchWord):
	url = ''
	pageNumber = 1
	while True:
		if pageNumber==1:
			url = MAIN_URL+SEARCH+searchWord+RESULT_TYPE
		else:
			url = MAIN_URL+PAGE+'&'+str(pageNumber)+'&'+SEARCH+searchWord+RESULT_TYPE
		content = getPageContent(url)
		if content==-1:
			break
		print("Crawling result page "+str(pageNumber))
		result = getNames(content)
		writeToFile(searchWord+'_search_result.txt', result)
		pageNumber +=1

def main():
	searchWord = input('Search Keyword: ')
	searchWord = searchWord.strip()
	result = getSearchResult(searchWord)