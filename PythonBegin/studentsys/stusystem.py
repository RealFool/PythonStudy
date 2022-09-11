# 李亚钦
# 2022/7/24 18:51
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in range(8):
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用!')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
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


def menu():
    print('============================学生信息管理系统=============================')
    print('-------------------------------功能菜单---------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('----------------------------------------------------------------------')


def insert():
    student_list = []
    while True:
        stu_id = input('请输入ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except ValueError:
            print('输入无效，成绩不是整数类型，请重新输入！')
            continue
        # 将信息保存在字典中
        student = {'stu_id': stu_id, 'name': name, 'English': english, 'Python': python, 'Java': java}
        # 将学生信息添加到列表
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break
    # 录入完毕写入文件
    save(student_list)
    print('学生信息录入完毕')


def save(lst):
    try:
        with open(filename, 'a', encoding='UTF-8') as file:
            for i in lst:
                file.write(str(i) + '\n')
    except BaseException as e:
        print(e)


def search():
    student_query = []
    while True:
        stu_id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                stu_id = input('请输入学生ID：')
            elif mode == '2':
                name = input('请输入学生姓名：')
            else:
                print('您的输入有误，请重新输入')
                continue
            with open(filename, 'r', encoding='utf-8') as file_r:
                students = file_r.readlines()
                for item in students:
                    w = dict(eval(item))
                    if stu_id:
                        if w.get('stu_id') == stu_id:
                            student_query.append(w)
                    elif name:
                        if w.get('name') == name:
                            student_query.append(w)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('stu_id'),
                                 item.get('name'),
                                 item.get('English'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('English')) + int(item.get('Python')) + int(item.get('Java'))
                                 ))


def delete():
    show()
    while True:
        stu_id = input('请输入要删除的学生ID：')
        if stu_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as file_w:
                    w = {}
                    for item in student_old:
                        w = dict(eval(item))
                        if w.get('stu_id') != stu_id:
                            file_w.write(str(w) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'ID为{stu_id}的学生信息已删除')
                    else:
                        print(f'没有找到ID为{stu_id}的学生信息')
            else:
                print('无学生信息！')
                break
            show()  # 删完之后重新显示学生信息
            answer = input('是否继续删除学生信息？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file_r:
            student_old = file_r.readlines()
    else:
        print('文件不存在')
        return
    stu_id = input('请输入要修改的学生ID：')
    with open(filename, 'w', encoding='utf-8') as file_w:
        for item in student_old:
            w = dict(eval(item))
            flag = False  # 要修改的学生信息是否存在标识
            id_get = w.get('stu_id')
            if id_get == stu_id:
                flag = True
                while True:
                    print('开始修改该学生信息：')
                    try:
                        w['name'] = input('请输入学生姓名')
                        w['English'] = int(input('请输入英语成绩：'))
                        w['Python'] = int(input('请输入Python成绩：'))
                        w['Java'] = int(input('请输入Java成绩：'))
                    except ValueError:
                        print('输入无效，成绩不是整数类型，请重新输入！')
                        continue
                    else:
                        break
                file_w.write(str(w) + '\n')
            else:
                file_w.write(item)
    if flag:
        print('修改成功!')
    else:
        print('该学生信息不存在')
    answer = input('是否还要继续修改其他学生信息?y/n\n')
    if answer == 'y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_list = file.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择（0.升序   1.降序）')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    model = input('请选择排序方式（1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序）：')
    if model == '1':
        student_new.sort(key=lambda i: int(i.get('English')), reverse=asc_or_desc_bool)
    elif model == '2':
        student_new.sort(key=lambda i: int(i.get('Python')), reverse=asc_or_desc_bool)
    elif model == '3':
        student_new.sort(key=lambda i: int(i.get('Java')), reverse=asc_or_desc_bool)
    elif model == '0':
        student_new.sort(key=lambda i: int(i.get('English') + int(i.get('Python')) + int(i.get('Java'))), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_new)
    answer = input('是否还要继续继续排序?y/n\n')
    if answer == 'y':
        sort()

def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            print(f'一共有{len(students)}名学生')
    else:
        print('暂无学生信息，就录入！')


def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            students = file.readlines()
            for item in students:
                student_list.append(dict(eval(item)))
            if student_list:
                show_student(student_list)
            else:
                print('无学生信息!')
    else:
        print('暂未保存学生信息，请录入！')


if __name__ == '__main__':
    main()
