#include <stack>
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        int max_area = 0;
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        stack<int> st;

        for(int i = 0; i < n; i++) {
            if(st.empty()) {
                st.push(i);
                continue;
            }

            while(st.empty() == false && heights[i] < heights[st.top()]) {
                right[st.top()] = i;
                st.pop();
            }

            st.push(i);
        }
        while(st.empty() == false) {
            right[st.top()] = n;
            st.pop();
        }

        for(int i = n - 1; i >= 0; i --) {
            if(st.empty()) {
                st.push(i);
            }

            while(st.empty() == false && heights[i] < heights[st.top()]) {
                left[st.top()] = i;
                st.pop();
            }

            st.push(i);
        }
        while(st.empty() == false) {
            left[st.top()] = -1;
            st.pop();
        }

        // for(auto i : right) {
        //     cout << i << " ";
        // }
        // cout << "\n";
        // for(auto i : left) {
        //     cout << i << " ";
        // }

        // We have now computed the left and right boundaries for each
        for(int i = 0; i < n; i++) {
            int left_stretch = heights[i] * abs(left[i] - i);
            int right_stretch = heights[i] * abs(right[i] - i);
            // We have counted the column itself twice
            int stretch_area = left_stretch + right_stretch - heights[i];
            max_area = max(max_area, stretch_area);
        }
        return max_area;
    }
};

// Constraints:
// n = len(heights)
// 1 <= n <= 10^6 -> test case -> n=1, n>1
// 0 <= heights[i] <= 10^5 -> test case -> height 0, normal heights

// Naive solution:
// On each row t (1, 2, 3, going up) find longest consecutive block k => area is kt
// Choose the max kt
// There are atmost 10^5 rows and each row has atmost 10^6 entries => O(max(heights)
// which is atmost 10^11 operations which is too much. It isn't polynomial to the input also
// but pseudo polynomial => we need something faster

// 