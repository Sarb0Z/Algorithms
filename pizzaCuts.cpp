#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int removeDuplicates(int arr[], int n)
{
 
    int i;
 
    // Initialise a set
    // to store the array values
    set<int> s;
 
    // Insert the array elements
    // into the set
    for (i = 0; i < n; i++) {
        // insert into set
        s.insert(arr[i]);
    }
 
    return s.size();
 
}
int main() {
    int T;
    cin >> T;
    int **arr=new int*[T];
    int temp;
    int *count=new int[T];
    for (int i=0;i<T;i++){
        cin>>temp;
        arr[i]=new int[temp];
        for (int j=0;j<temp;j++){
            cin>>arr[i][j];
            arr[i][j]= (arr[i][j]%180 + 180)%180;
        }
        count[i]=removeDuplicates(arr[i], temp);

    }
    for (int i=0;i<T;i++){
        if (count[i]==0){
            count[i]=1;
        }
        else{
            count[i]=count[i]*2;
        }
        cout<<count[i]<<endl;
    }
    
    return 0;
}