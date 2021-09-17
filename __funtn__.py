from dic import Science
from dic import Maths
from dic import descpt

def mt(a):
     """This Function Will connect u to Maths Dictonery"""
     while(True):
        print(f"\nSubject : {a}")
        take2 = input("\n\tName of Formula : ")
        
        if take2 in Maths and take2 in descpt:
           print(f"\n\tFormula of {take2} : {Maths[take2]}")

        elif take2 not in Maths and take2 in Science:
            print("\n\tThis Formula is in Science column.")

        elif take2 not in descpt and take2 in Maths:
            print(f"\n\tFormula of {take2} : {Maths[take2]}")
            print("\n\tNo Description Available.")

        elif take2 == "exit":
            exit()

        else:
           print("\nFormula Not Found.")
           print("\n\t* Check the first letter of Formula is Capital or not.")
           print("\n\t* Recheck the spelling of Formula.")
           continue
        dec = input("\nPress (y) to continue or (n) to exit. : ")
        if dec == "n":
            break

        elif dec == "Y" or "y":
           continue

     end = "\nMain Menu"
     return end
     

def sci(a):
    """This Function Will connect u to Science Dictonery"""
    while(True):
        print(f"\nSubject : {a}")
        take2 = input("\n\tName of Formula : ")
        
        if take2 not in descpt and take2 in Science:
            print(f"\n\tFormula of {take2} : {Science[take2]}")
            print("\n\tNo Description Available.")
        
        elif take2 not in Science and take2 in Maths:
            print("\nThis Formula is in Maths Column")
           
        elif take2 in Science and descpt:
            print(f"\n\tFormula of {take2} : {Science[take2]}")
            print(descpt[take2])

        elif take2 == "exit":
            exit()

        else:
           print("\nFormula Not Found.")
           print("\n\t* Check the first letter of Formula is Capital or not.")
           print("\n\t* Recheck the spelling of Formula.")
           continue
        dec = input("\nPress (y) to continue or (n) to exit. : ")
        if dec == "n":
            break

        elif dec == "Y" or "y":
           continue

    end = "\nMain Menu"
    return end
     