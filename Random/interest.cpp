#include<iostream>
#include <cmath>
using namespace std;
int main(){
    float interest,p_amt,rate,t_amt;
    int year;
    interest = p_amt * pow((1+rate/100.0),year);
    t_amt = p_amt + interest;
    cout<<"The Interest and total amount is- "<<interest<<" and "<<t_amt;
    return 0;
}