function solution(n) {
    const array = [];
    
    for (let i = 1; i <= n; i += 2) {
        array.push(i);
    }
    
    return array;
}



// function solution(n) {
//     const array = [];
    
//     for (let i = 1; i < n + 1; i++) {
//         i % 2 === 1 && array.push(i);
//     }
//     return array;
// }