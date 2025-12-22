def myfunction(username, **details):
    print("Username:", username)
    for key, value in details.items():
        print(" " + key + ": " + value)

myfunction("damoah1", phone = "0541267801", fname = "Daniel", lname = "Amoah")