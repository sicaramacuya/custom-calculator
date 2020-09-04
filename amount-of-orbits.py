### Gretting to the user. Also, here it will explain what the program does to the user.  -------
greetings = "The purpose of this program is to help you calculate the amount of orbits the planets of the Solar System have around the Sun within a certain amount of time.\nFirst, we will start with Earth. The program will use the Earth's sidereal period which is only the period of time for Earth to go 360 degrees around the sun.\nIn other words, the time for earth to get to the same sarting place around the sun.\n"
print(greetings)


#### Here the program will save in memory important information for use latter on.   -----------
def adding_comma(number):   # This function will add a comma every thousand separators.
    return("{:,}".format(number))

def get_rid_comma(value):   # This funtion will get rid of any comma provided by the user stating the earth years.
    return(value.replace(',',''))

def asking_user_planet_age(planet):   # Will ask for the user the input. Age of planet to calculate the orbits.
    planet_age_year = float(get_rid_comma(input(f"\nPlanet chossen: {planet}\nFor how many years you want to calculate the total amount of orbits {planet} have?\n")))
    return planet_age_year

def giving_results(planet, planet_age, planet_orbits):   # Will output the results.
    return print(f"\nThe total of orbits {planet} have done around the sun in a period of {adding_comma(planet_age)} years is {adding_comma(round(planet_orbits, 2))} orbits.\n")

# Each sidereal period is store as years parting from the premise that 365.23636 is equal to 1 year. 
mercury_sidereal_period = 0.240846
venus_sidereal_period = 0.615
earth_sidereal_period = 1
mars_sidereal_period = 1.881
jupiter_sidereal_period = 11.86
saturn_sidereal_period = 29.46
uranus_sidereal_period = 84.01
neptune_sidereal_period = 164.8


#### Ask to the user for input.   --------------------------------------------------------------
earth_age_year = float(get_rid_comma(input("Now, the time will be year-base. If for example you want to know the amount of orbits Earth have done around the sun in his entire existance\nwhich is 4.54 billion years you would write \"4,540,000,000\". So at last, please type the amount of years and the program will do the rest.\n")))


#### Here the program do the calculation.   ----------------------------------------------------
amount_earth_orbits = earth_age_year / earth_sidereal_period


#### Overhere the progran will present the results.   ------------------------------------------
# The round(number,[ndigits]) will round the amount of orbits just to two decimal places.
print(f"\nThe total of orbits Earth have done around the sun in a period of {adding_comma(earth_age_year)} years is {adding_comma(round(amount_earth_orbits, 2))} orbits.\n")





#### -------------------------- At this point user choose if he/she wants to continue -------------------------------------------

### Ask for the user if it want to continue for other planet in the Solar System.   ------------
user_decision = input("Well, I hope you got the hang of it because if you want, you can perform the same calculation with any of the other planets in the\nSolar System. If you don't want to continue just type \"No\" but if you want to calculate the orbits from other planets type \"Yes\"\n")

while user_decision.lower() == "yes":
    planet_choosen = input("\n\nThis is great! As a reminder the list of planets are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. Pick any of them by\nwritting the correct name. Don't worry the program is not case sensitive.\n")
    if planet_choosen.lower() == "mercury":
        planet = "Mercury"
        mercury_age_year = asking_user_planet_age(planet)
        amount_mercury_orbits = mercury_age_year / mercury_sidereal_period
        giving_results(planet, mercury_age_year, amount_mercury_orbits)
    elif planet_choosen.lower() == "venus":
        planet = "Venus"
        venus_age_year = asking_user_planet_age(planet)
        amount_venus_orbits = venus_age_year / venus_sidereal_period
        giving_results(planet, venus_age_year, amount_venus_orbits)
    elif planet_choosen.lower() == "earth":
        planet = "Earth"
        earth_age_year = asking_user_planet_age(planet)
        amount_earth_orbits = earth_age_year / earth_sidereal_period
        giving_results(planet, earth_age_year, amount_earth_orbits)
    elif planet_choosen.lower() == "mars":
        planet = "Mars"
        mars_age_year = asking_user_planet_age(planet)
        amount_mars_orbits = mars_age_year / mars_sidereal_period
        giving_results(planet, mars_age_year, amount_mars_orbits)
    elif planet_choosen.lower() == "jupiter":
        planet = "Jupiter"
        jupiter_age_year = asking_user_planet_age(planet)
        amount_jupiter_orbits = jupiter_age_year / jupiter_sidereal_period
        giving_results(planet, jupiter_age_year, amount_jupiter_orbits)
    elif planet_choosen.lower() == "saturn":
        planet = "Saturn"
        saturn_age_year = asking_user_planet_age(planet)
        amount_saturn_orbits = saturn_age_year / saturn_sidereal_period
        giving_results(planet, saturn_age_year, amount_saturn_orbits)
    elif planet_choosen.lower() == "uranus":
        planet = "Uranus"
        uranus_age_year = asking_user_planet_age(planet)
        amount_uranus_orbits = uranus_age_year / uranus_sidereal_period
        giving_results(planet, uranus_age_year, amount_uranus_orbits)
    elif planet_choosen.lower() == "neptune":   
        planet = "Neptune"
        neptune_age_year = asking_user_planet_age(planet)
        amount_neptune_orbits = neptune_age_year / neptune_sidereal_period
        giving_results(planet, neptune_age_year, amount_neptune_orbits)

    user_decision = input("If you want keep using the program just keep writing \"Yes\" other wise just type \"No\"\n")                                    

# When the user does not want to use the program more this will be printed.
print("Hope you learn something new today!")