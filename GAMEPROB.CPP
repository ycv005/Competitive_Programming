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
    int n;
    cin>>n;
    vector<int> v;
    ll sum=0;
    rep(i,n){
        int tmp;
        cin>>tmp;
        v.push_back(tmp);
    }
    do{
        cout<<v[0]<<" "<<v[1]<<" "<<v[2]<<"\n";
        vector<int> tmp;
        tmp=v;
        // cout<<tmp.size();
        while(tmp.size()!=0){
            tmp.erase(tmp.begin());
            sum =accumulate(tmp.begin(),tmp.end(),sum);
            cout<<"sum is-"<<sum<<"\n";
        }
    }
    while (next_permutation(v.begin(),v.end()));
    cout<<"before sum"<<sum<<endl;
    sum = (sum * 1000007 )/accumulate(begin(v), end(v), 1, std::multiplies<double>());
    cout<<sum;
    return 0;
}