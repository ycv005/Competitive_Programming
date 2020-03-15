#include<bits/stdc++.h>
using namespace std;
int main(){
    long int t;
    cin>>t;
    while(t--){
        string bydefault = "CHEF";
        long long int p1,p2,k,temp;
        cin>>p1>>p2>>k;
        // cout<<p1<<" "<<p2<<" "<<k<<endl;
        temp = floor((p1+p2)/k);
        // cout<<temp<<endl;
        if(temp%2!=0){
            // cout<<"chaning";
            bydefault = "COOK";
        }
        cout<<bydefault<<endl;
    }
    return 0;
}