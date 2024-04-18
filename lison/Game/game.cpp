#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int die1, die2, die3, total;
int rollDice()
{

    die1 = rand() % 6 + 1;
    die2 = rand() % 6 + 1;
    die3 = rand() % 6 + 1;
    total = die1 + die2 + die3;
    return die1 + die2 + die3;
}

bool continueRolling(int point)
{
    while (true)
    {
        cout << "Player rolled " << die1 << " + " << die2 << " + " << die3 << " = " << total << endl;
        if (total == point)
        {
            cout << "Congratulations! You made your point. You win!" << endl;
            return true;
        }
        else if (total >= 15)
        {
            cout << "Player Loses " << endl;
            return false;
        }
    }
}

int main()
{
    srand(time(0));

    int sum = rollDice();
    cout << "You rolled: " << sum << endl;
    if (sum >= 13)
    {
        cout << "Player Wins" << endl;
    }
    else if (sum <= 6)
    {
        cout << "Player Loses" << endl;
    }
    else
    {
        cout << "Your point is: " << sum << endl;
        continueRolling(sum);
        std::cin.get();
    }

    return 0;
}