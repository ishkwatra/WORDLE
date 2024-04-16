file = open(r'C:\Users\hp\Documents\Ish\codes\self study\wordledata.txt', 'r')
arr = file.readlines()
arr = [i.strip().upper() for i in arr]


print("WELCOME TO WORDLE!")
input("PRESS ENTER TO CONTINUE...")
print()


def compute(w1, w2, w3, w4, w5, g1, g2, g3, g4, g5):
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

    # print()
    # print("Answer format -", ",".join(ans))
    # print("Letters surely in word -", pool)
    if len(pool) == 5:
        alp = pool
    elif len(pool) < 5:
        # print(f"Other possible  letters for remaining {5-len(pool)} spots - ", alp)
        pass

    # print()
    # print("Searching database...")
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

    # print(database2)
    if len(database2) == 0:
        print("No such word exists\n\n")
        exit(0)
    elif len(database2) == 1:
        print("\nYour word is surely -", database2[0])
        exit(0)
    elif len(database2) > 1 and len(database2) < 31:
        print("Only possible answers are:")
        print(database2, "\n\n")
    else:
        print(
            f"Too many possibilities still! ({len(database2)} possibilities)\n\n")


print("Enter own word or use given suggestions.\nSuggestion 1 - R H Y M E")
w1 = input("Enter first word - ")
w1 = w1.upper()
print("Entered guess is - %s" % (" ".join(w1)))
g1 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g1 = g1.upper()
if g1 == "GGGGG":
    print("\nYour word is surely -", w1)
    exit(0)
compute(w1, w1, w1, w1, w1, g1, g1, g1, g1, g1)

print("Enter own word or use given suggestions.\nSuggestion 2 - P L A N T")
w2 = input("Enter second word - ")
w2 = w2.upper()
print("Entered guess is - %s" % (" ".join(w2)))
g2 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g2 = g2.upper()
if g2 == "GGGGG":
    print("\nYour word is surely -", w2)
    exit(0)
compute(w1, w2, w2, w2, w2, g1, g2, g2, g2, g2)

print("Enter own word or use given suggestions.\nSuggestion 3 - S Q U I Z")
w3 = input("Enter third word - ")
w3 = w3.upper()
print("Entered guess is - %s" % (" ".join(w3)))
g3 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g3 = g3.upper()
if g3 == "GGGGG":
    print("\nYour word is surely -", w3)
    exit(0)
compute(w1, w2, w3, w3, w3, g1, g2, g3, g3, g3)

print("Enter own word or use given suggestions.\nSuggestion 4 - F J O R D")
w4 = input("Enter fourth word - ")
w4 = w4.upper()
print("Entered guess is - %s" % (" ".join(w4)))
g4 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g4 = g4.upper()
if g4 == "GGGGG":
    print("\nYour word is surely -", w4)
    exit(0)
compute(w1, w2, w3, w4, w4, g1, g2, g3, g4, g4)

print("Enter own word or use given suggestions.\nSuggestion 5 - B L O C K")
w5 = input("Enter fifth word - ")
w5 = w5.upper()
print("Entered guess is - %s" % (" ".join(w5)))
g5 = input("Enter the result as a string of W, Y, G (White, Yellow, Green) - ")
g5 = g5.upper()
if g5 == "GGGGG":
    print("\nYour word is surely -", w5)
    exit(0)
compute(w1, w2, w3, w4, w5, g1, g2, g3, g4, g5)

"""
RAIN:
grain
brain
drain

badge
"""
