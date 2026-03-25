class Admin:
    
    def __init__(self, vehicles):
        self.vehicles = vehicles
    def add_vehicle(self, vehicle_id,vehicle_type,brand,rent_price,available):
        self.vehicles[vehicle_id] = {
            'vehicle_id': vehicle_id,
            'vehicle_type': vehicle_type,
            'brand': brand,
            'rent_price': rent_price,
            'available': True
        }
        print(f"Vehicle {vehicle_id} added successfully.")
    def view_vehicles(self):
        print("Available Vehicles:")
        for vehicle_id, vehicle_info in self.vehicles.items():
            status = "available" if vehicle_info["available"] else "Rented"
            print(f"ID: {vehicle_id}, Type: {vehicle_info['vehicle_type']}, Brand: {vehicle_info['brand']}, Rent Price: {vehicle_info['rent_price']}, Status: {status}")
    

