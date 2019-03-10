#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long int k,n;
        cin>>n>>k;
        long long int score[n];
        for(long int i=0;i<n;i++){
            cin>>score[i];
        }
        sort(score, score + n,greater<long long int>()); //takes nlogn, better we iterate via the list n.
        k-=1;
        long int count = 0;
        // cout<<"here is the score[k]-"<<score[k]<<endl;
        for(long int i=0;i<n;i++){
            if(score[i]>=score[k]){
                // cout<<"here is the score caught-"<<score[i]<<endl;
                count++;
            }
            // else{
            //     break;
            // }
        }
        cout<<count<<endl;
    }
    return 0;
}