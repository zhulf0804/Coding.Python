class Solution {
public:
    int getSum(int a, int b) {
        while(b){
            int cur = a ^ b;
            b = ((unsigned int )(a & b)) << 1;
            a = cur;
        }
        return a;
    }
};