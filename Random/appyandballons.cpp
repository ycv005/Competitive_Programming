// #include<bits/stdc++.h>
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
void printArray(int p[], int n) 
{ 
    for (int i = 0; i < n; i++) 
       cout << p[i] << " "; 
    cout << endl; 
} 
  
void printAllUniqueParts(int n) 
{ 
    int p[n]; 
    int k = 0;  
    p[k] = n; 
    while (true) 
    { 
        printArray(p, k+1); 
        int rem_val = 0; 
        while (k >= 0 && p[k] == 1) 
        { 
            rem_val += p[k]; 
            k--; 
        } 
        if (k < 0)  return; 
        p[k]--; 
        rem_val++; 
        while (rem_val > p[k]) 
        { 
            p[k+1] = p[k]; 
            rem_val = rem_val - p[k]; 
            k++; 
        } 
        p[k+1] = rem_val; 
        k++; 
    } 
} 

int main(){
    long int n;
    long long int m;
    cin>>n>>m;
    long long int a[n];
    long long int b[n];
    priority_queue<pair<long long int,long long int>,vector<pair<long long int,long long int>>,less<pair<long long int,long long int>>> pq;
    for(long int i=0;i<n;i++){
        cin>>a[i];
    }
    for(long int i=0;i<n;i++){
        cin>>b[i];
        pq.push(make_pair(i,a[i]*b[i]));
    }
    printAllUniqueParts(m); 
    return 0;
}