class Solution {
public:
    bool isPalindrome(string s) {
        string sk="";
         for(char c : s){
            if(isalnum(c)){
                sk.push_back(tolower(c));
            }
        }
        string rev=sk;
        reverse(rev.begin(),rev.end());

       if(sk==rev){
        return true;
       }return false;
       
    }
};