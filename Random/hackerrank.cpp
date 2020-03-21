#include <iostream>
#include<vector>
#include<sstream>
using namespace std;
 //Compiler version g++ 6.3.0
 int main()
 {  vector<int> v;
	string s;
	cin>>s;
	stringstream ss(s);
	char ch;
	int a[n];
    for(int i=0;i<n;i++){
        ss>>a[i];
        ss>>ch;
        v.push_back(a[i]);
    }
   	for(auto i=v.begin();i!=v.end();i++){
   		cout<<*i<<endl;
   	}
	   return 0;
 }