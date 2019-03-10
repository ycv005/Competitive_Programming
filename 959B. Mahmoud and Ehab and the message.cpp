#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k,m;
    cin>>n>>k>>m;
    string s[n];
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    map<string,int> mp;
    long long int price[n];
    for(int i=0;i<n;i++){
        cin>>price[i];
        mp[s[i]]=price[i];
        // mp.insert(pair<string,int> (s[i],cost));         //or this line
    }
    for(int i=0;i<k;i++){
        int sg;
        long long int minvalue = 10000000000;
        cin>>sg;
        vector<int> temp;
        for(int j=0;j<sg;j++){
            int index;
            cin>>index;
            temp.push_back(index);
            minvalue = std::min(minvalue,price[index -1]);
        }
        for(auto i=temp.begin();i!=temp.end();i++){
            mp[s[*i-1]]=minvalue;
        }
    }
    string msg;
    long long int cost=0;
    for(int i=0;i<m;i++){
        cin>>msg;
        cost+=mp[msg];
    }
    cout<<cost;
    return 0;
}