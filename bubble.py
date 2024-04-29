n = int(input('Array size : '))

nums = [None] * n

for i in range(n):
    nums[i] = int(input(f'{{{i}}} : '))
print(f'List : {nums}\n\nProcess :\n')

for i in range(n):
    for j in range(n):
        if j != n - 1:
            if nums[j + 1] < nums[j]: 
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
        print(f'{{{i}}} {{{j}}} : {nums}')
    print()

print(f'Result : {nums}')