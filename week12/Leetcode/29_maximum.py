from bisect import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        n = len(startTime)

        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        # print(jobs)

        dp = [[0, 0]]
        for s, e, p in jobs:
            # 이 시작 시간 이전에서의 최대 profit
            # dp[lo:i] 와 dp[i:hi] 로 이분
            # 왼쪽은 모두 [s+1]보다 작거나 같고
            # 오른쪽은 모두 [s+1]보다 크다
            # -1하므로 
            i = bisect(dp, [s+1])-1
            # 만약 p를 더한 값이 최댓값보다 크면
            if dp[i][1]+p > dp[-1][1]:
                dp.append([e, dp[i][1]+p])

        return dp[-1][1]



sol = Solution()
print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))