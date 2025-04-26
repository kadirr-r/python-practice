def string(x):
    string=""#kept this empty so ass to add characters in reverse order later
    for i in x:
        string= i+ string #add characters one by one
    return string    
    
user_input= input("enter word: ")

print([string(user_input)])
