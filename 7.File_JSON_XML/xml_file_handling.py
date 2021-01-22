def primeNumberCall(value):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
             227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
             349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
             467, 479, 487, 491, 499]
    if value in prime:
        return 1
    else:
        return 0


hrs, numberOfParts = [int(x) for x in input().split()]
timeslot = []
ans = []
part = 0
numberOfParts = int(hrs / numberOfParts)
for val1 in range(1, hrs + 1):
    if part != numberOfParts:
        ans.append(val1)
        part = part + 1
    else:
        timeslot.append(ans)
        ans = []
        part = 1
        ans.append(val1)

timeslot.append(ans)

ans = 0
temp = 0
ts=timeslot[0]

for i in range(len(ts) - 1):
    for j in range(len(timeslot)):
        if primeNumberCall(timeslot[j][i]) != 1:
            temp = 0
            break
        temp = 1

    if j == len(timeslot) - 1 and temp == 1:
        ans = ans + 1
print(ans, end='')