const 함수명 = function() {
    //함수의 기능을 표현한 구문
}
const sayHello = function(){
    let number = 3 + 3
    console.log(number)
}
sayHello() // 함수 호출!!
const sayBye = function(){
    console.log("good bye~")
}
function sayHello2() {
    let hello = "문자열 헬로우"
    console.log(hello)
}
//undefined 변수는 있지만 그 안에 데이터는 대입되지 않은 상태

function thereIsReturn(){
    console.log("반환한다, 몽!")
    return 10, 20, 30, 40, 50; //50만을 출력한다
}
const result = thereIsReturn()
console.log(result)
//return 은 하나의 변수만을 대입할 수 있으며 함수값을 종료시킨다.

function sayVegetable(vegetable){//매개변수(parameter)
    console.log("함수에 전달된 채소는?")
    console.log(vegetable)
}
sayVegetable("당근")//인자(argument)
sayVegetable("오이")

function sayAnything(ant, number){
    for(let i = 0; i < number; i++){
        console.log(ant)
    }
}
sayAnything("바빠서 영상을 못 만들고 있어요", 6)
sayAnithing("만드는 법을 까먹을 지경 ㅠㅠ", 2)

function oddsAndzzak(num){
    if(num % 2 == 0){
        console.log("짝수")
    } console.log("홀수")
}
console.log(oddsAndzzak(2))
console.log(oddsAndzzak(3))
