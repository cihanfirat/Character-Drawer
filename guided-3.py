#MAKING HEAD FIRST(fixed characters are - /\ and | user must choose hair and eye here)
def print_head(hair, eye):

    print(hair*12)
    print(hair + "|        |"+hair)
    print(hair + "|  " + eye +  "  " + eye +"  " "|" + hair)
    print(" |   /\   |")
    print(" |        |")
    print(" \  '--'  /")
    print("   ------")
#DRAWING BODY PART(fixed characters are X and # user should choose arm)
def print_body(height_setter, arm):

    print("     XX")
    print("#" + arm*4 + "XX" + arm*4 + "#")
    i=0
    while i< height_setter:
        print("    XXXX")
        i+=1
#REVERSING OTHER SHOE
def reverse_shoe(shoe_string):

    str = ""
    for i in shoe_string:
        str = i + str
    return str
#LEG PRINTING (it has helmet also, don't need extra character for helmet or legs. they are fixed)
def print_legs(height_setter, shoe):

    print("    ===")
    i=0
    while i<height_setter:
        print("   ||  ||")
        i+=1
    print(shoe + "   " + reverse_shoe(shoe))
#MAIN FUNCTION TO CALL AND PRINT ALL OF THEM IN ONCE
def main():
    print("Welcome to Character Creator! Please Enter the Followings.")
    height=int(input("Overall Character Height: "))
    hair=input("Character for the hair :")
    eye=input("Character for the eye: ")
    arm=input("Character for the arm :")
    shoe=input("Character for the shoe :")
    #Heigh setter for overall body.(if we don't use this formula body parts ,such as legs, will be too long)
    height_setter=(height-11)//2
    print_head(hair,eye)
    print_body(height_setter, arm)
    print_legs(height_setter,shoe)

main()

    

