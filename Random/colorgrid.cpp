#include<iostream>
#include<string>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        int flag = 0;
        string c[n];
        for(int i=0;i<n;i++){
                cin>>c[i];
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if((c[i][1]=='#' && i<n) || (c[1][j]=='#' && j<m) || (c[i][m-2]=='#' && m-2>=0) || (c[n-2][j]=='#' && n-2>=0)){
                        // cout<<"inside base case";s
                    flag = 1;
                    i=n;
                    j=m;
                }
                else if(c[i][j]=='#'){
                    if((j-2>=0 && c[i][j-2]=='#') || (i-2>=0 && c[i-2][j]=='#') || (i+2<n && c[i+2][j]=='#') || (j+2<m && c[i][j+2]=='#')){
                        flag = 1;
                        i=n;
                        j=m;    // cout<<"inside dobule case";
                    }
                }
            }
        }

        if(flag ==1){
            cout<<"NO"<<endl;
        }else{
            cout<<"YES"<<endl;
        }
    
    }
    return 0;
}