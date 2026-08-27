
class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        unordered_set<int> table;

        for(int i = 0; i < nums.size(); i++)
            table.insert(nums[i]);

        vector<int> candidate_starts;

        for(int i = 0; i < nums.size(); i ++)
            if(table.contains(nums[i] - 1) == false)
                candidate_starts.push_back(nums[i]);
        
        int longest_sequence = 0;
        for(int i = 0; i < candidate_starts.size(); i++)
        {

            int current_sequence = 1;
            int number_reached = candidate_starts[i];
            while(table.contains(number_reached+1))
            {
                current_sequence++;
                number_reached++;
            }

            longest_sequence = max(current_sequence, longest_sequence);
        }

        return longest_sequence;
    }
};
