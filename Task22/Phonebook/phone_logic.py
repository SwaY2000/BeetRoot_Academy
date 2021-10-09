import phone_methods

INST = """\nHello! I'm phone number book and i can:\n
Create new contact, for it, type "create":\n
Search contact, for it, type "search":\n
Delete contact, for it, type "delete":\n
Update a record for a given telephone number, for it, type "update":\n
And exit program, for it, type "exit":\n
"""

class PhoneLogic:
    def __init__(self):
        quest = str(input(INST)).lower()
        if quest == "search":
            phone_methods.search()
        elif quest == "create":
            phone_methods.add()
        elif quest == "delete":
            phone_methods.delete()
        elif quest == "update":
            phone_methods.udpate_contacts()
        else:
            print(f"\nI don't have this's function")