# printable-latex-calendar

This code generates a printable pdf calendar for a selected year with optional custom holidays.

## How to use

Edit the **config.yml** file contents to update the year and other parameters, then run the **flexiblecalendar.py** script to generate the appropriate LaTeX table structure:

```bash
python flexiblecalendar.py config.yml
```

If the country config parameter has an entry, you will probably need to install the [holidays library](https://pypi.org/project/holidays/):

```bash
pip install holidays
```

Now you can compile **main.tex** with LaTeX to generate a printable pdf. It uses the tables generated with **flexiblecalendar.py** and includes the images and captions from their respective folders. 

Print double-sided portrait format with settings for binding on short edge and assemble the calendar.

## Design

This is a basic calendar to print on Letter or A4 size paper with an image at the top and monthly calendar table below.

The template includes images from the Dover [Exotic Butterflies and Moths Coloring Book](https://store.doverpublications.com/0486423816.html) by Ruth Soffer that I hand-painted in watercolour. I retouched high-resolution scans to use as the decorative panels in the printable calendar. Each month shows a different illustration and is captioned with the name of the species.

The images, captions and title can be swapped out for others by replacing these files with new ones that have the same names. By default, the LaTeX template assumes there will be jpeg format images, but this could be switched to a different file type in the \includegraphics command.

## Customizable options

Here are some of the input parameters that can change to suit personal taste, year and location.

### Config file

The input configuration has a few options to generate the calendar. These are:
- **year**: The calendar year to print, runs from January to December.
- **firstweekday**: The day of the week to place as the leftmost column in the calendar. A value of 0 starts weeks on Monday and can be incremented up to 6 for Sunday.
- **custom\_holidays**: A list of dictionaries for personal holidays to print in the calendar. This could include birthdays, anniversaries or other events planned well in advance. Each entry takes *month*, *day* and *name* keys. The *name* value will be printed in the calendar on the appropriate day. Note that the month can be entered as the full string (case insensitive) or as the integer month (so "January", "january", 1 should all work the same).
- **country**: Country code for national holiday selection from the [holidays library](https://pypi.org/project/holidays/).
- **state** or **province**: Region of the country if applicable to get more specific holidays.
- **day\_height**: Height of the LaTeX weekly rows, can be adjusted if page geometry is altered.

### LaTeX 

The paper format in the template is portrait A4 with 1cm margins on the left and right and 3cm margins at top and bottom. This is purely based on visual preference and can easily be changed in the \usepackage command, but will make the tables and images fit a little differently and require tweaking. This may include trying different **day\_height** values in the config file.

There is a separate title file to input the title to print on the cover page, and the images and captions can be replaced as well as mentioned above.


