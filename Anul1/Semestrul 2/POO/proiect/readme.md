Banking System Simulator using OOP 

---
Workflow 
1. Separarea pe clase .h .cpp ale claselor  
2. Scris definitii functii pentru bank 
3. Implemnetare clasa bank 
---

! Important : No namespaces 

Main classes : Bank, Accounts, Transactions 

Bank : Manages multiple accounts and provides methods for creating accounts and viewing details. (Detail idea : Un user poate avea mai multe conturi la aceeasi banca)

Accounts :  deposit, transfer, withdrawal (Detail idea : Taxa pentru schimbat currency) // Represents a bank account with methods for depositing, withdrawing, and transferring funds. 

Transactions : keeps a transaction record to keep track of deposits, withdrawals, and transfers. 

Idei in general for enhancing : 

1. Error Handling : UNIT tests 
//  Implement error handling to manage invalid operations, 
such as transferring more than the available balance or withdrawing from a non-existent account.
Link util : https://stackoverflow.com/questions/10983791/c-transaction-like-pattern-for-all-or-nothing-work

2. Account Types : Student acc ; Adult acc ; Child acc ; Admin ? 

3. User Interface: Sa pot sa interactionez cu the banking system 

4. Data Persistence: Salvez datele dintre sesiuni 

5. Investitii: (Ca pe revo) in bonds ; mutual fonds ; crypto why not   

Link pentru implementare in Python : https://harshilbmk.medium.com/day-28-oop-practice-building-a-banking-system-2901d553eca8
Sau : https://dev.to/eteimz/modeling-a-banking-system-in-oop-g23
Link-uri posibil utile : https://www.youtube.com/watch?v=xTh-ln2XhgU&ab_channel=JohanGodinho

Header files sau source files / utility / files ...  
.h pentru header si .cpp pentru source files 

Alta idee : Partid politic xd ( Membrii, Program intalniri, Legi de implementat, oameni pentru recrutari, Prioritati de partid : sesiuni, recrutat, grind in parlament)
