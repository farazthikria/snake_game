class  Animal:
  def __init__(self):
    self.dog = 2
    self.dog_printer
  
  def dog_printer(self):
    print(f"dog have {self.dog} eyes")


class Dog(Animal):
  def __init__(self):
    super().__init__()
    
    


dog = Dog()
dog.dog_printer()


