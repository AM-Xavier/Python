from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

website = "https://store.steampowered.com/"
path = r"C:\Users\aless\Downloads\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(options=options, service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//a[@class="tab_item app_impression_tracked"]')


for container in containers:
    game_title = container.find_element(by="xpath", value='./div [@class="tab_item_content"]/div[@class="tab_item_name"]').text
    game_genre = container.find_element(by="xpath", value='./div [@class="tab_item_content"]/div[@class="tab_item_details"]').text
    game_link = container.find_element(by="xpath", value='//a[@class="tab_item app_impression_tracked"]').get_attribute("href")





# //a[@class="tab_item app_impression_tracked"]
# //a[@class="tab_item app_impression_tracked"]/div [@class="tab_item_content"]/div[@class="tab_item_details"]
# '//a[@class="tab_item app_impression_tracked"]/div [@class="tab_item_content"]/div[@class="tab_item_name"]'