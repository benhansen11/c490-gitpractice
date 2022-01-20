import my_object

class MyDerivedObject(my_derived_object.MyObject):

    def __init__(self):
        super().__init__()

    def __srt__(self):
        return self.greeting  
