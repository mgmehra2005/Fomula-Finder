from __funtn__ import mt
#print(mt.__doc__)
from __funtn__ import sci
#print(sci.__doc__)
from __funtn__ import chem
#print(chem.__doc__)


print("Formula Finder")
print("\tBuild By Matang Mehra")

#Select Subject
list = ["\n1. Physics", "2. Chemistry", "3. Maths"]
print("\nMain Menu")

while(True):
    for item in list:
           print(item)
    print("\nTo exit Press 0.")
    take = int(input("\nSelect Subject : "))
    
    if take == 1:
       print(sci("Science"))
       
    elif take == 2:
        print(chem("Chemistry"))

    elif take == 3:
        print(mt("Maths"))
        
    elif take == 0:
        exit("Good Bye!")

    elif take == "exit":
        exit("Good Bye!")

