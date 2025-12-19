#include "hashmap.h"
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

HashMap<MapElem<std::string, std::string>> dictionary;
  
void spellcheck(std::string s)
{
	std::cout << "> " << s << endl;
	if (dictionary.find(s) == nullptr){
		std::cout << "> " << s << " is NOT in the dictionary" <<endl;

		const int max = 15;
		int count = 0;
		std::string suggestions[max];

		for (size_t i = 0; i < s.length(); i++){
			std::string temp = s;
			for (char k = 'a'; k<='z'; k++){
				if (k==s[i]) continue;
				temp[i] = k;

				if (dictionary.find(temp) != nullptr){
					bool exists = false;
					for (int j=0; j<count; j++){
						if(suggestions[j] == temp){
							exists = true;
							break;
						} 
					}
					if (exists == false && count<max){
						suggestions[count++] = temp;
					}
				}
			}
		}

		if (count == 0){
			std::cout << "> " << s<< ": no suggestion\n"<< endl;
		}
		else {
			std::cout<< "> " << s << ": ";
			for (int i=0; i<count; i++){
				std::cout << suggestions[i];
				if (i != count-1){
					std::cout << ", ";
				} 
			}
			std::cout <<"\n"<< endl;
		}
	}

	if (dictionary.find(s) != nullptr){
		std::cout << "> " << s << " is in the dictionary\n"<< endl;
	}

	
}


int main()
{
	// load dictionary
	char filename[] = "dictionary.txt";
	std::ifstream ifs(filename, std::ifstream::in);
	std::string s((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
	std::transform(s.begin(), s.end(),
				   s.begin(), ::tolower);

	std::string token;	
	unsigned int len = s.length();
		
	for(int i=0; i<len; i++)
	{
		int ascii = s[i];
		
		if(ascii < 97 || ascii > 127) 
		{
			if(token.length() > 0) 
			{
				dictionary.insert(token, "brr");
				
				token.clear();
			}
			continue;
		}
		token.push_back(s[i]);
	}

	while(1)
	{
		std::string s;
		std::cout << "> ";
		std::cin >> s;
		
		if(s.compare("q") == 0) break;	
		
		spellcheck( s );
	}
	
	
	return 0;
}