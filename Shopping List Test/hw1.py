#Chris Fernandez
#3/31/16
#Assignment #1: Shopping List


def is_complete(shopping_list):
#Returns True if the inputted shopping list has 0 or less quantities for all of its items
  if shopping_list == []:
    return True
  for i in range(0, len(shopping_list)):
    if shopping_list[i][1] > 0:
      return False

  return True


def add_item(shopping_list, to_add):
#Appends new items and adds to exsisting items inputted to shopping list then returns list
  for i in range(0, len(shopping_list)):
    if shopping_list[i][0] == to_add[0]:
      shopping_list[i][1] += to_add[1]
      return shopping_list

  shopping_list.append(to_add)
  return (shopping_list)


def update_item(shopping_list, acquired):
#Subtracts from quantities of items exsisting on inputted shopping list and returns list
  for i in range(0, len(shopping_list)):
    if shopping_list[i][0] == acquired[0]:
      shopping_list[i][1] -= acquired[1]
      return shopping_list

  return shopping_list


def remaining(shopping_list):
#Takes inputted shopping list and from it returns a list of items with quantities greater than 0
  remList = []
  for i in range(0, len(shopping_list)):
    if shopping_list[i][1] > 0:
      remList.append(shopping_list[i])

  return remList


'''list = []
#list = [['sugar', 0], ['eggs', 0], ["bread", 3]]
print '      ShoppingList MACHINA:::Alfa 0.000000000000103 Version!\n'
while(True):
  print 'Funtion menu: press #1 to print current shopping_list'
  print '                    #2 to check is_complete'
  print '                    #3 to add_item to shopping_list'
  print '                    #4 to update_item in shopping_list'
  print '                    #5 check remaining items in shopping_list'
  print '                    #else Exit'
  choice = int(input('      Choose: '))
  print'\n'

  if choice == 1:
    print ":::", list
    print'\n\n'
  elif choice == 2:
    print ":::", is_complete(list)
    print'\n\n'
  elif choice == 3:
    newItem = raw_input("newItem: ")
    newQuant = int(input("newQuanity: "))
    print ":::", add_item(list, [newItem, newQuant])
    print'\n\n'
  elif choice == 4:
    updateItem = raw_input("updateItem: ")
    updateQuant = int(input("updateQuanity: "))
    print ":::", update_item(list, [updateItem, updateQuant])
    print'\n\n'
  elif choice == 5:
    print ":::", remaining(list)
    print'\n\n'
  else:
    break'''