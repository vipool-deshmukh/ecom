

class X:

   def init(self):                 # def __init__(self)    -->
        print('inside __init')

a = X()    # __init__      -- ?? -- no --> ()
a.init()  #
print(a)
import sys
sys.exit(0)


#memory allocation -- sequentially
#class/methods/functions-->execution --> the way we call to them
    #class-- object
    #methods- -> object
    # function


    #class/methods/function- -> callable

    #methods --> class/object chi

    #function --> function name thru call


    #method --. associated car
    #function


def start_car(car):  # start_car        --> is a reference to the start_car --function cha
    print('Car is starting')


class Car:

    def __init__(self,carId,carModel,carPrice):
        self.carId = carId
        self.carModel = carModel
        self.carPrice = carPrice

    def start_car(self):    #method
        print('Car is starting')

    def stop_car(self):
        print('Stop car..')

    def fill_fuel(self,type):
        if type == 'D':
            print('Filling diesel ')
        elif type=='P':
            print('Filling Petrol ')

car = Car(carId=101,carModel='XX',carPrice=12892)
car.start_car()
car.stop_car()
car.fill_fuel('D')





print('sample module started')

def m1():
    print('line1')
    print('line2')

print('m1-->',m1)

def m2():
    print('line3')
    print('line4')

print('m2-->',m2)

def m3():
    print('line5')
    print('line6')
print('m3-->',m3)

def m4():
    print('line7')
    print('line8')
    print('line9')

print('m4-->',m4)
print('sample module completed')

m2()
m2()
m2()
m4()
m4()
#top to down --> procedural code
'''
Types of method
Types of variables
Types

'''