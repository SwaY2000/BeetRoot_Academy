import phone_methods

INST = """\nHello! I'm phone number book and i can:
Create new contact, for it, type "create":
Search contact, for it, type "search": 
Delete contact, for it, type "delete":
Update a record for a given telephone number, for it, type "update":
And exit program, for it, type "exit":
"""

while True:
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
