from src.admin import Admin
from src.customer import Customer
def main():
    vehicles={}
    customers={}
    admin = Admin(vehicles)
    customers = Customer(vehicles,customers)
    while True:
        print("__welcome to renytal system__")
        print("1.Admin Panel")
        print("2.Customer Panel")
        print("3.Exit   ")
        choice = int(input("Enter your choice 1/2/3 : "))
        if choice==1:
            print("__Admin Panel__")
            print("1.add_vehicles to the system")
            print("2.show the all vehicles")
            print("3.Back to main panel")
            admin_choice=int(input("Enter your choice 1/2/3 : "))
            if admin_choice==1:
                vehicles_id=input("Enter vehicle id: ")
                vehicle_type=input("Enter vehicle type: ")
                brand=input("Enter vehicle brand: ")
                rent_price=input("Enter rent price: ")
                admin.add_vehicle(vehicles_id,vehicle_type,brand,rent_price,available=True)
            elif admin_choice==2:
                admin.view_vehicles()
            elif admin_choice==3:
                print("Exiting...")
                break   

        elif choice==2:
            print("__Customer Panel__")
            print("1.Register as a customer")
            print("2.Show available vehicles")
            print("3.Rent a vehicle")
            print("4.Return a vehicle")
            print("5.Back to main panel")
            cus_choice=int(input("Enter your choice 1/2/3/4/5 : "))
            if cus_choice==1:
                customer_id=input("Enter customer id: ")
                name=input("Enter customer name: ")
                customers.customer_register(customer_id,name)
            elif cus_choice==2:
                customers.show_available_vehicles()
            elif cus_choice==3:
                customer_id=input("Enter customer id: ")
                vehicle_id=input("Enter vehicle id: ")
                customers.rent_vehicle(customer_id,vehicle_id)
            elif cus_choice==4:
                customer_id=input("Enter customer id: ")
                customers.retrn_a_vehicle(customer_id)
            elif cus_choice==5:
                print("Exiting...")
                break   
        elif choice==3:
            print("Exit form the system...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



