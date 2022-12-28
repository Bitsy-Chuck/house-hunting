import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

log = open("log.txt", 'w')
driver = webdriver.Chrome(executable_path='chromedriver', options=chrome_options)
driver.set_page_load_timeout(10)
driver.implicitly_wait(100)
phone_numbers = [7424905217, 7824975217]
mssg = 'Hello. I am looking for a 3 bhk apartment near bellandur or kadubeesanahalli for rent from Feb or March.'

for ph in phone_numbers:
    print("ph", ph)
    time.sleep(5)
    driver.get("https://api.whatsapp.com/send/?phone=91{}&text&type=phone_number&app_absent=0".format(ph))
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a').click()
    print(driver.get_cookies())
    # Use whatsapp web
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a').click()
    time.sleep(2)
    if driver.find_element(by=By.CLASS_NAME, value="_2Nr6U").text != '':
        log.write("failed to send message to {}\n".format(ph))
        continue
    wElement = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    wElement.send_keys(mssg)
    send_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    time.sleep(5)
    send_button.click()
    print("done")
log.close()
'''
for (let i=0; i<10;i++){
try{
    console.log(document.getElementsByClassName("tviruh8d bze30y65 i0jNr selectable-text copyable-text")[i].getElementsByClassName('i0jNr selectable-text copyable-text')[0].innerHTML);
    }
    catch(err){
    }
    //*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/span
}
'''

