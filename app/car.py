import os, re


if not os.path.isfile("registered_cars.txt"):
    f = open("registered_cars.txt", "w")
    f.close()


class Car:
    """
        This class asigns a unique car number to a car instance
        with the shape of 'AAA-002' (regex: [A-Z]{3}-[0-9]{3}) 
    """

    statuses = [
        "The car has already a number assigned",
        "Not a valid number",
        "Already registered number",
        "Successfully registered"
    ]

    def __init__(self, car_number=None):
        self.status = None
        self._car_number = car_number
        self._registered_cars = Car.get_registered_cars()
        self._car_count = len(self.registered_cars) 

        self.save_car_number()


    @property
    def car_count(self):
        return len(self.registered_cars)

    @car_count.setter
    def car_count(self):
        self._car_count = len(Car.get_registered_cars())

    @property
    def registered_cars(self):
        return self._registered_cars

    @registered_cars.setter
    def registered_cars(self):
        self._registered_cars = Car.get_registered_cars()

    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, car_number):

        if self._car_number is None: 
            self._car_number = car_number
        else:
            self.status = "The car has already a number assigned"

        self.save_car_number()
        

    def car_number_not_valid(self):
        """ Check if car_number matches shape 'AAA-002' """
    
        pattern = "[A-Z]{3}-[0-9]{3}"
        match_found = re.search(pattern, self.car_number)
        
        if not match_found and self.car_number != None:
            self.status = "Not a valid number"
            return self.status


    def car_number_registered(self):
        if self.car_number in self.registered_cars:
            self.status = "Already registered number"
            return self.status


    @staticmethod
    def get_registered_cars():
        with open("registered_cars.txt", "r") as f:
            cars = f.read().splitlines()
        return cars


    def register_car_number(self):

        with open("registered_cars.txt", "a") as f:
            self.registered_cars.append(self.car_number)
            f.write(self.car_number + "\n")
            self.status = "Successfully registered"

    def run_validators(self):
        if self.car_number_not_valid(): 
            self._car_number = None
            return
        if len(self.car_number) != len("AAA-002"):
            self._car_number = None
            return
        if self.car_number_registered(): 
            self._car_number = None
            return
        
        

    def save_car_number(self):
        
        if not self.car_number: return
        
        self.run_validators()

        if self.status not in Car.statuses:
            self.register_car_number()


    def delete_car_number(self, car_number):

        if car_number in self.registered_cars:
            
            self.registered_cars.remove(car_number)

            with open("registered_cars.txt", "w") as f:
                f.write("\n".join(self.registered_cars)) 

            self.status = "Deleted successfully"
            
        else:
            self.status = "Car number not found"

    


        
           
        
            

        




        


    
        