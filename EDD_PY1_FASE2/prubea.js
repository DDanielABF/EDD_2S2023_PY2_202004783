function binarysearh(arr,num){
let start=0;
let end = arr.length-1;
while(start<= end){

let middle = Math.floor((start+end)/2);
if (arr[middle]===num){

return middle;
}else if (arr[middle]<num){
    start=middle+1;
}else{
end = middle-1

}
}


return -1;
}

const arr=[1,3,5,7,9];
const num=5;
console.log(binarysearh(arr,num))
