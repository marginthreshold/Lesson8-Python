import view as v
import add_to_file as add_f


def sign_in():
    role = 0
    new_list = []
    while role not in range(1, 3):
        v.ask_to_fill("\n 1 - Если вы учитель\n 2 - Если вы ученик")
        role = int(v.get_info())
    if role == 1:
        user_role = "teacher"
    else:
        user_role = "student"
    v.ask_to_fill("фамилию")
    new_list.append(v.get_info())
    v.ask_to_fill("имя")
    new_list.append(v.get_info())
    v.ask_to_fill("loggin")
    new_list.append(v.get_info())
    v.ask_to_fill("пароль")
    new_list.append(v.get_info())
    new_list.append(user_role)
    return list(new_list)


#add_f.add_to_file(sign_in(), "sign_in.csv", "a", ",")
