def contains_space(string):
    """Returns True if there is a space found within
    the string; False otherwise"""

    for char in string:
        if char == ' ':
            return True
    return False


def total_from_attempts(string):
    """Takes a string of a climbing grade and number of
    attempts and returns the product of the two numbers,
    as well as the number of attempts"""

    split_string = string.split()

    grade = int(split_string[0])
    attempts = int(split_string[1])

    return grade * attempts, attempts


print("Enter grades below. Enter STOP when complete."    )
print("To quickly input multiple attempts, put the grade")
print("first, then the attempts, separated by a space: " )
print("-------------------------------------------------")

# user input given during the while loop
user_input = ""
list_of_grades = []
number_of_boulders = 0

# main loop for user input
while user_input != "STOP":
    # prompt has already been given to user
    user_input = input()

    if contains_space(user_input):
        user_input, temp = total_from_attempts(user_input)
        number_of_boulders += temp
    elif not contains_space(user_input) and user_input != "STOP":
        user_input = int(user_input)
        number_of_boulders += 1

    list_of_grades.append(user_input)

# remove the STOP entry from the list of grades
list_of_grades.pop()
attempted_v_points = 0

for grade in list_of_grades:
    attempted_v_points += grade

print("V-Points: ", attempted_v_points)
print("Number of Attempts: ", number_of_boulders)

input("Press Enter to exit the program...\n")
