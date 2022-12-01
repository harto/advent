with open('2022/input/01.txt') as f:
    chunks = f.read().split('\n\n')
    amounts = [sum(int(line) for line in chunk.strip().split('\n')) for chunk in chunks]

print(max(amounts))
print(sum(sorted(amounts)[-3:]))
