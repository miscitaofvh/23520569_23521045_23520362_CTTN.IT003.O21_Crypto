// sun's code

#include <bits/stdc++.h>

using namespace std;

string password;

int main()
{
    cin >> password;

    for (auto &v : password)
        if (v < 'N') v += 13; 
            else v -= 13;

    cout << password << endl;
    
    return 0;
}