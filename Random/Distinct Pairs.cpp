//https://www.codechef.com/JAN19B/problems/DPAIRS
#include<bits/stdc++.h>
using namespace std;
int main(){
    long int n,m;
    cin>>n>>m;
    vector<long long int> va,vb;
    for(int i=0;i<n;i++){
        long long tmp;
        cin>>tmp;
        va.push_back(tmp);
    }
    for(int i=0;i<m;i++){
        long long tmp;
        cin>>tmp;
        vb.push_back(tmp);
    }
    map<long long int,map<long,long>> dp;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            dp.insert(make_pair(va[i]+vb[j],make_pair(i,j)));
        }
    }
    for(auto i=dp.begin();i!=dp.end();i++){
        // for(auto j=data.begin();j!=data.end();j++){
            // cout<<"Sum-"<<i->first<<","<<j->first<<", "<<j->second<<endl;
            cout<<"Sum-"<<i->first<<" "<<i->second<<endl;
        // }
    }
    return 0;
}