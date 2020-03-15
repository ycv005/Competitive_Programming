//https://www.codechef.com/problems/RAINBOWA
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

bool allprsnt(vector<int> &a, int mx,int mxind){//int *a
    if(mx<7){
        return false;
    }
    for(int i=mx;i>0;i--){
        bool exist = find(a.begin(), a.end(), i) != end(a);
        if(!exist){
            return false;
        }
    }
    auto pos= find(a.begin(),a.end(),mx);
    for(auto i=pos;i!=a.end();i++){
        if(i+1<a.end() && *i<*(i+1)){
            return false;
        }
    }
    for(auto i=a.begin();i!=pos;i++){//(*i!=*(i+1)+1 || *i!=*(i+1))
        if(i+1<pos && *i>*(i+1)){
            return false;
        }
    }
    return true;
}
bool isPalindrome(string s,int mxind,int times){//int *a
    string s2=s;
    reverse(s2.begin(),s2.end());
    if(s==s2){
        return true;
    }else{
        return false;
    }
}

int main(){
    FIO;
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int mx=0,mxind;
        vector<int> a;
        string s="";
        rep(i,n){
            int tmp;
            cin>>tmp;
            a.pb(tmp);
            if(mx<tmp){
                mx=tmp;
                mxind=i;
            }
            s+=to_string(tmp);
        }
        // cout<<mx<<" at "<<mxind<<"\n";
        int times = count(a.begin(),a.end(),mx);
        if(times){
            mxind+=times/2;
        }
        if(allprsnt(a,mx,mxind) && isPalindrome(s,mxind, times)){
            cout<<"yes"<<"\n";
        }else{
            cout<<"no"<<"\n";
        }
    }
    return 0;
}
//cout<<"\n";