import sys

def organizationCrawlerMain():
	sys.path.append('./organizationCrawler')
	import orgCrawlerMain

	orgCrawlerMain.main()


def main():
	orgChoice = input("Run the organization crawler code? (y/n) ")
	if orgChoice=='y':
		organizationCrawlerMain()

if __name__ == '__main__':
	main()