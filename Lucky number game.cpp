//https://www.codechef.com/JAN19B/problems/HP18
#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define pp pair<int,int>

#define rep(i,n) for (int i = 0; i < n; ++i) 
#define REP(i,k,n) for (int i = k; i <= n; ++i) 
#define REPR(i,k,n) for (int i = k; i >= n; --i) 
#define vecf(i,v) for (auto i=v.begin();i!=v.end();i++)

#define pb push_back
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
using namespace std;
int main(){
    FIO;
    int t;
    cin>>t;
    while(t--){
        long int n,a,b,la,lb;
        cin>>n>>a>>b;
        vector<ll> vcom,va,vb,vnot;
        string win;
        for(long int i=0;i<n;i++){
            ll tmp;
            cin>>tmp;
            if(tmp%a==0 && tmp%b==0){
                vcom.pb(tmp);
                // cout<<"in vcom"<<tmp<<" ";
                // cout<<"\n";
            }
            if(tmp%a==0 && tmp%b!=0){
                va.pb(tmp);
                // cout<<"in va"<<tmp<<" ";
                // cout<<"\n";
            }
            if(tmp%b==0 && tmp%a!=0){
                vb.pb(tmp);
                // cout<<"in vb-"<<tmp<<" ";
                // cout<<"\n";
            }
            if(tmp%a!=0 && tmp%b!=0){
                vnot.pb(tmp);
                // cout<<"in vnot"<<tmp<<" ";
                // cout<<"\n";
            }
        }
        //no. of move
        la=va.size();
        lb=vb.size();
        if(vcom.size()!=0){
            la+=1;
        }
        if(la>lb){
            win="BOB";
        }
        
        else if (la<=lb)
        {
            win="ALICE";
        }
        

        cout<<win<<"\n";
    }
    return 0;
}