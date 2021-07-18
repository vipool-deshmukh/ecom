num = 10
num = 20

def m1():       # m1 is a reference to funtion object
    pass

m1()        #

class Book:

    def __init__(self,bkid):        #__init__           1x
        self.bookId = bkid

    def __init__(self,bkid,bkname): #__init__           2x
        self.bookId =bkid
        self.bookName = bkname

    def show_book_publication(self):        #show_book_publication
        print('inside show publication')



a  = Book(101,"AA")     # init la call --> object --#error       # bydefault --   def __init__(self):
a.show_book_publication()   #obj thru                                          pass

val  = 10           # val - variable
                    # type -- int
                    #scope --> global

class Employee:     #class --> structure --> for my business purpose
                    # properties + behaviours --> states--variables --> behaviours-- methods

    def __init__(self,eid,enm,eag,esal,erole):      # constructor --> to initialize object properties
        self.empId = eid                            # whichever created thru --- self.fields--> instance/object properties
        self.empName = enm                          #self -- current object ref -->
        self.empAge = eag                           #params --> local variables
        self.empSalary = esal
        self.empRole = erole

     #Employee()        # call kartoy -- employee class-> init -->
e1 = Employee(101,"Mr. XXXX", 44,52898.23,'Manager')    #e1 -- defined at module--
e2 = Employee(102,"Mr. YYYY", 24,2898.23,'Cashier')     #
                    # e1 and e2 -- objects ahet -- of class Employee
                    # e1 and e2 - scope --> complex
                    # e1 and e2 -- are complex employee type
                    #e1 --> 5
                    #e2 --> 5


print(e1.empId) # 101
print(e2.empRole)#cashier

def m1():   #
    print('inside m1')

def m2():
    print('inside m2')


def addition(num1,num2):        # addition ---> ref -- function type chya object ch
    print(num1 + num2)

def substraction(num1,num2):
    print(num1 - num2)


addition(10,20) # caller to the
substraction(20,10)


print(type(e1) == type(e2))     #   same --> employee - user
                                # this is not the generic--> business specific

num1 =10
num2 = 20
print(type(num1) == type(num2)) # same  --> int ----> python defined
                            # int type lagel..
                            