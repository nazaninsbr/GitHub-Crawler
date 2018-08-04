import copy
import requests
from bs4 import BeautifulSoup 


MAIN_URL = 'https://github.com'
FILENAME = "TrendingRepoInfo.txt"

class Repository:
	def __init__(self):
		self.commitCount = 0
		self.contributorCount = 0
		self.owner = ''
		self.name = ''

	def getAll(self):
		return self.name+"#"+self.owner+"#"+str(self.contributorCount)+"#"+str(self.commitCount)+'\n'

	def getCommitCount(self):
		return self.commitCount

	def getContinutorCount(self):
		return self.contributorCount

	def getOwner(self):
		return self.owner

	def getName(self):
		return self.name

	def setAll(self, commitCount, contributorCount, owner, name):
		self.commitCount = commitCount 
		self.contributorCount = contributorCount
		self.owner = owner
		self.name = name


	def setCommitCount(self, count):
		self.commitCount = count

	def setContributorCount(self, count):
		self.contributorCount = count

	def setOwner(self, owner):
		self.owner = owner

	def setName(self, name):
		self.name = name


def getPageContent(url):
	try:
		r = requests.get(url)
		if not r.status_code==200:
			print("Problem accessing page data.")
			return -1
		return r.text
	except:
		print("Unexpected error")
		return -1

def getOwnerAndRepoName(name):
	splitted = name.split('/')
	return splitted[1], splitted[2]

def findCount(liPart):
	aTag = liPart.find_all('a')
	spanTag = aTag[0].find_all('span')
	value = spanTag[0].text
	value = value.replace(" ", "")
	value = value.replace("\n", "")
	value = value.replace(",", "")
	return int(value)

def getContributorAndCommitCount(content):
	soup = BeautifulSoup(content, 'html.parser')
	allUls = soup.find_all('ul')
	summaryUl = [x for x in allUls if 'class="numbers-summary"' in str(x)]
	summaryLis = []
	for x in summaryUl:
		res = x.find_all('li')
		summaryLis.append(res)
	contributorCount = findCount(summaryLis[0][3])
	commitCount = findCount(summaryLis[0][0])
	return commitCount, contributorCount


def singleRepositoryInformation(name):
	content = getPageContent(MAIN_URL+name)
	if not content==-1:
		ownerName, repoName = getOwnerAndRepoName(name)
		commitCount, contribCount = getContributorAndCommitCount(content)
		thisRepo = Repository()
		thisRepo.setAll(commitCount, contribCount, ownerName, repoName)
		return thisRepo
	return -1

def getAllRepositoryInformation(repoNames):
	allRepositories = []
	for name in repoNames:
		thisR = singleRepositoryInformation(name)
		if not thisR==-1:
			allRepositories.append(thisR)
	return allRepositories


def writeToFile(allRepositories):
	thefile = open(FILENAME, 'a')
	thefile.write('name#owner#contributorCount#commitCount\n')
	for repo in allRepositories:
		thefile.write(repo.getAll())
	thefile.close()

def main(repoNames):
	allRepositories = getAllRepositoryInformation(repoNames)
	writeToFile(allRepositories)



