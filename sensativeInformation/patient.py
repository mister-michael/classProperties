class Patient:

    def __init__(self, ssn, dob, insurance_acct_number, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__account_num = insurance_acct_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address 
    
    @property
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
           return 'ssn error'

    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return 0
 
    @property
    def full_name(self):
        try:
            return  f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0

    @property
    def account_num(self):
        try:
            return self.__account_num
        except AttributeError:
            return 0
    
    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0
    
    @address.setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError('address must be a string')
    
cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

print(cashew.full_name)