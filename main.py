def longest_increasing_streak(nums: list[int]) -> dict:
    result = {
        "length": 0,
        "streak": [],
    }
    if not len(nums) or len(nums) == 1:
        return result
    streak = []
    streak_temp = []
    streak.append(nums[0])
    streak_temp.append(nums[0])
    for i in range(1, len(nums)):
        if len(streak_temp) > len(streak):
            streak = streak_temp.copy()
        if nums[i] > nums[i-1]:
            streak_temp.append(nums[i])
        else:
            streak_temp = []
            streak_temp.append(nums[i])
    if len(streak_temp) > len(streak):
        streak = streak_temp.copy()
    if len(streak) != 1:
        result["length"] = len(streak)
        result["streak"] = streak
    return result

if __name__ == "__main__":
    nums = [1, 3, 2, 5, 8, 4, 7]
    print(longest_increasing_streak(nums))  # {"length": 3, "streak": [2, 5, 8]}
