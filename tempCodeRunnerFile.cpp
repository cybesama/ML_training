#include<iostream>
using namespace std;
int main(){
    int r;
    cin >> r;

    int c;
    cin >> c;

    for(int i = 0;i < r;i++){
        for(int j=0;j<=i;j++){
            cout<<"*";

        }
        cout<<"\n";
    }

    return 0 ;
}
