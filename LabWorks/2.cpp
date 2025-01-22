//4. Reverse the array elements in place

#include <iostream>
using namespace std;

int main() {
    const int SIZE = 10;
    int arr[SIZE];

    // Input array
    cout << "Enter 10 integers:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cin >> arr[i];
    }

    // Reverse the array
    for (int i = 0; i < SIZE / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[SIZE - 1 - i];
        arr[SIZE - 1 - i] = temp;
    }

    // reversed array
    cout << "Reversed array: ";
    for (int i = 0; i < SIZE; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}