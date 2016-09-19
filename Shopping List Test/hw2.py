#Chris Fernandez
#4/9/16
#Assignment #2: unittest module


import unittest #imports in the unittest class
from hw1 import * #imports all code from hw1.py


class shoppingListTest(unittest.TestCase): #class that defines code to be tested

  def testIsComplete_onePositiveQuantity(self):
    # is_complete function test case where one list item has a positive quantity: expected False
    self.assertFalse( is_complete([['cheese', 0], ['milk', 0], ['eggs', 12]]) )

  def testIsComplete_allQuantitiesZero(self):
    # is_complete function test case where all list items have a zero quantity: expected True
    self.assertTrue( is_complete([['bread', 0], ['pickles', 0], ['eggs', 0], ['radish', 0]]) )

  def testIsComplete_oneNegaiveQuantity(self):
    # is_complete test case where one list item has a negative quantity and the rest have a zero quantity: expected True
    self.assertTrue( is_complete([['salami', 0], ['waffle', -10], ['noodles', 0]]) )

  def testIsComplete_emptyList(self):
    # is_complete test case of an empty list: expected True
    self.assertTrue( is_complete([]) )


  def testAddItem_notInList(self):
    # add_item test case for adding an item to a list that was previously non-exsistent: expected new item appended to list
    self.assertEqual( [['flour', 3], ['potatoe', 10], ['toothpaste', 1], ['chips', 101]],
                      add_item([['flour', 3], ['potatoe', 10], ['toothpaste', 1]], ['chips', 101]) )

  def testAddItem_alreadyInList(self):
    # add_item test case for adding a positive quantity item to a list where such item already exsists
    # : expected item quantity addition to listed item qantity
    self.assertEqual( [['apples', 22], ['mushroom', 17], ['chicken breast', 16]],
                     add_item([['apples', 22], ['mushroom', 17], ['chicken breast', 8]], ['chicken breast', 8]) )


  def testUpdateItem_alreadyInList(self):
    # updae_item test case for updating an already listed item with a positive quantity copy
    # : expected item quantity subtraction from listed item qantity
    self.assertEqual( [['bananas', 6], ['yogurt', 4], ['bagels', 8]],
                      update_item([['bananas', 6], ['yogurt', 12], ['bagels', 8]], ['yogurt', 8]) )

  def testUpdateItem_notInList(self):
    # update_item test case for updating an item that doesn't exsist on the list: expected list remain unchanged
    self.assertEqual( [['provalone', 10], ['pepper jack', 3], ['mayonnaise', 1]],
                      update_item([['provalone', 10], ['pepper jack', 3], ['mayonnaise', 1]], ['cheddar', 13]) )


  def testRemaining_emptyList(self):
    # remaining test case where all listed items have quantities less than one: expected empty list
    self.assertEqual( [], remaining([['kiwi', -5], ['prezels', 0], ['avacado', 0]]) )

  def testRemainging_fullList(self):
    # remaining test case where all listed items have quantities greater than zero: expected entire list
    self.assertEqual( [['apricots', 27], ['chocolate', 17], ['ice', 2], ['sausage', 12]],
                 remaining([['apricots', 27], ['chocolate', 17], ['ice', 2], ['sausage', 12]]) )


if __name__ == "__main__":
  unittest.main(verbosity = 2)
