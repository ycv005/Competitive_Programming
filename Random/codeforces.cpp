#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>    //remove
#include <iterator>
#include<vector>
using namespace std;
int main(){
    int n,k,m;
    cin>>n>>k>>m;
    string str;
    cin>>str;
    string buf;                 // Have a buffer string
    stringstream ss(str);       // Insert the string into a stream

    vector<string> tokens; // Create vector to hold our words

    while (ss >> buf)
        tokens.push_back(buf);
    //words are in tokens
    int cost[n];
    for(int i=0;i<n;i++){
        cin>>cost[i];
    }
    auto it = find(tokens.begin(),tokens.end(),"me");
    
    return 0;
}