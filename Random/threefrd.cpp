#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int xp,yp,zp,xn,yn,zn;
        cin>>xp>>yp>>zp;
        // xn=-(xp);
        // yn=-(yp);
        // zn=-(zp);
        int a,b,c;
        int flag = 0;
        b = 10; //let

        a = b + xp;
        c = a + zp;
        b = yp + c;
        if(a>b && c>a && b>c){
            flag = 1;
        }

        a = b + xp;
        c = a + zp;
        b = -yp + c;
        if(a>b && c>a && (b>c || b<c)){
            flag = 1;
        }

        a = b + xp;
        c = a - zp;
        b = -yp + c;
        if(a>b && (c>a || c<a) && (b>c || b<c)){
            flag = 1;
        }
                
        a = b + xp;
        c = a - zp;
        b = yp + c;
        if(a>b && (c>a || c<a) && b>c){
            flag = 1;
        }
        
        a = b -xp;
        c = a - zp;
        b = -yp + c;
        if(a>b && c>a && b>c){
            flag = 1;
        }
        
        a = b - xp;
        c = a - zp;
        b = yp + c;
        if((a>b || b<a) && (c>a || c<a) && b>c){
            flag = 1;
        }
        
        a = b - xp;
        c = a + zp;
        b = yp + c;       
        if((a>b || b<a) && c>a && b>c){
            flag = 1;
        }  

        a = b - xp;
        c = a + zp;
        b = -yp + c;
        if((a>b || b<a) && c>a && (b>c || b<c)){
            flag = 1;
        }
        if(flag ==1){
            cout<<"yes"<<endl;
        }else{
            cout<<"no"<<endl;
        }
    }

    return 0;
}