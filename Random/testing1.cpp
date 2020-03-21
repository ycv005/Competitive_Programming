#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long int n;
        cin>>n;
        long int a[n];
        long int count=0;
        long long int sum=0;
        int knowabout[n];
        for(long int i=0;i<n;i++){
            cin>>a[i];
            knowabout[i]=0;
        }
        knowabout[0]=1;
        n-=1;
        while(n>0){
            count+=1;
            for(long int i=0;i<n;i++){
                if(knowabout[i]==1){
                    sum+=a[i];
                }
            }
            for(long int i=0;i<n;i++){
                if(knowabout[i]==1 && knowabout[i+1]==0 && i+1<n){
                    long int temp = a[i];
                    for(long int j=i+1;j<=temp;j++){
                        knowabout[j]=1;
                        // cout<<"Know about Snackdown-"<<j<<endl;
                    }
                }
            }
            n-=sum;
        }
        cout<<count<<endl;
    }

    return 0;
}