import json

def search(number_contact: str) -> dict:
    with open("phone_book.json", "r+") as jsonbook:
        jsonbookserializ = json.load(jsonbook)
        return jsonbookserializ[number_contact]

def add():
    with open("../phone_book.json", "r+") as jsonbook:
        jsonbookserializ = json.load(jsonbook)
        number, first_name, last_name, city = input("Number contact"), input("First name"), input("Last name"),\
                                                  input("City")
        jsonbookserializ.update({number :
                                     {"first_name" : first_name,
                                      "last_name" : last_name,
                                      "full_name" : last_name+" "+first_name,
                                      "city" : city}})
        jsonbook.seek(0)
        jsonbook.truncate(0)
        json.dump(jsonbookserializ, jsonbook, indent = 1)

def delete():
    while True:
        with open("../phone_book.json", "r+") as jsonbook:
            jsonbookserializ = json.load(jsonbook)
            quest_answear = input("""You want delete for:
    number, type "number"
    First Name, type "firstname"
    Last Name, type "lastname"
    City, type "city"
                                    """).lower()
            if quest_answear == "number":
                search_delete = input("\nPlease, input contact's number:").lower()
                for delete_for in jsonbookserializ:
                    if delete_for == search_delete:
                        answear = input(f"\nYou really want delete {delete_for, jsonbookserializ[delete_for]}?\nType: Yes or Not:\n").lower()
                        if answear == "yes":
                            print(f"Number {delete_for} succsesfull deleted!")
                            jsonbookserializ.pop(delete_for)
                            jsonbook.seek(0)
                            jsonbook.truncate(0)
                            json.dump(jsonbookserializ, jsonbook, indent=1)
                            return
                        else:
                            print("Okey, it's number not deleted")
            elif quest_answear == "firstname":
                search_delete = input("\nPlease, input contact's First Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["first_name"].lower():
                            answear = input(
                                f"\nYou really want delete {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear == "yes":
                                print(f"Number {jsonbookserializ[search_con]} succsesfull deleted!")
                                jsonbookserializ.pop(search_con)
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            elif quest_answear == "lastname":
                search_delete = input("\nPlease, input contact's Last Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["last_name"].lower():
                            answear = input(
                                f"\nYou really want delete {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear == "yes":
                                print(f"Number {jsonbookserializ[search_con]} succsesfull deleted!")
                                jsonbookserializ.pop(search_con)
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            elif quest_answear == "fullname":
                search_delete = input("\nPlease, input contact's Full Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["full_name"].lower():
                            answear = input(
                                f"\nYou really want delete {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear == "yes":
                                print(f"Number {jsonbookserializ[search_con]} succsesfull deleted!")
                                jsonbookserializ.pop(search_con)
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            if True:
                ans = input("contact doesnt search\n Maybe you want search again?\n Type \"yes\" or \"not\"").lower
                if ans == "yes": continue
                if ans == "not": return

def udpate_contacts():
    while True:
        with open("../phone_book.json", "r+") as jsonbook:
            jsonbookserializ = json.load(jsonbook)
            quest_answear = input("""You want update for:
    number, type "number"
    First Name, type "firstname"
    Last Name, type "lastname"
    City, type "city"
                                    """).lower()
            if quest_answear == "number":
                search_delete = input("\nPlease, input contact's number:").lower()
                for delete_for in jsonbookserializ:
                    if delete_for == search_delete:
                        answear = input(f"\nYou really want update {delete_for, jsonbookserializ[delete_for]}?\nType: Yes or Not:\n").lower()
                        if answear == "yes":
                            new_number = input("Which number be new?")
                            old_dic = ({new_number : jsonbookserializ[delete_for]})
                            print(old_dic)
                            jsonbookserializ.pop(delete_for)
                            print(f"Number succsesfull updated!")
                            jsonbookserializ.update(old_dic)
                            jsonbook.seek(0)
                            jsonbook.truncate(0)
                            json.dump(jsonbookserializ, jsonbook, indent=1)
                            return
                        else:
                            print("\nOkey, it's number not deleted")
            elif quest_answear == "firstname":
                search_delete = input("\nPlease, input contact's First Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["first_name"].lower():
                            answear = input(
                                f"\nYou really want update {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear == "yes":
                                new_number = input("\nWhich First Name be new?")
                                jsonbookserializ[search_con]["first_name"] = new_number
                                print(f"\nNumber succsesfull updated!")
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            elif quest_answear == "lastname":
                search_delete = input("\nPlease, input contact's Last Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["last_name"].lower():
                            answear = input(
                                f"\nYou really want update {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear == "yes":
                                new_number = input("\nWhich Last Name be new?")
                                jsonbookserializ[search_con]["last_name"] = new_number
                                print(f"\nNumber succsesfull updated!")
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            elif quest_answear == "fullname":
                search_delete = input("\nPlease, input contact's Full Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["full_name"].lower():
                            answear = input(
                                f"\nYou really want update {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear ==     "yes":
                                new_number = input("\nWhich First Name be new?")
                                jsonbookserializ[search_con]["full_name"] = new_number
                                print(f"\nNumber succsesfull updated!")
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            elif quest_answear == "city":
                search_delete = input("\nPlease, input contact's City:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["city"].lower():
                            answear = input(f"\nYou really want update {search_con, jsonbookserializ[search_con]}?\nType: Yes or Not:\n").lower()
                            if answear == "yes":
                                new_number = input("\nWhich City be new?")
                                jsonbookserializ[search_con]["city"] = new_number
                                print(f"\nNumber succsesfull updated!")
                                jsonbook.seek(0)
                                jsonbook.truncate(0)
                                json.dump(jsonbookserializ, jsonbook, indent=1)
                                return
                            elif answear == "not":
                                continue
            else:
                ans = input("contact doesnt search\n Maybe you want search again?\n Type \"yes\" or \"not\"").lower
                if ans == "yes": continue
                if ans == "not": return
