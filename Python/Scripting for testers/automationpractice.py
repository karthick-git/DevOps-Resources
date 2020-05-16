from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox(executable_path=r'C://Users//USER//Downloads//geckodriver.exe')
driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')


product_containers = driver.find_elements_by_class_name('product-container')
last_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for index,product_container in enumerate(product_containers):
    hover=ActionChains(driver).move_to_element(product_container)
    hover.perform()

    #To click on add to cart button on all products, replace li[1] with li[%s]
    #li starts from 1, but index by default starts from 0, so add 1 to index
    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1))
    
    #To click on continue shopping button
    driver.find_element_by_class_name('continue btn btn-default button exclusive-medium').click
    