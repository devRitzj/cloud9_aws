import json

def readJsonFile(filename):
    data =""
    try:
        with open('insulin.json') as json_file:
            data = json.load(json_file)
        return data
    except IOError:
        print("Could not find the file")
    return data
    
    
    
        