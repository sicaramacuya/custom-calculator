# Gretting to the user. Also, here it will explain what the program does to the user.
greetings = "Hello, this message will help you understand what this program does.\n\nThe purpose of this program is to help you calculate the amount of orbits Earth have around the Sun within a certain amount of time.\nThe program will use the Earth's sidereal period which is only the period for Earth to go 360 degrees around the sun. In other words, the time\nfor earth to get to the same sarting place around the sun.\n"
print(greetings)

#### Here the program will save in memory important information for use latter on.
def adding_comma(number):   # This function will add a comma every thousand separators.
    return("{:,}".format(number))

def replacing_comma(value):   # This funtion will get rid of any comma provided by the user stating the earth years.
    return(value.replace(',',''))

earth_sidereal_period = 365.25636   # This earth_sidereal_period is store as days.

#### Ask to the user for input.
earth_age_year = float(replacing_comma(input("Now, the time will be year-base. If for example you want to know the amount of orbits earth have done around the sun in his entire existance\nwhich is 4.54 billion years you would write \"4,500,000,000\". So at last, please type the amount of years and the program will do the rest.\n")))

#### Here the program do the calculation.
amount_orbits = earth_age_year / earth_sidereal_period

#### Overhere the progran will present the results.
# The round(number,[ndigits]) will round the amount of orbits just to two decimal places.
print(f"The total of orbits Earth have done around the sun in a period of {adding_comma(earth_age_year)} years is {adding_comma(round(amount_orbits, 2))} orbits.")