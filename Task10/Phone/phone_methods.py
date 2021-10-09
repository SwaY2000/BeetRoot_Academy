import json

def search(number_contact: str):
    """Search number contact"""
    with open("phone_book.json", "r+") as jsonbook:
        jsonbookserializ = json.load(jsonbook)
        print(jsonbookserializ[number_contact])
        return jsonbookserializ[number_contact]

def add(number: str, first_name: str, last_name: str, city: str):
    """Add in phonebook new number"""

    with open("phone_book.json", "r+") as jsonbook:
        jsonbookserializ = json.load(jsonbook)
        jsonbookserializ.update({number :
                                     {"first_name" : first_name,
                                      "last_name" : last_name,
                                      "full_name" : last_name+" "+first_name,
                                      "city" : city}})
        jsonbook.seek(0)
        jsonbook.truncate(0)
        json.dump(jsonbookserializ, jsonbook, indent = 1)

def delete(quest_answear:str, search_delete:str):
    """Delete contact in phonebook"""
    while True:
        with open("phone_book.json", "r+") as jsonbook:
            jsonbookserializ = json.load(jsonbook)
            if quest_answear == "number":
                for delete_for in jsonbookserializ:
                    if delete_for == search_delete:
                        print(f"Number {delete_for} succsesfull deleted!")
                        jsonbookserializ.pop(delete_for)
                        jsonbook.seek(0)
                        jsonbook.truncate(0)
                        json.dump(jsonbookserializ, jsonbook, indent=1)
                        return
                    else:
                        return 'Number not found'

            elif quest_answear == "firstname":
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["first_name"].lower():
                            print(f"Number {jsonbookserializ[search_con]} succsesfull deleted!")
                            jsonbookserializ.pop(search_con)
                            jsonbook.seek(0)
                            jsonbook.truncate(0)
                            json.dump(jsonbookserializ, jsonbook, indent=1)
                            return

            elif quest_answear == "lastname":
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["last_name"].lower():
                            print(f"Number {jsonbookserializ[search_con]} succsesfull deleted!")
                            jsonbookserializ.pop(search_con)
                            jsonbook.seek(0)
                            jsonbook.truncate(0)
                            json.dump(jsonbookserializ, jsonbook, indent=1)
                            return

            elif quest_answear == "fullname":
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["full_name"].lower():
                            print(f"Number {jsonbookserializ[search_con]} succsesfull deleted!")
                            jsonbookserializ.pop(search_con)
                            jsonbook.seek(0)
                            jsonbook.truncate(0)
                            json.dump(jsonbookserializ, jsonbook, indent=1)
                            return

def update_contacts(quest_answear, search_update, new):
    """Update contact in phonebook"""
    while True:
        with open("phone_book.json", "r+") as jsonbook:
            jsonbookserializ = json.load(jsonbook)
            if quest_answear == "number":
                for update_for in jsonbookserializ:
                    if update_for == search_update:
                        old_dic = ({new : jsonbookserializ[update_for]})
                        print(old_dic)
                        jsonbookserializ.pop(update_for)
                        print(f"Number succsesfull updated!")
                        jsonbookserializ.update(old_dic)
                        jsonbook.seek(0)
                        jsonbook.truncate(0)
                        json.dump(jsonbookserializ, jsonbook, indent=1)
                        return

            elif quest_answear == "firstname":
                for search_con in jsonbookserializ:
                    if search_update == jsonbookserializ[search_con]["first_name"].lower():
                        jsonbookserializ[search_con]["first_name"] = new
                        print(f"\nNumber succsesfull updated!")
                        jsonbook.seek(0)
                        jsonbook.truncate(0)
                        json.dump(jsonbookserializ, jsonbook, indent=1)
                        return

            elif quest_answear == "lastname":
                search_delete = input("\nPlease, input contact's Last Name:").lower()
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["last_name"].lower():
                        new_number = input("\nWhich Last Name be new?")
                        jsonbookserializ[search_con]["last_name"] = new_number
                        print(f"\nNumber succsesfull updated!")
                        jsonbook.seek(0)
                        jsonbook.truncate(0)
                        json.dump(jsonbookserializ, jsonbook, indent=1)
                        return

            elif quest_answear == "fullname":
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["full_name"].lower():
                        jsonbookserializ[search_con]["full_name"] = new
                        print(f"\nNumber succsesfull updated!")
                        jsonbook.seek(0)
                        jsonbook.truncate(0)
                        json.dump(jsonbookserializ, jsonbook, indent=1)
                        return

            elif quest_answear == "city":
                for search_con in jsonbookserializ:
                    if search_delete == jsonbookserializ[search_con]["city"].lower():
                        jsonbookserializ[search_con]["city"] = new
                        print(f"\nNumber succsesfull updated!")
                        jsonbook.seek(0)
                        jsonbook.truncate(0)
                        json.dump(jsonbookserializ, jsonbook, indent=1)
                        return

            else:
                print("Contact not found")
