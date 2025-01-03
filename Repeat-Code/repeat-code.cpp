#include <iostream>
#include <string>
using namespace std;

class Two_RepeatCode {
    public:
        static void make(string input) {
            int length = input.length();
            for (int i = 0; i < length; i++) {
                cout << input[i] << input[i];
            }
            cout << endl;
        }
        static void decode(string input) {
            int length=input.length();
            if (length%2!=0){
                cout << "Invalid input." << endl;
                return;
            }
            bool error=false;
            for(int i=0; i<length; i+=2){
                if (input[i]!=input[i+1]){
                    cout << "Error is here. " << (i+1)/2+1 << endl;
                    error=true;
                }
            }
            if (!error) cout << "No error." << endl;
            return;
        }
};

class Three_RepeatCode {
    public:
        static void make(string input) {
            int length = input.length();
            for (int i = 0; i < length; i++) {
                cout << input[i] << input[i] << input[i];
            }
            cout << endl;
        }
        static void decode(string input) {
            int length = input.length();
            if (length % 3 != 0) {
                cout << "Invalid input." << endl;
                return;
            }
            for (int i = 0; i < length; i += 3) {
                if (input[i] == input[i + 1] || input[i] == input[i + 2]) {
                    cout << input[i];
                } else if (input[i + 1] == input[i + 2]) {
                    cout << input[i + 1];
                }
            }
            cout << endl;
            return;
        }
};

int main(void){
    string input;
    int number;
    string select;
    cin >> input;
    cin >> number;
    cin >> select;
    for (int i = 0; i < input.length(); i++) {
        if (input[i] != '0' && input[i] != '1') {
            cout << "Invalid input." << endl;
            return 0;
        }
    }
    if (number == 2) {
        if (select == "make") Two_RepeatCode::make(input);
        else if (select == "decode") Two_RepeatCode::decode(input);
        else cout << "Invalid select." << endl;
    }
    else if (number == 3) {
        if (select == "make") Three_RepeatCode::make(input);
        else if (select == "decode") Three_RepeatCode::decode(input);
        else cout << "Invalid select." << endl;
    }
    else {
        cout << "Invalid number." << endl;
    }
    return 0;
}