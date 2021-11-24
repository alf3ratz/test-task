# с повторениями индексов
def solution(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                result.append((i, j))
    return result


# без повторений индексов
def solution2(nums, target):
    dictionary = {}
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and (not i in dictionary) and (not j in dictionary):
                dictionary[i] = j
                result.append((i, j))
    return result


nums = range(1, 100)

print(solution(nums, 12))
print(solution2(nums, 12))
