//https://codeforces.com/contest/982/problem/A
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    if(n==1){
        if(s=="1"){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
    else if(n==2){
        if(s=="10" || s=="01"){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
    else if(n==3){
        if(s=="101" || s=="010"){
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
    else{
        vector<int> ind;
        bool cond1 = false;
        for(int i=0;i<n;i++){
            if(s[i]=='1'){
                //check neighbour
                if(i==0 && i+1<n && s[i+1]=='0'){
                    cond1 = true;
                    ind.push_back(i);
                    // cout<<i<<"c1"<<endl;
                }
                else if(i==n-1){
                    cond1 = true;
                    ind.push_back(i);
                    // cout<<"c3"<<endl;                  
                }                
                else if(i-1>=0 && i+1<n && s[i-1]=='0' && s[i+1]=='0'){
                    cond1 = true;
                    ind.push_back(i);
                    // cout<<"c5"<<endl;
                }
                else{
                    cond1 = false;
                    // cout<<i<<"c6"<<endl;
                    break;                    
                }
            }
            else if(s[i]='0'){
                if(i+1<n && i+2<n && s[i+1]=='0' && s[i+2]=='0'){
                    //if 3 continous zero
                    cond1 = false;
                    break;
                }
                if(i==0 && s[i+1]=='0'){
                    cond1 = false;
                    break;
                }
                else if(i==n-1 && s[i-1]=='0'){
                    cond1 = false;
                    break;                   
                }
            }
        }
        if(cond1 == true){
            //2nd cond1
            bool cond2 = false;
            for(auto i=ind.begin();i+1<ind.end();i++){
                if(*(i+1)-*i==2 || *(i+1)-*i==3){
                    cond2 = true;
                    // cout<<"c7"<<endl;
                }
                else{
                    cond2 = false;
                    // cout<<"c8"<<endl;
                    break;
                }
            }
            if(cond2 == true){
                // cout<<"c9"<<endl;
                cout<<"Yes"<<endl;
            }
            else{
                // cout<<"c10"<<endl;
                cout<<"No"<<endl;
            }
        }
        else{
            // cout<<"c11"<<endl;
            cout<<"No"<<endl;
        }
    }
return 0;
}