// https://www.interviewbit.com/problems/arraybug/
vector<int> Solution::rotateArray(vector<int> &A, int B) {
    vector<int> ret(A.size(), 0);
    for (int i = 0; i < A.size(); i++) {
        ret[(i + ret.size() - B%ret.size())%ret.size()] = A[i];
    }
    return ret;
}