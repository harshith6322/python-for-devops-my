
def add():
    global a,b
   
    a=1
    b=1
    print(a+b)
    return None 

add()
print(a+b)


def outer_function():
    x = 10  # This is a variable in the outer function's scope

    def inner_function():
        nonlocal x  # Declares that 'x' refers to the 'x' in outer_function's scope
        X = 20      # Modifies the 'x' in outer_function's scope
        print(f"Inner function: x = {X}")

    print(f"Outer function (before inner call): x = {x}")
    inner_function()
    print(f"Outer function (after inner call): x = {x}")

outer_function()



server_name='ec2'
port=22
connection_type='ssh'
is_http_enable=True

print(f"server: {server_name}")
print(f"connection: {connection_type}")
print(f"is_http: {is_http_enable}")

    