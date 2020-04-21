class Student():

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, first):
        if type(first) is str:
            self.__first_name = first
        else:
            raise TypeError('please enter a string value for first_name')
    
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, last):
        if type(last) is str:
            self.__last_name = last
        else:
            raise TypeError('please enter a string value for first_name')

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError('please enter age as integer')

    @property
    def cohort(self):
        try:
            return self.cohort
        except:
            return 0
    
    @cohort.setter
    def cohort(self, cohort_number):
        if type(cohort) is int:
            self.__cohort = cohort_number
        else:
            raise TypeError('cohort must be an integer')
    
    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return 0
    
    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in Cohort {self.cohort}"


mike = Student()
mike.first_name = "Mike"
mike.last_name = "Ellis"
mike.age = 35
mike.cohort_number = 39

print(mike)

        
