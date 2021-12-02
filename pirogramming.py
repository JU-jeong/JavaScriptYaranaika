#Skeleton Code

import string
import random

class Player:
    def __init__(self, name, hp, damage, correct_alp):
        self.name = name      # 이름
        self.hp = hp          # 생명력
        self.damage = damage  # 데미지
        self.correct_alp = 0  # 알파벳 맞춘 횟수


class Game:

    def __init__(self):
        self.player = []  # 캐릭터의 목록. start_game()에서 생성
        self.user_character_array = []  # 사용자가 선택한 캐릭터
        self.remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
        self.cur_string = ["_"] * 10  # 현재까지의 글자상태를 저장
        self.answer_string = []  # 랜덤 10글자 단어

    def start_game(self):
        """
        - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
        - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
        - 랜덤 알파벳 10글자로 이루어진 answer_string 을 생성합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

		self.player.append(Player("김건웅", 50, 20, 0))
        self.player.append(Player("김현주", 70, 25, 0))
        self.player.append(Player("박진혁", 80, 30, 0))
        self.player.append(Player("유송경", 90, 35, 0))

        # TODO (1): 사용자의 캐릭터 선택하여 user_character에 저장해주세요.
        
        #이름 담기
        for i in range 3{
        self.user_character_array.append(self.player[i].name)
        }

        # TODO (2) : 랜덤 알파벳 10글자로 이루어진 단어 만들어 answer_string에 저장해주세요.
        
        #밑줄(숨겨진 단어)배열 생성
        answer_unrevealed = []
        
        #밑줄 담기
        for i in range(0,10):
        answer_unrevealed.append("_ ")
        
        #중복없는 알파벳 10자생성
        for i in range(0,10):
        answer_string[] += str(random.choice(string.ascii_letters))
        
        #한 자씩 맞추는 과정을 위해 List 생성후 한글자씩 담음
        lst_answer_string = []

        #대문자로 통일
        for i in answer_string.upper():
            lst_answer_string.append(i)

    def sort_data(self, i):      
  
				""" 
        - [ 게임 진행 ] 부분에서 게임진행 순서를 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
                """
        # TODO : ROUND 1 일 땐 이름순/ ROUDN 2,3 일 땐 HP 순 게임진행을 위한 data 를 재정렬해주세요.
        
        #람다식 사용 1라운드면 이름, 그 외 라운드(2,3)일때는 HP순으로 정렬
        for i in range(1, 4){
            if i == 1
                player(key=lambda d : d[player.name])
            else{
                player(key=lambda e : e[player.HP])    
            }
        }
        
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.

    def play_game(self):
                """ 
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
                 """

        print(
            f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        for i in range(3):

            if self.player[i] == self.user_character:
                print("***** 내 캐릭터 *****")
            else:
                print(f"***** {i+1} 캐릭터 *****")

            print(f"이름: {self.player[i].name} (HP: {self.player[i].name})")

            # TODO (1) : 랜덤의 알파벳 한글자를 선택하게 해주세요. 
						# 단 앞에 나왔던 알파벳과 중복되면 안됩니다.
      
            #input으로 입력후 생성한 answer_put 배열의 모든값과 비교해 중복값 이외의 값 출력
            answer_put = []
            
            while(true){
             answer = input()
                for i in range(len.answer_put){
                    if answer == answer_put[i]{
                    print("다시 선택해주십시오")
                    }
                    answer_put.append(answer)
                    break;
                    
                

            # TODO (2) : 선택된 알파벳이 맞았을 시에, 현재까지 맞춘 단어의 상태를 출력해주세요.
            #  print("***** 맞았습니다 ᵔεᵔ  *****")
            # TODO (3) : 선택된 알파벳이 틀렸을 시에, 생명력을 데미지 만큼 감소시켜주고 이를 출력해주세요.
            #  print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
            
            # 두 리스트 (입력값, 답) 비교해서 중복값을 기본값으로 하는 변수 생성
            # 그 값이 1개 이상이면 해당 위치를 얻어 빈칸  answer_unrevealed 배열의 같은 위치의 값을 _에서 해당 중복값으로 변경 
            # 이후 출력+맞춘단어갯수 1개 추가,  값이 없으면 체력 깎고 오답문 출력다시 입력
           
           ZungBok.upper()= [i for i, j in zip(lst_answer_string, answer_put) if i == j]
          
            if(len(ZungBok.upper())<=1){
                ZungBok = answer_unrevealed[lst_answer_string.index(ZungBok.upper())]
                print("선택알파벳:" + ZungBok.upper())
                print("***** 맞았습니다 ᵔεᵔ  *****")
                player.correct_alp += 1
            }else{
                self.player[i].HP -= self.player[i].damage
                 print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                 print(self.player[i].name + "님은 틀렸기 때문에 HP가" + self.player[i].HP + " 남았습니다.")
            }
        }

           

    def game_result(self):
        """
        - [ 게임 종료 후 ] 부분을 담당하는 함수 입니다.
        - 게임의 결과를 생명력순, 알파벳 맞춘 횟수 순 두가지의 경우로 출력해야 합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        print("\n\n******************* 게임이 끝났습니다 *******************")

        # TODO (1) : 생명력 순으로 결과값을 출력해주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        
        #람다식으로 남은 HP순으로 정렬 이후 출력
        
        player(key=lambda e : e[player.HP])
        f for i in range(4):
            if(player.HP[i] > 0){   
                print(i+1 + "등: " + player.name[i] +" (HP: " + player.HP[i] + ")")
            }print(i+1 + "등: " + player.name[i] +" (사망)")
        
        
        # TODO (2) : 알파벳 맞춘 횟수 순으로 결과값을 출력해주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        
        #람다식으로 맞춘갯수순으로 정렬 이후 출력
        
        player(key=lambda f : f[player.correct_alp])
         f for i in range(4):
             print(i+1 + "등: " + player.name[i] + " " + player.correct_alp[i] + "회")
            
        

    def game(self):
        """
        - 게임 운영을 위한 함수입니다. 
        - 별도의 코드 작성이 필요 없습니다. 
        """

        self.start_game()

#---------------------------------출력부-----------------------------------------------


        print("******************* 게임 시작 *******************\n")

        for i in range(1, 4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")

            self.sort_data(i) 
            self.play_game()

            print("===========================")
            print(f"     ROUND {i} - END")
            print("===========================")

        self.game_result()


if __name__ == '__main__':

    """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
    game = Game()
    game.game()