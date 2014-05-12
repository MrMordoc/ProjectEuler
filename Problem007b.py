nums = range(2, 120000)
results = []

while len(nums) > 0:
    results.append(nums[0])
    nums = [n for n in nums if n % nums[0] != 0]

print len(results)
print results[10000]
