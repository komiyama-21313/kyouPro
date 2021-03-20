#include<iostream>
#include<math.h>
#include<vector>
#include <iomanip>

using namespace std;

int main(void){
    cout << fixed << setprecision(15);
    int N;
    cin >> N;
    vector<long> x_vec(N);
    for(int i=0;i<N;i++){
        cin >> x_vec[i];
    }
    long ans1 = 0, ans2 = 0, ans3 = 0;
    for(int i = 0; i < N; i++) ans1 += abs(x_vec[i]);
    for(int i = 0; i < N; i++) ans2 += x_vec[i] * (long)x_vec[i];
    for(int i = 0; i < N; i++) ans3 = max(ans3, x_vec[i]);
    cout << ans1 << endl;
    cout << sqrt(ans2) << endl;
    cout << ans3 << endl;

    return 0;
}