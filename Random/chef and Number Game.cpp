//https://www.codechef.com/MARCH19B/problems/CHNUM
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
        int n,countp=0,countn=0;
        cin>>n;
        vector<int> v;
        rep(i,n){
            int tmp;
            cin>>tmp;
            v.pb(tmp);
            if(tmp>0){
                countp++;
            }else
            {
                countn++;
            }
        }
        if(countp==n || countn==n){
            cout<<n<<" "<<n<<"\n";
        }
        else
        {   if(countp>countn){
                cout<<countp<<" "<<countn<<"\n";
            }else{
                cout<<countn<<" "<<countp<<"\n";
        }
        }
    }
    
    return 0;
}
//cout<<"\n";