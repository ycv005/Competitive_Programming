#include<bits/stdc++.h>
// #include<limits.h>
using namespace std ;
#define speedup ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

#define ll long long int
#define endl "\n"
#define REP(i,n) for(int i=0;i<n;i++)

// #define max INT_MAX

int tmp[99999999];

int main()
{
    speedup;
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        int tmp1,tmp2,tmp3;
        tmp3 =0;
        for(int i=0;i<n;i++)
        {
            cin>>tmp1>>tmp2;

            if(tmp3<tmp2)
                tmp3 = tmp2;

            for(int j=tmp1;j<tmp2;j++)
                tmp[j]= 1;
        }

        int arr[m];
        int count =0;
        for(int i=0;i<m;i++)
        {
            cin>>arr[i];
        }
        int j=0;
        for(int i=0;i<m;i++)
        {
            // cin>>arr[i];
            if(arr[i]>=tmp3)
            {
                cout<<-1<<endl;
                continue;
            }
            if(tmp[arr[i]]==1)
            {
                cout<<0<<endl;
                continue;
            }
            else if(tmp[arr[i]]==0)
            {

                j= arr[i];
                count =0;
                while(tmp[j]!=1)
                {
                    count++;
                    j++;
                }
                // count =0;
                // for(int j=arr[i];j<tmp3;j++)
                // {
                //     if(tmp[j]!=1)
                //     {
                //         count++;
                //     }
                //     else
                //     {
                //         break;
                //     }
                // }
                cout<<count<<endl;
            }
        }
    }
}