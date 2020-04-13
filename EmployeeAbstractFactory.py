# Based on https://maryville.instructure.com/courses/43363/pages/abstract-factory?module_item_id=2745136
from abc import ABCMeta, abstractmethod

class EmployeeAbstractFactory(metaclass=ABCMeta):
   def __init__(self, eid: str, employee_name: tuple):
       self.employee_id = eid
       self.employee_name = employee_name
    
       
   @abstractmethod
   def get_role(self):
         pass
     
     
   def __str__(self):
       return f"Employee Role: {self.__class__. __name__}\nEmployee ID: {self.employee_id}\nEmployee Name: {self.employee_name[0]} {self.employee_name[1]}\n"
    
class Manager(EmployeeAbstractFactory):
    def get_role(self):
        return "Manager"
    
class Supervisor(EmployeeAbstractFactory):
    def get_role(self):
        return "Supervisor"
    
class Technician(EmployeeAbstractFactory):
    def get_role(self):
        return "Technicion"
        
    
class EmployeeFactory(object):
    @classmethod
    def create(cls, name, *args):
        name:name
    # name determines which role to return.    
        if name == 'man':
            return Manager(*args)
        elif name == 'sup':
            return Supervisor(*args)
        elif name == 'tech':
            return Technician(*args)

  
        
        
        
def main():
    # printing one of each role to verify each role is working
    print(EmployeeFactory.create("man", '0826', ("Ben", "Muzzy"))) 
    print(EmployeeFactory.create("sup", '0408', ("Atlas", "Muzzy")))
    print(EmployeeFactory.create("tech", '0818', ("Gizmo", "Muzzy")))
    
main()