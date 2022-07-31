import os
filename = 'student.txt'
def main():
    while True:
        menum()
        choice = int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用!')
                    break
                else:
                    continue
            if choice == 1:
                insert()
            if choice == 2:
                search()
            if choice == 3:
                delete()
            if choice == 4:
                modify()
            if choice == 5:
                sort()
            if choice == 6:
                total()
            if choice == 7:
                show()
            else:
                pass
def menum():
    print('==================学生管理系统==================')
    print('--------------------功能菜单-------------------')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出系统')
    print('---------------------------------------------')

def insert():
    student_list = []
    while True:
        no = int(input('请输入学号：'))
        if not no:
            break
        name = input('请输入姓名：')
        if not  name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
        except:
            print('输入无效，请重新输入')
            continue
        student = {
            'no': no,
            'name': name,
            'english': english,
            'python': python
        }

        student_list.append(student)

        answer = input('是否继续添加？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

        #输入学生信息完成之后保存信息
    save(student_list)

def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    pass

def delete():
    while True:
        stu_id = input('请输入要删除的学号：')
        if stu_id != '':
            stu_id = int(stu_id)
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    stu_old = file.readlines()
            else:
                stu_old = []
            flag = False
            if stu_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d = {}
                    for item in stu_old:
                        d = dict(eval(item))
                        print(stu_id)
                        print(d)
                        if d['no'] != stu_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'学号为{stu_id}的学生已删除')
                    else:
                        print(f'没有找到学号为{stu_id}的学生')
            else:
                print('没有该学生信息')
                break

            show()

            answer = input('是否继续删除？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('没有输入学号')
            break

def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass

if __name__ == '__main__':
    main()