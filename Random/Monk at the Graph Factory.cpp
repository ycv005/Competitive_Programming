//https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-at-the-graph-factory/
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
    int n,count=0;
    cin>>n;
    bool flag=false;
    vector<int> v;
    for(int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        if(tmp>=2){
            count++;
            v.push_back(i);
        }
    }
    for(auto i = v.begin(); i != v.end(); ++i){
        if( (i+1)!= v.end() && (i+2)!= v.end() && *i==*(i+1)-1 && *(i+1)==*(i+2)-1){
            // cout<<"Flag"<<"\n";
            flag=true;
            break;
        }
    }
    if(count>=3 && flag){//it is not tree
        cout<<"No"<<"\n";
    }
    else{//it is tree
        cout<<"Yes"<<"\n";
    }
    return 0;
}