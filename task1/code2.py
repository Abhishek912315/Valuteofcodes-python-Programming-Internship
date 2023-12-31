def get_age():
  age = input("Please enter your age: ")
  if age.isnumeric() and int(age) >= 18:
    return int(age)
  else:
    return None

def main():
  age = get_age()
  if age is not None:
    print(f"You are {age} years old and eligible.")
  else:
    print("Invalid input. You must be at least 18 years old.")
if __name__=="__main__":
    main()





# 1.I added 'int(age)' when checking if age is greater than or equal to 18 because 'age' is initially a string, and you need to convert it to an integer for comparison.
# 2.In the 'main' function, I changed the condition to 'if age is not None:' to properly check if 'get_age()' returned a valid age.
