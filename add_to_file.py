import codecs


def add_to_file(list,file_name, write_method,sep):
    with codecs.open(file_name, write_method, "utf-8") as file:
            file.writelines(sep.join(list))

def add_list_to_file(contact_list, contact_file_name, write_method,sep):
    with codecs.open(contact_file_name, write_method, "utf-8") as all_contacts_file:
        for line in contact_list:
            all_contacts_file.writelines(sep.join(list(map(str, line))))
            all_contacts_file.writelines("\n")           