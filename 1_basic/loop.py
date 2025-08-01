# Counter using for loop
i = 0
for_loop_count = 0
for _ in range(1000):
    i += 1.5
    for_loop_count += 1
    if i >= 1000:
        break
print("Final value (for loop):", i)
print("Number of loops (for loop):", for_loop_count)

# Counter using while loop
count = 0
while_loop_count = 0
while count < 1000:
    count += 1.8
    while_loop_count += 1
print("Final value (while loop):", count)
print("Number of loops (while loop):", while_loop_count)

