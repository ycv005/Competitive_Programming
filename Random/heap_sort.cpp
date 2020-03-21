#include <iostream>
using namespace std;
 
void minHeapify(int arr[], int n, int i)
{
    int smallest = i; // Initialize smallest as root
    int l = 2 * i + 1; // left = 2*i + 1
    int r = 2 * i + 2; // right = 2*i + 2
 
    if (l < n && arr[l] < arr[smallest])
        smallest = l;
 
    if (r < n && arr[r] < arr[smallest])
        smallest = r;
 
    // If smallest is not root
    if (smallest != i) {
        swap(arr[i], arr[smallest]);
 
        minHeapify(arr, n, smallest);
    }
}
 
void minHeap(int arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        minHeapify(arr, n, i);

    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        minHeapify(arr, i, 0);
    }
}
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << "\n";
}
int main()
{   int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
 
    minHeap(arr, n);
 
    cout << "Sorted array is \n";
    printArray(arr, n);
}