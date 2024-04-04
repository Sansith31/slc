#include <iostream>
#include <conio.h> // For non-blocking key press detection (getch())

using namespace std;

int main()
{
    string name1 = "Lison";
    string name2 = "Sansith";
    string name3 = "Chethana";

    cout << "****************************\n";
    cout << "Welcome to our Github Page !\n";
    cout << "Keep tuned for more retarted programs made by retards !\n";
    cout << "                   Fuck Society                \n";

    cout << "Retards in questions:\n";
    cout << "- " << name1 << endl;
    cout << "- " << name2 << endl;
    cout << "- " << name3 << endl;

    cout << "\nPress any key to delete System32 :)";

    // Non-blocking key press detection with getch()
    _getch();

    return 0;
}
