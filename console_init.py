class GamingPC:

    def __init__(self,cpu,ram,tb,gpu):
       self.cpu = cpu
       self.ram = ram
       self.tb = tb
       self.gpu = gpu


        
    def config(self):
        print("My config is ", self.ram, self.cpu, self.tb, self.gpu)




com1 = GamingPC('i8','16','1tb','Gforce_RTX')
com2 = GamingPC('Ryzen 4500','20','4tb','Radeon_RX580')

com1.config()
com2.config()
