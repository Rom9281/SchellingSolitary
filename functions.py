from tkinter import Canvas


# Imports
import random
import classes


# _____________________________   FUNCTIONS   __________________________________
def optimal_num_process(zones_in_line):
    """Determines the optimal number of processes"""
    num_proc = 9
    not_found = True

    while not_found:
        if zones_in_line%num_proc == 0:
            not_found = False # If the number of prox is a multiple of zones_in_list
        else:
            num_proc -= 1
    
    return num_proc

def generate_field_list(zones_in_line):
    """Generates the array containing all the objects"""
    ret_list = []

    for i in range(zones_in_line):
        ret_list.append([classes.box() for x in range(zones_in_line)])
    
    return ret_list

def generate_field(canvas,window,zones_in_line,window_len,boxes_array):
    '''Generates the zones on the canvas and adds the changes to the array of boxes'''
    step = window_len/zones_in_line

    for line_num in range(zones_in_line):
        for col_num in range(zones_in_line): 

            rand = random.randint(0,2) # Random generation of the color
            if rand == 0:
                color = 'black'
                boxes_array[col_num][line_num].set_full() # The box is full
                boxes_array[col_num][line_num].set_black() # the box is white

            elif rand == 1:
                color = "white"
                boxes_array[col_num][line_num].set_full() # The box is full
                boxes_array[col_num][line_num].set_black() # the box is white

            else:
                color = "grey"
                boxes_array[col_num][line_num].set_full() # The box is empty

            zone = canvas.create_rectangle(col_num*step,line_num*step,(col_num+1)*step,(line_num+1)*step,outline="black",fill = color)
