class Met:

    int=10
    @staticmethod                      # To make a method static we need "@staticmetod" decorator. No need to add self or cls as argument
    def hello(string):
        print('This is', string)

    @classmethod                       # To make a method class method we need "@classmethod" decorator. cls is needed instead of self.
    def hi(cls):
        cls.int=20
        print('Number is', cls.int)

Met.hello('Archana')
Met.hi()