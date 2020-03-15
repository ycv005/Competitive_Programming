#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long long int n;
        cin>>n;
        long int a[n];
        long int count=0;
        for(long long int i=0;i<n;i++){
            cin>>a[i];
        }
        if(a[0]>=n-1){
            count =1;
        }
        else{n-=1;
            long long int times = 1;
            long long int sum=0;
            long long int i=0;
            while(n>0){
                count+=1;
                for(;i<times;i++){
                        sum+=a[i];
                }
                times= times + sum;
                n-=sum;
            }
        }
        cout<<count<<endl;
    }
    return 0;
}