#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include<vector>
using namespace std;
void addEdge(vector<int> adj[], int u,int v){
    adj[u].push_back(v);    //making the directed graph
}
void printGraph(vector<int> adj[],int v){
    for(int i=0;i<v;i++){
        cout<<"Vertex is ->"<<i<<"\n";
        for(auto j:adj[i]){
            cout<<j<<" ";
        }
        cout<<"\n";
    }
}

int main(){
    int v=5;
    vector<int> adj[v];
    addEdge(adj,0,1);
    addEdge(adj,0,4);
    addEdge(adj,1,2);
    addEdge(adj,1,4);
    addEdge(adj,2,3);
    addEdge(adj,3,0);
    addEdge(adj,3,2);
    addEdge(adj,4,1);
    addEdge(adj,4,3);
    printGraph(adj,v);
    return 0;
}