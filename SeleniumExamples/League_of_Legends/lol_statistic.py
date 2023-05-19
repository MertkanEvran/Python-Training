from selenium import webdriver
from selenium.webdriver.common import by
import time


# Create summoner class
class Summoner:

    def __init__(self,username, region):
        self.username = username
        self.region = region
        self.url = f"https://www.leagueofgraphs.com/{self.region}/summoner/{self.region}/{self.username}"
        self.browser = webdriver.Chrome("chrome.exe")

    def summoner_dict(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        time.sleep(2)

        # Fill the dict
        match_table = self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[5]/table").find_element(by.By.TAG_NAME, "tbody")
        summoner = {}
        summoner["nick"] = self.browser.find_element(by.By.XPATH,"//*[@id='pageContent']/div[1]/div/div[2]/h2").text
        summoner["level"] = self.browser.find_element(by.By.XPATH,"//*[@id='pageContent']/div[1]/div/div[2]/div").text
        summoner["played_game"] = self.browser.find_element(by.By.XPATH,"//*[@id='graphDD5']").text
        summoner["win_rate"] = self.browser.find_element(by.By.XPATH,"//*[@id='graphDD6']").text
        summoner["soloq"] = {"wins":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[5]/span[1]/span").text,
                             "loses":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[5]/span[3]/span").text,
                             "rank":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[1]").text,
                             "lp":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[4]/span").text}
        summoner["flex"] = {"wins":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/span[1]/span").text,
                             "loses":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/span[3]/span").text,
                             "rank":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]").text,
                             "lp":self.browser.find_element(by.By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/span").text}
        return summoner



summoner = Summoner("Senkami","tr")
summoner_infos = summoner.summoner_dict()



