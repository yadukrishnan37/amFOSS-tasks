


function is_prime(num) {
    var count = 0;
    for (let i = 1; i <= num; i++) {
        if (num % i === 0) {
            count+=1;
        }
    }
    if(count === 2)
        return true;
    else
        return false;
}


function main() {
    const n = parseInt(prompt("Enter a number:"));
    for (let i = 2; i <= n; i++) {
        if (is_prime(i)) {
            console.log(i);
        }
    }
    
}

main();
