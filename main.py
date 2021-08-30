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

    # Initialisation:

    for num_line in range(first_zone,last_zone):
        for num_col in range(zones_in_line):
            
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
  
    # BOUCLE :

    while True:

        # For each block in the area
        for num_line in range(first_zone,last_zone):
            for num_col in range(zones_in_line):
                
                # getting the state of the zone
                state_array_lock.acquire()
                state_block = state_array[get_array_coord(num_line,num_col,zones_in_line)]
                state_array_lock.release()
                
                if state_block:
                    # If the state block exists

                    # Getting the color of the zone
                    color_array_lock.acquire()
                    color_block = color_array[get_array_coord(num_line,num_col,zones_in_line)]
                    color_array_lock.release()

                    # Defining the number of bad neighbors
                    bad_nei = 0

                    for nei_tuple in boxes_array[num_line][num_col].get_neighbors():
                        # getting the state of the neighbor
                        state_array_lock.acquire()
                        state_block_nei = state_array[get_array_coord(num_line,num_col,zones_in_line)]
                        state_array_lock.release()

                        if state_block_nei:
                            # Getting the color of the neighbor
                            color_array_lock.acquire()
                            color_block_neighbor = color_array[get_array_coord(nei_tuple[0],nei_tuple[1])]
                            color_array_lock.release()

                            if color_block != color_block_neighbor:
                                bad_nei += 1

                    if bad_nei > 4:
                        # If there are more than 4 bad neighbors, the person is unhappy
                        feeling_array_lock.acquire()
                        feeling_array[get_array_coord(num_line,num_col,zones_in_line)] = 0
                        feeling_array_lock.release()
                    else:
                        feeling_array_lock.acquire()
                        feeling_array[get_array_coord(num_line,num_col,zones_in_line)] = 1
                        feeling_array_lock.release()

                    


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

state_array = mp.Array('i',zones_in_line**2)
color_array = mp.Array('i',zones_in_line**2)
feeling_array = mp.Array('i',zones_in_line**2)

state_array_lock = mp.Lock()
color_array_lock = mp.Lock()
feeling_array_lock = mp.Lock()


process_list = []

for i in range(num_process):
    first_zone = int(i*zones_in_line/num_process)
    last_zone = int((i+1)*zones_in_line/num_process)
    process_list.append(mp.Process(target= process_target, args=(i,first_zone,last_zone,zones_in_line,boxes_array)))



# ===============================   PROGRAM   =================================

window.geometry("%sx%s"%(window_len,window_len)) # Defining window geo

canvas.pack()

generate_field(canvas,window,zones_in_line,window_len,boxes_array)



for i in range(num_process):
    process_list[i].start()


window.mainloop() # Tk mainloop


for i in range(num_process):
    process_list[i].join()

