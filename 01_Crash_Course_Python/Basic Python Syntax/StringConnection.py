# The following 5 lines assign strings to a list of variables.

salutation = "Dr."
first_name = "Jane"
middle_name = "A."
last_name = "Doe"
suffix = "PhD"

print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix)
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.

# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

full_name = f"{salutation} {first_name} {middle_name} {last_name}, {suffix}"
print(full_name)