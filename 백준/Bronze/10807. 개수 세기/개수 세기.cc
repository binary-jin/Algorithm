#include <iostream>

using namespace std;


int main()
{
    int n; //입력받을 정수 개수
    int arr[101]; //입력 받을 정수들을 배열에 넣기위해 배열 초기화
    int v; //찾을 정수

    int result=0; //결과값 저장

    cin >> n; //입력받을 정수 개수를 입력받음

    for(int i = 0; i < n; i++) { //배열의 [i]번째에 입력하는 숫자를 차레로 넣기
        cin >> arr[i];
    }
    cin >> v; //찾을 숫자 입력받기

    for(int i = 0; i < n; i++) { //[0]부터 차례로 [i]까지 돌면서
        if(arr[i] == v) //만약 [i]번째 값이 찾으려는 정수와 같다면 result에 +1하기(어차피 같은 숫자의 개수만 알면 됨)
            result++;
    }

    cout << result;
    
}