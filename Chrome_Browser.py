from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading

class Web_Automations():

    def run_browser_for_pearl(self):
        if self.check_all_entry_boxes_has_value(): # will run only if the values are filled in the entry box
            driver = webdriver.Chrome("C:\\Users\\Jalal\\Desktop\\Python Notes\\NLP and ChatBot\\chromedriver.exe")
            driver.get("http://www.python.org")
            assert "Python" in driver.title
            elem = driver.find_element_by_name("q")
            elem.clear()
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            time.sleep(20)
            assert "No results found." not in driver.page_source
            driver.close()
    def run_browser_for_smart(self):
        if self.check_all_entry_boxes_has_value(): # will run only if the values are filled in the entry box
            driver = webdriver.Chrome("C:\\Users\\Jalal\\Desktop\\Python Notes\\NLP and ChatBot\\chromedriver.exe")
            driver.get("http://www.python.org")
            assert "Python" in driver.title
            elem = driver.find_element_by_name("q")
            elem.clear()
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            time.sleep(20)
            assert "No results found." not in driver.page_source
            driver.close()

    def run_browser_threaded_pearl(self):
        job_thread = threading.Thread(target=self.run_browser_for_pearl)
        job_thread.start()

    def run_browser_threaded_smart(self):
        job_thread = threading.Thread(target=self.run_browser_for_smart)
        job_thread.start()