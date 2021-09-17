from __funtn__ import mt
#print(mt.__doc__)
from __funtn__ import sci
#print(sci.__doc__)


print("Formula Finder")
print("\tBuild By Matang Mehra")

#Select Subject
list = ["\n1. Science", "2. Maths"]
print("\nMain Menu")

while(True):
    for item in list:
           print(item)
    print("\nTo exit Press 0.")
    take = int(input("\nSelect Subject : "))
    
    if take == 1:
       print(sci("Science"))
       
    elif take == 2:
        print(mt("Maths"))
        
    elif take == 0:
        exit()

    elif take == "exit":
        exit()

