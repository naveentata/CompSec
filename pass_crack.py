import hashlib
import json
import pandas as pd




# m.update(b'Hello')

# print(m.hexdigest())

yahoo_file = open('Password Lists/yahoo/password.file', 'rb')
Lines = yahoo_file.readlines()

# print(Lines)
user_pass = list(map(lambda x : str(x)[2:-5], Lines[3072:456564]))
# print(user_pass)
passwd_list = list(map(lambda x : x.split(":")[-1], user_pass))

# print(passwd_list)

dic = {}
encrypt_pwd_list = set()

excel_file = open('common_passwords.txt')
common_list = excel_file.read().splitlines()

print (common_list[0])

for i in passwd_list:
    # b = str(i)[1:-1]
    # print(b)
    m = hashlib.sha1(i.encode())
    dic[m.hexdigest()] = i
    # encrypt_pwd_list.add('00000'+m.hexdigest()[5:])
    encrypt_pwd_list.add(m.hexdigest())

# print(dic)
print(list(encrypt_pwd_list)[0:10])

# excel_file = pd.read_csv('common_passwords.csv')
# common_list = excel_file['password'].tolist()

# print (common_list[0])

formspring_file = open('Password Lists/linkedin/SHA1.txt')
lines = formspring_file.read().splitlines()
# lines = formspring_file.read()

print(lines[:3])

# passwd_list = list(map(lambda x : str(x)[:-1], lines))
passwd_list = lines
print(passwd_list[:3])
print(type(passwd_list[6]))
print(len(passwd_list))

passwords = []

print("*****************************************************************")

# for k in encrypt_pwd_list:
#     if k in ['312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76']:
#     # if k == '312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76':
#         print (True)

# count = 0
# for i in passwd_list:
#     for j in encrypt_pwd_list:
#         if (i == j):
#             count = count+1

# print([i for i, j in zip(encrypt_pwd_list, passwd_list) if i == j])
for i in passwd_list:
    if i in encrypt_pwd_list:
        print(i, dic[i])
        passwords.append(i)

print(len(dic))
print(len(set(passwords)))
# print(passwords)
# print(count)
print("*****************************************************************")
# print(passwords)

# hashing = files = open('Password Lists/formspring/formspring.txt', 'r')

# hashlist = set(hashing.readlines())



# print(passwd)