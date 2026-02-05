class CustomerManager:
	def __init__(self, customers):
		self.customers = customers

	def display_customers(self):
		print("\nCustomer Records:")
		for cust_id, details in self.customers.items():
			print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

	def filter_customers_by_city(self, city):
		filtered_customers = {cust_id: details 
							  for cust_id, details in self.customers.items() 
							  if details["location"].lower() == city.lower()}

		if filtered_customers:
			print(f"\nCustomers in {city}:")
			for cust_id, details in filtered_customers.items():
				print(
					f"ID: {cust_id} | Name: {details['name']} | "
					f"Location: {details['location']} | Purchases: {details['purchases']}"
				)
		else:
			print(f"\nNo customers found in {city}.")

	def get_unique_locations(self):
		pass

	def update_customer_location(self, customer_id, new_location):
		if customer_id in self.customers:
			self.customers[customer_id]["location"] = new_location
			print(f"Updated {customer_id} to {new_location}")
		else:
			print(f"Customer {customer_id} not found.")
