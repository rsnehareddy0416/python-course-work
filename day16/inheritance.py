'''class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f"Hey {self.username},Welcome to the Instagram!!!")
komali=Instagram('Komali','klmn@2004')
sneha=Instagram('Sneha','sneha@123')'''

#single inherirance
#multiple inheritance
#multilevel inheritance
#hierarcial inheritance
#hybrid inheritance

class InstagramV1:
    def __init__(self,username):
        self.username=username
        print(f"Hey {self.username},Welcome to the Instagram")
    def reels(self):
        print("You can upload and scroll the reels")
    def posts(self):
        print("You can post your pics")

class InstagramV2(InstagramV1):
    def __init__(self,username):
        super().__init__(username)
    def story(self):
        print("You can upload stories")
class InstagramV3(InstagramV2):
    def __init__(self,username):
        self.username=username
        super().__init__(username)
    def note(self):
        print("You can upload a note")
class Live:
    def launchlive(self):
        print("Now you can go to live")
class verification:
    def verify(self):
        print("You can verify the account for better feature")
class InstagramV4(InstagramV3,Live,verification):
    def __init__(self,username):
        super().__init__(username)
class Creator(InstagramV4):
    def __init__(self,username):
        super().__init__(username)
    def insights(self):
        print("You can check your post insights")
class Business(Creator):
    def __init__(self,username):
        super().__init__(username)
    def buttons(self):
        print("You can contact them mail and number")
    
        
komali=InstagramV1('Komali')
komali.reels()
komali.posts()

sneha=InstagramV2('Sneha')
sneha.reels()
sneha.posts()
sneha.story()

rishika=InstagramV3('Rishika')
rishika.reels()
rishika.posts()
rishika.story()
rishika.note()

bhavana=InstagramV4('Bhavana')
bhavana.reels()
bhavana.posts()
bhavana.story()
bhavana.note()
bhavana.launchlive()
bhavana.verify()

swathi=Business('Swathi')
swathi.reels()
swathi.posts()
swathi.story()
swathi.note()
swathi.launchlive()
swathi.verify()
swathi.insights()
swathi.buttons()



