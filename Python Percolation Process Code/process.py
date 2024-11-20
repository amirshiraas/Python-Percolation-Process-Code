import random
import sys
import os
from datetime import datetime
import prettytable
from text_html import text
from text_html import html

def generate_grid(rows, cols):
    # This function insert random values inside the grid
    row_num=rows
    col_num=cols
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if random.random() < 0.3:  # 30% chance of an empty cell
                row.append(None)
            else:
                row.append(random.randint(10, 99))  # Inserting random numbers
        grid.append(row)
    display_grid(grid, row_num,col_num)

def display_grid(grid,row_num,col_num):
    # This fuction is to insert prettytable to the grid
    rows=row_num
    cols=col_num
    table = prettytable.PrettyTable()
    table.set_style(prettytable.SINGLE_BORDER)
    table.hrules = prettytable.ALL
    table.left_padding_width=2
    table.header = False
    num_columns = len(grid[0])
    filled_columns = []
    for i in range(num_columns):
        column_filled = all(row[i] is not None for row in grid);
        filled_columns.append(column_filled);

    for row in grid:
        table_row = []
        for cell in row:
            if cell != None:
                table_row.append(cell)
            else:
                table_row.append('')
        table.add_row(table_row)
    
    # Display the table
    print(table)

    # Display the indicators below each column
    ok_no=[]#Creating a list to save ok or no for text file
    for i in range(num_columns):
        if filled_columns[i]:
            indicator = '  OK '
            ok_no.append("OK")
        else:
            indicator = '   NO '
            ok_no.append("NO")
        print(indicator, end="")
    grid.append(ok_no)
    text.save_txt(grid)
    html.save_html(table,rows,cols,ok_no)



            



