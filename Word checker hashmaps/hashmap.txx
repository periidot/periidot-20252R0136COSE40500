/** 
  * Assignment 3 for COSE213 Data Structures
  *
  * Won-Ki Jeong (wkjeong@korea.ac.kr)
  *
  */


template <class HashMapElemType>
HashMap<HashMapElemType>::HashMap(unsigned int c) 
{
	mapsize = 0;
	capacity = c;
	divisor = c;
	ht = new HashMapElemType*[capacity]; //*!! PTRs to hashmapelemtype obj
	for (int i=0; i<capacity; i++){
		ht[i] = nullptr; //all buckets point nowhere rn, chains 
	}
}

// destructor
template <class HashMapElemType>
HashMap<HashMapElemType>::~HashMap() 
{
	for (int i=0; i<capacity; i++){
		HashMapElemType* current = ht[i];
		while (current !=nullptr){
			HashMapElemType* next = current->link;
			delete current;
			current = nullptr;
			current = next; //allat until no els in non empty chain
		}
	}
	delete [] ht; //now delete table
}

template <class HashMapElemType>
HashMapElemType* 
HashMap<HashMapElemType>::find(const KeyType k) 
{ 
	int ind = hashfunction(k);
	HashMapElemType* bucket = ht[ind];

	while (bucket != nullptr){
		if (bucket->key == k){
			return bucket;
		}
		bucket = bucket->link;
	}
	return nullptr;
}

template <class HashMapElemType>
void 
HashMap<HashMapElemType>::insert(const KeyType k, const ValType v) 
{

	int ind = hashfunction(k);
	HashMapElemType* bucket = ht[ind];
	bool exist = false;

	while (bucket != nullptr){
		if (bucket->key == k){ 
			exist = true;
			bucket->val = v; //update value w given one
			break;
		}
		bucket = bucket->link;
	}
	if (exist == false){
		HashMapElemType* newentry = new HashMapElemType();
		newentry->key = k;
		newentry->val = v;

		newentry->link = ht[ind];
		ht[ind] = newentry;
		mapsize++;
	}
}

template <class HashMapElemType>
bool 
HashMap<HashMapElemType>::remove(const KeyType k) 
{

	int ind = hashfunction(k);
	HashMapElemType* bucket = ht[ind];
	HashMapElemType* prev = nullptr;
	bool exist = false;

	while (bucket != nullptr){
		if (bucket->key == k){ 
			exist = true;
			if (prev == nullptr){ //if bucket is first el
				ht[ind] = bucket->link;
			}
			else {
				prev->link = bucket->link;
			}
			delete bucket;
			mapsize--;
			return true;
		}
		prev = bucket;
		bucket = bucket->link;
	}
	if (exist == false){
		return false;
	}
}

template <class HashMapElemType>
unsigned int 
HashMap<HashMapElemType>::hashfunction(const KeyType k)
{
	int number = 0;
	for (int i = 0; i< k.length(); i++){
		number += static_cast<int>(k[i]);
		if (i+1 < k.length()){
			number += static_cast<int>(k[i+1]) << 8;
		}
	}
	return number % divisor;

}

template <class HashMapElemType>
void 
HashMap<HashMapElemType>::print()
{
	for (int i=0; i<capacity; i++){
		HashMapElemType* n = ht[i];
		while (n !=nullptr){
			std::cout << "Key : " << n->key << ", Val : " << n->val << std::endl;
			n = n->link;
		}
	}
}