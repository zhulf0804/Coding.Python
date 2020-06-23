y, b, r = list(map(int, input().split()))

mmin = min(y, b)
mmin = min(mmin, r)

#if b > mmin and r > mmin + 1:
#    ans = 3 * mmin + 3

if y == b and y == r:
    ans = 3 * y - 3
else:
    if mmin == r:
        ans = r + r - 1 + r - 2
    elif mmin == b:
        if r == mmin:
            ans = r + r - 1 + r - 1
        else:
            ans = 3 * b
    else:
        if r >= mmin + 2:
            ans = 3 * mmin + 3
        else:
            ans = 3 * mmin
print(ans)



'''
# qincheng
# python2

y,b,r = map(int,raw_input().split(" "))
s = min(b-1,r-2,y)
print 3*s+3
'''

'''
# huas_xy
# GNU G++

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int y,b,r;
    cin>>y>>b>>r;
    for(int i=r;i>=1;i--){
        if(i-1<=b&&i-2<=y){
            cout<<i*3-3<<endl;
            break;
        }
    }
    return 0;
}
'''