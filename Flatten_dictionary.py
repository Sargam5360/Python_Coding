def flattenDictionary(dict):
    flatDictionary = {}
    flattenDictionaryHelper("", dict, flatDictionary)

    return flatDictionary


def flattenDictionaryHelper(initialKey, dict, flatDictionary):
    for key in dict:
        value = dict.get(key)

        if type(value) != type(dict): # the value is of a primitive type
            if (initialKey == None or initialKey == ""):
                flatDictionary[key] = value
            else:
                flatDictionary[initialKey + "." + key] =  value
        else:
        	if (initialKey == None or initialKey == ""):
                    flattenDictionaryHelper(key, value, flatDictionary)
    		else:
                    flattenDictionaryHelper(initialKey + "." + key, value, flatDictionary)
            
 dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }
 flattenDictionary(dict)
