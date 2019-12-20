class Singleton:
    __instance = None
    def __init__(self, some):
        if Singleton.__instance is None:
            Singleton.__instance = some
            print(" __init__ method called..")
    def __new__(cls, some):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    def name(self):
        self.name = self.getInstance()
        return print(self.name)
        
ukraine_capital_1 = Singleton('wwed')
ukraine_capital_2 = Singleton('4432')
print(ukraine_capital_1)
print(ukraine_capital_2)
ukraine_capital_2.name()
ukraine_capital_2.name()


