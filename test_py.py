class ABC:
    
    @classmethod
    def p(cls):
        print("P")

    def hello(self):
        ABC.p()

ob = ABC()
ob.hello()