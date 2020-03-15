//https://www.hackerrank.com/challenges/append-and-delete/problem
#include<bits/stdc++.h>
using namespace std;
int main(){
    string s,t;
    cin>>s>>t;
    
    int k,ind=0,l = min(s.length(),t.length());
    cin>>k;
    for(int i=0;i<l;i++){
        if(s[i]!=t[i]){
            ind = i;
            break;
        }
    }

    // cout<<"ind"<<ind;
    if(ind==0 && s[0]==t[0]){
        if(k%2==0 && t.length()-s.length()>0 && (k-(t.length()-s.length()))%2!=0){
            cout<<"No"<<endl;
        }
        else if(k>=max(s.length(),t.length())-min(s.length(),t.length())){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }

    }
    else if(ind==0 && s[0]!=t[0]){
        if(k>=t.length()+s.length()){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }        
    }
    else{
        if(k>=s.length()+t.length()-2*ind){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }

    }

    return 0;
}