import sys

def organizationCrawlerMain():
	sys.path.append('./organizationCrawler')
	import orgCrawlerMain

	orgCrawlerMain.main()

def trendingMain():
	sys.path.append('./Trending')
	import trendingRepos

	trendingRepos.main()

def main():
	orgChoice = input("Run the organization crawler code? (y/n) ")
	if orgChoice=='y':
		organizationCrawlerMain()

	trendingChoice = input("Run the trending projects crawler code? (y/n) ")
	if trendingChoice=='y':
		trendingMain()

if __name__ == '__main__':
	main()