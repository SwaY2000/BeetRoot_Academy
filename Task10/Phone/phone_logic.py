import phone_methods

CHOOSE = """\nHello! I'm phone number book and i can:
Create new contact, for it, type "create":
Search contact, for it, type "search": 
Delete contact, for it, type "delete":
Update a record for a given telephone number, for it, type "update":
And exit program, for it, type "exit":
"""

while True:
    quest = str(input(CHOOSE)).lower()

    if quest == "search":
        phone_for_search = input("Input phone number for search")
        phone_methods.search(phone_for_search)

    elif quest == "create":
        number, first_name, last_name, city = input("Number contact"), input("First name"), input("Last name"), \
                                                   input("City")
        phone_methods.add(number, first_name, last_name, city)

    elif quest == "delete":
        while True:
            quest_answear = input("""You want delete for:
                number, type "number"
                First Name, type "firstname"
                Last Name, type "lastname"
                """).lower()
            if quest_answear == "number":
                search_delete = input("Input phone number for search").lower()
                phone_methods.delete(quest_answear, search_delete)
            elif quest_answear == "firstname":
                search_delete = input("Input first name for search").lower()
                phone_methods.delete(quest_answear, search_delete)
            elif quest_answear == "lastname":
                search_delete = input("Input lastname for search").lower()
                phone_methods.delete(quest_answear, search_delete)
            else:
                print("Not found function, check your answer and try again")

    elif quest == "update":
        while True:
            quest_answear = input("""You want update for:
                number, type "number"
                First Name, type "firstname"
                Last Name, type "lastname"
                City, type "city"
                                                """).lower()
            if quest_answear == "number":
                search_update = input("Input phone number for search").lower()
                new = input("Which phone number be new?")
                phone_methods.update_contacts(quest_answear, search_update, new)

            elif quest_answear == "firstname":
                search_update = input("Input first name for search").lower()
                new = input("Which first name be new?")
                phone_methods.update_contacts(quest_answear, search_update, new)

            elif quest_answear == "lastname":
                search_update = input("Input last name for search").lower()
                new = input("Which last name be new?")
                phone_methods.update_contacts(quest_answear, search_update, new)

            elif quest_answear == "city":
                search_update = input("Input city for search").lower()
                new = input("Which city be new?")
                phone_methods.update_contacts(quest_answear, search_update, new)

            else:
                print("Not found function, check your answer and try again")

    else:
        print(f"\nI don't have this's function")
