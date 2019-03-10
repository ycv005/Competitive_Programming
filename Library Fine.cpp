//https://www.hackerrank.com/challenges/library-fine/problem
#include<bits/stdc++.h>
using namespace std;
int main(){
	int rd,rm,ry,ed,em,ey;
	cin>>rd>>rm>>ry>>ed>>em>>ey;
	if(ry>ey){
		cout<<10000<<endl;
	}else if(ry<ey){
		cout<<0<<endl;
	}
	else if(rm<em && ry==ey){
		cout<<0<<endl;			
	}
	else if(rm==em && ry==ey){
		if(rd<=ed){
			cout<<0<<endl;
		}
		else{
			cout<<15*(rd-ed)<<endl;
		}
	}else if(rm>em && ry==ey){
		int tmp= 500*(rm-em);
		cout<<tmp<<endl;
	}
	return 0;
}