import random
from datetime import datetime


def save_txt (grid):
    # This function is to save output in text file
    now = datetime.now() # Taking current date
    # Naming the file as per instruction
    filename = now.strftime("%Y_%m_%d_") + str(random.randint(1000, 9999)) + ".txt"
    file=open(filename,'w') # Opening text file in writing mode
    for i in grid :
        for x in i:
            num=str(x) # chaninging int to str
            if num == "None":
                file.write("     ") # Leaving blank for none value
            else:
                file.write(num)  # Inserting same values to table
                file.write('   ')
        file.write('\n')
    file.close() # Closing the text file
    
