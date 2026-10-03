#include <stack>
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        int max_area = 0;
        stack<int> st;

        for(int i = 0; i <= n; i ++) {

            // Add a dummy height at the end to flush everything
            int h = (i == n ? -1 : heights[i]);

            while(st.empty() == false && h < heights[st.top()]) {
                int height = heights[st.top()];
                st.pop();

                int low = st.empty() ? -1 : st.top();
                max_area = max((i - low - 1) * height, max_area);
            }

            st.push(i);
        }

        return max_area;
    }
};