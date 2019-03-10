#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k,q;
    cin>>n>>k>>q;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<q;i++){
        int m;
        cin>>m;
        if(k==1){
            
        }
        else if(k>=n && k%n==0){
            cout<<a[m]<<endl;
        }
        else{cout<<a[(m+k-1)%n]<<endl;} //k<n
    }    
    return 0;
}