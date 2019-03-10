//https://www.codechef.com/problems/LECANDY
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
        int n,c;
        ll sum=0;
        cin>>n>>c;
        rep(i,n){
            int tmp;
            cin>>tmp;
            sum+=tmp;
        }
        if(sum<=c){
            cout<<"Yes"<<"\n";
        }
        else{
            cout<<"No"<<"\n";
        }
    }
    return 0;
}