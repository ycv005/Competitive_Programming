#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define pp pair<int,int>

#define rep(i,n) for (int i = 0; i < n; ++i) 
#define REP(i,k,n) for (int i = k; i <= n; ++i) 
#define REPR(i,k,n) for (int i = k; i >= n; --i) 

#define pb push_back
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
using namespace std;
bool sortbysec(const pair<int,int> &a, 
              const pair<int,int> &b) 
{ 
    return (a.second < b.second); 
} 
vector<vector<int> > performOps(vector<vector<int> > &A) {
    vector<vector<int> > B;
    B.resize(A.size());
    for (int i = 0; i < A.size(); i++) {
        B[i].resize(A[i].size());
        for (int j = 0; j < A[i].size(); j++) {
            B[i][A[i].size() - 1 - j] = A[i][j];
        }
    }
    return B;
}
int main(){
    FIO;
    vector<vector<int> > A{ { 1, 2, 3, 4 }, 
                               { 5, 6, 7, 8 }, 
                               { 9, 10, 11, 12 } };
    vector<vector<int> > B = performOps(A);
for (int i = 0; i < B.size(); i++) {
    for (int j = 0; j < B[i].size(); j++) cout<<B[i][j]<<" ";
}
    return 0;
}
//cout<<"\n";