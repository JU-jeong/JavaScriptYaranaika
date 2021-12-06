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


211207

/* JSON은 자바스크릭트 객체 표기법(JavaSript Object Notation)
을 뜻하며, 이는 자바스크립트 객체를 문자열로 표현하는
데이터 포맷이다. 자바스크립트에서만 사용할 수 있는 객체 타입을 다른 프로그래밍
언어에서도 사용할 수 있는 형태(문자열)로 변환하기 위해 사용한다. */

stringify 객체 to JSON

parse JSON to 객체 

------------------------------------------------------------------------

XMLHttpRequest 는 서버와 상호작용하기 위해 사용하는 자바스크립트 내장생성자. 서버로부터 데이터를 받아와 전체 페이지의 새로고침 없이도 페이지의 일부만 업데이트 하는것이 가능

XMLHttpRequest 객체를 생성한다

서버와 통신할 때 필요한 정보 및 처리 방법 등을 기입한다

요청을 전송해 통신을 시작한다

ajax - 비동기로 뿌린다

//open 메서드 사용 시 기본 형태

const. request = new XMLHttpRequest()
request.open("HTTP메서드", "서버URL")
request.send()

