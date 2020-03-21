#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    int maxi = 0, mini = 51;
    for(int i=0;i<n;i++){
        cin>>a[i];
        if(a[i]>maxi){
            maxi = a[i];
        }
        if(a[i]<mini){
            mini = a[i];
        }
    }
    //operation
    while(mini<=maxi){
        //find mini's index in array
        int ind = distance(a,find(a,a+n,mini)) +1;
        int nxtind = distance(a,find(a,a+n,ind)) +1;
        cout<<nxtind<<endl;
        mini++;
    }
    
    return 0;
}