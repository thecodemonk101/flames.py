 #import tkinter and all its functions
from tkinter import *

def remove_match_char(name1,name2) :

    for i in range(len(name1)):
         for j in range(len(name2)):

             if ( name1[i] == name2[j] ):
                 c = name1[i]

                 name1.remove(c)
                 name2.remove(c)

                 name3 = name1 + ["*"] + name2
                 return[name3, True]


    name3 = name1 + ["*"] + name2
    return [ name3, False ]

def status():
    # take a 1st player name from Player1_field entry box
    p1 = Player1_field.get()

    # converted all letters into lower case
    p1 = p1.lower()

    # replace any space with empty string
    p1.replace(" ", "")

    # make a list of letters or characters
    p1_list = list(p1)

    #same for Person2

    p2 = Player2_field.get()
    p2 = p2.lower()
    p2.replace(" ","")
    p2_list = list(p2)

    proceed = True

    # keep calling remove_match_char function
    # untill common characters is found or
    # keep looping untill proceed flag is False

    while proceed:

        ret_list = remove_match_char(p1_list , p2_list)

        con_list= ret_list[0]

        proceed = ret_list[1]

        star_index = con_list.index("*")

        p1_list= con_list[:star_index]
        p2_list= con_list[star_index+1:]

    count= len(p1_list) + len(p2_list)

    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]


    while len(result) > 1 :

        # store that index value from
        # where we have to perform slicing.
        split_index = (count % len(result) - 1)

        # this steps is done for performing
        # anticlock-wise circular fashion counting.
        if split_index >= 0 :

            # list slicing
            right = result[split_index + 1 : ]
            left = result[ : split_index]

            # list concatenation
            result = right + left

        else :
            result = result[ : len(result) - 1]

    # insert method inserting the
        # value in the text entry box.
    Status_field.insert(10, result[0])

# Function for clearing the
# contents of all text entry boxes
def clear_all() :
    Player1_field.delete(0, END)
    Player2_field.delete(0, END)
    Status_field.delete(0, END)

    # set focus on the Player1_field entry box
    Player1_field.focus_set()

# Driver code
if __name__ == "__main__" :

    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background = 'light blue')

    # Set the configuration of GUI window
    root.geometry("500x325")

    # set the name of tkinter GUI window
    root.title("Play the Flame")

    # Create a Player 1 Name: label
    label1 = Label(root, text = "Enter your  Name: ",
                   fg = 'black', bg = 'green')

    # Create a Player 2 Name: label
    label2 = Label(root, text = "Your Flame Name: ",
                   fg = 'black', bg = 'green')

    # Create a Relation Status: label
    label3 = Label(root, text = "Relationship Status: ",
                   fg = 'black', bg = 'yellow')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    label1.grid(row = 2, column = 2, sticky ="E")
    label2.grid(row = 3, column = 2, sticky ="E")
    label3.grid(row = 5, column = 2, sticky ="E")

    # Create a text entry box
    # for filling or typing the information.
    Player1_field = Entry(root)
    Player2_field = Entry(root)
    Status_field = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    # ipadx keyword argument set width of entry space .
    Player1_field.grid(row = 2, column = 3, ipadx ="50")
    Player2_field.grid(row = 3, column = 3, ipadx ="50")
    Status_field.grid(row = 5, column = 3, ipadx ="50")

    # Create a Submit Button and attached
    # to tell_status function
    button1 = Button(root, text = "Submit", bg = "red",
                     fg = "black", command = status)

    # Create a Clear Button and attached
    # to clear_all function
    button2 = Button(root, text = "Clear", bg = "red",
                     fg = "black", command = clear_all)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    button1.grid(row = 4, column = 3)
    button2.grid(row = 6, column = 3)

    # Start the GUI
    root.mainloop()
