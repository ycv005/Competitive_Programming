//https://www.hackerrank.com/challenges/sherlock-and-squares/problem
#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int a,b,c=0;
        cin>>a>>b;
        vector<int> tmp;
        int sum =0;
        while(a<b+1){
            int s = sqrt(a);
            if(s*s==a){
                c++;
                // cout<<a<<endl;
                if(c==0 || c==1 || c==2){
                    tmp.push_back(a);
                }
            }
            if(c==0 || c==1){
                a++;
                continue;
            }
            else if(c==2){
                auto i=tmp.begin();
                sum = *(i+1)-*i;
            }
            if(c>=2){
                sum+=2;
                a+=sum;
            }
        }
        cout<<c<<endl;
    }
    return 0;
}