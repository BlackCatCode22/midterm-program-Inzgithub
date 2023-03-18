# used python style guide: https://peps.python.org/pep-0008/
# read the file - https://www.w3schools.com/python/python_file_open.asp

ANIMAL_FILE = open(
    "C:\\Users\\Inez\\Documents\\GitHub\\python-cit95\\midterm-program-Inzgithub\\arrivingAnimals.txt", "r", encoding="utf-8")
# was receiving error found solution https://stackoverflow.com/questions/71715517/syntaxerror-unicode-error-unicodeescape-codec-cant-decode-bytes-in-positio

ANIMAL_DATA = ANIMAL_FILE.read()
ANIMAL_FILE.close()

# ANIMAL_LINES now holds the data in the arriving animals file as a list
# sought help converting a text file into a list: https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/
ANIMAL_LINES = ANIMAL_DATA.split("\n")


print(ANIMAL_LINES)
print(type(ANIMAL_LINES))

#used pip install numpy on console before importing numpy
#----
# import numpy 

# ANIMAL_ARRAY = numpy.asarray(ANIMAL_LINES)

# print(ANIMAL_ARRAY)
# # print(type(ANIMAL_ARRAY))
# #class 'numpy.ndarray'

# print(ANIMAL_ARRAY[0])
# print(ANIMAL_ARRAY[1])
# print(ANIMAL_ARRAY[2])

