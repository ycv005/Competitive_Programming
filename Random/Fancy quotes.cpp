#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;

#define dbg printf("in\n")
#define nl printf("\n")
#define N 150
#define inf 1000000000
#define pp pair<int,int>

#define sf(n) scanf("%d", &n)
#define sff(n,m) scanf("%d%d",&n,&m)
#define sfl(n) scanf("%I64d", &n)
#define sffl(n,m) scanf("%I64d%I64d",&n,&m)

#define pf(n) printf("%d",n)
#define pfl(n) printf("%I64d",n)
#define pfs(s) printf("%s",s)

#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define pb push_back

using namespace std;
int main(){
    FIO;
	int t;
    bool flag;
    string s,tok;
    
    cin >> t;
    
    getline(cin,s);
    while(t--){
        getline(cin,s);
        
        stringstream tokenizer(s);
        
        flag=false;
        
        while(getline(tokenizer,tok,' '))
            if(tok=="not"){
                flag=true;
                break;
            }
            
        if(flag)
            cout << "Real Fancy\n";
        else
            cout << "regularly fancy\n";
    }
    return 0;
}