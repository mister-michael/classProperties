class Student():

    def __init__(self):
        
        @property
        def first_name(self):
            try:
                return self.first_name
            except AttributeError:
                return "Student has no first name"

        @first_name.setter
        def first_name(self, first):
            if type(first) is str:
                self.first_name = first
            else:
                raise TypeError('please enter a string value for first_name')
        
        @property
        def last_name(self):
            try:
                return self.last_name
            except AttributeError:
                return "Student has no last name"

        @last_name.setter
        def last_name(self, last):
            if type(last) is str:
                self.last_name = last
            else:
                raise TypeError('please enter a string value for first_name')

        @property
        def age(self):
            try:
                return self.age
            except AttributeError:
                return "Student has no Age"

        @age.setter
        def age(self, age):
            if type(age) is int:
                self.age = age
            else:
                raise TypeError('please enter age as integer')

        @property
        def cohort(self):
            try:
                return self.cohort
            except:
                return 'student is not assigned to a cohort'
        
        @cohort.setter
        def cohort(self, cohort_number):
            if type(cohort) is int:
                self.cohort = cohort_number
            else:
                raise TypeError('cohort must be an integer')
        
        @property
        def full_name(self):
            try:
                return f"{self.first_name} {self.last_name}"
            except AttributeError:
                return 'first or last name not entered'
        
        @full_name.setter
        def full_name(self, name):
            return 'full_name property is read only'

        
