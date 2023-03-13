import random

x = input("How many dice to roll?(1-6) ")

def parse_input(input):
    try:
        y = int(input)
    except:
        print("Only Whole Numbers")
        exit()
    if y < 1 or y > 6:
        print("Only Numbers Between 1-6")
        exit()

face = []
def roll_dice(input):
    for x in range(int(input)):
        face.append(random.randint(1,6))

art = {  
    1: (  
        "┌─────────┐",  
        "│         │",  
        "│    ●    │",  
        "│         │",  
        "└─────────┘",  
    ),  
    2: (  
        "┌─────────┐",  
        "│    ●    │",  
        "│         │",  
        "│    ●    │",  
        "└─────────┘",  
    ),  
    3: (  
        "┌─────────┐",  
        "│ ●       │",  
        "│    ●    │",  
        "│       ● │",  
        "└─────────┘",  
    ),  
    4: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│         │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
    5: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│    ●    │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
    6: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│ ●     ● │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
}  
# count the rows of the die,which equal height
die_height = len(art[1])
# counts the amount of stuff in a single row
die_width = len(art[1][0])
# blank space to add between dice face rows
die_separator = " "


def generate_dice_faces_diagram():
    #finale is an array of the random dice face 
    finale = []
    for x in face:
        finale.append(art[x])

    
    die_face_rows = []
    # loop through every row of die height
    for row_x in range(die_height):
        row_components = []
        # nested loop to loop through each row of each die in finale array
        for die in finale:
            # adds individual row from finale die to an array
            row_components.append(die[row_x])
        #the row with all the same rows from the finale die array get joined with empty space 
        row_string = die_separator.join(row_components)
        # adds one item in below array , of all the same finale die rows joined together as a string with space between individual die faces
        die_face_rows.append(row_string)

    for x in die_face_rows:
        print(x)

    

parse_input(x)
roll_dice(x)
generate_dice_faces_diagram()