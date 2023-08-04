from prettytable import PrettyTable

p=PrettyTable()
p.add_column("Cityname",["Mumbai","Chennai","Hyderabad"])
p.add_column("Candidate name",["Aditi","lara","Satwik"])
p.align="r"
print(p)
