# os and os path for reading and writing to files
# and pands to do excel operation
import os
import os.path
import random
import sys
import pandas as pd
import numpy
import time
import PyQt5.QtWidgets
from pandas.core.frame import DataFrame


###
# dict Structure
###
# Test dict for testing purposes
test_dict = {
    'Tutorial-08': {
        'weeks': 9,
        'num_chosen_student': 12,
        'num_chosen_time': 3,
        'student_info': {
            '519H0288': {
                'ordinal_number': 1,
                'first_name': "Thien Hoang",
                'last_name': "Nguyen",

            },
            '519H0258': {
                'ordinal_number': 2,
                'first_name': "Hoang Thien",
                'last_name': "Nguyen"
            },
        },
        'randomized_list': [(), (), ()]
    },

    'Tutorial-09': {
        'weeks': 9,
        'num_chosen_student': 9,
        'num_chosen_time': 3,
        'student_info': {
            '519H0189': {
                'ordinal_number': 1,
                'first_name': "Van Hong",
                'last_name': "Ta"
            },
            '519H0199': {
                'ordinal number': 2,
                'first name': "Van An",
                'last name': "Le"
            }
        },
        'randomized_list': [(), (), ()]
    }
}

student_dict = {
    # Above structure
}


def create_student_dict_from_sheet(existing_dict, sheet_name, sheet_info, dataframe):
    # storing student info
    students_dict = {}
    sheet_dict = {}
    # updating the student dict with info
    for index, row_info in dataframe.iterrows():
        per_student_dict = {}
        per_student_dict['ordinal_number'] = row_info[0]
        per_student_dict['first_name'] = row_info[2]
        per_student_dict['last_name'] = row_info[3]
        # student dict using id as key
        students_dict[str(row_info[1])] = per_student_dict

    # generate info for the sheet, including chosing time, num of students and student dict
    sheet_dict['num_chosen_student'] = sheet_info[0]
    sheet_dict['num_chosen_time'] = sheet_info[1]
    sheet_dict['weeks'] = sheet_info[2]
    sheet_dict['students_info'] = students_dict

    # append the info to the sheet dict
    existing_dict[sheet_name] = sheet_dict

###
# File operation funcitons
###


def create_file_list_from_directory(path, folder_name):
    try:
        # return [os.path.join(path, files) for files in os.listdir(path)]
        return [file.strip() for file in os.listdir(path)]
    except FileNotFoundError:
        ## print("The", folder_name, "directory doesn't exists, therefore I created one in the root directory(where the software is located)")
        try:
            os.mkdir("./" + folder_name)
        except:
           # print(folder_name,
           # "cannot be created, could be a windows permission problem ?")
            return []
    except:
        ## print("The folder name is incorrect")
        return []

###
# Randomize functions
###
# Generates a list of ids from the dict key


def get_key_to_list(dict):
    # Generates a list of ids from the dict key
    return [id for id in dict.keys()]


def generate_randomised_list(students_list, weeks, num_of_students_selected, num_of_selected_time):
    time_limit = time.time() + (0.05 * len(students_list))
    if(num_of_students_selected * weeks) > (len(students_list) * weeks):
        result_array = [[None for i in range(
            len(students_list))] for j in range(weeks)]
    else:
        result_array = [[None for i in range(
            num_of_students_selected)] for j in range(weeks)]

    for student in students_list:
        for _ in range(num_of_selected_time):
            while True:
                random_arr = random.choice(result_array)
                if time.time() > time_limit:
                    raise TimeoutError()
                if student in random_arr:
                    continue
                index = random.randint(0, len(random_arr) - 1)
                if random_arr[index] != None:
                    continue
                random_arr[index] = student
                break

    for arr in result_array:
        for position in range(len(arr)):
            if arr[position] is not None:
                continue
            while True:
                new_value = random.choice(students_list)
                if new_value in arr:
                    continue
                arr[position] = new_value
                break
    return result_array


###
# Excel Processing functions
###
def read_to_dict_from_excel(excel_file):
    # Initiate the excel file for iterating through the sheets
    excel_file = pd.ExcelFile(excel_file)
    excel_file_dict = {}
    # Reading multiple sheets with this loop
    for sheet in excel_file.sheet_names:
        # This should have not been done...
        # This load the sheet into the memory the first time
        cell_data = excel_file.parse(sheet)

        # just to read 3 cells...
        # 1: num student per list, 2: time per student and 3: weeks
        sheet_info = []
        sheet_info.append(cell_data['Unnamed: 0'][1])
        sheet_info.append(cell_data['Unnamed: 0'][3])
        sheet_info.append(cell_data['Unnamed: 1'][3])

        # And, ah yes, load the sheet to the memory, yet again! marvelous!
        sheet_data = excel_file.parse(sheet, skiprows=range(1, 6), header=1)
        student_info = pd.DataFrame(
            sheet_data, columns=['ORDINAL NUMBER', 'STUDENT_CODE', 'FIRST_NAME', 'LAST_NAME'])

        # skips the sheet if above parameters are in correct
        randomizing_space = numpy.prod(sheet_info)
        if(randomizing_space < len(student_info)):
            print("The chosen space (student numbers * weeks / student's time chosen) is less than the total number of students, please revise!")
            print(
                "Therefore, the randomisation process for the following sheet is skipped:", sheet)
            continue
        create_student_dict_from_sheet(
            excel_file_dict, sheet, sheet_info, student_info)
    return excel_file_dict


# write to file
def write_to_file(student_dict, export_file_address):
    with pd.ExcelWriter(export_file_address) as writer:
        for sheet in student_dict:
            print_list = []
            column_names = ['ORDINAL NUMBER',
                            'STUDENT CODE', 'FIRST NAME', 'LAST NAME']
            sheet_data = student_dict.get(sheet)
            student_info = sheet_data.get('students_info')
            randomized_lists = sheet_data.get('randomized')
            student_id_list = get_key_to_list(student_info)

            # Sheet Preparation
            for id in student_id_list:
                student = student_info.get(id)
                row = ["" for i in range(0, 4)]
                row[0] = student.get('ordinal_number')
                row[1] = id
                row[2] = student.get('first_name')
                row[3] = student.get('last_name')
                for id_list in randomized_lists:
                    if(id in id_list):
                        row.append("X")
                    else:
                        row.append("")
                print_list.append(row)

            for i in range(0, len(randomized_lists)):
                column_names.append('WEEK ' + str(i+1))

            # Print Sheet
            sheet_data = pd.DataFrame(print_list, columns=column_names)
            sheet_data.to_excel(writer, index=False, sheet_name=sheet)


###
# Main function/loop
###
def file_worker(student_dict, import_dir, export_dir, import_file_list, export_file_list):
    if(import_file_list):
        for file in import_file_list:
            # Declaring import and export file Path
            import_file_address = import_dir + "\ " + file
            import_file_address = import_file_address.replace(" ", "")

            export_file_address = export_dir + "\ " + file
            export_file_address = export_file_address.replace(" ", "")

            # File Import
            student_dict = read_to_dict_from_excel(
                import_file_address)

            # File Export aka writing
            export_file_list = create_file_list_from_directory(
                export_dir, "export")

            if (file in export_file_list):
                ## print(file, "was found!")
                continue

            for sheet in student_dict:
                # declare the variables
                student_id_list = []
                selected_students = []
                sheet_info = student_dict.get(sheet)

                weeks = sheet_info['weeks']
                num_chosen_student = sheet_info['num_chosen_student']
                num_chosen_times = sheet_info['num_chosen_time']

                # Processing
                # Generates a list of ids from the dict based on keys
                student_id_list = get_key_to_list(
                    sheet_info['students_info'])

                while(True):
                    try:
                        selected_students = generate_randomised_list(
                            student_id_list, weeks, num_chosen_student, num_chosen_times)
                    except:
                        # case: 27ids 9selected 9weeks 3times
                        ## print("Randomization timed out due to tight lists, retrying...")
                        continue
                    else:
                        break

                student_dict[sheet]['randomized'] = selected_students

            # Write sheets to the file
            try:
                write_to_file(student_dict, export_dir + "\ " + file)
            except PermissionError:
               # print("File is being opened! Please close the file named",
               # file, "and rerun the program!")
                continue


import_dir = r"./import"
export_dir = r"./export"
import_file_list = create_file_list_from_directory(import_dir, "import")
export_file_list = []
file_worker(student_dict, import_dir, export_dir,
            import_file_list, export_file_list)
# Debugging code to count the number of times X id appeared in the list
#   print(sheet)
#   for student_id in student_id_list:
#       count = runs.count(student_id)
#       print(student_id, "appeared:", count, "times")

# Very gross code that generate randomized element for lists within list
#      base_n_random_gen_for_all(
#          student_id_list, runs, num_chosen_student, num_chosen_times)
#      selected_students = [runs[student:student+num_chosen_student]
#                           for student in range(0, len(runs), num_chosen_student)]

# Old generation method, has dupes in arr
# def base_n_random_gen_for_all(students, runs, num_of_students, times):
#   # Initial generation
#   for student in students:
#       for _ in range(times):
#           while True:
#               rand_index = random.randint(0, len(runs))
#               start_of_row = rand_index - rand_index % num_of_students
#               end_of_row = start_of_row + num_of_students
#               if student not in runs[start_of_row:end_of_row]:
#                   # student isn't in the row yet, so add them to the run bc they aren't appearing twice in the run.
#                   runs[rand_index-1] = student
#                   break
#
#   # Filler code to fill the remaining None in the list
#   # keeps track of the number of students counted to n times
#   student_counted_to_time_list = []
#   while None in runs:
#       for student in students:
#           count_for_student = runs.count(student)
#           rand_index = random.randint(0, len(runs))
#           if(count_for_student < times) and runs[rand_index-1] is None:
#               runs[rand_index-1] = student
#           if(count_for_student == times) and student not in student_counted_to_time_list:
#               student_counted_to_time_list.append(student)
#           if(len(student_counted_to_time_list) == len(students)) and runs[rand_index-1] is None:
#               runs[rand_index-1] = student
#
