//https://www.hackerrank.com/challenges/cut-the-sticks/problem
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> arr;
    int count= 0;
    // int arr[n];
    for(int i=0;i<n;i++){
        int tmp;
        cin>>tmp;
        arr.push_back(tmp);
        // arr[i]=tmp;
    }
    sort(arr.begin(),arr.end());
    reverse(arr.begin(), arr.end());

    while(!arr.empty()){

        cout<<arr.size()<<endl;
        for(int i = 0; i<arr.size();++i)
            arr[i]-=arr[arr.size()-1];
        while(arr.back() ==0 && !arr.empty())
            arr.pop_back();

        }
    return 0;
}