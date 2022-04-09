# A kerosene home delivery company is implementing a system to track their 
# delivery trucks on a daily basis. All data
# members must be PRIVATE.
# A KeroseneDeliveryTruck class should have the following data members:
# . price_per_litre Float What the company charges per litre of kerosene.
# . litres_in_truck Float The current amount of Kerosene in the Truck
# . truck_capacity Float The overall Capacity of the Truck to hold kerosene
# . min_delivery_qty Float The minimum delivery order amount of Kerosene
# . deliveries_today Int The number of deliveries made by the truck today
# . total_sales Float The total monetary value taken from deliveries today
class KeroseneDeliveryTruck:
    def __init__(self, price_per_litre_in, min_delivery_qty_in, truck_capacity_in, litres_in_truck=None):
        if price_per_litre_in > 0:
            self.__price_per_litre = price_per_litre_in
        else:
            self.__price_per_litre = 0
            
        if min_delivery_qty_in > 0:
            self.__min_delivery_qty = min_delivery_qty_in
        else:
            self.__min_delivery_qty = 0
            
        if truck_capacity_in > 0:
            self.__truck_capacity = truck_capacity_in
        else:
            self.__truck_capacity = 0
            
        if litres_in_truck is not None:
            self.__litres_in_truck = litres_in_truck
        else:
            self.__litres_in_truck = 0
            
        self.__deliveries_today = 0
        self.__total_sales = 0

    def fill_truck(self, fill_amount_in):
        if fill_amount_in > 0 and self.__litres_in_truck + fill_amount_in <= self.__truck_capacity:
            self.__litres_in_truck += fill_amount_in
        else:
            print("Fill amount is invalid or truck is full")
            
    def make_delivery(self, litres_for_delivery):
        if self.__litres_in_truck >= litres_for_delivery and litres_for_delivery >= self.__min_delivery_qty:
            self.__deliveries_today += 1
            self.__litres_in_truck -= litres_for_delivery
            
            if litres_for_delivery < 500:
                self.__total_sales += self.__price_per_litre * litres_for_delivery
                
            else:
                self.__total_sales += self.__price_per_litre * litres_for_delivery * 0.9
                
            return self.__total_sales
        else:
            return -1
        
    def set_price_per_litre(self, new_price_per_litre):
        if new_price_per_litre > 0:
            self.__price_per_litre = new_price_per_litre
        else:
            print("Price per litre is invalid")
            
    def print(self):
        print("Price per litre: ", self.__price_per_litre)
        print("Litres in truck: ", self.__litres_in_truck)
        print("Truck capacity: ", self.__truck_capacity)
        print("Minimum delivery quantity: ", self.__min_delivery_qty)
        print("Deliveries today: ", self.__deliveries_today)
        print("Total sales: ", self.__total_sales)

print("\n{:=^50}".format("Truck 1"))

truck1 = KeroseneDeliveryTruck(0.88, 100, 20000, 8000)
truck1.fill_truck(8000)
returned = truck1.make_delivery(400)

if returned != -1:
    print("Cost of delivery: ", returned)
    
else:
    print("Delivery was not successful")

truck1.print()

print("\n{:=^50}".format("Truck 2"))

print("----Fule: 0.87")
truck2 = KeroseneDeliveryTruck(0.87, 50, 21000, 500)
truck2.fill_truck(10000)
returned = truck2.make_delivery(1000)

if returned != -1:
    print("Cost of delivery: ", returned)
    
else:
    print("Delivery was not successful")

truck2.print()

print("----Fule: 0.98")
truck2.set_price_per_litre(0.98)
truck2.print()