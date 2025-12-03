# Built-in functions

#print()
# The print() function outputs a specified object to the screen. The print()
# function is one of the most commonly used functions in Python because it 
# allows you to output any detail from your code.

month = "February"
print("Investigate failed login attempts during", month, "if more than", 100)

#type()
# The type() function returns the data type of its argument. The type() 
# function helps you keep track of the data types of variables to avoid 
# errors throughout your code. 

print(type(month))  # Outputs: <class 'str'>

#str()
# The str() function converts its argument to a string data type. The str()
# function is useful when you need to concatenate a string with a non-string
# data type, such as an integer or float.

failed_logins = 150
string_representation = str(failed_logins)
print(string_representation)  # Outputs: '150'
