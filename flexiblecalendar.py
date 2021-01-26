import calendar

year = 2022
firstweekday = 6  # 6 to start week on Sun, 0 to start on Mon

y = calendar.Calendar(firstweekday=firstweekday)
selected_year = y.yeardayscalendar(year, width=1)

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

import sys

if len(sys.argv) > 1:
    import yaml

    with open(sys.argv[1], "r") as f:
        holidays = yaml.safe_load(f)["holidays"]
else:
    holidays = []

# sort holidays into chronological order
def sort_holidays(holidays):
    return sorted(holidays, key=lambda x: (months.index(x[0]), x[1]))


# format the week rows for LaTex table
def table_week(week, month_title):
    row_string = ""
    for index, day in enumerate(week):
        row_string += "\t"
        if day:
            row_string += "\\textbf{" + str(day) + "}"
            while holidays and month_title == holidays[0][0] and day == holidays[0][1]:
                row_string += "\\scriptsize{ - " + holidays[0][2] + "}"
                holidays.pop(0)
        row_string += "\t"
        if index < 6:
            row_string += "&"
        else:
            row_string += "\\\\ [20ex] \hline \n"
    return row_string


# combine rows into full month LaTeX table
def table_month(month, title):
    month_string = ""
    for index in range(7):
        month_string += "\t" + weekdays[(firstweekday + index) % 7] + "\t"
        if index < 6:
            month_string += "&"
        else:
            month_string += "\\\\ \hline \n"
    for week in month[0]:
        month_string += table_week(week, title)
    return month_string


# write to files by month
holidays = sort_holidays(holidays)
for index, month in enumerate(selected_year):
    filename = f"tables/{months[index]}.tex"
    tex_file = open(filename, "w")
    tex_file.write(table_month(month, months[index]))
    tex_file.close()

# write year to file so that it can be printed on cover
tex_file = open("year-label.tex", "w")
tex_file.write(str(year))
tex_file.close()
