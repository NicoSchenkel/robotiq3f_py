# Import necessary libraries
from robotiqcontrol.GripperController import GripperController
import time

modes = ["Basic", "Pinch", "Wide", "Scissor"]

def main():

# Initialize the GripperController object with the IP address of the server
    gripper = GripperController("192.168.1.11")
    #gripper.activate()
   
    # Activate the gripper
    
    print('Starting')
    # Set up the initial parameters for the gripper command
    target_position = [10, 20, 11]  # Desired finger positions
    speed = [200, 200, 200]  # Speed of the movement
    force = [250, 250, 250]  # Force applied by the fingers


    for pos in modes:
    # Select gripper mode - options: "Basic", "Wide", "Pinch", "Scissor"
        mode = pos
        
        # Define if individual finger control is required
        individual_control = False

        # If individual control is not required, replicate the first element across the list
        target_position = [target_position[0]] * 3 if not individual_control else target_position
            
        # Send command to the gripper with the specified parameters
        gripper.command_gripper(rPRA=target_position, rSP=speed, rFR=force, rMOD=mode, rICF=individual_control)
        print('get into position')
        # Wait for the gripper to reach the target positions
        while ([gripper.FingerA_Position, gripper.FingerB_Position, gripper.FingerC_Position] != target_position):
            time.sleep(0.1)
            
        print(f'{mode} reached')
        # Output the current finger positions
    #while 1:
           # print(f"FingerA_Position: {gripper.FingerA_Position} FingerB_Position: {gripper.FingerB_Position} FingerC_Position: {gripper.FingerC_Position}")
            #time.sleep(1)
    '''
    # # # Update the command parameters for the next movement
    # individual_control = True
    # speed = [25, 20, 25]  # Speed of the movement
    # target_position = [200, 20, 110]  # New target positions
    # mode = "Basic"  

    # # # Adjust target_position if individual control is not enabled
    # # target_position = [target_position[0]] * 3 if not individual_control else target_position
    # time.sleep(5)
    # # Send the new command to the gripper
    # gripper.command_gripper(rPRA=target_position, rSP=speed, rFR=force, rMOD=mode, rICF=individual_control)

    # # Wait for the gripper to reach the new target positions
    # while ([gripper.FingerA_Position, gripper.FingerB_Position, gripper.FingerC_Position] != target_position):
    #     time.sleep(0.1)
    #     print([gripper.FingerA_Position, gripper.FingerB_Position, gripper.FingerC_Position])'''

    # # Print the updated positions of the fingers
    # print(f"FingerA_Position: {gripper.FingerA_Position} FingerB_Position: {gripper.FingerB_Position} FingerC_Position: {gripper.FingerC_Position}")
    
    # Close the connection when finished
    gripper.close()

if __name__ == '__main__':
    main()
