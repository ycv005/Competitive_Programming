#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long long int n;
        long long int k;
        unsigned int M = 1000000007; 
        long long int prod=0;
        cin>>n>>k;
        if(n<k){
            prod = -1;
        }
        else if(k==1){
            prod = fmod((n*n-n),M); // (n*n-n)%M
        }
        else if(k==n || n<2*k){
            prod  = 0;
        }
        else if( 2*k == n ){ 
            prod = fmod(pow(2,k), M);//pow(2,k)%M;
        }
        else if(n==k*k){//perfect sq
                prod = fmod(( (k*k-k)*k ), M);//( (k*k-k)*k )%M;
            }
        else{
            long long int d=0;
            long long int count=0;
            d = floor(n/k);
            if(d<k){
                long long int temp =n;
                while(temp--){
                    n = n-d;
                    count++;
                    if(n%k==0){
                        break;
                    }
                }
                prod = fmod(( ((d*d-d)*count) * ((k*k-k)*(k-count)) ), M);//( ((d*d-d)*count) * ((k*k-k)*(k-count)) )%M;
            }
            else if(d>k){
                long long int temp =n - d*(k-1);
                prod = fmod(( ((d*d-d)*(k-1)) * (temp*temp-temp) ), M);//( ((d*d-d)*(k-1)) * (temp*temp-temp) )%M;
            }
        }
        cout<<prod<<endl;
    }
    return 0;
}