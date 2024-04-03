import random as rn
from datetime import date

def export_list(array, check_list):
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    random_no = rn.randint(1000, 9999)
    file_name_txt = f"{year}_{month}_{day}_{random_no}.txt"
    file_name_html = f"{year}_{month}_{day}_{random_no}.html"
    
    with open(file_name_txt, "w") as txt:
        for i in array:
            y = (" ".join(str(x)for x in i))
            txt.write(str(y))
            txt.write(str("\r"))
        strfortxt = (" ".join(str(x)for x in check_list))
        txt.write(str(strfortxt))

    with open(file_name_html, "w") as html:
        html.write("""<!DOCTYPE html>
<html>
<head>
<title>20231615</title>
</head>
<body>
<h2>20231615 Assignment</h2>
<table>
<style>
table, th, td {border: 3px solid black;
border-collapse: collapse;}
th, td {padding: 10px;}
body {background-color: rgb(53, 53, 53);
color: rgb(255, 255, 255);}
</style>
""")
        for i in range(len(array)):
            html.write("<tr>")
            for j in range(len(array[0])):
                html.write(f"<td>{array[i][j]}</td>")  
            html.write("</tr>")
        
        html.write("<tr>")
        for i in check_list:
            if i == "OK":
                html.write(f"<td style ='color : rgb(85, 102, 230);'>{i}</td>")
            if i == "NO":
                html.write(f"<td style ='color : red;'>{i}</td>")
        html.write("\n</tr>\n</table>\n</body>\n</html>")