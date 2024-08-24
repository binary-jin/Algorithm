#include <iostream>

using namespace std;

int main()
{
    int a, b;
    int result;

    cin >> a >> b;

    if(a>b){
        cout << ">";
    }
    if(a<b){
        cout << "<";
    }
    if(a==b){
        cout << "==";
    }
}