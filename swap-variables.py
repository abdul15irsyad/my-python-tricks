# menukar variable

# menggunakan variable bantuan (temp)
age1, age2 = 15, 22
print('before:',age1,age2)
temp = age1 + age2
age1 = age2
age2 = temp - age1
print('after:',age1,age2)

# tanpa variable bantuan
age1, age2 = 15, 22
print('before:',age1,age2)
age1 = age1 + age2
age2 = age1 - age2
age1 = age1 - age2
print('after:',age1,age2)

# most efficient
age1, age2 = 15, 22
print('before:',age1,age2)
age1, age2 = age2, age1
print('after:',age1,age2)
