//https://www.codechef.com/problems/CNOTE
#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define pp pair<int,int>

#define rep(i,n) for (int i = 0; i < n; ++i) 
#define REP(i,k,n) for (int i = k; i <= n; ++i) 
#define REPR(i,k,n) for (int i = k; i >= n; --i) 

#define pb push_back
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
using namespace std;
int main(){
    FIO;
    int t;
    cin>>t;
    while(t--){
        int x,y,k,n;
        cin>>x>>y>>k>>n;
        bool flag=false;
        rep(i,n){
            int pg,cost;
            cin>>pg>>cost;
            if(cost<=k && pg>=(x-y)){
                flag =true;
            }
        }
        cout<<(flag?"LuckyChef\n":"UnluckyChef\n");
    }
    return 0;
}