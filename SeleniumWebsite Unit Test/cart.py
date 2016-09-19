#Chris Fernandez
#5/30/16
#CS 4320 Software Testing
#Assignment #6 cart.py

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart:

  def __init__(self, driver):
    #Cart class Constructor: takes a webdriver element as a parameter
    #Attempts to create a Cart object if the current url of the driver is around https://www-secure.target.com/co-cart
    self.driver = driver
    url = WebDriverWait(driver, 15).until(lambda driver: driver.current_url)
    if (url[:37] != "https://www-secure.target.com/co-cart"):
      raise ValueError("THIS SITE ISN'T RIGHT! url: " + url +"\n  expected: https://www-secure.target.com/co-cart")


  def count_items(self):
    #Takes the unicode text string "# items" in cart, cuts the non-digit elements from it, converts the string digit values into ints,
    #  and returns the cart item count
    cartStr = (WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_class_name("js-cartQuantitySr"))).text
    if cartStr[:2] == '1 ':
      cartCount = cartStr[:-5]
    else:
      cartCount = cartStr[:-6]
    cartCount = int(cartCount)
    return cartCount

    
  def clear_cart(self):
  #Function that uses a loop to remove all items out of Target.com's shopping cart
  #Added a sleep statement to the end to keep the loop's check consistent with Target.com's bad load times
    while self.count_items() != 0:
      WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_class_name("cartItem--options")
        .find_element_by_tag_name("button")).click()
      WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_xpath
        ("/html/body/div[2]/div[4]/div[1]/div[2]/div[2]/div/div[2]/button[1]")).click()
      time.sleep(5)


  def increment_item(self, item_index, section_index):
    #Takes an item_index and section parmeter. Uses xpath to Increment the quanity for the item found at that given index in target.com's checkout menu by 1
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[2]
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[2]/div/div[1]/div[2]/div/button[2]

    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[2]
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[2]/div/div[1]/div[2]/div/button[2]
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[3]/div/div[1]/div[2]/div/button[2]

    #/html/body/div[2]/div[4]/div[1]/div[1]/section[3]/div[1]/div[1]/div/div[1]/div[2]/div/button[2] headphone
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[2] tv
    #                                       ---------
    #Added a section_parameter because some target.com items have a different xpath in that area for whichever reason and this was the best solution
    #  I could think of that worked
    item_index = str(item_index)
    section_index = str(section_index)
    xpath = "/html/body/div[2]/div[4]/div[1]/div[1]/section[" + section_index + "]/div[1]/div[" + item_index + "]/div/div[1]/div[2]/div/button[2]"
    WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_xpath(xpath)).click()


  def decrement_item(self, item_index, section_index):
    # Takes an item_index parameter. Uses xpath to Decrement the quanity for the item found at that given index in target.com's checkout menu by 1
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[1]
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[2]/div/div[1]/div[2]/div/button[1]
    #/html/body/div[2]/div[4]/div[1]/div[1]/section[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[1]
    # Added a section_parameter because some target.com items have a different xpath in that area for whichever reason and this was the best solution
    #  I could think of that worked
    item_index = str(item_index)
    section_index = str(section_index)
    xpath = "/html/body/div[2]/div[4]/div[1]/div[1]/section[" + section_index + "]/div[1]/div[" + item_index + "]/div/div[1]/div[2]/div/button[1]"
    WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element_by_xpath(xpath)).click()
