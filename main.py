import admin as ad
import view as v
import log_in as lgn
import add_to_file as add_f
import add_users as adus
import teacher as t


enter = 1
while enter in range(1, 3):
    v.ask_to_fill(
        "\n 1 - У вас уже есть логин и пароль\n 2 - Вы еще не зарегистрированы")
    enter = int(v.get_info())
    if enter == 1:
        v.ask_to_fill("логин")
        login = v.get_info()
        v.ask_to_fill("пароль")
        password = v.get_info()
        user_data_list = lgn.login_check(login, password)
        if not user_data_list:
            break
        else:
            print(
                f"\nДобро пожаловать {user_data_list[0]} {user_data_list[1]}")
            user_menu = 1
            role = user_data_list[2]
            if role == "admin":
                admin = 1
                while admin in range(1, 5):
                    v.ask_to_fill(
                        "\n 1 - просмотреть новых пользователей\n 2 - удалить пользователя\n 3 - добавить новых пользователей\n 4 -выход")
                    admin = int(v.get_info())
                    if admin == 1:
                        v.print_list(ad.from_csv_to_list("sign_in.csv"))
                    elif admin == 2:
                        ad.delete_user()
                    elif admin == 3:
                        add_f.add_list_to_file(ad.from_csv_to_list(
                            "sign_in.csv"), "users.csv", "a", ",")
                        ad.del_from_sign_in()
                    elif admin == 4:
                        break
            elif role == "teacher":
                teacher = 1
                while teacher in range(1, 5):
                    v.ask_to_fill(
                        "\n 1 - добавить домашнее задание по предметам\n 2 - посомтреть комментарии\n 3 - добавить комментарии \n 4 -выход")
                    teacher = int(v.get_info())
                    if teacher == 1:
                        t.add_home_work()
                    if teacher == 2:
                        t.check_home_work()
                    if teacher == 3:
                        t.chat_add_comments(user_data_list[0],user_data_list[1])
                    if teacher == 4:
                        break
            elif role == "student":
                student = 1
                while student in range(1, 4):
                    v.ask_to_fill(
                        "\n 1 - посмотреть домашнее задание по предметам и комментарии\n 2 - добавить комментарии\n 3 -выход")
                    student = int(v.get_info())
                    if student == 1:
                        t.check_home_work()
                    if student == 2:
                        t.chat_add_comments(user_data_list[0],user_data_list[1])
                    if student == 3:
                        break
    elif enter == 2:
        add_f.add_to_file(adus.sign_in(), "sign_in.csv", "a", ",")
        print("Ожидайте, когда администратор проверит вашу информацию")
        break
