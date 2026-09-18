
#Interactive Terminal E-Commerce Cart & Inventory Tracker
# catalog = { "laptop": 800, "mouse": 20, "keyboard": 50, "monitor": 150 }
# grandtotal = 0

# while True:
#     inputy = input("Enter item to buy (or 'checkout' / 'exit'): ").lower()

#     if inputy == 'exit':
#         print('Order Cancelled')
#         break
#     elif inputy == 'checkout':
#         break
#     elif inputy in catalog:
#         price = catalog[inputy]
#         grandtotal += price
#         print(f"Added {input} (${price}) to order")
#     else:
#         print("ERROR! Item not found in catalog. Try again!")    

# if inputy =='checkout':
#     if grandtotal >= 500:
#         discount = grandtotal*0.1
#     elif grandtotal >= 200:
#         discount = grandtotal*0.05
#     else:
#         discount = 0

# Total = grandtotal - discount

# print('CHECKOUT RECEIPT')
# print('+'*20)
# print(f'Subtotal = {grandtotal}')
# print(f'Discount = {discount}')
# print(f'Total = {Total}')
# print('+'*20)
# print('Thank You!')

#Student Grade Evaluator & Class Performance Tracker
# totalnumber = int(input("How many student entries do you want to create? "))
# studentsrecords = {}
# for i in range(totalnumber):
#     print(f'Entry {i + 1}')
#     name = input("Enter student name: ")
#     score = int(input("Enter score (0-100): "))
#     studentsrecords[name] = score


# print('Evaluation Results')
# print('+'*40)

# passed = 0
# failed = 0
# for name, score in studentsrecords.items():
#     if score >= 70:
#         grade = "A"
#         status = "Passed with Distinction"
#         passed += 1
#     elif score >= 50:
#         grade = "B"
#         status = "Passed"
#         passed += 1
#     else:
#         grade = "F"
#         status = "Needs Improvement"
#         failed += 1

#     print(f'{name}: Score {score} | Grade {grade} | {status}')

# totalscore = sum(studentsrecords.values())
# classaveragescore = totalscore / totalnumber

# print('+'*40)
# print('CLASS PERFORMANCE')
# print('+'*40)
# print(f"Class Average Score: {classaveragescore}")
# print(f"Total Passed: {passed}")
# print(f"Total Failed: {failed}")

# # Backend Data Processing & User Audit Tool
# Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts)
users = [ (101, "Alice", "admin", True, 1),
(102, "Bob", "member", True, 4),
(103, "Charlie", "editor", False, 0),
(104, "Diana", "admin", False, 6),
(105, "Evan", "member", True, 2),
(106, "Fiona", "guest", True, 0), ]

activecount = 0
inactivecount = 0
flaggedcount = 0

for userid, name, role, isactive, loginattempts in users:
    if isactive and role == "admin":
        print(f"[GRANT] Full system access granted to {name} (ID: {userid})")
        activecount += 1

    elif isactive and (role == "member" or role == "editor"):
        print(f"[GRANT] Standard access granted to {name} (ID: {userid})")
        activecount += 1

    elif not isactive:
        print(f"[DENIED] Account {name} is inactive.")
        inactivecount += 1


    if loginattempts >= 5:
        print(
            f"[ALERT] Account {name} is LOCKED due to excessive failed logins "
            f"({loginattempts} attempts)."
        )
        flaggedcount += 1

print('+'*40)
print("AUDIT SUMMARY REPORT")
print('+'*40)
print(f"Total Active Users Granted: {activecount}")
print(f"Total Inactive Accounts: {inactivecount}")
print(f"Total Security Alerts: {flaggedcount}")








