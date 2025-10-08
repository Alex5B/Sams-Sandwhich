#sams sandwhich
import datetime

def force_number(message,lower,upper):
    while True:
        try:
            num=int(input(message))
            if num>=lower and num<=upper:
                return num
            else:
                print(f"Invalid number, please enter between {lower} - {upper}")
        except:
            print("Error - only type in numbers please")
    
def bread_selection(): #lets user select bread
    bread_list = ["White","Brown","Italian","Flatbread"]
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list
        print(count+1," ", bread_list[count])
        count+=1
    bread_selected=force_number("What bread do you want",1,len(bread_list))
    return bread_list[bread_selected-1] #returns back a string

def meat_selection(): #lets user select meat
    meat_list = ["No meat","Chicken","Pork","Ham","Meatballs","Turkey"]
    count=0
    print("We have the following meats: ")
    while count < len(meat_list):
        print(count+1," ", meat_list[count])
        count+=1
    meat_selected=force_number("Which meat did you want? Enter a number: ",1,len(meat_list)) #plugs in force number function to add boundaries
    return meat_list[meat_selected-1]

def cheese_selection(): #lets user select cheese
    cheese_list = ["No cheese","Cheddar","American","Mozzerella","Swiss"]
    count=0
    print("We have the following cheeses: ")
    while count < len(cheese_list):
        print(count+1," ", cheese_list[count])
        count+=1
    cheese_selected=force_number("Which cheese do you want? Enter a number: ",1,len(cheese_list))
    return cheese_list[cheese_selected-1]

def salads_selection():
    salad_list = ["Lettuce","Tomato","Carrot","Cucumber","Onions"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count <len(salad_list):
        print(count+1," ",salad_list[count])
        count +=1
    print("Press ENTER when you have finished chosing your salads")
    salads_added = "" #will hold a string of more than one item
    selected_salad = " " #prompts the user to enter a number in to select a salad

    while selected_salad != "":
        selected_salad = input(f"What number salad do you want?\nYou have selected: {salads_added}")
        if selected_salad != "": #if you press enter the statement wont run
            selected_salad = int(selected_salad)
            #this variable keeps adding on each selected item from salad list
            salads_added = salads_added + " " + salad_list[selected_salad-1]
    return salads_added.strip() #removes empty space at start of the string


def dressing_selection(): #lets user select dressing/sauce
    dressing_list = ["No dressing","Honey Musted","Garlic Aioli","BBQ Sauce","Mayonnaise","Ketchup","Sweet Chilli", "Ranch"]
    count=0
    print("We have the following dressings: ")
    while count < len(dressing_list):
        print(count+1," ", dressing_list[count])
        count+=1
    dressing_selected=force_number("Which dressing did you want? Enter a number: ",1,len(dressing_list))
    return dressing_list[dressing_selected-1]

def output_textfile(first_name,cell_phone,sandwhich_order):
    date_time=datetime.datetime.now()
    outF=open("sams_sandwhich.txt","a")#opening up a new file
    print(f"\n*** Order for {first_name} - {cell_phone}: ***")
    for item in sandwhich_order:
        outF.write((item))#printing each item in the list to the console
        outF.write("\n")
    outF.write(f"\nEnd of order: {date_time}")
    outF.write(f"\n*****************************")
    print(f"***End of order: {date_time} ***")
    outF.write("\n")
    outF.write("\n")
    outF.close()#closes off text file
    #once the file prints, it goes back to the menu



#main program
first_name=str(input("What is your first name?"))
cell_phone=str(input("What is your cellphone number?"))
bread_choice=bread_selection()
meat_choice=meat_selection()
cheese_choice=cheese_selection()
salad_choice=salads_selection()
dressing_choice=dressing_selection()

sandwhich_order=[] #empty list to append order to

sandwhich_order.append(f"\n\n***********************************")
sandwhich_order.append(f"*** Order for {first_name} - {cell_phone} ***\n")
sandwhich_order.append(f"Bread: {bread_choice}")
sandwhich_order.append(f"Meat: {meat_choice}")
sandwhich_order.append(f"Cheese: {cheese_choice}")
sandwhich_order.append(f"Salad(s): {salad_choice}")
sandwhich_order.append(f"Dressing: {dressing_choice}")
output_textfile(first_name,cell_phone,sandwhich_order)

print(f"Your selected bread: {bread_choice}")
print(f"Your selected meat: {meat_choice}")
print(f"Your selected cheese: {cheese_choice}")
print(f"Your selected salad(s): {salad_choice}")
print(f"Your selected dressing: {dressing_choice}")

