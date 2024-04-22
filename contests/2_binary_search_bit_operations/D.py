def main(nums: list):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            l = mid + 2
        else:
            r = mid
    return nums[l]


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(main(nums))
