const pet = ["강아지","고양이"]
console.log(...pet)
console.log(pet)

const animal = ["호랑이","코끼리","코뿔소","다람쥐"]
const animalPlus = [...animal, "살쾡이", "원숭이"]

function printNames(param1, param2, param3){
    console.log(param1, param2, param3)
}
printNames(...animal)

const person = {
    name: "유노",
    job: "이것저것",
    eat: function(){
        console.log("밥을 먹습니다 냠냠")
    }
}

const teacher = {
    ...person,
    teach: function(boolean){
        console.log("가르칩니다")
    }
}

console.log(teacher.teach(true))
console.log(teacher.teach(true))