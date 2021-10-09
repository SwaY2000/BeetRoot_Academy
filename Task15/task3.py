def arg_rules(type_:type, max_length:int, contains: list):
    def checks(function):
        def checks_arg(name: str):
            if max_length < len(name):
                return f"{name} is False"
            for arg in contains:
                if arg not in name:
                    return f"{name} is False"
            if type_ != type(name):
                return f"{name} is False"
            return function(name)
        return checks_arg
    return checks

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("johndoe05@gmail.com"))
print(create_slogan('S@SH05'))