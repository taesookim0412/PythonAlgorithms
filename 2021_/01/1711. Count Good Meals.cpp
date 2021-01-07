//O(NLogN) Runtime (1852 ms)
class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        unsigned long int ct = 0;
        sort(deliciousness.begin(), deliciousness.end());
        unordered_map<int, unsigned long int> dels;
        for (const int dish: deliciousness){
            for (int i = 0; i < 22; i++){
                int powNum = pow(2, i);
                int diff = powNum - dish;
                if (diff > deliciousness[deliciousness.size() - 1]){
                    break;
                }
                ct += dels[diff];
            }
            dels[dish] += 1;
        }
        return ct % 1000000007;
    }
};

//C++ O(N^2) Runtime (TLE)
class Solution {
public:
    set<int> nums;
    int countPairs(vector<int>& deliciousness) {
        int ct = 0;
        if (nums.size() == 0){
            for (int i  =0; i < 21; i++){
                nums.insert(pow(2, i));
            }
        }
        for (int i = 0; i < deliciousness.size(); i++){
            for (int j = i + 1; j< deliciousness.size(); j++){
                if (nums.find(deliciousness[i] + deliciousness[j]) != nums.end()){
                    ct += 1;
                }
            }
        }
        return ct;
    }
};