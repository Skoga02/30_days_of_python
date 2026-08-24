# Day 2 

## Variables 
Variables store data in a computer memory. Memonic varibales are recommended to use in many programming languages. A mneomonic varivale is a varible name that can be easily rememberd and associated. A variable refers to a memory address in wich data is stored. Number at the beginning, special character, hyphen are not allowed when namin a varible. A varibale can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Varible Name Rules
* A variable name must start with a letter or a undescore character
* A variable name cannot start with a number 
* A variable name can onlu contain alpha-numeric characters and underscores (A-z, 0-9, and _)
* Variable names are case-sensitive (firstnmae, Firstname, FirstName and FIRSTNAME) are diffrent variables

here are som more valid varible names:

```python
firstname
lastname
age 
country
city
first_name
last_name
capital_city
year_2021
year2021
current_year_2021
birth_year
```

Invalid variable names
```python
first-name
first@name
first¢name
num-1
1num
```

We will use standard Python varibale naming style which has been adopted by many Python developers. Python developers use snake case (snake_case) variable naming convertion. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

WHen we assign a certain data type to a variable, it is called variable declaration. For instance in the example below the first name is assigned to a variable first_name. The equal sign is an assignment operator. Assign means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

Example:
```Python
first_name = 'Julius'
last_name = 'Skoglund'
country = 'Sweden'
city = 'Stockholm'
age = '24'
person_info = {
    'firstname': 'Julius',
    'lastname': 'Skoglund',
    'country': 'Sweden'
}
```

Let us use the print() and len() built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

Example:
```Python
print("Hllo, world!")
print('Hello'',''world','!')
print(len('Hello, world!'))
```

Let us print and also fint the length of the variables declared at the top:

Example: 
```Python
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Declaring multiple varibales in a line
multiple variables can also be declared in one line:

Example:
```Python
first_name, last_name, country, age, is_married = 'Julius', 'Skoglund', 'Stockholm', 24, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables.
Example:
```Python
first_name = input('What is your name?')
age = inpur('How old are you?')

print(first_name)
print(age)
```

## Data types
There are several data types in Pyhthon. To identify the data we use the _type_ built-in function. I would like to ask you to focus on understanding diffrent data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more. detail in their respective sections.

## Checking data types and casting 
* Check data types: to check data type of certain data/variable we use the _type_ function.

```Python
-- Diffrent Python data types
-- Let´s declare variables with various data types

first_name = 'Julius' -- str
last_name = 'SKoglund' -- str
country = 'Sweden' -- str
city = 'Stockholm' -- str
age = '24' -- int


-- How to print the diffrent data types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
```

* Casting: converting one data type to another data type. We use int(), float(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in stringsection. 

Examples: 
```Python
-- int to float 
num_int = 10
print('num_int', num_int) -- 10 
num_float = float(num_int)
print('num_float:' num_float) -- 10.0

-- flaot to int
gravity = 9.81
print(int(gravity)) -- 9

-- int to str
num_int = 10
print(num_int) -- 10 
num_str = str(num_int)
print(num_str) -- '10'

-- str to int or float 
num_str = '10,6'
num_float = float(num_str) -- Convert the string to a float first
num_int = int(num_float) -- Then convert the float to an integer
print('num_int', int(num_str)) -- 10
print('num_float', float(num_str)) -- 10.6 
num_int = int(num_float)
print('num_int', init(num_int)) -- 10 

-- str to list 
first_name = 'Julius'
print(first_name) -- 'Julius'
first_name_to_list 0 list(first_name)
print(first_name_to_list) --['J', 'u', 'l', 'i', 'u', 's']

```

### Numbers

Number data types in python:
1. Integers: Integer(negative, zero and positive) numbers Example: -3, -2, -1, 0, 1, 2, 3,
2. Flaoting point numbers(Decimal numbers) Example: -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5
3. Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j

