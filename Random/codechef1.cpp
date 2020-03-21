#include<iostream>
#include<vector>
using namespace std;
vector<string> split(string target){
    vector<string> s;
    if(!target.empty()){
        string::size_type start=0;
        while(true){
            size_t x=target.find(start," ");
            if(x==string::npos)
                break
            s.push_back(target.substr(start,start-x));
        }
    }
}
int main(){
    string s;
    cin>>s;

    return 0;
}