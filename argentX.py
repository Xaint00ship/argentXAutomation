from selenium.webdriver.common.by import By
from time import sleep

class ArgentX:

    def __init__(self, phrase, argentXPass, driver):
        self.phrase = phrase
        self.argentXPass = argentXPass
        self.driver = driver


    def installArgentX(self): # не до конца сделано, проблема в модальном окне
        self.driver.get('https://chrome.google.com/webstore/detail/argent-x/dlcobpjiigpikoobohmabehhmhfoodbb')
        sleep(5)
        self.driver.find_element(By.CLASS_NAME, 'webstore-test-button-label').click()
        sleep(100)


    def importWallet(self): # импорт кошелька
        self.driver.switch_to.window(self.driver.window_handles[1])  # переключение на 2 окно(аргент икс)
        sleep(5)
        self.driver.set_window_size(500, 1000)
        self.driver.find_element(By.CLASS_NAME, "kNJcqd").click()

        # создадим из фразы список слов
        list_phrase = list(self.phrase.split(" "))
        # вставить слова в соответствующие поля
        index = 1
        for word in list_phrase:
            print(word)
            self.driver.find_elements(By.CLASS_NAME, "chakra-input")[index-1].send_keys(word)
            index+=1
        sleep(5)
        self.driver.find_elements(By.CLASS_NAME, "ljIPqN")[0].click()
        sleep(5)
        self.driver.find_elements(By.CLASS_NAME, "TyKKa")[0].send_keys(self.argentXPass)
        self.driver.find_elements(By.CLASS_NAME, "TyKKa")[1].send_keys(self.argentXPass)
        self.driver.find_element(By.CLASS_NAME, "ZDzRo").click()
        sleep(10)
        self.driver.find_element(By.CLASS_NAME, "jzVsKG").click()
        sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[0])  # переключение на 1 окно


    def connectConfirmWallet(self): # вход в аргент икс по паролю
        self.driver.switch_to.window(self.driver.window_handles[1]) # переключение на 2 окно(аргент икс)
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "css-1eonw3x").send_keys(self.argentXPass)
        self.driver.find_element(By.CLASS_NAME, "css-1xr2u50").click()
        sleep(5)
        self.driver.find_elements(By.CLASS_NAME, "cCKSOO")[1].click()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])  # переключение на 1 окно
        sleep(10)


