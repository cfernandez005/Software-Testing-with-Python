#Chris Fernandez
#5/30/16
#CS 4320 Software Testing
#Assignment #6 test_cart.py

import unittest
import time
from cart import Cart
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class test_cart(unittest.TestCase):

  def setUp(self):
    #non-tested function used to clear the cart of all items before each testcase
    #Added a sleep statment and reloaded the cart webpge because sometimes the first load wouldn't produce the correct cart results
    driver.get("https://www-secure.target.com/co-cart")
    time.sleep(5)
    driver.get("https://www-secure.target.com/co-cart")
    clearCart = Cart(driver)
    clearCart.clear_cart()


  def testConstructor(self):
    #Test the creation of objects from the Cart class constructor for correctness
    self.setUp()
    driver.get("http://www.csueastbay.edu/")
    with self.assertRaises(ValueError):
      constructorTest1 = Cart(driver)
    driver.get("https://www-secure.target.com/co-cart")
    constructorTest2 = Cart(driver)


  def testAddItem(self):
    #Adds one Samsung 40" LED Smart TV to target.com's shopping cart. Then test target.com's shopping cart item# value for correctness--expects 1
    self.setUp()
    driver.get("http://www.target.com/p/samsung-40-class-1080p-60hz-led-smart-tv-black-un40j5200afxza/-/A-16390220#prodSlot=_1_2")
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
      ("/html/body/div[2]/div[4]/div/aside/div[2]/div[4]/div[3]/div/div/div[1]/div/button")).click()
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
      ("/html/body/div[2]/div[4]/div/div[5]/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/button")).click()
    cartCountTest = Cart(driver)
    self.assertEqual(1, cartCountTest.count_items())


  def testPlusMinusButtons(self):
    #Adds an item to target.com's shopping cart. Calls the Cart class increment function to add one additional quanity of that item to shopping cart.
    #Test the change in target.com's shopping cart item# value for correctness--expects 2. Calls the Cart class decrement function to subtract one
    #  additional quanity of that item same item from shopping cart. Again, test target.com's shopping cart item# value for correctness--expects 1
    #Added sleep statments before each count_item() and assert call to keep the tests consistent with Target's bad load times
    self.setUp()
    driver.get("http://www.target.com/p/gopro-hero-chdha-301/-/A-16399081")
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
      ("/html/body/div[2]/div[4]/div/aside/div[2]/div[4]/div[3]/div/div/div[1]/div/button")).click()
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
      ("/html/body/div[2]/div[4]/div/div[5]/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/button")).click()
    cart = Cart(driver)
    cart.increment_item(1, 2)
    time.sleep(5)
    countTest = cart.count_items()
    self.assertEqual(2, countTest)
    cart.decrement_item(1, 2)
    time.sleep(5)
    countTest = cart.count_items()
    self.assertEqual(1, countTest)


  def testAppleEarPodByLimit(self):
    #Adds one pair of Apple Earpods to target.com's shopping cart. Calls the Cart class increment function to attempt to add an additional pair of
    #  Apple Earpods to cart. Expects the Cart to remain unchanged due to the limited amount of Apple Earpods allowed per checkout transaction with
    #  website. Test target.com's shopping cart item# value for correctness--expects 1
    # Added a sleep statment before the count_item() and assert call to keep the test consistent with Target's bad load times
    self.setUp()
    driver.get("http://www.target.com/p/apple-earpods-with-remote-and-mic-white-md827ll-a-/-/A-14213685")
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
      ("/html/body/div[2]/div[4]/div/aside/div[2]/div[4]/div[3]/div/div/div[1]/div/button")).click()
    WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath
      ("/html/body/div[2]/div[4]/div/div[5]/div[2]/div[2]/div/div[2]/div/div[1]/div[4]/button")).click()
    earPod = Cart(driver)
    earPod.increment_item(1, 3)
    time.sleep(5)
    countTest = earPod.count_items()
    self.assertEqual(1, countTest)



if __name__ == '__main__':
  driver = webdriver.Firefox()
  unittest.main(verbosity = 2)
  driver.quit()
