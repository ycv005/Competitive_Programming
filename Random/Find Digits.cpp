#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long n;
        cin>>n;
        string s = to_string(n);
        long count = 0;
        for(int i=0;i<s.length();i++){
            if(s[i]=='0'){
                continue;
            }
            else if(s[i]=='1'){
                count++;
            }
            else{
                int tmp = s[i] - '0';
                if(n%tmp==0){
                    count++;
                }
            }
        }
        cout<<count<<endl;
    }
return 0;
}