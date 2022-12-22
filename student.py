import admin as ad
import view as v


def check_home_work():
    v.print_list(ad.from_csv_to_list_with_first_row("chat_teacher_student.csv"))

#check_home_work()