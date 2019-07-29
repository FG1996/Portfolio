#include <cstdlib>
#include <iostream>
#include "List.h"

using namespace std;

struct node_t
{
	unsigned v;
	struct node_t* next;
};

void List::add_node(int value){
		
	node_t *temp= new node_t;
	temp->v=value;
	temp->next=NULL;
	
	if(head==NULL){
		
		head=temp;
		tail=temp;
		temp=NULL;
	}
	
	else{
		
		tail->next=temp;
		tail=temp;
		temp=NULL;
	}
}

//used during testing to check whether everything was working
void List::traverse(){
	node_t *temp=head;
	while(temp!=NULL){
		cout<<temp->v<<endl;
		temp=temp->next;
	}
}	
