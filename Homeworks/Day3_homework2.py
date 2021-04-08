#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={"admin":"1234","user":"parola","Nedd":"0000"}
username,password = str(input("Username: ")),str(input("Password: "))

while not username in d.keys():
    print("The user named {} has not been found".format(username))
    username = str(input("Username: "))
    password = str(input("Password: "))



if username in d.keys():
    if password in d.values():
        print("login successful")
    else:
        print("wrong password")
        print("You have 5 chances to try again")
        for i in range(5):
            password = str(input("Password: "))
            if password in d.values():
                print("login successful")
                break
            else:
                print("wrong password")
                print("You have {} chances to try again".format(4-i))
                if i == 4:
                    break
else:
    print("The user named {} has not been found".format(username))

