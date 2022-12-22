import codecs
import add_to_file as add_f
import view as v
import csv



def from_csv_to_list(file_name):
    with codecs.open(file_name, "r", "utf-8") as file:
        reader = csv.reader(file, skipinitialspace=True)
        rows = list(reader)
    rows.pop(0)
    return rows

def from_csv_to_list_with_first_row(file_name):
    with codecs.open(file_name, "r", "utf-8") as file:
        reader = csv.reader(file, skipinitialspace=True)
        rows = list(reader)
    return rows

def delete_user():
    v.print_list(from_csv_to_list("sign_in.csv"))
    check_list = from_csv_to_list("sign_in.csv")
    v.ask_to_fill("кого вы хотите удалить")
    to_delete = (v.get_info())
    for i in check_list:
        if i.count(to_delete) > 0:
            check_list.remove(i)
    check_list.insert(0,["Фамилия,Имя,login,password,role"])
    add_f.add_list_to_file(check_list,"sign_in.csv", "w", ",")

def del_from_sign_in():
    rewrite_list=[["Фамилия,Имя,login,password,role"]]
    add_f.add_list_to_file(rewrite_list,"sign_in.csv", "w", ",")

#del_from_sign_in()
#delete_user()

#add_f.add_list_to_file(from_csv_to_list("sign_in.csv"), "users.csv", "a", ",")
