//https://www.codechef.com/DEC18B/problems/MAXEP
#include<bits/stdc++.h>
using namespace std;
int main(){
    srand(time(0)); //should be called only once
    int n,c,lower=1,upper=150000,startC = 1000,x=150000,d=2;
    cin>>n>>c;
    while(1){
        int t[2]={1,3}; //for chosing
        int l= rand() % (2); //get 0 or 1
        int y = (rand() % (upper-lower + 1)) + lower;
        if(t[l]==1){
            cout<<t[l]<<" "<<y<<endl;
        }
        else{
            cout<<3<<" "<<x<<endl;
            break;
        }
        
        cin>>d; //Decision
        if(d==-1){
            //invalid op
            continue;
        }
        else if(d==0){
            startC--;

        }
        else if(d==1){ //broken
            x=min(y,x);
            startC-=c;
            cout<<2<<endl;
            d=2;
        }
    }
    return 0;
}