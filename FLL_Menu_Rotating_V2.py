from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Direction, Port, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu, run_task

# Import run functions
from Unearthed_Run_1 import Run_1, Run_3, Run_4
from Unearthed_Run_2 import Run_2
# Main Program starts here
# Set up all devices
Robocrafters_Hub1 = PrimeHub()
Col_Sens = ColorSensor(Port.D)
Dist_Sens = UltrasonicSensor(Port.C)
Left_Mot = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Right_Mot = Motor(Port.F, Direction.CLOCKWISE)
Left_AD = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Right_AD = Motor(Port.E, Direction.COUNTERCLOCKWISE)
Robot_1 = DriveBase(Left_Mot, Right_Mot, 62, 97)

# Assign center button in the hub as STOP button
Robocrafters_Hub1.system.set_stop_button(Button.CENTER)

# List of Programs
programs = ["1", "2", "3", "4"]

def get_last_selection():
    # Read the last run number (route) stored in memory
    last_Selection = [v for v in Robocrafters_Hub1.system.storage(0, read=1)]
    # Return the last selection or default to "1" if not found
    return str(last_Selection[0]) if last_Selection and str(last_Selection[0]) in programs else "1"

def update_last_selection(selected):
    # Write the last selected run number to memory
    val = ord(selected) - ord("0")
    write_value = [val]
    Robocrafters_Hub1.system.storage(0, write=bytes(write_value))

def create_rotated_menu(last_selection):
    # Get the index of the last selection
    start_index = programs.index(str(last_selection))
    # Rotate the menu items based on the last selection
    return programs[start_index + 1:] + programs[:start_index + 1]

def stopEverything():
    Robot_1.use_gyro(False)
    Left_Mot.stop()
    #wait(250)
    Right_Mot.stop()
    #wait(250)
    Left_AD.stop()
    #wait(250)
    Right_AD.stop()
    #wait(250)
# Use variables defined in setup above to pass inputs to the Task blocks defined in main program 
def run_selected_program(selected):
    try:
        if selected == "1":
            result = Run_1(Robocrafters_Hub1, Robot_1, Left_AD, Right_AD)
            print(f"Result: {result}")
        elif selected == "2":
            result = Run_2(Robocrafters_Hub1, Robot_1, Left_AD, Right_AD)
            print(f"Result: {result}")
        elif selected == "3":
            result = Run_3(Robocrafters_Hub1, Robot_1, Left_AD, Right_AD)
            print(f"Result: {result}")
        elif selected == "4":
            result = Run_4(Robocrafters_Hub1, Robot_1, Left_AD, Right_AD)
            print(f"Result: {result}")
        
    except BaseException as menuException:
        print(menuException)
        print("Program execution stopped due to an error")
    finally:
        stopEverything()

def main():
    while True:
        last_selection = get_last_selection()
        menu_items = create_rotated_menu(last_selection)
        selected = hub_menu(*menu_items)
        
        run_selected_program(selected)
        update_last_selection(selected)
        
        print("Program execution completed")
        wait(500)  # Wait before returning to menu
main()
