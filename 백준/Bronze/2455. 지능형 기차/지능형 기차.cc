#include <iostream>

using namespace std;

int station[4];
int main()
{
    int a, b, c, d, e, f, g, h;
    // int station1, station2, station3, station4;

    cin >> a >> b;
    cin >> c >> d;
    cin >> e >> f;
    cin >> g >> h;

    station[0] = a+b;
    station[1] = station[0]-c+d;
    station[2] = station[1]-e+f;
    station[3] = station[2]-g+h;

    int x = 0;
    for(int i=0;i<4;i++){
        if(station[i]>x){
            x = station[i];
        }
    }

    cout << x;

}

//0+32 = 32 
//(0+32)-3+13 = 42
//42 -28+25 = 39
//39 -39+0