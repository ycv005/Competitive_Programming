#include<bits/stdc++.h>
using namespace std;
int main(){
    long int t;
    cin>>t;
    int a1=2,b=8,c=16;
    while(t--){
        int time;
        long long int a[3]={1,0,0};   //t  =0
        cin>>time;
        time = time - 1;
        while(time){
            if(time-a1>=0){
                time-=a1;
                a[1]=a[0];
                a[0]=0;
                a[2]=0;
            }
            else{break;}
            if(time-b>=0){
                time-=b;
                a[2]=a[1];
                a[1]=0;
                a[0]=0;
            }        
            else{break;}
            if(time-c>=0){
                time-=c;
                a[0]=2*a[2];
                a[2]=0;
                a[1]=0;
            }           
            else{break;} 
        }
        // cout<<"Ans-";
        for(int i = 0 ;i<3;i++){
            cout<<a[i]<<" ";
        }
        cout<<endl;
    }
return 0;
}