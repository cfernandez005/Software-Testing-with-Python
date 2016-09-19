#Chris Fernandez
#5/21/16
#CS 4320 Software Testing
#Assignment #5

import unittest
from datetime import date
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCSUEB(unittest.TestCase):

  def testFooter(self):
    #Takes the footer of the CSUEB homepage and copies it's text into a string footer.
    #Footer is then divided into copyright, address, and phoneNum
    #Each of these strings are tested for correctness.
    #The copyright string has the added bonus of being tested against the date.today() function from the datetime library
    footer = (WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("footer-content"))).text
    copyright = footer[0:74]
    address = footer[77:122]
    phoneNum = footer[125:143]

    self.assertEquals("Copyright " + str(date.today().year) + " California State University, East Bay. All Rights Reserved.", copyright)
    self.assertEquals("25800 Carlos Bee Boulevard, Hayward, CA 94542", address)
    self.assertEquals("phone 510-885-3000", phoneNum)


  def testLinks(self):
    #Clickes each of links--Prospective Students, Current Students, Alumni & Friends--and checks their html page titles for correctness
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("main-nav-prospective-students")).click()
    self.assertEquals("Prospective Students Home Page", driver.title)
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("main-nav-current-students")).click()
    self.assertEquals("Current Students at Cal State East Bay", driver.title)
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("main-nav-alumni-friends")).click()
    self.assertEquals("Alumni Association", driver.title)


  def testQuicklinks(self):
    #Opens the quicklinks drop-down menu from CSUEB homepage, clicks the Blackboard link, and checks BlackBoard's html page title for correctness.
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("quicklinks-toggle-link")).click()
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("Blackboard")).click()
    self.assertEquals("My Blackboard " + unichr(8211) + " Blackboard Learn", driver.title)


  def testSearchBox(self):
    #Goes to the CSUEB homepage, inputs "housing" into the search box, clicks Go, and then checks the results for a link labeled "Housing".
    driver.get("http://www.csueastbay.edu/")
    inputElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("search-query"))
    inputElement.send_keys("housing")
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("button-search-go")).click()
    check = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("Housing")).text
    self.assertEqual("Housing", check)


  def testSlideshow(self):
    #Goes to the CSUEB homepage, gather's a list of img elements found under the slideShow id, and loops through each element's src attribute checking for the .jpg file type.
    driver.get("http://www.csueastbay.edu/")
    images = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("slideShow").find_elements_by_tag_name("img"))
    for i in images:
      self.assertEqual(".jpg", i.get_attribute("src")[-4:])



if __name__ == '__main__':
  driver = webdriver.Firefox()
  driver.get("http://www.csueastbay.edu/")
  unittest.main()
  driver.quit()
