#include <iostream>
using namespace std;
int main() {
    int n, m, k;
    cin >> n >> m >> k;
    int a[n][m];

    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> a[i][j];
    long int vect[m][k+1] = {0};
    
    for(int i=n-1; i>=0; i--) {
        bool downest = (i == n-1);
        for(int j=m-1; j>=0; j--) {
            bool rightest = (j == m-1);
            int v = a[i][j];
            for(int q=0; q<=k; q++) {
                if (rightest && downest) {
                    vect[j][q] = int((q==k) || (q+v==k));
                }
                else if (downest) {
                    vect[j][q] = vect[j+1][q];
                    if (q+v <= k)
                        vect[j][q] += vect[j+1][q+v];
                }
                else if (rightest) {
                    if (q+v <= k)
                        vect[j][q] += vect[j][q+v];
                }
                else {
                    vect[j][q] += vect[j+1][q];
                    if (q+v <= k)
                        vect[j][q] += vect[j+1][q+v] + vect[j][q+v];
                }
                vect[j][q] %= (1000000007);
            }
        }
    }
    cout << vect[0][0] << endl;
}