/**
 * @param {number} n
 * @return {boolean}
 */

const isHappy = (n) => {
    while (happyHelper(n) > 10) {
        n = happyHelper(n)
    }

    if (n === 1 || n === 7) {
        return true
    } else {
        return false
    }
};

const happyHelper = (n) => {
    if (parseInt(n / 10) > 0) {
        let quotient = parseInt(n / 10); // 
        let remainder = n % 10; // 
        if (quotient === 10) return quotient;
        n = (quotient * quotient) + (remainder * remainder); // 1
    }

    return n;
};