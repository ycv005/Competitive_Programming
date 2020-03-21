#include<iostream>
#include<algorithm>
using namespace std;
double GetMode(double daArray[], int iSize) {
    // Allocate an int array of the same size to hold the
    // repetition count
    int* ipRepetition = new int[iSize];
    for (int i = 0; i < iSize; ++i) {
        ipRepetition[i] = 0;
        int j = 0;
        bool bFound = false;
        while ((j < i) && (daArray[i] != daArray[j])) {
            if (daArray[i] != daArray[j]) {
                ++j;
            }
        }
        ++(ipRepetition[j]);
    }
    int iMaxRepeat = 0;
    for (int i = 1; i < iSize; ++i) {
        if (ipRepetition[i] > ipRepetition[iMaxRepeat]) {
            iMaxRepeat = i;
        }
    }
    delete [] ipRepetition;
    return daArray[iMaxRepeat];
}

int main(){
    cout<<"How many number did you want to enter-";
    int number,sum=0;
    cin>>number;
    double a[number];
    for(int i=0;i<number;i++)
        {  cin>>a[i];
           sum = sum + a[i];}
    float mean,median;
    mean= (sum)/(number+0.0);
    sort(a,a+number);
    if((number-1)%2!=0){
     median= (a[(number-1)/2] + a[(number-1)/2 + 1])/2.0;
    }
    else{
        median = (a[number-1/2])/2.0;
    }
cout<<"The Mean and Median are: "<<mean<<" "<<median;
cout<<"\nThe Mode Value is: "<<GetMode(a, number);
    return 0;
}