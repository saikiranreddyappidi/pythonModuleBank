

def get_unique(a: str, b: str):
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                b = b[:j] + b[j+1:]
                count += 1
                break
    print('len a [Without Removing duplicates]', len(a))
    print('count', count)
    print('leb b [After Removing duplicates]', len(b))
    return len(a) - count + len(b)


print("Enter a name : ", end=" ")
n = input().lower()
print("Enter another name : ", end=" ")
m = input().lower()

if len(n) < len(m):
    unique = get_unique(n, m)
elif len(n) > len(m):
    unique = get_unique(m, n)
else:
    unique = get_unique(m, n)

game = "LEFT"
print('unique : ', unique)


def findLEFT(unique :int, s: str, position: int):
    i = 0
    index = -1 + position
    while i < unique:
        index += 1
        if index == len(s):
            index = 0
        i += 1
    if i == unique:
        return s[:index] + s[index+1:], index


position=0
print(f"[{game}]")

while len(game) != 1:
    game, position = findLEFT(unique, game, position)
    print(f"[{game}]", position)

print('----------------')
if game == 'L':
    print('Long Time Friends.')
elif game == 'E':
    print('Enemies.')
elif game == 'F':
    print('Friends.')
elif game == 'T':
    print('Time pass.')
