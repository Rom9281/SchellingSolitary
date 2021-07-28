# Developped by Romain GAUD

# Exercice from INFORMATIQUE de Nicolas Audfray & others, DUNOD

# Started on 27/07/2021

# _____________________   IMPORT   _______________________

# System
import os,sys,time
import multiprocessing as mp

# Exterior
import tkinter as tk

# Own libraries
from functions import *
from classes import *

# _____________________   PROCESS TARGET   _____________________

def process_target(process_id,first_zone,last_zone,zones_in_line,boxes_array):
    pass
    # Initialisation:
    for num_line in range(first_zone,last_zone):
        for num_col in range(zones_in_line):
            # For each element in the processes area
            boxes_array[num_line][num_col].set_process_id(process_id) # attribute to a process 
            
            # verifying each neighbor
            delta_line = -1
            delta_col = -1

            for nei_num in range(8):
                if nei_num < 3:
                    delta_col +=1

                elif nei_num == 3:
                    delta_line += 1
                    delta_col = -1

                elif nei_num == 4:
                    delta_col = 1
                
                elif nei_num == 5:
                    delta_col = -1
                    delta_line += 1

                else:
                    delta_col += 1
                
                nei_line = delta_line+num_line
                nei_col = delta_col+num_col

                if nei_line < 0:
                    nei_line = zones_in_line-1
                elif nei_line > zones_in_line-1:
                    nei_line = 0
                
                if nei_col < 0:
                    nei_col = zones_in_line-1
                elif nei_col > zones_in_line-1:
                    nei_col = 0
                
                boxes_array[num_line][num_col].add_neighbors((nei_col,nei_line))

            pass
            
    # BOUCLE :
    while True:
        pass
    # 1. Modification du statut

    # 2. Modification du physique
# ________________________   VARIABLES   _______________________


# Field Parameters
# ________________

zones_in_line = 70
zones_number = zones_in_line**2
boxes_array = generate_field_list(zones_in_line)

# Tk related variables
# ____________________

window_len = 700 #In pixels
window = tk.Tk() #Main window
canvas = tk.Canvas(window,width=window_len,height=window_len) # Defining the canvas

# Multiprocessing related variables
# _________________________________

num_process = optimal_num_process(zones_in_line)



# ===============================   PROGRAM   =================================

window.geometry("%sx%s"%(window_len,window_len)) # Defining window geo

canvas.pack()

generate_field(canvas,window,zones_in_line,window_len,boxes_array)

window.mainloop() # Tk mainloop