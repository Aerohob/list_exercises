class Todo:
    # instructions for how to construct
    # a new Todo object
    # Use the __init__() to create instances
    # of the Todo class
    # this method is known as the constructor
    # 'dunder init' - 'double underscore init'
    def __init__(self, title, completed=False):
        #assume that a new todo is not already completed
        #so we set the default value to false
        self.title = title
        self.completed = completed
    
    #examples of "Encapsulation", meaning to hite the details of how your code works
    #you present an interface to anybody using your code, but don't require them to know those details

    def update_title(self, new_title):
        if self.title != new_title:
            self.updated_on = '2019-11-18'
            #whatever the current date is
        self.title = new_title   

    def update_completed(self, new_completed):
        self.completed = new_completed
        if self.completed:
            self.completed_on = '2019-11-2018'



    def display(self):
        #You must use the keyword "self" for the first argument
        #So that the argument can call the function
        #It links the function, to the object
        print(self.title)
        print(self.completed)

    def __str__(self):
        return f'{self.title} ({self.completed})'
