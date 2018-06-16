import urllib.request
from selenium import webdriver


allAnchorTexts = ["American Sparrows", "Amphibians", "Animal Faces", "Antarctic Animals", "Aquatic Mammals", "Arachnids", "Bears", "Beetles", "Big Cats", "Bird of prey", "Birds", "Butterflies", "Cats", "Chipmunks", "Corals", "Dogs", "Extinct Animals", "Farm Animals", "Fishes", "Horses", "Insects", "Jellyfishes", "Kangaroos", "Lemurs", "Lizards", "Marine Mammals", "Mollusks", "Other Animals", "Owls", "Parrots", "Primates", "Reptiles", "Rodents", "Scorpions", "Sea Water Animals", "Seabirds", "Seals", "Sharks", "Shorebirds", "Snails", "Snakes", "Squids", "Starfishes", "Turtles and Tortoises", "Wild Animals", "Woodpeckers", "Worms", "Zoo Animals"]
browser = webdriver.Firefox(executable_path="/home/techierishi/selenium_drivers/geckodriver")

# myfile = open('xyz.txt', 'w')

for textToClick in allAnchorTexts:
	browser.get('https://www.drawingtutorials101.com/Animals-drawing-tutorials')
	print(textToClick)
	anchorToClick = browser.find_element_by_xpath("//*[contains(text(), '"+textToClick+"')]")
	anchorToClick.click()

	tutorialsToClick = browser.find_elements_by_xpath("//*[contains(text(), 'View this Tutorial')]")
	tutorialLinks = []

	for tutorialToClick in tutorialsToClick:
		tutUrl = tutorialToClick.get_attribute("href")
		tutorialLinks.append(tutUrl)

	# print('tutorialLinks',tutorialLinks)

	for tutUrl in tutorialLinks:
		# print('tutUrl',tutUrl)
		browser.get(tutUrl)
		# tutorialToClick.click()
		image = browser.find_elements_by_tag_name("img")
		img_src = image[2].get_attribute("src")
		print(img_src);
		# myfile.writelines(img_src)
# download the image
# urllib.request.urlretrieve(img_src, "captcha.png")
# myfile.close()
