class Solution {
public:
    int climbStairs(int n) {
        int step=2;
        int meth=0;
        int c=0;
        int a=1;
        int b=2;
        if (n<=2){
            return n;
        }
        else{
            while(step<n){
                c=a+b;
                meth=c;
                a=b;
                b=c;
                step++;
            }
        }
        return meth;
    }
};