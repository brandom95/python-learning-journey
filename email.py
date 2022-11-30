email=input("what is your email address?:").strip()
user=email[:email.index("@")]
domain=email[email.index("@")+1:]
output= "your username is {} and your domain is {}"
message= output.format(user,domain)
print(message)
