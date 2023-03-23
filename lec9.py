'''
lec9
define class
'''
class car:
    maker = 'toyota'
    
    #def report_maker(self):
        
    #    return self.maker
    def __init__(self,input_model):
        self.model = input_model
    def report(self):
        return self.maker,self.model
my_camry = car('camry')
print(my_camry.maker)
print(my_camry.model)
print(my_camry.report())

my_camry.maker='Ford'
print(my_camry.report())
        