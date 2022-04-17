from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



browser = webdriver.Firefox()

browser.get('https://staging4.tstprep.com/store/')

wait = WebDriverWait(browser, 3)


#object of ActionChains
a = ActionChains(browser)

#identify element
# emergencyCourseBtn = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()[contains(.,'Emergency')]][text()[contains(.,'Course')]]")))

emergencyCourseBtn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mgbutton.moove-gdpr-infobar-allow-all.gdpr-fbo-0")))



a.move_to_element(emergencyCourseBtn).click().perform()

