# ----------------------------------------------------
##   Project: Python Price
##   Author: Vedang Vivek Dicholkar
##   Email: Vedangdicholkar@proton.me
##   Created: Sunday, September 11th, 2022
##   Last Commit: Monday, September 12th, 2022
# ----------------------------------------------------

# Importing Webdriver from Selenium, It manages the backend for use browsers. <pip install selenium>
from selenium import webdriver as wd

# Asking the User if they want to shop
buyerOpt = input("========================================================================\nDo you want to shop for something today? [Y]es or [N]o\n>> ")
# If user responeded with a Yes or Y, it'll continue, if not they'll exit the code.
buyerOptAns = buyerOpt.find("Y")
if buyerOptAns == 0:
    # Asks user what they want to buy 
    searchResult = input("===================================\nWhat do you want to shop for today? [Ex: Eggs]\n>> ")
    # Asks user the max amout they want to spent, press <ENTER> to skip.
    budgetPrice = input("===================================\nWhats the amount that you're looking to spend? (Optional)\n>> $")
    # Ask if they want to go on Amazon or Google Shopping. (Nested Selection)
    retailerOptions = input("===================================\nChoose from the 2 Retailers:\n1. Amazon\n2. Google Shopping\n========================================================================\n>> ")
    # If user responds with Answer Choice Number 2 it'll open google shopping and there query.
    retailerOptionsAnswer = retailerOptions.find("2")
    # Provides the drivers to start Chrome
    driver = wd.chrome.webdriver.WebDriver(executable_path='C:/Users/2000152748/videoProject/chromedriver.exe')
    # If user responded with Google Shopping it'll open chrome and paste query.
    if retailerOptionsAnswer == 0:
        driver.get("https://shopping.google.com/search?hl=en-US&tbm=shop&psb=1&q=" + searchResult + "&tbs=mr%3A1%2Cprice%3A1%2Cppr_max%3A" + budgetPrice)
    # Open Amazon and paste query
    else:
        # Side Note: amazon has a rather strange system dealling with max price meaning you'll need another 00 to the link.
        budgetPriceCorrect = str(budgetPrice) + str("00")
        driver.get("https://www.amazon.com/s?k=" + searchResult + "&rh=p_36%3A-" + budgetPriceCorrect)        
else:
    print("Ok, Goodbye.")
# The code it self is only 18 Lines of Code!