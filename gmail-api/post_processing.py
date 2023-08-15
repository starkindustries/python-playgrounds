total = 0
with open("senders.txt", "r") as file:
    for line in file.readlines():        
        count = int(line.strip().split(":")[1])
        total += count

print(f"{total=}")