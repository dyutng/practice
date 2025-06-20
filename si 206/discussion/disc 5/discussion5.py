import unittest

#TASK 1: Complete test_count_a()
#TASK 2: Complete the test cases for the Warehouse class methods

# Counts the number of a's in a string
def count_a(string):

# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):

	# Print
	def __str__(self):

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):

	# Adds an item to the warehouse	
	def add_item(self, item):

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):


	# Returns the item in the warehouse with the highest price
	def get_max_price(self):


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		

	## Check to see whether count_a works
	def test_count_a(self):
        # Sentence with an a
		self.assertEqual(count_a("warning"), 3)
        
        # With 0 a's
		self.assertEqual(count_a("xyz"), 0)
        
        # A at beginning
		self.assertEqual(count_a("apple"), 1)

        # A at end
		self.assertEqual(count_a("soda"), 1)
        
        # Only a's
		self.assertEqual(count_a("aaaaa"), 5)

        # Capital A's (case sensitive, so this should be 0)
		self.assertEqual(count_a("Apple"), 1)
		self.assertEqual(count_a("AAAA"), 0)

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		w1 = Warehouse()
		w1.add_item(self.item1)
		self.assertEqual(len(w1.items), 1)
		self.assertEqual(w1.items[0], self.item1)

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stock(self):
			w2 = Warehouse([self.item1, self.item2, self.item3, self.item4, self.item5])
			self.assertEqual(w2.get_max_stock(), self.item3)

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
			w3 = Warehouse([self.item1, self.item2, self.item3, self.item4, self.item5])
			self.assertEqual(w3.get_max_price(), self.item1) 
		
def main():
	unittest.main(verbosity=2)

if __name__ == "__main__":
	main()