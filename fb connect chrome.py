from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from chatterbotapi import ChatterBotFactory, ChatterBotType
import requests, bs4

#Options for the Google Chrome Browser 
chrome_options = Options()
#Path to Chrome's User Data Directory. Among Other things, User Data Directory contains Profile data.
chrome_options.add_argument("--user-data-dir=C:\\Users\\I16881\\AppData\\Local\\Google\\Chrome\\User Data")

#When you have multiple Profiles, Specify the User Profile with which Chrome has to be opened.
#Default Profile is selected when nothing is specified
chrome_options.add_argument("--profile-directory=Profile 2")


try:
    driver = webdriver.Chrome(chrome_options=chrome_options)
except:
    print 'driver error!'

#Use the driver to open this URL.
#Inorder to directly go to the following URL without being directed to the login page, your FB credentials have to be saved in your Profile
#ashwinachar - This is my friend's name on FB. Replace it with your friend's name
driver.get('https://www.facebook.com/messages/ashwinachar')
htmlElem = driver.find_element_by_name('message_body')

#Use ChatterBot API to get responses for messages
#Here CLEVERBOT is used as the Chatbot. You can also use JABBERWACKY or PANDORABOTS
factory = ChatterBotFactory()
bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()


#This whole block of code waits for a text message from your friend. As soon as a text arrives, it replies to that message using cleverbot's response.
# Don't forget to tick the "Press Enter to send" option
var = 1
while var==1 :
    prevmsg = driver.find_element_by_xpath("(//strong[@class='_36']/a[text()='Ashwn Achar'])[last()]/following::div[@class='_37'][1]//p")
    curmsg = prevmsg
	#As long as a new message doesn't arrive 
    while prevmsg.text == curmsg.text :
        try:
            prevmsg = curmsg
            curmsg = driver.find_element_by_xpath("(//strong[@class='_36']/a[text()='Ashwn Achar'])[last()]/following::div[@class='_37'][1]//p")
        except:
            print 'error!'
    #Send the bot's response to the friend's message
	htmlElem.send_keys(bot1session.think(curmsg.text))
    htmlElem.send_keys(Keys.ENTER)
    

driver.close()    

