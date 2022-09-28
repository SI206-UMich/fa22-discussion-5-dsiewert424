from itertools import count
import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = 0
		max_item = None
		for item in self.items:
			if item.stock > max_stock:
				max_stock = item.stock
				max_item = item
		return max_item
		pass

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = 0
		max_item = None
		for item in self.items:
			if item.price > max_price:
				max_price = item.price
				max_item = item
		return max_item
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("a a aaa:a"), 6)
		self.assertEqual(count_a("Aaa : a"), 3)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w1 = Warehouse()
		item7 = Item("Pepsi", 3, 40)
		w1.add_item(self.item1)
		w1.add_item(self.item2)
		w1.add_item(self.item3)
		w1.add_item(self.item4)
		w1.add_item(self.item5)

		self.assertEqual(self.item1 in w1.items, True)
		self.assertEqual(self.item2 in w1.items, True)
		self.assertEqual(self.item3 in w1.items, True)
		self.assertEqual(self.item4 in w1.items, True)
		self.assertEqual(self.item5 in w1.items, True)
		self.assertEqual(item7 in w1.items, False)




	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		Costco = Warehouse([self.item1, self.item2, self.item3])
		mx_stock = Costco.get_max_stock()

		self.assertEqual(mx_stock, self.item3)
		

		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		Costco = Warehouse([self.item1, self.item2, self.item3])
		mx_price = Costco.get_max_price()

		self.assertEqual(mx_price, self.item1)

		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()