import admin as ad


def login_check(login, password):
    new_list = ad.from_csv_to_list("users.csv")
    logined_list=[]
    for i, j in enumerate(new_list):
        if j[2] == login and j[3] == password:
            logined_list.append(j[0])
            logined_list.append(j[1])
            logined_list.append(j[4])
        else:
            continue
    if not logined_list:
        print("логин и пароль не найдены, сначала зарегистрируйтесь")
    return logined_list
    
     


# print(login_check("lavan","pass"))
