const cat = {
    name: " 국회 ",
    town: " 부천 ",
    eat: function() {
        console.log("밥을 먹는다냥")
    },
    scratch: function(){
        console.log("건드리면 할퀸다냥")
    }
}

//속성 참조하기

console.log(cat.town)
cat.scratch()
console.log(cat['name'])
cat['eat']()

const cat = {}
console.log(typeof cat)

const cat = {
    name: "tom",
    color: "gray"
}
console.log(cat.color)
console.log(cat[name])

const cat = {
    name = "tom",
    color = "gray",
    eat : function(){
        console.log("냠냠 맛있다")
    }
}

cat.eat()

console.log(cat.name)
cat['name']="도라에몽"
console.log(cat)