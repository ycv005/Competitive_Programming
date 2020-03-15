//https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/can-you-solve-it/
#include<bits/stdc++.h>
typedef long long int ll;
typedef unsigned long long int ull;

#define pp pair<int,int>
#define rep(i,n) for (int i = 0; i < n; i++) 
#define REP(i,k,n) for (int i = k; i <= n; i++) 
#define REPR(i,k,n) for (int i = k; i >= n; i--) 

#define pb push_back
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
using namespace std;
int main(){
    FIO;
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[n],fa[n],fb[n];
        rep(i,n){
            int tmp;
            cin>>tmp;
            a[i]=tmp;
            fa[i]=tmp+i;
            fb[i]=tmp-i;
        }
        int ans1 = *max_element(fa,fa+n)-*min_element(fa,fa+n);
        int ans2= *max_element(fb,fb+n)-*min_element(fb,fb+n);
        cout<<max(ans1,ans2)<<"\n";
    }
    return 0;
}