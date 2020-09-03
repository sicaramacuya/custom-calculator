# Gretting to the user. Also, here it will explain what the program does to the user.
greetings = "Hello, this message will help you understand what this program does.\n\nThe purpose of this program is to help you calculate the amount of orbits Earth have around the Sun within a certain amount of time.\nThe program will use for the Earth's sidereal period which is only the period for Earth to go 360 degrees around the sun. In other word the time\nfor earth to get to the same sarting place around the sun.\n"
print(greetings)

#### Here the program will save in memory important information for use latter on.
# This earth_sidereal_period is store as days.
earth_sidereal_period = 365.25636

#### Ask to the user for input.
earth_age_year = int(input("Now, the time will be year-base. If for example you want to know the amount of orbits earth have done around the sun in his entire existance which is 4.54 billion years\nyou would write 4,500,000,000 but ignore the commas, the computer doesn't need them. It will be just 4500000000.\n"))

#### Here the program do the calculation.
amount_orbits = earth_age_year / earth_sidereal_period

#### Overhere the progran will present the results.
# The round(number,[ndigits]) will round the amount of orbits just to two decimal places.
print(f"The total of orbits Earth have done around the sun in a period of {earth_age_year} years is {round(amount_orbits, 2)} orbits.")