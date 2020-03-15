//https://www.codechef.com/LTIME69B/problems/AVG
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
        int n,k,v;
        cin>>n>>k>>v;
        vector<int> va;
        int sum=0;
        rep(i,n){
            int tmp;
            cin>>tmp;
            va.push_back(tmp);
            sum+=tmp;
        }
        if(sum>=v*(n+k) || (v*(n+k)-sum)%k!=0 ){
            cout<<-1<<"\n";
        }
        else{
            cout<<(v*(n+k) - sum)/k<<"\n";
        }
        // int r = 0

        /* code */
    }
    
    return 0;
}
//cout<<"\n";