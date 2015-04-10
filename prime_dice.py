from splinter import Browser
import time

user = "dfklsfkjkjjk"
passw = "password"


def set_bet(browser, bet):
	browser.find_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/input").first.fill(bet)

def set_odds(browser, odds):
	#DOESNT WORK :(
	browser.find_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div/span/a").click()
	browser.find_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div/span/a").fill("10")

def roll_dice(browser):
	k = browser.find_by_id("spinner")
	browser.execute_script("window.scrollTo(0, 100);")

	browser.find_by_xpath("/html/body/div/div[4]/nav/ul/li[5]/a").click()

	client_seed = browser.find_by_xpath("/html/body/div/div[5]/div/div[3]/div/div[1]/div/div[2]/span").first.value
	server_seed = browser.find_by_xpath("/html/body/div/div[5]/div/div[3]/div/div[1]/div/div[3]/span").first.value
	k.click()

	return (client_seed, server_seed)

def login(browser):
	browser.visit("https://www.primedice.com")
	browser.find_by_xpath("/html/body/div/div/div/div/div/form/div[2]/span").click()
	browser.find_by_xpath("/html/body/div/div[1]/div/div/div/div/form/input[1]").fill(user)
	browser.find_by_xpath("/html/body/div/div[1]/div/div/div/div/form/input[2]").fill(passw)
	browser.find_by_xpath("/html/body/div/div[1]/div/div/div/div/form/button").click()



with Browser() as browser: 
	login(browser)
	set_bet(browser, "0.00000001")
	seeds = roll_dice(browser)

	time.sleep(100)
