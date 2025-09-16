arn = '   arn:aws:iam::123456789012:user/JohnDoe'

#1. string_concat
a='hello'
b='world'
c=a+b
print(a+b)
print(a+ " " +b)
print(c)

#2. string_length
print(arn.__len__())
print(len(arn))

#3. other methods
print(arn.split("/")[0])
print(arn.split("/"))
print(arn.upper())
print(arn.lower())
print(arn.strip()) #lstrip rstrip
print(arn.replace("JohnDoe", "harshith"))
print(arn.strip("").startswith("har")) 
print(arn.strip("").endswith("E"))
# count occurrences
print(arn.count(":")) 


#4 substring
d="i love python"
if "a" in d:
    print("this is substring")
elif " " in d:
    print("space is there")
else:
    print("nothing")

#5 string_fing
print(arn.find("i")) #(returns -1 if not found)
print(arn.index("i"))
#print(arn.index("I")) #(throws error if not found)

# join a list into string
parts = ["arn", "aws", "iam", "123456789012", "user", "JohnDoe"]
print(":".join(parts))   # arn:aws:iam:123456789012:user:JohnDoe
# splitlines (for logs)
multi = "line1\nline2\nline3"
print(multi.splitlines())   # ['line1', 'line2', 'line3']




# check content
print(arn.isalpha())      # False (not only alphabets)
print(arn.isdigit())      # False
print("12345".isdigit())  # True
print("AWS".isupper())    # True
print("aws".islower())    # True


# formatting
region = "us-east-1"
service = "s3"
bucket = "mybucket"
print(f"arn:aws:{service}::{region}:{bucket}")
print("arn:aws:{}::{}:{}".format(service, region, bucket))





# ✅ In short, important string methods to remember for DevOps scripting:

# .strip(), .lstrip(), .rstrip()

# .split(), .join(), .splitlines()

# .startswith(), .endswith()

# .find(), .index(), .count()

# .upper(), .lower(), .title(), .capitalize()

# .replace(), .removeprefix(), .removesuffix()

# .isalpha(), .isdigit(), .isalnum(), .isspace(), .istitle()



# Extract AWS username from ARN
arn_clean = arn.strip()
username = arn_clean.split("/")[-1]
print(username)   # JohnDoe

# Masking secret
secret = "MySecretPassword"
print(secret.replace(secret[2:-2], "*" * (len(secret)-4)))  # My**********rd

# Log sanitizing
log = "[ERROR] 2025-09-09 Something failed"
print(log.removeprefix("[ERROR] "))   # "2025-09-09 Something failed"
print(log.removesuffix("failed"))     # "[ERROR] 2025-09-09 Something "






