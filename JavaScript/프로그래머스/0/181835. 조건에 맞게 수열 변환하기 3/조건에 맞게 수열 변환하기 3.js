function solution(arr, k) {
    var answer = [];
    const n = arr.length;
    if (k%2 == 1) {
        for (i = 0; i < n; i++) {
            answer.push(arr[i] * k)
        }
    } else {
        for (i = 0; i < n; i++) {
            answer.push(arr[i] + k)
        }
    };
    return answer;
}