# Importing the necessary files.
import time
import json

# All standard functions in Python3 are generally thread-safe.


# [Optional Usage] as the code is already included in the functions below

# Function to open the JSON file.
# def loadFile():
#     with open('data.json', 'r') as openfile:
#         dict = json.load(openfile)


# Function to insert new data into the JSON file.
# def dumpData():
#     with open("data.json", "w") as outfile:
#         json.dump(dict, outfile)





# CRD operations of our Datastore

# This "create" method inserts a new key and value into the "self.data" dictionary.
def create(key, value, timer=0):

    with open('data.json', 'r') as openfile:
        dict = json.load(openfile)

    if key in dict:
        print("Invalid: Key Already Exists")
    else:
        if key.isalpha():
            if len(dict) < 1024 * 1024 * 1024 and value <= (16 * 1024 * 1024): # Data size and constraints check.
                if timer == 0:
                    temp = [value, timer]
                else:
                    temp = [value, time.time() + timer]

                if len(key) <= 32:
                    dict[key] = temp

                    with open("data.json", "w") as outfile:
                        json.dump(dict, outfile)

            # Memory Limit Exceeded warning.
            else:
                print("Memory Limit Exceeded")

        # If the key format is invalid
        else:
            print("Invalid Key Format")

# This "read" method fetches a key which is already present in "self.data".
def read(key):

    with open('data.json', 'r') as openfile:
        dict = json.load(openfile)

    if key not in dict:
        print("Enter a valid key")
    else:
        temp = dict[key]
        if temp[1] != 0:
            if time.time() < temp[1]:
                print(str(key) + " : " + str(temp[0]))
            else:
                print("Time-To-Live of this key has expired")
        else:
            print(str(key) + " : " + str(temp[0]))


# "delete" method deletes a key-value pair inside "self.data".
def delete(key):

    with open('data.json', 'r') as openfile:
        dict = json.load(openfile)

    # If the key is not present in the datastore.
    if key not in dict:
        print("Enter a valid key")
    else:
        temp = dict[key]
        if temp[1] != 0:
            if time.time() < temp[1]:
                del dict[key]

                with open("data.json", "w") as outfile:
                    json.dump(dict, outfile)

                print("Key deleted successfully")
            else:
                del dict[key]
                print("Time-To-Live of this key has expired")

        else:
            del dict[key]

            with open("data.json", "w") as outfile:
                json.dump(dict, outfile)

            print("Key deleted successfully")
