#include<iostream>
#include<limits>
using namespace std;
#define V 5
void floydWarshall(int graph[V][V]){
    for(int inter=0;inter<V;inter++){
        for(int i=0;i<V;i++){
            for(int j=0;j<V;j++){
            //udpating the graph that include the ith path
                if(i!=inter || j!=inter || i!=j){//path already included
                    if(graph[i][j]> graph[i][inter] + graph[inter][j]){ //checking path with the intermediate
                        graph[i][j]= graph[i][inter] + graph[inter][j];
                    }
                }
            }
            
        }
    }  
for (int i = 0; i < V; i++) 
    { 
        for (int j = 0; j < V; j++) 
        { 
            if (graph[i][j] == INT16_MAX) 
                printf("%7s", "INF"); 
            else
                printf ("%7d", graph[i][j]); 
        } 
        printf("\n"); 
    } 
}
int main()
{
    int graph[V][V] = {{0,3,8,INT16_MAX,-4},
                       {INT16_MAX,0,INT16_MAX,1,7},
                       {INT16_MAX,4,0,INT16_MAX,INT16_MAX},
                       {2,INT16_MAX,-5,0,INT16_MAX},
                       {INT16_MAX,INT16_MAX,INT16_MAX,6,0}};
 
    floydWarshall(graph);
    return 0;
}
