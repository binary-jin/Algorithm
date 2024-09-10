#include <iostream>

using namespace std;

int arr[42];
int main()
{
    int num;

    for(int i = 1; i < 11; i++) {
        cin >> num;
        arr[num%42] = 1;
    }

    int result = 0;
    for(int i = 0; i <= 42; i++) {
        if(arr[i]==1){
            result++;
        }
    }

    cout << result;


    return 0;
}