// This file contains the 'main' function. Program execution begins and ends here.

#include <iostream>
#include "C:/Users/Ciprian/OneDrive - unibuc.ro/Desktop/facultate/Anul I sem II/POO/proiect/account.h"
#include "C:/Users/Ciprian/OneDrive - unibuc.ro/Desktop/facultate/Anul I sem II/POO/proiect/bank.h"
#include "C:/Users/Ciprian/OneDrive - unibuc.ro/Desktop/facultate/Anul I sem II/POO/proiect/transactions.h"

// Main function to demonstrate the banking simulation system
int main() {
    // Create accounts
    Account acc1("Ana", 1000.0);  // Account holder "Ana" with $1000
    Account acc2("Vasile", 500.0);     // Account holder "Vasile" with $500

    // Display initial balances
    std::cout << "Initial balances:\n";
    std::cout << "Ana: $" << acc1.getBalance() << "\n";
    std::cout << "Vasile: $" << acc2.getBalance() << "\n\n";

    // Create a transaction (3% fee)
    Transactions transfer(&acc1, &acc2, 200.0, -3.0);  // This is why we need error checking 

    // Execute and check result
    std::cout << "Executing transfer...\n";
    if (transfer.execute()) {
        std::cout << "Transfer succeeded!\n";
    }
    else {
        std::cout << "Transfer failed (insufficient funds or invalid accounts).\n";
    }

    // Display final balances
    std::cout << "\nFinal balances:\n";
    acc1.displayDetails(); 
    // std::cout << "Vasile: $" << acc2.getBalance() << "\n";

    return 0;
}