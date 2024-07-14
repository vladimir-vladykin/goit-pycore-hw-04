# Reads files from path, extracts data, and calculated total and medium salaries.
# Does not throws anything, instead handles all exceptions by itself, and in case of error
# logs message and just returns fallback data. 
def total_salary(path: str) -> tuple[float, float]:
    fallback_result = (0.0, 0.0)
    separator = ","
    users_and_salaries = []

    print(f"Trying to read users data from file {path}.....")

    # let's open file and read users/salaries data

    try:
        # we use combination of try/except (to handle specific exceptions) and with (for auto-closing file)
        with open(path, mode = "r", encoding="utf-8") as file:
            users_and_salaries = [el.strip() for el in file.readlines()]
    except FileNotFoundError:
        print("Couldn't read users data from file. Make sure you provided correct path to file")
        return fallback_result


    if len(users_and_salaries) == 0:
        print("File is empty, no data provided")
        return fallback_result
    
    
    # so data is here, let's calculate what we need
    total_salary = 0.0
    for user_data in users_and_salaries:
        _, user_salary = user_data.split(separator)
        try:
            total_salary += float(user_salary)
        except:
            print(f"Cannot extract user's salary from string \'{user_data}\'. Make sure you have file which follows \'name{separator}salary\' format")
            return fallback_result

    # normalize total and calculate medium
    total_salary = round(total_salary, 2)
    medium_salary = round(total_salary / len(user_data), 2)
    
    return (total_salary, medium_salary)

if __name__ == "__main__":
    sum_of_salary, medium_salary = total_salary("files/salary_file.txt")
    print(f"Total salary sum is {sum_of_salary}, medium salary is {medium_salary}")