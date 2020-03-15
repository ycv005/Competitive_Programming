//https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-learning-graph-3/
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
bool sortinrev(const pair<int,int> &a,  
               const pair<int,int> &b) 
{ 
       return (a.first > b.first); 
}

int main(){
    FIO;
    int n,m,k;
    cin>>n>>m>>k;
    int val[n];
    rep(i,n){
        cin>>val[i];
    }
    //creating adj list of vector which has advanatge over linked list bcoz of cache friendliness
    vector<int> a[n];
    rep(i,m){
        int u,v;
        cin>>u>>v;
        a[u-1].push_back(v-1);
        a[v-1].pb(u-1);
    }
    rep(i,n){
        vector<pair<int, int>> t;
        for(auto x: a[i]){
            // t.push_back(val[x]);//todo: use map
            t.push_back(make_pair(x,val[x]));
        }
        sort(t.begin(),t.end(),sortinrev);
        // cout<<"Node-"<<t[k-1].first<<"value of-"<<t[k-1].second<<endl;
        cout<<"size of-"<<t.size()<<endl;
        for(int i=0;i<t.size();i++){
            cout<<t[i].first+1<<"-"<<t[i].second<<"\n";
        }
    }//sort() function used here is not a stable sort, as in question stability is mandatory. why not stable_sort() is used?
    return 0;
}