#include<iostream>
#include<ctype.h>
#include<sstream>
#include<string>
#include<vector>
using namespace std;
vector<int> parseInts(string str){
    stringstream ss(str);
    vector<int> n;
    char ch;
    int temp;
    while(ss>>temp){
        n.push_back(temp);
        ss>>ch;
    }
    return n;
}
int main(){
    string str[2];
          for(int i=0;i<2;i++){
            // for(int j=0;j<m;j++){
                cin>>c[i];
            // }
        }
    
    return 0;
}