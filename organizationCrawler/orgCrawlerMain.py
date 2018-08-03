import requests
from bs4 import BeautifulSoup 
import singleUser

NEX_PAGES_URL = 'https://github.com/orgs/google/people?page='

def getPageContent(url):
	r = requests.get(url)
	if not r.status_code==200:
		print("Problem accessing page data.")
		return -1
	return r.text

def getNames(content):
	result = {}
	soup = BeautifulSoup(content, 'html.parser')
	allLinks = soup.find_all('a')
	nameLinks = [x for x in allLinks if "css-truncate-target f4" in str(x)]
	for val in nameLinks:
		result[val.contents[0].strip()] = val['href']
	# print(result)
	return result

def getAllPages():
	pageIndex = 2
	content = 0
	result = {}
	while True:
		url = NEX_PAGES_URL + str(pageIndex)
		content = getPageContent(url)
		if content==-1:
			break
		names = getNames(content)
		result.update(names)
		pageIndex +=1
	return result


def averageRepoCount():
	names = {}
	content = getPageContent('https://github.com/orgs/google/people')
	if not content==-1:
		result = getNames(content)
		names.update(result)

	result = getAllPages()
	names.update(result)
	count = 0
	repoCount = 0
	for name in names.keys():
		if count >20:
			break
		count +=1
		thisCount = singleUser.mainFunc(names[name])
		if 'k' in thisCount:
			thisCount = thisCount[:-1]
			thisCount.replace('.','')
			thisCount = thisCount + '000'
		repoCount += int(thisCount)
		
	print("The average is "+str(repoCount/count))
	return names 

def main():
	names = averageRepoCount()


