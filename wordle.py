file = open(r'C:\Users\hp\Documents\Ish\codes\self study\wordledata.txt', 'r')
arr = file.readlines()
arr = [i.strip().upper() for i in arr]

print("WELCOME TO WORDLE!")
input("PRESS ENTER TO CONTINUE...")

print("My first guess is - R H Y M E")
w1 = "RHYME"
g1 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g1 = g1.upper()
if g1 == "GGGGG":
    print("\nYour word is -", w1)
    exit(0)

print("My second guess is - P L A N T")
w2 = "PLANT"
g2 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g2 = g2.upper()
if g2 == "GGGGG":
    print("\nYour word is -", w2)
    exit(0)

print("My third guess is - S Q U I Z")
w3 = "SQUIZ"
g3 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g3 = g3.upper()
if g3 == "GGGGG":
    print("\nYour word is -", w3)
    exit(0)

print("My fourth guess is - F J O R D")
w4 = "FJORD"
g4 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g4 = g4.upper()
if g4 == "GGGGG":
    print("\nYour word is -", w4)
    exit(0)

print("My fifth guess is - B L O C K")
w5 = "BLOCK"
g5 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g5 = g5.upper()
if g5 == "GGGGG":
    print("\nYour word is -", w5)
    exit(0)

ans = ["_"]*5
pool = []
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
temp = w1+w2+w3+w4+w5
guess = g1+g2+g3+g4+g5

for i in range(25):
    if guess[i] == "W":
        if temp[i] in alp:
            alp.pop(alp.index(temp[i]))
    if guess[i] == "Y":
        if temp[i] not in pool:
            pool.append(temp[i])
    if guess[i] == "G":
        ans[i % 5] = temp[i]
        if temp[i] not in pool:
            pool.append(temp[i])

print()
print("Answer format -", ",".join(ans))
print("Letters surely in word -", pool)
if len(pool) == 5:
    alp = pool
elif len(pool) < 5:
    print(f"Other possible  letters for remaining {5-len(pool)} spots - ", alp)

print()
print("Searching database...")
database = []
for i in arr:
    if i[0] not in alp:
        continue
    elif i[1] not in alp:
        continue
    elif i[2] not in alp:
        continue
    elif i[3] not in alp:
        continue
    elif i[4] not in alp:
        continue

    if set(pool).issubset(set(i)):
        count = 0
        if i[0] == ans[0] or ans[0] == "_":
            count += 1
        if i[1] == ans[1] or ans[1] == "_":
            count += 1
        if i[2] == ans[2] or ans[2] == "_":
            count += 1
        if i[3] == ans[3] or ans[3] == "_":
            count += 1
        if i[4] == ans[4] or ans[4] == "_":
            count += 1

        if count == 5:
            database.append(i)

database2 = []
if len(database) > 1:
    bad = [[], [], [], [], []]
    for i in range(0, 25, 5):
        if guess[i] == "Y":
            bad[0].append(temp[i])
    for i in range(1, 25, 5):
        if guess[i] == "Y":
            bad[1].append(temp[i])
    for i in range(2, 25, 5):
        if guess[i] == "Y":
            bad[2].append(temp[i])
    for i in range(3, 25, 5):
        if guess[i] == "Y":
            bad[3].append(temp[i])
    for i in range(4, 25, 5):
        if guess[i] == "Y":
            bad[4].append(temp[i])

    for i in database:
        if (i[0] in bad[0]):
            continue
        elif (i[1] in bad[1]):
            continue
        elif (i[2] in bad[2]):
            continue
        elif (i[3] in bad[3]):
            continue
        elif (i[4] in bad[4]):
            continue
        else:
            database2.append(i)
else:
    database2 = database.copy()
print(database2)
print("\nYour word is -", database2[0])
