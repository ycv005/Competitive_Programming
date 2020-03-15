#include<bits/stdc++.h>
using namespace std;
int main(){
    int size,k1,k2,flag=0;
    int e=0;
    cin>>size>>k1>>k2;
    int a[size],b[size];
    for(int i=0;i<size;i++){
        cin>>a[i];
    }
    for(int i=0;i<size;i++){
        cin>>b[i];
    }
    for(int i=0;i<size;i++){  
        if(k1==0){
            // e = pow(k1-k2,2);
            break;
        }
        else{ 
            while(k1){
                if(a[i]>b[i]){
                    a[i]-=1;
                    k1--;
                }
                else if (a[i]<b[i]){
                    a[i]+=1;
                    k1--;
                }
                else{
                    if(i==size-1){//end
                        // cout<<"the k1-"<<k1<<endl;
                        // e = pow(k1-k2,2);
                        // cout<<"e in in k1 "<<e<<endl;
                        // flag =1;
                        // k1--; 
                        a[i]+=1;
                        k1--;
                        }
                    else{break;}
                    }
                }
            }
    }
    for(int i=0;i<size;i++){
        if(k2==0){
            // e = pow(k1-k2,2);
            break;
        }
        else{ 
            while(k2){
                if(a[i]>b[i]){
                    b[i]+=1;
                    k2--;
                }
                else if (a[i]<b[i]){
                    b[i]-=1;
                    k2--;
                }
                else{
                    if(i==size-1){//end
                        // cout<<"the k2-"<<k2<<endl;
                        // e = pow(k1-k2,2);
                        // cout<<"e in in k2 "<<e<<endl;
                        // flag =1;
                        // k2--; 
                        b[i]+=1;
                        k2--;
                        }
                    else{break;}
                    }
                    
                }
            }
    }

    // if(flag == 0){
        for(int i=0;i<size;i++){
            cout<<a[i]<<"  "<<b[i]<<endl;
            e+=pow(a[i]-b[i],2);
        }
    // }
    cout<<e;
    return 0;
}