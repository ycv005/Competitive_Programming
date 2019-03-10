#include<bits/stdc++.h>
using namespace std;
bool prime(int n){
    if (n <= 1) 
        return false;
        
    // Check from 2 to n-1 
    for (int i = 2; i < n; i++) 
        if (n % i == 0) 
            return false; 
  
    return true;
}
bool subprime(int n){
    // cout<<"Number for subprime-"<<n<<endl;
    for(int j=1;j<=n;j++){
        for(int k=n;k>j;k--){
            if(j*k==n){
        	    // cout<<"J as subp is-"<<j<<" and k as subp is-"<<k<<endl;
            //only to check whether both of them are prime are not.
                if(prime(j) && prime(k)){
                    // cout<<"J is- "<<j<<" and K is- "<<k<<endl;
                    return true;
                }
            }
        }
    }
    return false;
}
int main(){
    int t,n;
    cin>>t;
    // string def = "NO";
    
    while(t--){
        int flag =0;
        cin>>n; 
        int last = n-2;
        for(int i=2;i<=int(n/2);i++){

            if(subprime(i) && subprime(last)){
                // cout<<"Yes is here -"<<i<<" "<<last<<endl;
                flag =1 ;
                // return 0;
                // brea k;
            }
            last-=1;
        }
        if(flag==0){
            cout<<"NO"<<endl;
        }
        else if(flag==1){
            cout<<"YES"<<endl;
        }
    }
    return 0;   //it is imp to return a value in main. not on other but linux use to collect this value as teh status value of teh program.
}