//https://www.codechef.com/FEB19B/problems/HMAPPY2
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
        ll n,a,b,k,count=0;
        bool result=false;
        cin>>n>>a>>b>>k;
        if(a>(n/2) && b>(n/2) && k!=1){
            cout<<"Lose"<<"\n";
            continue;
        }
        else if(a==b){
            cout<<"Lose"<<"\n";
            continue;
        }
        else if(n==k){
            cout<<"Lose"<<"\n";
            continue;            
        }
        else if(n%a!=0 && n%b!=0){
            cout<<"Lose"<<"\n";
            continue;            
        }
        else{
            for(int i=1;i<=n;i++){
                if(i%a==0 && i%b!=0){
                    // cout<<i<<" ";
                    count++;
                    if(k==count){
                        result = true;
                        break;
                    }
                }
                if(i%a!=0 && i%b==0){
                    // cout<<i<<" ";
                    count++;
                    if(k==count){
                        result = true;
                        break;
                    }
                }
            }
        }
        if(result){
            cout<<"Win"<<"\n";
        }
        else{
            cout<<"Lose"<<"\n";
        }
    }
    return 0;
}