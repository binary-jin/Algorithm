#include <iostream>

using namespace std;

int arr[9][9];
int main()
{
    int a; 
    int max = 0; 
    int x, y;

	for (int i = 0; i < 9; i++) {

		for (int j = 0; j < 9; j++) {
            
			cin >> a;
			arr[i][j] = a;

			if (arr[i][j] > max) {
				max = arr[i][j];
				x = i; 
                y = j;
			}
		}
	}
    cout << max << "\n";
    cout << x + 1 << " " << y + 1;
}