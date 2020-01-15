class AbstractCook:
    def __init__(self):
        self.food_name = "food"
        self.drink_name = "drink"
        self.am_food = 0
        self.am_drink = 0
        self.f_pr = 0
        self.d_pr = 0        
    def total(self): 
        summ = self.d_pr+self.f_pr
        return print("{}: {}, {}: {}, Total: {}".format(self.food_name, self.f_pr, self.drink_name, self.d_pr, summ))
        
    def add_food(self, cnt, price):
        self.am_food += cnt
        self.f_pr += cnt * price 
        
    def add_drink(self, cnt, price):
        self.am_drink += cnt 
        self.d_pr += cnt * price        
    
class RussianCook(AbstractCook):
    def __init__(self):
        AbstractCook.__init__(self)
        self.food_name = "Dumplings"  
        self.drink_name = "Compote"
        
class JapaneseCook(AbstractCook):
    def __init__(self):
        AbstractCook.__init__(self)
        self.food_name = "Sushi"  
        self.drink_name = "Tea"

class RussianCook(AbstractCook):
    def __init__(self):
        AbstractCook.__init__(self)
        self.food_name = "Pizza"  
        self.drink_name = "Juice"        
        
        
cl = RussianCook()
cl.add_food(2, 40)
cl.add_food(10, 10)
cl.add_drink(3, 40)
cl.total()


                
    