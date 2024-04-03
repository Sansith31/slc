# Import necessary modules
from time import strftime
import random

# Function to export grid to a text file
def text_file(grid):
    # Generate a random number for file name uniqueness
    rand=random.randrange(1000,9999)
    time=strftime(f"%Y_%m_%d_{rand}")
    # Create and write grid to text file
    with open(f'{time}.txt', "w") as txt: 
        for row in grid:
            string_to_type=' '.join(str(i) for i in row)
            txt.write(string_to_type + '\n')
    return time

# Function to export grid to an HTML file            
def html(time,grid):
    html=open(f'{time}.html', "w") 
    html.write("""<html>
<style>
table, td {border: 3px solid black;border-collapse: collapse;}
td {padding: 10px;}
body {background-color: rgb(48, 45, 77);
color: rgb(255, 255, 255);}
</style>
<table>
""")
    for row in grid:
        html.write('<tr>\n')
        for i in row:
            # Write table cell with appropriate styling based on percolation status
            if i == 'OK':
                html.write(f"<td style ='color : green;'>{i}</td>")
            elif i == 'NO':
                html.write(f"<td style ='color : red;'>{i}</td>")
            else: 
                html.write(f'<td>{i}</td>\n')
        html.write('</tr>\n')
    html.write("""</table>
</body>
</html>""")

