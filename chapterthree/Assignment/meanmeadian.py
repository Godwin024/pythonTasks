import statistics


value = [9, 11, 22, 34, 17, 22, 34, 22, 40]

print (statistics.mean(value))
print (statistics.median(value))
print (statistics.mode(value))

added_value = value + [34]


print(f"\nNew Mean: {(statistics.mean(added_value)):.2f}")
print(f"New Median: { (statistics.median(added_value))}")
print(f"New Modes: { (statistics.mode(added_value))}")

