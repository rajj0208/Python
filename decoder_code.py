def formatEmail(func):
    def decoder(*args, **kwargs):
        print("Dear sir\n I hope this mail finds you well and I want to inform you that")
        func(*args, **kwargs)
        print(f"Thank you \n\n Sincerly,\n {args[0]}")
    return decoder


@formatEmail
def email(name):
    print(f"My name is {name}. You have to send me the documents latest by today")


email("Raj")