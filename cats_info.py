separator = ","

# Reads file from path and returns cats info as a list of dicts.
# Does not throw anything, instead handles all exceptions by itself, and in case of error
# logs message and just returns fallback data. 
def get_cats_info(path) -> list:
    print(f"Trying to read cats info from file {path}.....")

    raw_cats_info = []
    try:
        # we use combination of try/except (to handle specific exceptions) and with (for auto-closing file)
        with open(path, mode = "r", encoding="utf-8") as file:
            raw_cats_info = [el.strip() for el in file.readlines()]
    except FileNotFoundError:
        print("Couldn't read cats info from file. Make sure you provided correct path to file")
        return []
    
    if len(raw_cats_info) == 0:
        print("No cats info found, file is empty")
        return []
    
    # let's parse cats info, pack each cat's info into dict, and then pack all this into list of dicts
    result_list = []
    for raw_cat_info in raw_cats_info:
        id, name, age = raw_cat_info.split(separator)
        try:
            # float is goona be better than int here, it's possible there's age line 3.5 in file
            result_list.append({"id": id, "name": name, "age": float(age)})
        except:
            print(f"Cannot extrac cat's info from string \'{raw_cat_info}\'. Make sure your file follows \'id{separator}name{separator}age\' format")
            return []

    return result_list

if __name__ == "__main__":
    cats_info = get_cats_info("files/cats_info.txt")
    print(f"Cats info is {cats_info}")