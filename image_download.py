import urllib.request
from selenium import webdriver

def getAllImgLinks():
	mainURL = 'https://www.drawingtutorials101.com/Anime-and-Manga-drawing-tutorials'
	browser = webdriver.Firefox(executable_path="/home/techierishi/selenium_drivers/geckodriver")
	browser.get(mainURL)

	allAnchorTexts = browser.find_elements_by_class_name("block_category")
	allAnchorTextsLinks = []

	for linkToKeep in allAnchorTexts:
		linkTextPair = {}
		tutUrl = linkToKeep.get_attribute("href")
		tutText = linkToKeep.text
		linkTextPair["link"] = tutUrl
		linkTextPair["text"] = tutText
		allAnchorTextsLinks.append(linkTextPair)
	
	# print('allAnchorTextsLinks',allAnchorTextsLinks)
	myfile = open('Animes.html', 'w')

	for linkToGo in allAnchorTextsLinks:
		browser.get(linkToGo["link"])
		print(linkToGo["text"])
		tutorialsToClick = browser.find_elements_by_xpath("//*[contains(text(), 'View this Tutorial')]")
		tutorialLinks = []

		for tutorialToClick in tutorialsToClick:
			tutUrl = tutorialToClick.get_attribute("href")
			tutorialLinks.append(tutUrl)

		# print('tutorialLinks',tutorialLinks)
		count = 1
		for tutUrl in tutorialLinks:
			# print('tutUrl',tutUrl)
			browser.get(tutUrl)
			image = browser.find_elements_by_tag_name("img")
			img_src = image[2].get_attribute("src")
			print(img_src)
			myfile.writelines('<a href="'+img_src+'"> '+linkToGo["text"]+' '+str(count)+' </a></br>')
			count +=1
	myfile.close()

getAllImgLinks()