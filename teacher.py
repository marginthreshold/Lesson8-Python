import admin as ad
import view as v
import add_to_file as add_f


def add_home_work():
    subjects_list = ad.from_csv_to_list("school subject.csv")
    for i in subjects_list:
        v.ask_to_fill(f"задание по предмету {i}")
        i.append(v.get_info())
    add_f.add_list_to_file(subjects_list, "chat_teacher_student.csv", "w", ",")
    


def chat_add_comments(name, second_name):
    chat_list = ad.from_csv_to_list_with_first_row("chat_teacher_student.csv")
    for i in chat_list:
        v.ask_to_fill(f"комментарий по предмету {i}")
        i.append(name+" "+second_name+" "+v.get_info())
    add_f.add_list_to_file(chat_list, "chat_teacher_student.csv", "w", ",")
    


def check_home_work():
    chat_list = v.print_list(ad.from_csv_to_list_with_first_row("chat_teacher_student.csv"))





#add_home_work()
#check_home_work()