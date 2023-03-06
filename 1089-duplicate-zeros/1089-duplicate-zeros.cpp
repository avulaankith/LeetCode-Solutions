class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int size = arr.size();
        for(int i = 0;i < size;i++){
            if(!arr[i]){
                arr.pop_back();
                arr.insert(arr.begin()+i, 0);
                i++;
            }
            else{
                continue;
            }
        }
        // int size = arr.size();
        // arr.resize(size);
        // return arr;
    }
};