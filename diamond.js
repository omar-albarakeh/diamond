//printing reasult by console
function printhalfdiamond(num){
    for(let i=0 ; i<num ; i++){
        console.log("*".repeat(2*i + 1));
    }
    for(let i=rows-1 ; i>0 ;i--){
        console.log("*".repeat(2*i - 1));
    }
}
//let x = parseInt(prompt("enter ur nb: "));
//printhalfdiamond(rows);