from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

website = "https://store.steampowered.com/"
path = r"C:\Users\aless\Downloads\chromedriver-win64\chromedriver.exe"

#headless-mode
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(options=options, service=service)
driver.get(website)

wait= WebDriverWait(driver, 10)
section = wait.until(EC.presence_of_element_located((By.ID, "tab_newreleases_content")))
containers = section.find_elements(By.CLASS_NAME, "tab_item")

game_titles = []
game_genres = []
game_links = []

for container in containers:
    game_title = container.find_element(By.CLASS_NAME, "tab_item_name").text
    game_genre = container.find_element(By.CLASS_NAME, "tab_item_details").text
    game_link = container.get_attribute("href")
    game_titles.append(game_title)
    game_genres.append(game_genre)
    game_links.append(game_link)
    print(f"Obtido: {game_title}")


steam_dict = {'Game Title': game_titles,
        'Game Genre': game_genres,
        'Game Link': game_links}

df_steam = pd.DataFrame(steam_dict)
df_steam.to_csv('new_trending-headless.csv', index=False)

driver.quit()