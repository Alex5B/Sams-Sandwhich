#Sams Sandwhich Ordering menu. Allows user to create a sandwhich with the order outputted to a seperate text file.
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

def print_lists(list,item): #creates a function which condences code length by removing repeated lines of printing code
    count = 0
    print(f"We have the follwing {item};")
    while count < len(list):               #prints out all available options of the food
        print(count+1," ",list[count])
        count+=1
    return  #returns variable


#bread selection menu
def bread_selection(): #lets user select bread
    bread_list = ["White","Brown","Italian","Flatbread"] 
    print_lists(bread_list,"breads")
    bread_selected=force_number("What bread do you want?: ",1,len(bread_list)) #uses force_number to validate entered number.
    return bread_list[bread_selected-1] #returns back a string

def meat_selection(): #lets user select meat
    meat_list = ["No meat","Chicken","Pork","Ham","Meatballs","Turkey"]
    print_lists(meat_list,"meats")
    meat_selected=force_number("Which meat did you want? Enter a number: ",1,len(meat_list)) #plugs in force number function to prevent code breaking
    return meat_list[meat_selected-1]

def cheese_selection(): #lets user select cheese
    cheese_list = ["No cheese","Cheddar","American","Mozzerella","Swiss"]
    print_lists(cheese_list,"cheeses")
    cheese_selected=force_number("Which cheese do you want? Enter a number: ",1,len(cheese_list))  #plugs in force number to prevent breaking
    return cheese_list[cheese_selected-1]

def salads_selection(): #function allows for salad selection, of which multiple are allowed
    salad_list = ["Lettuce","Tomato","Carrot","Cucumber","Onions","None"]
    print_lists(salad_list,"salads")
    salad_choice = [] #empty list to hold selected salads
    while True: #allows for looping the salad choosing option so user can pick multiple salads
        salad_options=force_number("What number salad do you want?",0,len(salad_list))
        salad_choice.append(salad_list[salad_options-1]) #adding selected salad to the list
        print(f"Your selected salads are {salad_choice} \nPress 0 to exit.")
        if salad_options==6 or salad_options==0: #both options work and allow user to exit out of while true loop
            break
    return ", ".join(salad_choice) #returns a string formatting the selected options

def dressing_selection(): #lets user select dressing/sauce
    dressing_list = ["No dressing","Honey Musted","Garlic Aioli","BBQ Sauce","Mayonnaise","Ketchup","Sweet Chilli", "Ranch"]
    print_lists(dressing_list,"dressings")
    dressing_selected=force_number("Which dressing did you want? Enter a number: ",1,len(dressing_list))
    return dressing_list[dressing_selected-1]

def output_textfile(first_name,cell_phone,sandwhich_order): #function allows for outputting final order in a formatted display in a text file
    date_time=datetime.datetime.now() #gathers the date from when the order is finalised
    outF=open("sams_sandwhich.txt","a")#opening up a new file
    print(f"\n*** Order for {first_name} - {cell_phone}: ***")
    for item in sandwhich_order: #prints out each item appeneded to sandwhich_order
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

#appends all necessary parts to create a formatted display in notepad
sandwhich_order.append(f"\n\n***********************************")
sandwhich_order.append(f"*** Order for {first_name} - {cell_phone} ***\n")
sandwhich_order.append(f"Bread: {bread_choice}")
sandwhich_order.append(f"Meat: {meat_choice}")
sandwhich_order.append(f"Cheese: {cheese_choice}")
sandwhich_order.append(f"Salad(s): {salad_choice}")
sandwhich_order.append(f"Dressing: {dressing_choice}")
output_textfile(first_name,cell_phone,sandwhich_order)

#prints out selected options to the terminal
print(f"Your selected bread: {bread_choice}")
print(f"Your selected meat: {meat_choice}")
print(f"Your selected cheese: {cheese_choice}")
print(f"Your selected salad(s): {salad_choice}")
print(f"Your selected dressing: {dressing_choice}")

