#include <iostream>
using namespace std;

int cost(char input, int costA, int costC, int costG, int costT) {
    switch (input) {
        case 'A' :
            return costA;
        case 'C' :
            return costC;
        case 'G' :
            return costG;
        case 'T' :
            return costT;
    }
}

int main()
{
    string base;
    string target;
    int costA, costC, costG, costT;
    cin >> base >> target >> costA >> costC >> costG >> costT;

    int blen = base.size();
    int tlen = target.size();

    int i = 0;
    int mincost = 0;
    for (int q=0; q<tlen; q++)
        mincost += cost(target[q], costA, costC, costG, costT);

    while (i < blen) {
        int j = 0;
        int k = 0;
        int newCost = 0;
        while (j < tlen) {
            // cout << base[i+k] << endl;
            if((i+k < blen) && (base[i+k] == target[j])) {
                // cout << "yay" << endl;
                j++;
                k++;
            } else {
                newCost += cost(target[j], costA, costC, costG, costT);
                // cout << "->" << target[j] << endl;
                j++;
            }
        }
        // cout << "===" << endl;
        if (newCost < mincost)
            mincost = newCost;
        i++;
    }
    cout << mincost;
}