'''
@Project :Student Information Management System
@File    :stusystem.py
@Author  :Sunshine
@Date    :30/09/2023 13:36
'''

import time
import os

file_name = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('Please Select: '))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('Are you sure you want to log out of the system?\ny/n\n')
                if answer == 'y' or answer == 'Y':
                    print('Thank you for your use!!!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()

            elif choice == 2:
                search()

            elif choice == 3:
                delete()

            elif choice == 4:
                modify()

            elif choice == 5:
                sort()

            elif choice == 6:
                total()

            elif choice == 7:
                show()

        else:
            print('\n\nThis option is not available, please select again! \n')
            time.sleep(1)


def menu():
    print('================ Student Information Management System =================')
    print('------------------------------- Function Menu --------------------------------')
    print('\t\t\t\t\t\t1. Record Student Information')
    print('\t\t\t\t\t\t2. Search Student Information')
    print('\t\t\t\t\t\t3. Delete Student Information')
    print('\t\t\t\t\t\t4. Modify Student Information')
    print('\t\t\t\t\t\t5. Sort')
    print('\t\t\t\t\t\t6. Statistics of the total number of students')
    print('\t\t\t\t\t\t7. Show all student information')
    print('\t\t\t\t\t\t0. Exist')
    print('----------------------------------------------------------------------------------------')


def insert():
    student_lst = []
    while True:
        id = input('Please Enter Student ID (for example: 1001)\n')
        if not id:
            break
        with open(file_name, 'r', encoding='utf-8') as rf:
            student_info = rf.readlines()
            # print(student_info)
            id_lst = []
            for i in student_info:
                d = dict(eval(i))
                id_lst.append(d['id'])
            id_lst.sort()
            last_id = id_lst[-1]
        if id in id_lst:
            print(f'This ID has been used, the last ID used is {last_id}\n')
            time.sleep(1)
            return
        else:
            name = input('Please Enter Student Name\n')
            if not name:
                break

            try:
                englst = int(input('Please Enter Student\'s English Score\n'))
                python = int(input('Please Enter Studet\'s Python Score\n'))
                java = int(input('Please Enter Studet\'s Java Score\n'))
            except:
                print('Invalid input, not an integer type, please re-enter \n')

        student = {'id': id, 'name': name, 'english': englst, 'python': python, 'java': java}
        student_lst.append(student)
        answer = input('Do you want to continue adding?\ny/n\t')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    save(student_lst)
    print('Student information entry completed!!!')


def save(lst):
    try:
        student_txt = open(file_name, 'a', encoding='utf-8')
    except:
        student_txt = open(file_name, 'w', encoding='utf-8')
    for item in lst:
        student_txt.write(str(item) + '\n')
    student_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
            choice = int(input('Search by ID, please enter 1; Search by name, please enter 2: '))
            if choice == 1:
                id = input('Please Enter Student ID: ')
            elif choice == 2:
                name = input('Please Enter Student Name: ')
            else:
                print('Invalid Input, Please re-enter.')
                search()
            with open(file_name, 'r', encoding='utf-8') as rf:
                student = rf.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name or d['name'].upper() == name or d['name'].lower() == name:
                            student_query.append(d)

            show_student(student_query)
            student_query.clear()
            answer = input('Do you want to continue querying?\ny/n\t')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('Student information not saved yet')
            return


def show_student(lst):
    if len(lst) == 0:
        print('No student information was found, no data displayed!!!')
        return

    format_tile = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_tile.format('ID', 'Name', 'English Score', 'Python Score', 'Java Score', 'Total Score'))

    format_data = '{:^6}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^6}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


def delete():
    while True:
        student_id = input('Please enter the ID of the student you want to delete: ')
        if student_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as f:
                    student_old = f.readlines()
            else:
                student_old = []

            flag = False
            if student_old:
                with open(file_name, 'w', encoding='utf-8') as wf:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wf.write(str(d) + '\n')
                        else:
                            flag = True

                    if flag:
                        print(f'The student information with ID {student_id} has been deleted')
                    else:
                        print(f'No student information found with ID {student_id}')
            else:
                print('No student information recorded.')
                break
            show()

            answer = input('Do you want to continue deleting? \ny/n\t')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rf:
            student_old = rf.readlines()
    else:
        return

    student_id = input('Please enter the ID of the student you want to modify: ')
    with open(file_name, 'w', encoding='utf-8') as wf:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('The student information is found, you can modify it.')
                while True:
                    try:
                        d['name'] = input('Please Enter Student Name: ')
                        d['english'] = int(input('Please Enter Student\'s English Score: '))
                        d['python'] = int(input('Please Enter Studet\'s Python Score: '))
                        d['java'] = int(input('Please Enter Studet\'s Java Score: '))
                    except:
                        print('Your input is incorrect, please re-enter')
                    else:
                        break
                wf.write(str(d) + '\n')
                print('Modify Success!!!')
            else:
                wf.write(str(d) + '\n')

        answer = input('Do you want to continue modifying other student information? \ny/n\t')
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rf:
            student_list = rf.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return

    asc_or_desc = input('Please select (0. ascending order 1. descending order):')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('Your input is incorrect, please re-enter')
        sort()

    mode = input('Please select the sorting method\n'
                 '1.Sort by English score \n'
                 '2.Sort by Python score\n'
                 '3.Sort by Java score\n'
                 '0.Sort by Total score\n')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('Your input is wrong, please re-enter!!!')
        sort()
    show_student(student_new)
    time.sleep(2)


def total():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rf:
            students = rf.readlines()
            if students:
                print(f'There are {len(students)} students in total.')
            else:
                print('No student information has been entered yet.')
    else:
        print('No data saved yet...')


def show():
    student_list = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rf:
            student = rf.readlines()
            for item in student:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)
    else:
        print('No data saved yet')


if __name__ == '__main__':
    main()
