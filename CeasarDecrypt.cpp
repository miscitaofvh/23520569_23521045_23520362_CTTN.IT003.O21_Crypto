#include<bits/stdc++.h>
using namespace std;

void CeasarDecrypt(string encrypt_text) {
  for(int shilf=0; shilf<26; shilf++) {
    string shilfed_text = "";
    for(char u:encrypt_text) {
      if(u == ' ' || u == '_' || u == '-') shilfed_text += u;
      else {
        shilfed_text += char((u-'A'-shilf+26) % 26 + 'A');
      }
    }
    cout << "Shilf " << shilf << ": " << shilfed_text << endl;
  }
}
int main() {
  freopen("Decrypt.out", "w", stdout);
  string encrypt_text;
  getline(cin, encrypt_text);

  CeasarDecrypt(encrypt_text);
}