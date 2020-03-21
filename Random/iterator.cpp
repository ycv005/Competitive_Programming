#include<iostream>
using namespace std;
#include<iterator>
#include<vector>
int main(){
    vector<int> v={2,3,1};
    for(auto p=v.begin();p<v.end();p++){
        cout<<*p<<" ";
    }
    return 0;
}