#ifndef CHILD_ACOOUNT_H
#define CHILD_ACOOUNT_H

#include "C:/Users/Ciprian/OneDrive - unibuc.ro/Desktop/facultate/Anul I sem II/POO/proiect/account.h" // base header 
#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <chrono>

class Child_Acc : public Account {

private:
	double interest_rate; // interest rate for savings account
	std::chrono::system_clock::time_point last_deposit_time; // the last time of deposit 
public:
	// Constructor 
	Child_Acc(const std::string& holder, double initialBalance, double rate = 3.0);

	// Destructor
	~Child_Acc();

	// override deposit to track the timestamp
	void deposit(double amount) override;

	// apply interest to the balance
	void applyInterest();

	// display account details
	void displayDetails() const override;
};
#endif
