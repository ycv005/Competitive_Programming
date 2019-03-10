//https://www.codechef.com/DEC18B/problems/CHFIDEAL
#include<bits/stdc++.h>
using namespace std;
int main(){
    int x,y,upper=3,lower=1;
    srand(time(0));     //intialize the random number generator at the begining to initialize the random seed.
    x = (rand() % (upper-lower + 1)) + lower;
    cout<<x<<endl;
    cin>>y;
    for(int i=1;i<=3;i++){
        if(x==i || y==i){
        }
        else{
            cout<<i<<endl;
        }
    }
    return 0;
}