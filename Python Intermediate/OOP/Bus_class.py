

class Bus():

    def __init__(self, passengers_capacity):
        self.passengers_capacity =  passengers_capacity
        self.passenger_onboard = []

    def passenger_counter(self,person):

        if len(self.passenger_onboard) < self.passengers_capacity:
            self.passenger_onboard.append(person)
            print(f"Passenger {person.name} is onboard")
        else:
            print(f"{person.name} bus is full, take the next")
    
    def bus_stop(self, person):
        self.passenger_onboard.remove(person)
        print(f"{person.name} has gotten off the bus")





class Person(): 

    def __init__(self, name):
        self.name = name


bus_1 = Bus(3)

person_1 = Person("Ingrid")
bus_1.passenger_counter(person_1)

person_2 = Person("Mambo Nuñez")
bus_1.passenger_counter(person_2)

person_3 = Person("Pilar Cisneros")
bus_1.passenger_counter(person_3)

person_4 = Person("Yogurt")
bus_1.passenger_counter(person_4)
bus_1.bus_stop(person_1)
bus_1.passenger_counter(person_4)


