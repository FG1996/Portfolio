#include <iostream>
#include "List.h"

struct node_t
{
	unsigned v;
	struct node_t* next;
};

struct node_t* even_nodes(struct node_t** point_to_head_point){
 	
 	List even, odd;
 	node_t * head=*point_to_head_point;
 	node_t *current_element= head;
 	
 	while(current_element!=NULL){
	 	if (current_element->v%2==0){
	 		even.add_node(current_element->v); 		
		}
		else{
			odd.add_node(current_element->v);
		}
		current_element=current_element->next;
	}
	point_to_head_point=&odd.head;
	return even.head;
}
