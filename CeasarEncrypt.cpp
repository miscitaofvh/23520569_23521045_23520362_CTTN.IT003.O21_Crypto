#include<bits/stdc++.h>
using namespace std;

string CeasarEncrypt(string plain_text, int shilf_pattern) {
  string encrypted_text = "";

  for(char u:plain_text) {
    if(u == ' ' || u == '_' || u == '-') encrypted_text += u;
    else {
      encrypted_text += char((u-'A'+shilf_pattern)%26 + 'A');
    } 
  }
  return encrypted_text;
}
int main() {
  string plain_text;
  getline(cin, plain_text);
  int shilf_pattern; cin >> shilf_pattern;
  cout << CeasarEncrypt(plain_text, shilf_pattern);
}