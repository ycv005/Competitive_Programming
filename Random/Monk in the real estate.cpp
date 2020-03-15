//https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-in-the-real-estate/description/
#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		int r,x,y;
		cin>>r;
		map<int, int> city;
		for(int i=0;i<r;i++){
			cin>>x>>y;
			city.insert(pair<int,int>(x,1));
			city.insert(pair<int,int>(y,1));
		}
		cout<<city.size()<<"\n";
		
	}
	return 0;						
}