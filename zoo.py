# INEZ FRIAS - CIT95 MIDTERM
#


# # used python style guide: https://peps.python.org/pep-0008/
# # read the file - https://www.w3schools.com/python/python_file_open.asp
# from datetime import date
# import numpy
# import math
# import re

# ANIMAL_FILE = open(
#     "C:\\Users\\Inez\\Documents\\GitHub\\python-cit95\\midterm-program-Inzgithub\\arrivingAnimals.txt", "r", encoding="utf-8")
# # was receiving error found solution https://stackoverflow.com/questions/71715517/syntaxerror-unicode-error-unicodeescape-codec-cant-decode-bytes-in-positio

# ANIMAL_DATA = ANIMAL_FILE.readlines()
# ANIMAL_FILE.close()
# # print(ANIMAL_DATA)
# # ANIMAL_LINES now holds the data in the arriving animals file as a list
# # sought help converting a text file into a list: https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/

# # ANIMAL_LINES = ANIMAL_DATA.split("\n")
# # ANIMAL_LINES = ANIMAL_DATA.split(",")
# # print(type(ANIMAL_DATA))
# ANIMAL_LINES = []
# line_count = 0
# for line in ANIMAL_DATA:
#     ANIMAL_LINES.append('**animal**, '+line)
#     line_count += 1
# # print(ANIMAL_LINES)
# # print(type(ANIMAL_LINES))

# # counting the number of animals in my list  https://www.geeksforgeeks.org/python-count-strings-with-substring-string-list/
# ANIMAL_COUNT = len([i for i in ANIMAL_LINES if 'pounds' in i])
# # print(ANIMAL_COUNT)

# # used pip install numpy on console before importing numpy
# ANIMAL_ARRAY = numpy.asarray(ANIMAL_LINES)

# # print(ANIMAL_ARRAY)

# # Output the new array - FROM DENNIS MOHLE CODE
# array_line = -1
# for element in ANIMAL_ARRAY:
#     print("\n" + str(ANIMAL_ARRAY[array_line]))
#     array_line += 1

# split_on_space = ANIMAL_ARRAY[array_line].split(" ")
# print(split_on_space)

# AGE = split_on_space[1]
# SEX = split_on_space[4]
# ANIMAL_TYPE = split_on_space[5]
# SEASON = split_on_space[8]

# print(AGE, SEX, ANIMAL_TYPE, SEASON)

# Following along with Dennis Mohle code and editing variable names/experimenting with changes as i go. writing notes to show i follow what is happenning


import numpy
import re
from datetime import date
import math


#function to calculate birthdate based on age. we will use the animal age from the arriving animal text file to obtain a birthdate for each animal

#function takes todays date, minus the birthdate that gets passed into the function to calculate the difference between the two days and dividing those by the days in a year then truncating thet to get the age in years.
def calc_age_in_years(birth_date):
    today = date.today()
    date_diff = today - birth_date
    age_in_days = date_diff.days
    age_in_years = age_in_days/365.242199
    age_in_years = math.trunc(age_in_years)
    return age_in_years


print("\n\n\n")

#########################################
# Get animal names into four lists...

animal_file = open(
    "C:\\Users\\Inez\\Documents\\GitHub\\python-cit95\\midterm-program-Inzgithub\\animalNames.txt", "r", encoding="utf-8")

# Reading the file, passing the data into the Names_of_animals variable, then closing the file.
Names_of_animals = animal_file.readlines()
animal_file.close()

# Output each line in animal_lines and putting that into a python list called list_of_animals
line_count = 0
for line in Names_of_animals:
    print("Line " + str(line_count+1) + ":  " + line)
    line_count += 1
list_of_animals = []
for line in Names_of_animals:
    list_of_animals.append(line)

# Demonstrate the list
print("\n\n Here is a list of the lines in the animal names file...\n\n")
print("line 0 is: " + str(list_of_animals[0]))

hyena_names_list = list_of_animals[2].replace(',', "").split()
lion_names_list = list_of_animals[6].replace(',', "").split()
tigers_names_list = list_of_animals[10].replace(',', "").split()
bears_names_list = list_of_animals[14].replace(',', "").split()
# end of getting animal names
###################################################

################ User-defined Functions #########################
# the birthday function uses if else logic to assume a birth month based on the season listed on the arrivingAnimals.txt file.
def the_birthday_function(years_old, season_of_birth):
    birth_year = 2023 - int(years_old.strip())
    birth_year = birth_year - 1
    if season_of_birth == "spring":
        birthday_date = "03-21"
    elif season_of_birth == "summer":
        birthday_date = "06-21"
    elif season_of_birth == "fall":
        birthday_date = "09-21"
    elif season_of_birth == "winter":
        birthday_date = "12-21"
    else:
        birthday_date = "01-01"
    animal_birthday = str(birth_year) + "-" + birthday_date

    return animal_birthday

# uniqueID function - this function creates a unique ID for eaxh animal by using the species name to add a prefix and a unique number to that animal.
def uniqueID(species_name, num_of_animals_in_species):
    match species_name:
        case "hyena":
            prefix = "Hy"
        case "lion":
            prefix = "Li"
        case "tiger":
            prefix = "Ti"
        case "bear":
            prefix = "Be"
        case default:
            prefix = "Xx"

    return prefix + "0" + str(num_of_animals_in_species)
##################################################################


# Global variables needed for some user-defined functions
num_of_hyenas = 0
num_of_lions = 0
num_of_tigers = 0
num_of_bears = 0

# Global lists needed for organizing animals into a single-species habitats
hyena_list = []
lion_list = []
tiger_list = []
bear_list = []


## it was interesting to see that i could use the same variable name as before when opening a file to read. i changed it so i could follow the code easier.
animal_file = open(
    "C:\\Users\\Inez\\Documents\\GitHub\\python-cit95\\midterm-program-Inzgithub\\arrivingAnimals.txt", "r", encoding="utf-8")

# Read the file line by line into a data structure called 'animal_lines'
animal_lines = animal_file.readlines()

# Close the input file (if you open a file, be sure to close it)
animal_file.close()

# Output each line in animal_lines
line_count = 0
for line in animal_lines:
    print("Line " + str(line_count+1) + ":  " + line)
    line_count += 1

# Read the file into a Python list
list_of_animals = []
for line in animal_lines:
    list_of_animals.append(line)


# Get the file contents into an array
my_array = numpy.asarray(list_of_animals)

# Find how many elements are in our new array
num_of_array_elements = my_array.size

# Output the new array
array_line = 0
for element in my_array:
    print("\n" + str(my_array[array_line]))
    array_line += 1

# Process each element of the new array
array_line = 0
for element in my_array:
    print("\n" + str(my_array[array_line]))

    # get the data elements needed from this one line for the birthday
    #
    # Split on blank space to get words in the line
    split_on_space = my_array[array_line].split(" ")
    print(split_on_space)

    # from this split, get what data elements we can
    # ['4', 'year', 'old', 'female', 'hyena,', 'born', 'in', 'spring,', 'tan', 'color,', '70', 'pounds,', 'from', 'Friguia', 'Park,', 'Tunisia\n']
    # years_old will always be the first data element, so we use 0 for the first element in our split list
    years_old = split_on_space[0]

    # output every small change so you know you got it right
    # print("years_old: " + years_old)

    # next is sex, which will always be the fourth word (element number 3 because list element numbering starts at 0)
    sex = split_on_space[3]
    # print("sex: " + sex)

    # we can get species here
    species = split_on_space[4]
    # print("species: " + species)

    # we have a comma at the end of this word, so we must remove it
    species = re.sub(",", "", species)

    # test with a print()
    # print(" species without a comma: " + species)

    # season of birth
    season = split_on_space[7]
    # print("season: " + season)

    # we have a comma at the end of this word, so we must remove it
    season = re.sub(",", "", season)

    # test with a print()
    # print(" season without a comma: " + season)

    # we got a couple of our needed data elements. now let's calculate what we can using the functions we wrote
    birth_date = the_birthday_function(years_old, season)
    # print("birthdate: " + birth_date)

    # increment the number of animals in species
    # and while we know the species...
    # generate a uniqueID and get a name!
    if (species == "hyena"):
        num_of_hyenas += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_hyenas)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = hyena_names_list[num_of_hyenas]
    elif (species == "lion"):
        num_of_lions += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_lions)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a lion name
        name = lion_names_list[num_of_lions]
    elif (species == "tiger"):
        num_of_tigers += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_tigers)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = tigers_names_list[num_of_tigers]
    elif (species == "bear"):
        num_of_bears += 1

        # and now we can call uniqueID()
        unique_id = uniqueID(species, num_of_bears)

        # get a name from the name list that we created with file io
        # if we are here, we know we need a hyena name
        name = bears_names_list[num_of_bears]
    else:
        print("\n error in incrementing species")

    print("unique_id: " + unique_id)
    print("name is: " + name)
    ##########################################

    # Split on comma because some data elements (like color, wright, and origin)
    # have a varied number of words
    after_split_on_comma = my_array[array_line].split(", ")

    print(after_split_on_comma)

    color = after_split_on_comma[2]
    print("color = " + color)

    weight = after_split_on_comma[3]
    print("weight is: " + weight)

    origin = after_split_on_comma[4] + " " + after_split_on_comma[5]
    print("origin = " + origin)

    #  get rid of the lf+cr that is showing up in the output file...
    origin = origin.strip()
  
    split_on_dash = birth_date.split("-")
    my_year = split_on_dash[0]
    my_month = split_on_dash[1]
    my_day = split_on_dash[2]

    # test our split()
    # print("my_year = " + my_year)
    # print("my_month = " + my_month)
    # print("my_day = " + my_day)

    # cast strings to ints because that's what our date object needs
    birth_date_object = date(int(my_year), int(my_month), int(my_day))

    # pass our new date object to our calc_age_in_years() function
    animal_age_in_years = calc_age_in_years(birth_date_object)

    # validate our function
    # print("animal_age_in_years is: " + str(animal_age_in_years))

    # arrival date is easy (after all that date() processing!
    arrival_date = date.today()
    # print("arrival_date = " + str(arrival_date))

    # That should be it. Let's see....
    str01 = unique_id + "; " + name + "; " + \
        str(animal_age_in_years) + " years old; " + \
        "birth date: " + birth_date + "; "
    str02 = color + "; " + sex + "; " + weight + "; " + \
        origin + "; arrived: " + str(arrival_date)

    output_line = str01 + str02

    print("\noutput_line = " + output_line)

    # get this output line into the proper list()
    if (species == "hyena"):
        hyena_list.append(output_line)
    elif (species == "tiger"):
        tiger_list.append(output_line)
    elif (species == "lion"):
        lion_list.append(output_line)
    else:
        bear_list.append(output_line)

    array_line += 1
    # End of processing each line with the two splits()
    # Write our species list to our output file.
    # Pro tip: write this to screen output before writing to your external file
    #  I had a pesky lf+cr after origin that I had no idea about
    print("Hyena Habitat: \n\n")
    for line in hyena_list:
        print(line + "\n")

    animal_file = open(
        "C:\\Users\\Inez\\Documents\\GitHub\\python-cit95\\midterm-program-Inzgithub\\myMidtermOutput.txt", "w", encoding="utf-8")

    animal_file.write(
        "Midterm Program Output; by Dennis Mohle and reviewed by Inez Frias ro understand how to complete the requirements. No major changes made by Inez.\n")
    animal_file.write(
        "Note: This is the approved solution file for Spring 2023 midterm program.\n\n")

    animal_file.write("Hyena Habitat: \n\n")
    for i in hyena_list:
        animal_file.write(i)
        animal_file.write("\n")
    animal_file.write("\n\n")

    animal_file.write("Lion Habitat: \n\n")
    for i in lion_list:
        animal_file.write(i)
        animal_file.write("\n")
    animal_file.write("\n\n")

    animal_file.write("Tiger Habitat: \n\n")
    for i in tiger_list:
        animal_file.write(i)
        animal_file.write("\n")
    animal_file.write("\n\n")

    animal_file.write("Bear Habitat: \n\n")
    for i in bear_list:
        animal_file.write(i)
        animal_file.write("\n")
    animal_file.write("\n\n")

    # "if you open a barn door, make sure you close it"
    # close opened files otherwise your program will not work as expected.
    animal_file.close()
