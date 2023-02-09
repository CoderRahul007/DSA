class Solution{
public:

	void rearrange(int arr[], int N) {
	    // code here
	     vector<int> ans;
	    int p = 0 , n = 0;
	    while(p < N || n < N){
	        while(p < N && arr[p] < 0) p++;
	        while(n < N && arr[n] >= 0) n++;
	        
	        if(p < N) ans.push_back(arr[p]);
	        if(n < N) ans.push_back(arr[n]);
	        p++; n++;
	    }
	    for(int i = 0 ; i < N ; i++) arr[i] = ans[i];
	}
};