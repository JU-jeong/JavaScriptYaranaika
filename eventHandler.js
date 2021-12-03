/* const inputType = document.querySelector("#typing")
const inputClick = document.querySelector("#push")
const inputClick = document.querySelector("#push2")

const handleTyping = function(){
    console.log("타이핑 되고 있어요!")
}

const handleClick = function(){
    console.log("클릭되고 있어요!")
}

inputType.onkeydown = handleTyping
inputClick.onclick = handleClick

EventTarget.onclick = function(){}

EventTarget.addEventListener('click', function(){})

push2.addEventListener('click', handleClick) */

/* const btn1 = document.getElementById("push")
const btn2 = document.getElementById("push2")
const btn3 = document.getElementById("push3")

const handleClick = function() {
    console.log("저를 클릭하셨나요?")
}

btn2.addEventListener('click', handleClick)
btn2.addEventListener('click', function(){
    console.log("또 다른 핸들러가 추가 등록되었다!")
})

btn2.removeEventListener('click', handleClick) */

const button = document.getElementById("push")
const div = documnet.getElementById("area")

button.addEventListener('click', function(){
    console.log("div 생성 중!")
    document.createElement("div")
    newDiv.style.backgroundColor = "red"
    newDiv.style.width = "200px"
    newDiv.style.heigth = "200px"
    div.appendChild(newDiv)
})