//https://www.codechef.com/DEC18B/problems/CHFINTRO
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,r;
    cin>>n>>r;
    for(int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        if(tmp>=r){
            cout<<"Good boi"<<endl;
        }
        else{
            cout<<"Bad boi"<<endl;
        }
    }
return 0;
}