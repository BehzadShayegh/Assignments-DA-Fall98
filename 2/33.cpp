#include <iostream>
#define magic 1000007
using namespace std;

int main()
{
    long int n = 0;
    cin >> n;
    long int a[n];
    for(long int i=0; i<n; i++)
        cin >> a[i];
    
    long int max[n];
    max[0] = 1;
    for(long int i=1; i<n; i++)
        max[i] = a[i-1] == max[i-1] ? max[i-1]+1 : max[i-1];

    long int vect[n] = {0};
    for(long int i=0; i<n; i++)
        vect[i] = 1;

    // long int vect[n][n] = {0};
    // for(long int i=0; i<n; i++)
    //     vect[0][i] = 1;
    
    // for(long int j=1; j<n; j++) {
    //     for(long int i=j; i<n; i++)
    //         vect[j][i] = (vect[j-1][i] + (i-j+1)*vect[j-1][i-1]) % magic;
    // }

    // cout << "________________________________________________________________________________________________________________\n";
    //  for(long int i=0; i<n; i++){
    //     cout << "        ";
    //     for(long int j=0; j<n; j++)
    //         if(vect[i][j] == 0)
    //             cout << "\t|\t";
    //         else
    //             cout << vect[i][j] << "\t|\t";
    //     cout << endl << "________________|_______________|_______________|_______________|_______________|_______________|_______________|\n";
    // }
    // cout << "=================================================\n";
    long int ans = a[n-1];
    
    for(long int i=0; i<n; i++)
        cout << vect[i] << '\t';
    cout << endl;

    for(long int j=1; j<n; j++){
        // for(int i=0; i<j; i++)
        //     cout << '\t';
        for(long int i=n-1; i>=j; i--){
            vect[i] = (vect[i] + (i-j)*vect[i-1]) % magic;
            cout << vect[i] << '\t';
        }
        cout << endl;
        // for(long int i=0; i<j; i++)
        //     cout << '\t';
        // for(long int i=j; i<n; i++)
        //     cout << vect[i] << '\t';
        // cout << endl;

        for(long int i=1; i<a[n-j-1]; i++) {
            if (i+1 >= max[n-j-1]+1) {
                ans = (ans + vect[j+i-1]) % magic;
            }
            else {
                ans = (ans + vect[j+max[n-j-1]-1]) % magic;
            }
        }
    }

    // long int ans = 1;
    // long int max = 0;
    // for(long int j=n-1; j>=0; j--) {
    //     for(long int i=1; i<a[n-j-1]; i++) {
    //         if (i+1 >= max) {
    //             // cout << "i = " << i << endl;
    //             ans = (ans + vect[j][j+i-1]) % magic;
    //             // cout << vect[j][j+i-1] << endl;
    //         }
    //         else {
    //             // cout << "max = " << max << endl;
    //             ans = (ans + vect[j][j+max-2]) % magic;
    //             // cout << vect[j][j+max-2] << endl;
    //         }
    //     }
    //     if (a[n-j-1]+1 > max)
    //         max = a[n-j-1]+1;
    //     // cout << "- - - - - - - - -\n";
    // }
    // // cout << "=================================================\n";
   
    cout << (ans)%magic << endl;
}