##python3

print("python for devops")

### data types --comments
## premitive

number=5
floa_t=5.9
string="harshith"
string1= "harshith, hi"
boolean=True
none=None
complexx=2+3j


## non-premitive
arrays= [1,2,3,"har", 9.0, True, {"a": 2}]
tupple=(1,2,4,"har", 9.0, True, {"a": 1})
dic={
    "a":1,
    "b":2,
    "c":[1,2,3,4,5]
}


### Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


## Variable names are case-sensitive.
A=10
a=11
print(A,a)

## valid varnames
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

## invalid varnames
# 2myvar = "John"
# my-var = "John"
# my var = "John"


### Many Values to Multiple Variables

#many val to many var
x,y,z = "a", "b", "c"
#single val to many var
X=Y=Z = "hi"
#Unpack a Collection
arr=[1,2,3]
x,y,z=arr