# Based On https://maryville.instructure.com/courses/43363/pages/iterator?module_item_id=2745150
import abc

class Tasks:
    def __init__(self, name):
        self.task_name = name

    def __str__(self):
        return f"{self.task_name}"

class MenuIterator:
    def __init__(self, tasks):
        self.index = 0
        self.tasks = tasks

    def has_next(self):
        return False if self.index >= len(self.tasks) else True

    def next(self):
        task = self.tasks[self.index]
        self.index += 1
        return task

    def remove(self):
        return self.tasks.pop()

class Menu:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def iterator(self):
        return MenuIterator(self.tasks)


def main():
    t1 = Tasks("View Leave")
    t2 = Tasks("Approve Leave")
    t3 = Tasks ("Deny Leave")
    menu = Menu()
    menu.add(t1)
    menu.add(t2)
    menu.add(t3)
  

    print("Displaying Menu:")
    iterator = menu.iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)
    print()

    print("Removing last item returned\n")
    iterator.remove()

    print("Displaying Menu:")
    iterator = menu.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)
        
        
main()