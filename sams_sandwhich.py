#Sams Sandwhich Ordering menu
import datetime  #imports datetime 

#Validates the input of the number to be between lower and upper variables, with only valid numbers.
def force_number(message,lower,upper):
    while True:
        try:
            num=int(input(message))
            if num>=lower and num<=upper:   #if number is between lower and upper it continues or gives error statement
                return num
            else:
                print(f"Invalid number, please enter between {lower} - {upper}")
        except:         #except statement; if everything is invalid
            print("Error - only type in numbers please")

#validates the input of a name, name must be between lower and upper character length.
def force_name(message,lower,upper): 
    while True: #this is an infinite loop
        name = str(input(message)).title() #asks for the user to enter their name, adds capital letter
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            return name #returns a valid name back to the variable that called the function
        else:
            print("Invalid name, enter in 2-15 valid characters")
        
#validates the cellphone number input; checks length between lower and upper variables, and inputted data is all numbers
def force_cellphone_number(message,lower,upper):
    while True:
        cell=str(input(message))
        if len(cell)>=lower and len(cell) <=upper and cell.isnumeric(): #checks length of cellphone and is a number
            break
        else:
            print(f"ERROR! Please enter {lower} - {upper} valid numbers") #error message
    return cell

#bread selection menu
def bread_selection(): #lets user select bread
    bread_list = ["White","Brown","Italian","Flatbread"] 
    count=0
    print("We have the following breads: ")
    while count < len(bread_list): #prints out each item on the list 
        print(count+1," ", bread_list[count])
        count+=1
    bread_selected=force_number("What bread do you want?: ",1,len(bread_list)) #uses force_number to validate entered number.
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
    salad_list = ["Lettuce","Tomato","Carrot","Cucumber","Onions","None"]
    count = 0
    print("We have the following salads, you can have as many as you want")
    while count <len(salad_list):
        print(count+1," ",salad_list[count])
        count +=1
    salad_choice = [] #empty list to hold selected salads
    while True:
        salad_options=force_number("What number salad do you want?",0,len(salad_list))
        salad_choice.append(salad_list[salad_options-1]) #adding selected salad to the list
        print(f"Your selected salads are {salad_choice} \nPress 0 to exit.")
        if salad_options==6 or salad_options==0:
            break
    return ", ".join(salad_choice) #returns a string formatting the selected options

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
first_name=force_name("What is your first name?",2,15)
cell_phone=force_cellphone_number("What is your cellphone number?",7,15)
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

