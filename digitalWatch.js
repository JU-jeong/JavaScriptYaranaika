//객체만들기

function dog(){
    this.bark = "와르르르르"
    this.bark2 = "우르르르르르"
}

const doggie = new dog()
console.log(doggie.bark)
console.log(doggie.bark2)


function dog2(paramShit, paramBark){
    this.poo = paramShit
    this.bark = paramBark
}
const kelly1 = new dog2("끄응", "왈왈")
const kelly2 = new dog2("끄응2", "왈왈2")
const kelly3 = new dog2("끄응3", "왈왈3")
const kelly4 = new dog2("끄응4", "왈왈4")

console.log(kelly1.bark, kelly1.poo)
console.log(kelly1)
console.log(kelly4.bark, kelly2.poo)

const now = new Date()
const then = new Date(2008, 5, 10)
const interval = now - then
console.log(interval)

const now2 = new Date();
console.log(now2)
const then2 = new Date(2020, 9, 10)
console.log(then2)

const h1 = document.querySelector('h1')
const now = new Date();
const hour = now.getHours()
const minu = now.getMinutes()
const seco = now.getSeconds()

const nowTime = '${hour}:${minu}:${seco}'
h1.textContent = nowTime;

const h1 = document.querySelector('h1')
const now = new Date();
console.log(now.toLocaleString())