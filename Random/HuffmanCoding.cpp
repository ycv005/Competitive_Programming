#include <bits/stdc++.h>
using namespace std;

struct minHeapNode{
    char data;
    int freq;
    minHeapNode *left;
    minHeapNode *right;
    //Assigning the default values to the 
    minHeapNode(char data,int freq){
        this->data = data;
        this->freq = freq;
        left = right = NULL;
    }
};
struct compare{
        bool operator()(minHeapNode* l, minHeapNode* r)
    {
        return (l->freq > r->freq);
    }
};

void printCode(struct minHeapNode *top,string s){
   if(top != NULL){
       return;
   }
   if(top->data != '$'){
       cout<<top->data<<" : "<<s;
   }
   printCode(top->left,s+"0");
   printCode(top->right,s+"1");  
}

void huffman(char arr[],int freq[],int size){

    struct minHeapNode *left, *right, *top;
    //creating a minHeap
    priority_queue<minHeapNode*,vector<minHeapNode*>,compare> minHeap;

    //adding the element in the minArray
    for(int i=0;i<size;i++){
        minHeap.push(new minHeapNode(arr[i],freq[i]));
    }

    while (minHeap.size() != 1){
        //extracting two min frequency
        left = minHeap.top();
        minHeap.pop();
        right = minHeap.top();
        minHeap.pop();
        top = new minHeapNode('$',left->freq + right->freq);        // "" and '' are string and char respectively. "a" is equal to 'a' and '\0' whereas 'a' is 
        top->left = left;
        top->right = right;
        minHeap.push(top);         //it is not a character, that's why not passing a character
        }

        //cout<<"The top of the minHeap "<<minHeap.top()->freq;
        printCode(minHeap.top(),"");
}

int main(){
    char arr[] = {'a','b','c','d','e','f'};
    int freq[] = {5,9,12,13,16,45};
    int size = sizeof(arr)/sizeof(arr[0]);
    cout<<size;
    huffman(arr,freq,size);         //passing the base address of the array to the function
    cout<<"\n"<<size;
    return 0;
}