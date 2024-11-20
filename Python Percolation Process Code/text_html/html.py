import random
from datetime import datetime


def save_html(table, rows, columns,ok_no):
    # This function is to save the output in html
    now = datetime.now()  # Taking current date
    # Naming the file as per instruction
    filename = now.strftime("%Y_%m_%d_") + str(random.randint(1000, 9999)) + ".html"
    with open(filename, 'w') as file: # Opening html file
        file.write(table.get_html_string(attributes={"style": "border: 1px solid black; border-collapse: collapse; width:{}px; height:{}px;".format(30 * columns, 25 * rows)}))  # Applying style to the table
        for x in ok_no:
            file.write(x) # Inserting ok or no below the table
            file.write(' ')
        file.close() # Closing html file

