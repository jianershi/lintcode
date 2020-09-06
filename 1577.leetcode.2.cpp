/**
 * 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
 * https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
 * two sum
 * https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/discuss/831467/C%2B%2BJava-Two-Sum-O(n-*-m)
 */
class Solution {
    typedef long long ll;
public:
    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
        return accumulate(nums1.begin(), nums1.end(), 0, [&](const int init, const long long num) {return init + twoProduct(num * num, nums2);}) + accumulate(nums2.begin(), nums2.end(), 0, [&](const int init, const long long num) {return init + twoProduct(num * num, nums1);});
        
    }
    int twoProduct (long long target , vector<int>& nums) {
        int count = 0;
        unordered_map<int, int> seen; //num, times
        for (int &num: nums) {
            if (target % num == 0)
                count += seen[target / num];
            seen[num]++;
        }
        return count;
    }
};