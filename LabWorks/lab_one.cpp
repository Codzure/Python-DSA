#include <iostream>
using namespace std;

// Create an array of integers with 10 elements. Populate the array with values entered by
// the user and Print the array elements.

int main() {
    int arr[10];
    for (int i = 0; i < 10; i++) {
        cout << "Enter the value for element " << i + 1 << ": ";
        cin >> arr[i];
    }
    cout << "The array elements are: ";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}


