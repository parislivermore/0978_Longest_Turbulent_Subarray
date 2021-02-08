"""
Runtime: 552 ms, faster than 30.72% of Python3 online submissions for Longest Turbulent Subarray.
Memory Usage: 18.3 MB, less than 99.33% of Python3 online submissions for Longest Turbulent Subarray.
"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        up=[1]*n
        down=[1]*n
        ans=1
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                up[i]=down[i-1]+1
            if arr[i]<arr[i-1]:
                down[i]=up[i-1]+1
            ans=max(ans,max(up[i],down[i]))
        return ans
"""
Solution: DP
Time complexity: O(n)
Space complexity: O(n) -> O(1)

// Author: Huahua, running time: 120 ms
class Solution {
public:
  int maxTurbulenceSize(vector<int>& A) {
    vector<int> up(A.size(), 1);
    vector<int> down(A.size(), 1);
    int ans = 1;
    for (int i = 1; i < A.size(); ++i) {
      if (A[i] > A[i - 1]) up[i] = down[i - 1] + 1;
      if (A[i] < A[i - 1]) down[i] = up[i - 1] + 1;
      ans = max(ans, max(up[i], down[i]));      
    }
    return ans;
  }
};
"""
