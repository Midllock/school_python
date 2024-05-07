count = 0
attempts = 0

for i in range(100000):
    numbers = [int(d) for d in str(i)]
    if sum(numbers) == 13 and len(set(numbers)) == 4:
        if len(set(numbers)) == 4 and numbers == sorted(numbers, key=lambda x: -x):
            numbers.reverse()
            count += 1
            print(f"Čísla {count} s součtem 13:", numbers)
            attempts += 1
            if attempts == 10:
                break

    



