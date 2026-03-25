class Customer:
    def __init__(self, vehicles,customers):
        self.vehicles = vehicles
        self.customers = customers

    def customer_register(self, customer_id, name):
        self.customers[customer_id] = {
            'customer_id': customer_id,
            'name': name,
            'rented_vehicles': False
        }
        print(f"Customer {name} registered successfully.")

    def show_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle_id, vehicle_info in self.vehicles.items():
            if vehicle_info["available"]:
                print(f"ID: {vehicle_id}, Type: {vehicle_info['vehicle_type']}, Brand: {vehicle_info['brand']}, Rent Price: {vehicle_info['rent_price']}")
                available = True
        if not "available":
            print("No vehicles available at the moment.")

    def rent_vehicle(self, customer_id, vehicle_id):
        if customer_id not in self.customers:
            print("customer not found.")
            return
        elif vehicle_id not in self.vehicles:
            print("vehicle not found.")
            return
        elif not self.vehicles[vehicle_id]["available"]:
            print("vehicle is not available for rent.")
            return
        else:
            self.vehicles[vehicle_id]["available"]= False
            self.customers[customer_id]["rented_vehicles"] = True
            print(f"Vehicle {vehicle_id} rented successfully to customer {customer_id}.")

    def retrn_a_vehicle(self,customer_id):
        if customer_id not in self.customers:
            print("custeromer not found.")
            return
        rented = self.customers[customer_id]["rented_vehicles"]
        if not rented:
            print("customer has not rented any vehicle.")
            return
        self.customers[customer_id]["rented_vehicles"] = False
        self.vehicles[vehicle_id]["available"] = True
        print(f"Vehicle {vehicle_id} returned successfully by customer {customer_id}.")
    