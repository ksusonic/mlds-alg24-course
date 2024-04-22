def main(nums: list, target: int):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            # left is sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            # right is sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    targ = int(input())
    print(main(nums, targ))
