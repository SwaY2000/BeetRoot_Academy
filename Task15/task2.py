def stop_words(words: list): #list with stop words
    def stop_words_wrapper(function):
        def wrapper(name: str):
            string = function(name)
            for word_stop in words: #call in turn evry call stop
                if word_stop in string:# if string has word_stop
                    string = string.replace(word_stop, "*")
            print(string)
            return string
        return wrapper
    return stop_words_wrapper

@stop_words(["pepsi", "BMW"])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW"

create_slogan("Danil")
