#include<iostream>
#include<limits>
using namespace std;
struct Edge{
    int src,dst,weight;
};
struct Graph{
    int V,E;
    struct Edge* edge;
};
struct Graph* createGraph(int v, int e){
    struct Graph* graph = new Graph;
    graph->V = v;
    graph->E = e;
    graph->edge = new Edge[e];
    return graph; 
};

void print(int* dist, int V){
    for(int i=0;i<V;i++){
        printf("%d \t\t %d\n", i, dist[i]);
    }
}

void bellmanFord(struct Graph* graph,int src){
    int V=graph->V;
    int E = graph->E;
    int dist[V];
    for(int i=0;i<V;i++){
        dist[i]=INT16_MAX;
    }
    dist[src]=0;
    for(int i=0;i<V-1;i++){ //running relaxing for v-1 times
        for(int j=0;j<E;j++){
            if(dist[graph->edge[j].dst] > dist[graph->edge[j].src] + graph->edge[j].weight && dist[graph->edge[j].src]!=INT16_MAX){
                dist[graph->edge[j].dst] = dist[graph->edge[j].src] + graph->edge[j].weight;
            }
        }
    }
    //checking for the negative cycle
    for(int j=0;j<E;j++){
        if(dist[graph->edge[j].dst] > dist[graph->edge[j].src] + graph->edge[j].weight && dist[graph->edge[j].src]!=INT16_MAX){
            cout<<"Contains Negative Weight Cycle"<<endl;
        }
    } 
    print(dist,V);
}

int main(){
    int V = 5;
    int E= 9;
    struct Graph* graph = createGraph(V,E);

    //Using -> when ClassPointer->FieldName
    //Using . when ClassInstance.FieldName
    //Using :: when ClassName.FieldName, FieldName must be static
    graph->edge[0].src = 0;
    graph->edge[0].dst = 1;
    graph->edge[0].weight=6;

    graph->edge[0].src = 0;
    graph->edge[0].dst = 4;
    graph->edge[0].weight=7;

    graph->edge[0].src = 1;
    graph->edge[0].dst = 2;
    graph->edge[0].weight=5;

    graph->edge[0].src = 1;
    graph->edge[0].dst = 3;
    graph->edge[0].weight=-4;

    graph->edge[0].src = 1;
    graph->edge[0].dst = 4;
    graph->edge[0].weight=8;

    graph->edge[0].src = 2;
    graph->edge[0].dst = 1;
    graph->edge[0].weight=-2;

    graph->edge[0].src = 3;
    graph->edge[0].dst = 2;
    graph->edge[0].weight=7;
    
    graph->edge[0].src = 4;
    graph->edge[0].dst = 3;
    graph->edge[0].weight=9;

    graph->edge[0].src = 4;
    graph->edge[0].dst = 2;
    graph->edge[0].weight=-3;

    return 0;
}