# user_bills = {'hh': [],'tt':['Amazon_us_5*1000','Amazon_us_5*120','Nintendo5*11','Nintendo5*11']}

# # Create a dictionary to store the merged quantities
# merged_quantities = {}

# for item in user_bills['tt']:
#     name, quantity = item.rsplit('*', 1)
#     quantity = int(quantity)
#     if name in merged_quantities:
#         merged_quantities[name] += quantity
#     else:
#         merged_quantities[name] = quantity

# # Reconstruct the 'tt' list with the merged quantities
# user_bills['tt'] = [f"{name}*{quantity}" for name, quantity in merged_quantities.items()]

# print(user_bills)
# # Output: {'hh': [], 'tt': ['Amazon_us_5*13', 'Nintendo5*11']}


# t = 'aaaa-aaaaaa-aaA'
# if (len(t) % 16 == 15 and t[4:5] == '-' and t[11:12] == '-' and t[14:15] == 'A'):
#     print('hi')

# user_bills={'hh': [] ,'tt':['Amazon_us_5*1']}
# c= 'hh'
# if c not in user_bills:
#     print('yes')

ze = 'EOJVF05NPGPHY5SG'
za = '62838571850217'
if 'O' in ze or 'I' in ze :
    print('Yes')
else:
    print('no')