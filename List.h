class List{
	 
public:
	struct node_t *head, *tail;
	List(){
		head=NULL;
		tail=NULL;			
	}	
	void add_node(int);
	void traverse();
};
