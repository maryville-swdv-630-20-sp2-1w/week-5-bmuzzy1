# based on http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html
from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, observable, *args):
        pass


class Observable:

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self.__observers:
            observer.update(self, *args)
            
class Employee(Observable): 

    def __init__(self, name:tuple, hours):
        super().__init__() 
        self._name = name
        self._hours = hours
        
    def __str__(self):
        return f"Employee: {self._name[0]} {self._name[1]}\nHours: {self._hours}\n"

    @property
    def name(self):
        return f'{self._name[0]} {self._name[1]}'

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, new_hours):
        self._hours= new_hours
        self.notify_observers(new_hours) 


class LeaveManagement(Observer): 

    def update(self, changed_employee, new_hours):
        print(f'{changed_employee.name} now has {new_hours} hours')


class Manager(Observer): 
    
    def update(self, changed_employee, new_hours):
        if new_hours >= 8:
            print(f'{changed_employee.name} IS eligible to take time off. \n')
        else:
            print(f'{changed_employee.name} IS NOT eligible to take time off \n')
        


def main():
    e = Employee(("Ben", "Muzzy"), 6)
    lm = LeaveManagement()
    m = Manager()
    e.add_observer(lm)
    e.add_observer(m)
    
    print(e)
   
    print('First Update')
    e.hours = 20
    print('Second Update')
    e.hours = 5
   


main()