#include<bits/stdc++.h>
using namespace std;
int main(){

    int a[]={34,1,2,5};
    int a1[]={23,0,5,1};
    int sa = sizeof(a)/sizeof(a[0]);
    int sa1 = sizeof(a1)/sizeof(a1[0]);
    vector<pair<int,int>> pairV(sa<sa1?sa:sa1); //creating a vector<pair<int,int>> of size-4
    cout<<pairV.size()<<endl;
    // for(auto i=pairV.begin();i!=pairV.end();i++){
    //     cout<<*i<<" ";
    // }
    for(int i=0;i<sizeof(a);i++){
        pairV.push_back(make_pair(a[i],a1[i]));
    }
    cout<<pairV.size();
    return 0;
}