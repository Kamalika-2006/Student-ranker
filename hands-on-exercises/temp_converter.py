class converter:
    # Constructer 
    # def __init__(self, opt, temp):
    #     self.opt = opt
    #     self.temp = temp

    def calc(self,opt,temp): 
        if opt == 1:
            print("In farenheit:")
            return temp*(9/5)+32
        else:
            print("In celsius: ")
            return (temp-32)*(5/9)