#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    int countA=0,countB=0,countC=0;
    int flag =0 ;
    for(int i=0;i<s.length();i++){
        if(s[i]=='a'){
            countA++;
        }
        else if(s[i]=='b'){
            countB++;
        }
        else if(s[i]=='c'){
            countC++;
        }    
        if((s[i]=='a' && s[i+1]=='c' && i+1<s.length()) or (s[i]=='b' && s[i+1]=='a' && i+1<s.length()) or (s[i]=='c' && s[i+1]=='a' && i+1<s.length()) or (s[i]=='c' && s[i+1]=='b' && i+1<s.length())){
        // cout<<"NO";
        flag = 1;          
        }
    }
    // cout<<countA<<" "<<countB<<" "<<countC<<endl;
    if(countA<1 or countB<1){
        // cout<<"NO";
        flag = 1;
    }
    if(countA != countC){
        // cout<<"NO";
        if(countB!=countC){
            flag =1;
            // cout<<"3f";
        }
        
    }
    if(flag==1){
        cout<<"NO";
    }
    else{cout<<"YES";}
    
    return 0;
}