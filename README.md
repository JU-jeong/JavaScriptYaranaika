211130

//주석
/*window.console = console 둘 다 사용가능
자바스크립트에서는 대소문자 구분 철저히
browser객체
window.console*/ 

211203
각가의 이벤트들은 이벤트 핸들러를 가질 수 있다. 이벤트 핸들러란 이벤트가 발생되면 실행될 코드 블록을 뜻하며, 주로 함수가 이 역할을 담당한다. 이벤트 핸들러 역할을 수행할 함수를 저의하는 것을 이벤트 핸들러 등록이라 한다.

event handler register

const handleClick = function(){
	window.alert("환영합니다^^")
}
const button = document.query

타겟.on이벤트명 = 이벤트핸들러함수
button.onclick = handleClick

button.onclick = handleClick
button.onclick = handleClick()

-------------------------------------------------------

createElement 지정된 이름의 HTML 요소를 만들어 반환한다

argument를 지정

append 해주어야 한다

appendChild 메소드는 DOM 내 개별 요소 노드라고도 함에 자식요소를 추가할때 씀

target.appendChild(자식으로_추가할_요소)

const p = document.createElement("p")
documnet.body.appendChild(p)

const newDiv = document.div.appendChild()

사용자가 입력한 값을 읽어들일 때는 요소의 value 속성에 접근하면 된다.

value에 접근함으로써 입력 값 읽기 또는 쓰기를 수행할 수 있다

form에 포함된 입력 요소의 name을 통해 각 입력 요소에 접근할 수 있다

form이벤트가 제출되는 submit 이벤트가 발생하면 action 속성의 url로 리다이렉트 되지만, 이벤트 객체를 통해 기본 기능을 차단할 수 있다.
