# Visitor Management System by Gerson joshua dbitnrb212220:DBT1303

# Pseudocode for the process when the visitor enters the premisses

#STEP 1

# Taking of details of visitors at the gate:
name = float
house_Owner = float
Arival_time= string

name =input(" Enter your name: ")
house_owner = input(" Enter the house number:")
Arival_time = input("Enter your expected time (use dots):")

print ("Hello" + name  + "you are here top visit " + house_owner + "at" + Arrival_time)


#STEP 2

#Security checks with the house owner if he was expecting any guest without mentioning names

is_expected= True
is_nameknown= True

if is_expected or is_nameknown:
print( "Hi" + name + " , you are welcomed to wait for " + house_owner)

elif is_expected and not (is_nameknown)
print(+ name +"you are expected but not fully known by host");

elif not (is_expected) and is_nameknown but name given
print ( + name +"you were not expected but the host geussed it was you coming")

else: 
print(+ name + "kindly note that you  cannot proceed ,kindly come another day when expected")

#step3

'''for the visitors that were either expected or allowed to wait are  requested to give a visitation code'''

# This visitation Code verification by security and hosts.

#Password confirmation

class code number
def_int_(self,number,min=0,max=100):

self.number=number
selfcode=0
self.min=mn
self.max=mx

def get_code(self):
   code=input(f"please enter 2 number code({self.min}-{self.max}):)
              if self.valid_number(code):
                 return int(code)
else:
print("dear" + name + "please enter a valid code:")
return self.get_code()

def valid_number(self,str_number):
   try:
      number=int(str_number)
      expect:
      return False
   return self.min <=number<=self.max
def play(self):
   while True:
      self.code += 1
       code = self.get_code()
       if code < self.number:
          print("Dear" + name + "your try was the correct expected figures ,You are welcomed to visit")
           elif code > self.number
           print("Dear" + name +"your try was over the expected figure")
       else:
          break
       print(f" you enter it in {self.code} times.")
   game= Enter code (66 , 0 , 100)
game.play()

game= Enter code (86 , 0 , 100)
game.play()






