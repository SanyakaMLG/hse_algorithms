from tracer.main import trace

def permutations(nums: list[int]) -> list[list[int]]:
    result = []

    # @trace
    def backtrack(nums: list[int], path: list[int] = None):
        if len(nums) == 0:
            result.append(path if path else [])
            return

        for idx, num in enumerate(nums):
            backtrack(
                nums[:idx] + nums[idx + 1:],
                path + [nums[idx]] if path else [nums[idx]]
            )

    backtrack(nums)
    return result
