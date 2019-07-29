#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

void new_base_rep(unsigned int value, unsigned int base);

int main(int argc, char** argv) {
	
	new_base_rep(-10, 4);
	return 0;
}

void new_base_rep(unsigned int value, unsigned int base){

    string table[]={"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H",
           "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
           
    int remainder;      	 
    vector <int> output;

    if (value==0){
        cout<<value<<endl;
        return;
	}
	
    while (value>0){
	
        remainder=value%base;
        output.push_back(remainder);
        value=(int)floor(value/base);
	}
	
	for(int i=output.size()-1;i>=0;i--){
		cout<<table[output[i]];
	}
}
