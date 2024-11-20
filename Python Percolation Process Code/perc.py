import process
import sys
def grid_demension():
    #This function takes in grid demensions
    if len(sys.argv) > 1:   # Cheacking if user inputs grid demensions
        grid = sys.argv[1]
    else : # User did not input grid demensions
        grid="5x5" # Setting grid demensions to default 5x5
    split = grid.split('x')
    cols = int(split[0])
    rows = int(split[1])
    if cols < 2 or cols > 9 or rows < 2 or rows > 9:
        print("**Grid demension must be between 3x3 and 9x9!!**")
        print()
        return
    process.generate_grid(rows,cols)



    
grid_demension()
