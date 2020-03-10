import csv
import webbrowser
import string

import faster_than_csv as ft_csv


def generate_letter_list(number_to_generate):
    alpha_list = list(string.ascii_lowercase)
    letter_list = []
    generate_amount = number_to_generate
    for x in range(1, generate_amount):
        if x <= 27:
            for index, value in enumerate(alpha_list, 1):
                if index == x:
                    letter_list.append(value)
        if 27 < x <= 54:
            for index, value in enumerate(alpha_list, 1):
                if (index+27) == x:
                    letter_list.append("a"+value)
        if 54 < x <= 80:
            for index, value in enumerate(alpha_list, 1):
                if (index+54) == x:
                    letter_list.append("b"+value)
    return letter_list


number_to_generate = input("How many people to schedule (up to 80)? ")
adjusted_number = int(number_to_generate)+1
letter_list = generate_letter_list(adjusted_number)
header = "person," + ",".join(
    [str(x) for x in range(1, adjusted_number)]
)
header = header.split(",")
with open("schedule.csv", "w", newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    filewriter.writerow(header)
    alternate_list = generate_letter_list(adjusted_number)
    first_temporary_letter = alternate_list.pop(0)
    alternate_list.append(str(first_temporary_letter))
    shifting_letter_list = alternate_list
    for index, row_letter in enumerate(letter_list):
        first_letter = letter_list[index]
        row = first_letter + "," + ",".join(
            [letter if letter != first_letter else '---' for letter in shifting_letter_list]
        )
        row = row.split(",")
        filewriter.writerow(row)
        last_letter = shifting_letter_list.pop()
        shifting_letter_list.insert(0, last_letter)
ft_csv.csv2htmlfile(csv_file_path="schedule.csv", html_file_path="output.html")

webbrowser.open_new_tab("output.html")
