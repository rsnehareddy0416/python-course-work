class Flipkart:
    discount=10
    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount=newdiscount
    #instancemethod
    def userinfo(self,name,phno):
        self.name=name
        self.phno=phno
        print(f'Username:{self.name}')
        print(f'Phone number:{self.phno}')
    @staticmethod
    def banner():
        print("Welcome to the flipkart\n10% discount is going on,shop now")


komali=Flipkart()
#call instance method by object
komali.userinfo('Komali',9870654567)

komali.updatediscount(30)
#call class method by object or class name
Flipkart.updatediscount(40)

komali.banner()
#call static method by object
Flipkart.banner()

sneha=Flipkart()
sneha.userinfo('Sneha',6578902345)
rishika=Flipkart()
rishika.userinfo('Rishika',9895678900)