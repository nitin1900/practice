from collections import Counter
import json
import math

from bokeh.plotting import figure, show, output_file


DATA_FILE = "birthdays.json"
output_file("birthday.html")

with open(DATA_FILE, "r") as f:
	DATA = json.load(f)

num_to_string = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

months = []
for name, birthday_string in DATA.items():
	month = int(birthday_string.split("/")[0])
	months.append(num_to_string[month])
months = Counter(months)

months, counts = list(zip(*months.items()))

categories = list(num_to_string.values())
p = figure(x_range=categories, title="Scientists' Birthday Months")
p.xaxis.major_label_orientation = math.pi/4
p.vbar(x=months, top=counts)

show(p)