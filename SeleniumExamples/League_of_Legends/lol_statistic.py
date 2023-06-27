from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Belli bir sayfada arama yapıcak kullanıcıyı bulursa verileri alıp saklıcak
# Görüntü varsa sorun değil hocam
# Create summoner class
class Summoner:

    def __init__(self, summoner_nickname, region):
        self.summoner_nick = summoner_nickname
        self.region = region
        self.summoner_dict = {}
        self.url = f"https://www.leagueofgraphs.com/tr/summoner/{self.region}/{self.summoner_nick}"
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.get_summoner_info()

    def check_summoner(self):
        try:
            self.browser.find_element(By.CLASS_NAME, 'solo-text').text
            return False
        except NoSuchElementException:
            return True

    def get_summoner_info(self):
        if self.check_summoner():
            time.sleep(5)
            # Fill the dict
            self.summoner_dict["nick"] = self.browser.find_element(By.XPATH,"//*[@id='pageContent']/div[1]/div/div[2]/h2").text
            self.summoner_dict["level"] = self.browser.find_element(By.XPATH,"//*[@id='pageContent']/div[1]/div/div[2]/div").text
            self.summoner_dict["played_game"] = self.browser.find_element(By.XPATH,"//*[@id='graphDD5']").text
            self.summoner_dict["win_rate"] = self.browser.find_element(By.XPATH,"//*[@id='graphDD6']").text
            self.summoner_dict["soloq"] = {"wins":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[5]/span[1]/span").text,
                                "loses":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[5]/span[3]/span").text,
                                "rank":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[1]").text,
                                "lp":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[4]/span").text}
            self.summoner_dict["flex"] = {"wins":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/span[1]/span").text,
                                "loses":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/span[3]/span").text,
                                "rank":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]").text,
                                "lp":self.browser.find_element(By.XPATH,"//*[@id='mainContent']/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/span").text}
            counter = 3
            for id in range(1,11):
                self.summoner_dict[id] = {
                    "character":self.browser.find_element(By.XPATH,f"//*[@id='mainContent']/div[1]/div[1]/div[5]/table/tbody/tr[{counter}]/td[1]/a/div[1]/img").get_attribute("title"),
                    "state":self.browser.find_element(By.XPATH,f"//*[@id='mainContent']/div[1]/div[1]/div[5]/table/tbody/tr[{counter}]/td[3]/a/div[1]").text,
                    "mod":self.browser.find_element(By.XPATH,f"//*[@id='mainContent']/div[1]/div[1]/div[5]/table/tbody/tr[{counter}]/td[3]/a/div[2]").text,
                    }
                counter = counter + 1
            self.display_summoner()
        else:
            print("There is no summoner like this")
    # evet. Varsa bilgileri yazdırıyor
    def display_summoner(self):
        if self.check_summoner():
            print("Nick: " + self.summoner_dict["nick"] +
            "\nLevel: " + self.summoner_dict["level"] +
            "\nPlayed Game: " + self.summoner_dict["played_game"] +
            "\nWin Rate: " + self.summoner_dict["win_rate"] +
            "\n--Soloq--" +
            "\n    Wins: " + self.summoner_dict["soloq"]["wins"] +
            "\n    Loses: " + self.summoner_dict["soloq"]["loses"] +
            "\n    Rank: " + self.summoner_dict["soloq"]["rank"] +
            "\n    Lp: " + self.summoner_dict["soloq"]["lp"] +
            "\n--Flex--" +
            "\n    Wins: " + self.summoner_dict["flex"]["wins"] +
            "\n    Loses: " + self.summoner_dict["flex"]["loses"] +
            "\n    Rank: " + self.summoner_dict["flex"]["rank"] +
            "\n    Lp: " + self.summoner_dict["flex"]["lp"]
            )
        else:
            print("There is no summoner like this ")
            
        
# summoner kullanıcı oluyor.
summoner = Summoner("Senkami","tr")




