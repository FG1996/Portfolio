class Objs {
	
public:
	
    Objs() { 
		count++; 
	}
    
	Objs(const Objs&) {
		count++;
	}
	
    ~Objs() {
		count--;
	}
 
    int Nobjs(){
		return count;
	}
 
private:
	
    int count;
};
 
// assuming the implementation file would contain a definition like the one provided:
int Objs::count = 0;
