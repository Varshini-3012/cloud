
# Simulate clock drift for one minute

clock_a = 0.0
clock_b = 0.0

drift_per_second = 0.010  # 10 milliseconds = 0.010 seconds

print("Second\tClock A\tClock B\tDifference")

for second in range(1, 61):
    clock_a += 1.0
    clock_b += 1.0 + drift_per_second

    difference = clock_b - clock_a

    if second % 10 == 0:
        print(
            f"{second}\t{clock_a:.3f}s\t"
            f"{clock_b:.3f}s\t{difference:.3f}s"
        )

print("\nFinal difference:", round(clock_b - clock_a, 3), "seconds")
print("Final difference:", round((clock_b - clock_a) * 1000), "milliseconds")
