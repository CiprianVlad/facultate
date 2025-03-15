#include <iostream>

using namespace std;

class A
{
public: // Tot ce e public este interfata 
    A() { cout << "A"; }
    ~A() { cout << "~A"; }

    string get_Status() const { return status; }
    void set_Status(string s) { status = s; }
private:
    string status;
};

class B : public A
{
public:
    B() { cout << "B"; }
    ~B() { cout << "~B"; }
};

int main()
{
    A obj1;
    B obj2;
    return 0;
}

