#include<iostream>
#include<limits>
#include<algorithm>
using namespace std;
#define v 5
void relax(int graph[v][v],int u,int j,int *dis,int *isRelax){
    if(dis[j]>dis[u]+graph[u][j] && isRelax[u]==0){
        dis[j] = dis[u]+graph[u][j];
    }  
}
int chosingV(int* dis,int* isRelax){
    int max = INT16_MAX,min,set=0;
    for(int i=0;i<v;i++){
        if(isRelax[i]==0 && dis[i]<max){
            min = dis[i];
            max = dis[i];
            set =i;
        }
    }
    return set;
}
void dijkstra(int graph[v][v],int source){
    int dis[v],isRelax[v];
    for(int i=0;i<v;i++){
        dis[i]=INT16_MAX;
        isRelax[i]=0;
    }    
    dis[source]=0;
    for(int i=0;i<v;i++){
        int u = chosingV(dis,isRelax);
        for(int j=0;j<v;j++){
            if(graph[u][j]!=0){
                relax(graph,u,j,dis,isRelax);
            }
        }
        isRelax[u]=1;
    }

    for(int i=0;i<v;i++){
        cout<<"The Shortest Distance to Vertex "<<i<<" is "<<dis[i]<<endl;
    }
}
int main(){
                    //0,1,2,3,4
    int graph[v][v] = {{0,10,0,0,5},
                     {0,0,1,0,2},
                     {0,0,0,4,0},
                     {7,0,6,0,0},
                     {0,3,9,2,0}};

    dijkstra(graph,0);
    return 0;
}