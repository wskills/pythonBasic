rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(vacancy)