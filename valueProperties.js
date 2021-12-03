const textInput = document.getElementById("text")
const button = document.getElementById("button")

button.addEventListener("click",function(e){
    e.preventDefault()
    textInput.value = "클릭하면 이렇게 바뀝니다"
})

/* const textInput = document.getElementById("text")
const button = document.getElementById("button")

button.addEventListener("click",function(){
    console.log(textInput.value)
}) */