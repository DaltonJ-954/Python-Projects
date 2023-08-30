class Devices:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        def move(self):
            print("Welcome.")
            
            
class PC:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        def move(self):
            print("LogIn")
            
            
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        def move(self):
            print("Android.")
            
            
class Tablet:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        def move(self):
            print("Swipe.")
            
myPC = PC("Aura", "EdgeGame")
myPhone = Phone("Samsung", "Z-Fold 4")
myTablet = Tablet("Sony", "Mirror")