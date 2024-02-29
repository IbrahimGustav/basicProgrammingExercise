email = input("Input your email here: ")
domain_start = email.index('@') + 1
domain = email[domain_start:]


print("The domain name is", domain)