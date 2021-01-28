
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
        data = yaml.safe_load(f)
        year = data["year"]
        firstweekday = data["firstweekday"]
        holiday_list = data["custom_holidays"]
        country = data["country"]
        prov = data["province"]
        state = data["state"]
        day_height = data["day_height"]
        if country:
            import holidays
            holiday_list += [{"month": date.month, "day": date.day, "name": name} for date, name in holidays.CountryHoliday(country=country, years=year, prov=prov, state=state).items()]
        # format month string consistently in holiday
        for index, holiday in enumerate(holiday_list):
            if type(holiday["month"]) is int:
                holiday_list[index]['month'] = months[holiday['month'] - 1]
            elif type(holiday["month"]) is str:
                holiday_list[index]['month'] = holiday['month'].strip().lower().title()
else:
    print("No config provided, using defaults and no holidays")
    year = 2021
    firstweekday = 6
    holidays = []
    day_height = "20ex"

# sort holidays into chronological order
def sort_holidays(holidays):
    return sorted(holidays, key=lambda x: (months.index(x['month']), x['day']))


# format the week rows for LaTex table
def table_week(week, month_title):
    row_string = ""
    for index, day in enumerate(week):
        row_string += "\t"
        if day:
            row_string += "\\textbf{" + str(day) + "}"
            while holiday_list and month_title == holiday_list[0]['month'] and day == holiday_list[0]['day']:
                row_string += "\\scriptsize{ - " + holiday_list[0]['name'] + "}"
                holiday_list.pop(0)
        row_string += "\t"
        if index < 6:
            row_string += "&"
        else:
            row_string += "\\\\ [" + day_height + "] \hline \n"
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

# create calendar dates by week
import calendar
y = calendar.Calendar(firstweekday=firstweekday)
selected_year = y.yeardayscalendar(year, width=1)

# write to files by month
holiday_list = sort_holidays(holiday_list)
for index, month in enumerate(selected_year):
    filename = f"tables/{months[index]}.tex"
    tex_file = open(filename, "w")
    tex_file.write(table_month(month, months[index]))
    tex_file.close()

# write year to file so that it can be printed on cover
tex_file = open("year-label.tex", "w")
tex_file.write(str(year))
tex_file.close()
