#sams sandwhich

def bread_selection(): #lets user select bread
    bread_list = ["White","Brown","Italian","Flatbread"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list[count])
        count+=1
    bread_selected=int(input("Which bread did you want? Enter a number: "))
    return bread_list[bread_selected-1] #returns back a string

def meat_selection(): #lets user meat bread
    meat_list = ["No meat","Chicken","Pork","Ham","Meatballs","Turkey"]
    count=0
    print("We have the following meats: ")
    while count < len(meat_list):
        print(count+1," ", meat_list[count])
        count+=1
    meat_selected=int(input("Which meat did you want? Enter a number: "))
    return meat_list[meat_selected-1]

def cheese_selection(): #lets user select cheese
    cheese_list = ["No cheese","Cheddar","American","Mozzerella","Swiss"]
    count=0
    print("We have the following cheeses: ")
    while count < len(cheese_list):
        print(count+1," ", cheese_list[count])
        count+=1
    cheese_selected=int(input("Which cheese did you want? Enter a number: "))
    return cheese_list[cheese_selected-1]



def dressing_selection(): #lets user select dressing/sauce
    dressing_list = ["No dressing","Honey Musted","Garlic Aioli","BBQ Sauce","Mayonnaise","Ketchup","Sweet Chilli", "Ranch"]
    count=0
    print("We have the following dressings: ")
    while count < len(dressing_list):
        print(count+1," ", dressing_list[count])
        count+=1
    dressing_selected=int(input("Which dressing did you want? Enter a number: "))
    return dressing_list[dressing_selected-1]

#main program
print("Welcome to Sam's Sandwich Shop!")
bread_choice=bread_selection()

meat_choice=meat_selection()

cheese_choice=cheese_selection()

dressing_choice=dressing_selection()
#print statements
print(f"Your selected bread: {bread_choice}")
print(f"Your selected meat: {meat_choice}")
print(f"Your selected cheese: {cheese_choice}")
print(f"Your selected dressing: {dressing_choice}")
