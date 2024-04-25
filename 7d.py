# thislist = ["apple", "banana", "cherry"]

def listtostr(thislist):
    list_to_str = ""
    for i in range(len(thislist)):
        list_to_str += thislist[i]

    print(list_to_str)

listtostr(["Lawrence", "Quarshie"])