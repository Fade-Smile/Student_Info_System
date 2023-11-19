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
        choice = int(input('Please Select （请选择）: '))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('Are you sure you want to log out of the system?\n'
                               '(您确定要退出系统吗？) \ny/n ')
                if answer =='y' or answer =='Y':
                    print('Thank you for your use!!! \n(谢谢您的使用!!!)')
                    break # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息

            elif choice == 2:
                search()  # 查找学生信息

            elif choice == 3:
                delete()  # 删除学生信息

            elif choice == 4:
                modify()  # 修改学生信息

            elif choice == 5:
                sort()  # 对学生成绩排序

            elif choice == 6:
                total()  # 统计学生总人数

            elif choice == 7:
                show()  # 显示所有学生信息

        else:
            print('\n\nThis option is not available, please select again! \n'
                  '(没有该选项, 请重新选择!)\n\n')
            time.sleep(1)

def menu():
    print('================ Student Information Management System (学生信息管理系统)=================')
    print('------------------------------- Function Menu (功能菜单) --------------------------------')
    print('\t\t\t\t\t\t1. Record Student Information (录入学生信息)')
    print('\t\t\t\t\t\t2. Search Student Information (查找学生信息)')
    print('\t\t\t\t\t\t3. Delete Student Information (删除学生信息)')
    print('\t\t\t\t\t\t4. Modify Student Information (修改学生信息)')
    print('\t\t\t\t\t\t5. Sort (排序)')
    print('\t\t\t\t\t\t6. Statistics of the total number of students (统计学生总人数)')
    print('\t\t\t\t\t\t7. Show all student information (显示所有学生信息)')
    print('\t\t\t\t\t\t0. Exist (退出)')
    print('----------------------------------------------------------------------------------------')

def insert():
    student_lst = []
    while True :
        id = input('Please Enter Student ID(For example: 1001)\n'
                   '(请输入学号（例如：1001）): ')
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
            last_id= id_lst[-1]
        if id in id_lst:
            print(f'This ID has been used, the last ID used is {last_id}\n'
                  f'(该ID已被使用, 最后一个被使用的ID为{last_id})')
            time.sleep(1)
            return
        else:
            name = input('Please Enter Student Name\n(请输入学生姓名): ')
            if not name:
                break

            try:
                englst = int(input('Please Enter Student\'s English Score\n'
                                   '(请输入学生的英语成绩): '))
                python = int(input('Please Enter Studet\'s Python Score\n'
                                   '(请输入学生的Python成绩): '))
                java = int(input('Please Enter Studet\'s Java Score\n'
                                 '(请输入学生的Java成绩): '))
            except:
                print('Invalid input, not an integer type, please re-enter \n'
                      '(输入无效，不是整数类型，请重新输入)')

        #  将录入的学生信息保存到字典里
        student = {'id': id, 'name':name, 'english':englst, 'python':python, 'java':java}
        #  将学生信息添加到列表中
        student_lst.append(student)
        answer=input('Do you want to continue adding?\n'
                     '(是否继续添加？) \ny/n\t')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    save(student_lst)
    print('Student information entry completed!!!\n'
          '(学生信息录入完毕!!!）')

def save(lst):
    try:
        student_txt= open(file_name, 'a', encoding='utf-8')
    except:
        student_txt= open(file_name, 'w', encoding='utf-8')
    for item in lst:
        student_txt.write(str(item)+'\n')
    student_txt.close()

def search():
    student_query=[]
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
           choice = int(input('To search by ID, please enter 1, to search by name, please enter 2'
                              '\n(按ID查找请输入1， 按姓名查找请输入2): '))
           if choice == 1:
               id = input('Please Enter Student ID(请输入学生ID): ')
           elif choice == 2:
               name = input('Please Enter Student Name(请输入学生姓名): ')
           else:
               print('Invalid Input, Please re-enter.')
               search()
           with open(file_name, 'r', encoding='utf-8') as rf:
               student = rf.readlines()
               for item in student:
                   d = dict(eval(item))
                   if id !='':
                       if d['id'] == id:
                           student_query.append(d)
                   elif name !='':
                       if d['name'] == name or d['name'].upper() == name or d['name'].lower() == name:
                           student_query.append(d)

           # 显示查询结果
           show_student(student_query)
           # 清空列表
           student_query.clear()
           answer = input('Do you want to continue querying?\n'
                          '(是否继续查询？)\ny/n\t')
           if answer == 'y' or answer == 'Y':
                continue
           else:
                break
        else:
            print('Student information not saved yet \n'
                  '(暂未保存学生信息)')
            return

def show_student(lst):
    if len(lst) == 0:
        print('No student information was found, no data displayed!!!\n'
              '(没有查询到学生信息， 无数据显示!!!)')
        return
    # 定义标题显示格式
    format_tile='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_tile.format('ID','Name(姓名)','English Score(英语成绩)','Python Score(Python成绩)','Java Score(Java成绩)','Total Score(总成绩）'))

    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^20}\t{:^24}\t{:^24}\t{:^14}'
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
        student_id = input('Please enter the ID of the student you want to delete \n'
                           '(请输入要删除的学生的ID): ')
        if student_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as f:
                    student_old = f.readlines()
            else:
                student_old = []

            flag = False  # 标记是否删除
            if student_old:
                with open(file_name, 'w', encoding='utf-8') as wf:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item)) #将字符串转成字典
                        if d['id'] != student_id:
                            wf.write(str(d)+'\n')
                        else:
                            flag = True

                    if flag:
                        print(f'The student information with ID {student_id} has been deleted \n '
                              f'(ID 为{student_id}的学生信息已被删除)')
                    else:
                        print(f'No student information found with ID {student_id}\n'
                              f'(没有找到ID为{student_id}的学生信息)')
            else:
                print('No student information recorded. \n'
                      '(无学生信息)')
                break
            show() # 删除后要重新显示所有学生信息

            answer = input('Do you want to continue deleting? \n'
                           '(是否继续删除？) \ny/n\t')
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


    student_id = input('Please enter the ID of the student you want to modify \n'
                           '(请输入要修改的学生的ID): ')
    # if student_id not in student_old:
    #     print('该学生没有入录到系统中， 请重新输入.')
    with open(file_name, 'w', encoding='utf-8') as wf:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('The student information is found, you can modify it.'
                      '\n(找到学生信息，可以修改他的相关信息了)')
                while True:
                    try:
                        d['name'] = input('Please Enter Student Name\n(请输入学生姓名): ')
                        d['english'] = int(input('Please Enter Student\'s English Score\n'
                                   '(请输入学生的英语成绩): '))
                        d['python'] = int(input('Please Enter Studet\'s Python Score\n'
                                   '(请输入学生的Python成绩): '))
                        d['java'] = int(input('Please Enter Studet\'s Java Score\n'
                                 '(请输入学生的Java成绩): '))
                    except:
                        print('Your input is incorrect, please re-enter\n'
                              '(您的输入有误，请重新输入!!!)')
                    else:
                        break
                wf.write(str(d) + '\n')
                print('Modify Success!!!'
                      '\n(修改成功!!!)')
            else:
                wf.write(str(d) + '\n')

        answer = input('Do you want to continue modifying other student information? \n'
                       '(是否继续修改其他学生信息)\ny/n\t')
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

    asc_or_desc = input('请选择(0.升序 1.降序):')
    if asc_or_desc =='0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('Your input is incorrect, please re-enter\n'
              '(您的输入有误，请重新输入)')
        sort()

    mode = input('Please select the sorting method(请选择排序方式)\n'
                             '1.Sort by English score(按英语成绩排序) \n'
                             '2.Sort by Python score(按Python成绩排序)\n'
                             '3.Sort by Java score(按Java成绩排序)\n'
                             '0.Sort by Total score(按总成绩排序)\n')
    if mode == '1':
        student_new.sort(key = lambda x: int(x['english']), reverse = asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key = lambda x: int(x['python']), reverse = asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key = lambda x: int(x['java']), reverse = asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key = lambda x: int(x['english'])+int(x['python'])+int(x['java']), reverse = asc_or_desc_bool)
    else:
        print('Your input is wrong, please re-enter!!!\n'
              '(您的输入有误， 请重新输入!!!)')
        sort()
    show_student(student_new)
    time.sleep(2)

def total():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rf:
            students=rf.readlines()
            if students:
                print(f'There are {len(students)} students in total.\n'
                      f'(一共有{len(students)}名学生)')
            else:
                print('No student information has been entered yet.\n'
                      '(还没有录入学生信息)')
    else:
        print('No data saved yet...\n'
              '(暂未保存数据信息...)')

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
        print('No data saved yet\n'
              '(暂未保存数据信息)')


if __name__ == '__main__':
    main()

