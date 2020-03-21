#include<iostream>
using namespace std;
#define V 10
void dfs(int graph[V][V],int src){}
void dfsTraversal(int graph[V][V],int src){
    //let's start with 0 as the source
    //need a visited List and Stack to 
    int visit[V];
    int parent[V];
    for(int i=0;i<V;i++){
        visit[i]=0;
        parent[i]=-1;
    }
    visit[src]=1;
    dfs(graph,src);
}
int main(){
    int graph[V][V] = {{0,1,1,1,0,0,0,0,0,0},
                       {1,0,1,0,0,0,0,0,0,0},
                       {1,1,0,0,0,0,0,0,0,0},
                       {1,0,0,0,1,0,0,1,0,0},
                       {0,0,0,1,0,1,1,0,0,0},
                       {0,0,0,0,1,0,1,1,1,0},
                       {0,0,0,0,1,1,0,0,0,0},
                       {0,0,0,1,0,1,0,0,1,0},
                       {0,0,0,0,0,1,0,1,0,0},
                       {0,0,0,0,0,0,0,0,1,0}};
    int src=0;
    // cout<<"Enter Src Vector-";
    // cin>>src;
    dfsTraversal(graph,src);
    return 0;
}