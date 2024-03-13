filename='student.txt'
def main():
    while True:
        menum()
        choice=int(input('请选择：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗?y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delect()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                totol()
            elif choice==7:
                show()


def menum():
    print('==================学生信息管理系统=====================')
    print('------------------功能菜单------------------------')
    print('               1.录入学生信息')
    print('               2.查找学生信息')
    print('               3.删除学生信息')
    print('               4.修改学生信息')
    print('               5.对学生成绩排序')
    print('               6.统计学生总人数')
    print('               7.显示所有学生成绩')
    print('               0.退出')

def insert():
    student_list=[]
    while True:
        id=input('请输入id:')
        if not id:
            break
        name=input('请输入name:')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            java=int(input('请输入java成绩:'))
        except:
            print('请重新输入')
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y':
            continue
        else:
            break

    save(student_list)
    print('学生信息录入完毕！！！')

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    pass

def delect():
    pass

def modify():
    pass

def sort():
    pass

def totol():
    pass

def show():
    pass
if __name__ == '__main__':
    main()