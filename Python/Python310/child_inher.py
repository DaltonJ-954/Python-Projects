
class Console:
  def __init__(self, brand, name):
    self.brandName = brand
    self.consoleName = name

  def printName(self):
    print(self.brandName, self.consoleName)


class Microsoft(Console):
    pass

z = Microsoft("Xbox", "Series X")
z.printName()

class Sony(Console):
    pass

y = Sony("Playstation", 5)
y.printName()


class Nintendo(Console):
    pass
x = Nintendo("Switch", "OLED")
x.printName()


class PC(Console):
    pass
a = PC("AMD", "Intel")
a.printName()
    

