"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions.

Learning objectives:
- Defining and using functions

Complete the script by filling in the missing code sections marked with <---.

@author: PLACE YOUR NAME HERE
"""

# Import any necessary libraries
import math
import os

import numpy as np

#import pandas as pd


# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(building_length, building_width, roof_angle, panel_width, panel_heignt, panel_power): # <--- include parameters for building length, width, roof angle, panel width, panel height and panel power
    """
    The function returns Total PV capacity and the number of panels that can fit on the roof.
    """
    # calculate the roof area and the number of panels fitting
    roof_area = building_length * building_width /math.cos(math.radians(roof_angle))
    nb_panels = roof_area // (panel_width * panel_heignt)
    pv_capacity = nb_panels * panel_power 

    return(pv_capacity, nb_panels)# <--- return the total PV capacity in kW and number of panels

if __name__ == "__main__":
    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    panel_width = 1.046
    panel_height = 1.690
    building_length = 31.75
    building_width = 7.5
    pv_capacity_kw, num_panels = calculate_pv_size(building_length, building_width, 22, panel_width, panel_height, 0.4) # <--- call the calculate_pv_size function with appropriate arguments



    print('PV capacity in kW :',pv_capacity_kw, 'Number of panels :', num_panels) # <--- Add a print statement to display the number of PV panels and the total PV capacity in kW
