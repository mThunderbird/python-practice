
class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        unordered_set<int> table;

        for(int i = 0; i < nums.size(); i++)
            table.insert(nums[i]);
        
        int longest_sequence = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(table.contains(nums[i]-1))
                continue;

            int current_sequence = 1;
            while(table.contains(nums[i] + current_sequence))
                current_sequence++;

            longest_sequence = max(current_sequence, longest_sequence);
        }

        return longest_sequence;
    }
};
