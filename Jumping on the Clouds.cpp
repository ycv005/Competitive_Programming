#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,k;
	cin>>n>>k;
	int c[n];
	for(int i=0;i<n;i++){
		cin>>c[i];
	}
	int ind =0,e=100;
	do{
		ind = (ind+k)%n;
		e-=1; //jump
		if(ind<n && c[ind]==1){
			e-=2;
		}
	}while(ind!=0);
	cout<<e<<endl;
	return 0;
}