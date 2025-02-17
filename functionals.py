def calculateage(name,age):
    from datetime import datetime
    current_year = datetime.now.year
    age = current_year - birth_year
    return (f"hello{name} your age is ")
user_name = int(input("Enter age: "))
user_birth_year = int(input("Enter your date of birth"))
result = calculateage(user_name, user_birth_year)
print(result)