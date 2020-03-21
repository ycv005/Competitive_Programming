#include<bits/stdc++.h>
using namespace std;
long long int xorpy(long long int a[],long int l,long int r){
    int i=0;
    long long int xorir=0;
    for(long int j=l;j<r;j++){
        if(i==0){
            cout<<"Number are-"<<a[j]<<" "<<a[j+1]<<endl;
            xorir = a[j]^a[j+1];
            cout<<"xorir is-"<<xorir<<endl;
        }
        else{
            xorir = xorir ^ (a[j]^a[j+1]);
            cout<<"xorir is-"<<xorir<<endl;
        }
        i+=1;
    }
    return xorir;
}
int main(){
    long int n;
    cin>>n;
    long long int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    long int q;
    cin>>q;
    for(long int i=0;i<q;i++){
        long int l,r;
        cin>>l>>r;
        l-=1;
        r-=1;
        if(l==r){
            cout<<a[l]<<endl;
        }
        else{
            cout<<xorpy(a,l,r)<<endl;
        }
    }
    return 0;
}