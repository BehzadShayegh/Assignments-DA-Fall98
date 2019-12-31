#include <iostream>
#define magic 1000007
using namespace std;

int main()
{
    int n = 0;
    cin >> n;
    int a[n];
    for(int i=0; i<n; i++)
        cin >> a[i];
    
    int vect[n][n] = {0};
    for(int i=0; i<n; i++)
        vect[0][i] = 1;
    
    for(int j=1; j<n; j++) {
        for(int i=j; i<n; i++)
            vect[j][i] = (vect[j-1][i] + (i-j+1)*vect[j-1][i-1]) % magic;
    }

    cout << "________________________________________________________________________________________________________________\n";
     for(int i=0; i<n; i++){
        cout << "        ";
        for(int j=0; j<n; j++)
            if(vect[i][j] == 0)
                cout << "\t|\t";
            else
                cout << vect[i][j] << "\t|\t";
        cout << endl << "________________|_______________|_______________|_______________|_______________|_______________|_______________|\n";
    }
    cout << "=================================================\n";
    int ans = 1;
    int max = 0;
    for(int j=n-1; j>=0; j--) {
        for(int i=1; i<a[n-j-1]; i++) {
            if (i+1 >= max) {
                cout << "i = " << i << endl;
                ans = (ans + vect[j][j+i-1]) % magic;
                cout << vect[j][j+i-1] << endl;
            }
            else {
                cout << "max = " << max << endl;
                ans = (ans + vect[j][j+max-2]) % magic;
                cout << vect[j][j+max-2] << endl;
            }
        }
        if (a[n-j-1]+1 > max)
            max = a[n-j-1]+1;
        cout << "- - - - - - - - -\n";
    }
    cout << "=================================================\n";
   
    cout << (ans)%magic << endl;
}