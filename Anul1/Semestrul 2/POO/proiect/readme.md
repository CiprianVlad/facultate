Banking System Simulator using OOP 

---

Workflow 

1. Separarea pe clase .h .cpp ale claselor  
2. Implementare account.h, bank.h, transactions.h 
3. Implemnetare account.cpp, bank.cpp, transactions.cpp
4. Implementare main.cpp 
5. Testare & Debugging
6. Implementare tipuri de conturi + functii\
    6.1. Implementare savings_acc.h & savings_acc.cpp\
	6.2. Implementare adult_acc.h & adult_acc.cpp\
	6.3. Implementare child_acc.h & child_acc.cpp\
	6.4. Implementare student_acc.h & student_acc.cpp\
7. Error Handling pentru fee (N-ar trebui sa setez eu fee din main)
8. Implement Namespaces 
9. Research Investing Simulation 
10. Implementare investii din banca (bonds, mutual funds, stocks)

---

Main classes : Bank, Accounts, Transactions 

Bank : Manages multiple accounts and provides methods for creating accounts and viewing details. 
(Detail idea : Un user poate avea mai multe conturi la aceeasi banca)

Accounts :  deposit, transfer, withdrawal (Detail idea : Taxa pentru schimbat currency)
// Represents a bank account with methods for depositing, withdrawing, and transferring funds. 

Transactions : keeps a transaction record to keep track of deposits, withdrawals, and transfers. 

Idei in general for enhancements :

1. Error Handling : UNIT tests 
Implement error handling to manage invalid operations, 
such as transferring more than the available balance 
or withdrawing from a non-existent account.

+ Nu exista mai multe conturi cu acceeasi adresa. 

2. Account Types : Student acc ; Adult acc ; Admin ? 

3. Data Persistence: Salvez datele dintre sesiuni 

4. Investitii:  in bonds ; mutual fonds ; stocks ; 
	4.1. Bonds ( return fixed rate, usor de implementat) 
	4.2. Mutual Funds ( Return an average of 8 to 12 percent per year) -> Needs a bit of research sa vad care ar fi limita 
	4.3. Stocks ( Higher risk, higher reward) -> Similar cu Mutual funds

	Pentru stocks : o iteratie reprezinta o luna / o zi 
1. (Pick a random number care sa fie return ul dintre 0 si 4 
1. si flip a coin pentru positive or negative number )
