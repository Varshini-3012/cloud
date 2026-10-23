
# Berkeley's Clock Synchronization Algorithm

clocks = [10, 12, 8, 15]
master = 0

print("Berkeley's Algorithm")
print("Initial clock times:", clocks)

# Calculate offsets relative to the master clock
master_time = clocks[master]
offsets = [clock - master_time for clock in clocks]

# Calculate average offset
average_offset = sum(offsets) // len(offsets)

print("Clock offsets:", offsets)
print("Average offset:", average_offset)

# Calculate adjustment for each clock
for i in range(len(clocks)):
    adjustment = average_offset - offsets[i]
    clocks[i] += adjustment
    print(f"Clock {i + 1}: Adjustment = {adjustment}")

print("Synchronized clock times:", clocks)
