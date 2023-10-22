class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        g_size = defaultdict(int)
        for n in nums:
            g_size[n] += 1
        
        sizes = list(g_size.values())
        minn = min(sizes) + 1
        ans = inf
        while minn >= 1:
            ans = 0
            for i, v in enumerate(sizes):
                groups = v// minn
                remain = v % minn
                cur = inf
                if not remain or minn- 1 - remain <= groups:
                    cur = groups + (0 if not remain else 1)
                ans += cur
                if ans == inf:
                    break
            if ans != inf: return ans
            minn -= 1

        # # tle Solution
        # count_dict = {}
        # s = list(set(nums))
        # min_value = 99999
        # for i in s:
        #     count_dict[i]=nums.count(i)
        #     if min_value > nums.count(i):
        #         min_value = nums.count(i)
        
        # max_allowed_val = min_value+1
        # min_sets = 999999999999
        # sets = 0
        # while(max_allowed_val > 0):
        #     sets=0
        #     for i in count_dict:
        #         a = count_dict[i]//max_allowed_val
        #         b = count_dict[i]%max_allowed_val
        #         if (b) == 0:
        #             rem_val = 0
        #         elif ((max_allowed_val-1)-b) <= a:
        #             rem_val = 1
        #         else:
        #             sets=0
        #             break
        #         sets += a + rem_val
        #     if sets != 0:
        #         min_sets = min(min_sets,sets)
        #         return min_sets
        #     max_allowed_val-=1
        # return min_sets