import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
import pygame.rect
import random
import time

pygame.init() #파이게임 초기화

BG = (255, 255, 200)
size = [900,600]
screen = pygame.display.set_mode(size)
#게임판의 높이,폭 색 지정

pygame.display.set_caption("쿠킹학생~")
#게임타이틀 지정

clock = pygame.time.Clock()
#fps설정을 위한 클락 생성


pygame.mixer.music.load( "HOW ARE YOU.mp3" )#배경음악 무한반복
pygame.mixer.music.play(-1)
print("배경음악 출처: 배경음악: HOW ARE YOU, 김재영, 공유마당, CC BY (https://gongu.copyright.or.kr/gongu/wrt/wrt/view.do?wrtSn=13073758&menuNo=200020)")

#메인화면
def main():
    while True:
        screen.fill(BG)#배경색채우기
        clock.tick(60) #fps 설정 
        
        #이미지요소들 불러오기
        student = pygame.image.load("image/student.png")
        desk = pygame.image.load("image/desk.png")
        btn_dal = pygame.image.load("image/btn_dal.png")
        btn_toast = pygame.image.load("image/btn_toast.png")
        
        

    
        #이미지요소 배치
        screen.blit(student,(105,65))
        screen.blit(desk,(45,300))

        btnT_Position = btn_toast.get_rect(topleft=(500,120))
        screen.blit(btn_toast, btnT_Position) #토스트 버튼 배치
        
        btnD_Position = btn_dal.get_rect(topleft=(500,300))
        screen.blit(btn_dal, btnD_Position) #달고나 버튼 배치
        
        pygame.display.update() #이미지요소들 배치한 것 업데이트.
        
            
            
        
        
        #버튼 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if btnT_Position.collidepoint(mouse):
                    print("프렌치토스트를 만들어봅시다~")
                    play_toast()

                elif btnD_Position.collidepoint(mouse):
                    print("달고나커피를 만들어 봅시다~")
                    play_dal()




#메인에서 토스트 버튼을 누를 시 실행될 함수
def play_toast():
    while True:
        #말풍선+게임설명용 함수 생성.
        def bubble_s(script,x):
            screen.blit(bubble,(50,50))
            font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
            text = font.render(script, True, (20,30,80))
            screen.blit(text,(x,85))
        def explain(script,x):
            font = pygame.font.Font("NanumBarunGothicBold.ttf", 15)
            text = font.render(script, True, (120,120,150))
            screen.blit(text,(x,127))

        screen.fill(BG) #배경초기화.

        #학생아이콘과 말풍선이미지 불러오기
        student_i = pygame.image.load("image/student_icon.png")
        bubble = pygame.image.load("image/bubble.png")
        screen.blit(student_i,(700,25))
    
        bubble_s("이번엔 프렌치 토스트를 만들어 볼 거예요!",150)
        explain("클릭 시 다음 대사로 넘어갑니다.", 250)
        pygame.display.update()
        
        #스테이지1
        def stage1():
            while True:
                bubble_s("우선 계란을 그릇에 담아볼까요?", 200)
                explain("정답을 클릭할 시 계란이 그릇에 담겨요!", 230)
                question_bg = pygame.image.load("image/question_bg.png")
                
                
            
                    
                #1스테이지의 문제용 함수~ 인수자리에 몇번문제인지 들어가도록  
                def stage1_question(question_num):

                    egg = pygame.image.load("image/egg1.png")
                    egg_bg= pygame.image.load("image/egg_bg.png")
                    egg_bg = pygame.transform.scale(egg_bg, (109, 118))

                    x = random.randrange(1,100)
                    y = random.randrange(1,100) #문제에 쓰일 x,y 값 설정.
                    a1= random.randrange(2,200) 
                    a2= random.randrange(2,200)
                    a3= random.randrange(2,200)
                    a4= random.randrange(2,200) #정답이 아닌 이외 보기들에서 쓰일 값 랜덤으로 불러오기
                    correct = random.randrange(1,4) #정답 번호를 몇번으로 할지 정하자~(범위1~4)
                    
                    if int(question_num)==1: #1번문제일 경우 아무것도안담긴 그릇 불러온다
                        bowl= pygame.image.load("image/bowl.png")
                        screen.blit(bowl,(500,310))
                        pygame.display.update()

                    if int(question_num)==2: #2번문제일 경우 계란1개담긴그릇 불러온다
                        bowl= pygame.image.load("image/bowl_egg1.png")
                        screen.blit(bowl,(500,310))
                        pygame.display.update()

                    if int(question_num)==3: #3번 문제일 경우 계란2개담긴그릇불러온다
                        bowl= pygame.image.load("image/bowl_egg2.png")
                        screen.blit(bowl,(500,310))
                        pygame.display.update()

                    while True: 
                        screen.blit(question_bg,(70,200)) 
                        screen.blit(egg_bg,(620,170))
                        screen.blit(egg,(620,170)) #질문용배경이미지, 계란이미지 불러온다
                        question = str(x)+"+"+str(y) #질문 생성.
                        q_answer = x+y #질문의 답 생성.
                        font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
                        question_a = font.render("문제 %s."%question_num, True, (70,70,100)) 
                        question_b = font.render("%s의 답은?!"%question , True, (120,120,150)) 
                        screen.blit(question_a,(130,230))
                        screen.blit(question_b,(230,230)) #질문텍스트
                        if correct==1: #정답의 번호가 1번일 경우 1번자리에 들어갈 내용, 아닐 경우 들어갈 내용 정해준다
                            answer1 = font.render("(1) %d" %q_answer, True, (100,100,100))
                            answer_Xpos = [210,310]
                            answer_Ypos = [320,345]
                        elif correct != 1:
                            answer1 = font.render("(1) %d" %a1, True, (100,100,100))
                        if correct==2: #정답의 번호가 2번일 경우 2번자리에 들어갈 내용, 아닐 경우 들어갈 내용 정해준다
                            answer2 = font.render("(2) %d" %q_answer, True, (100,100,100))
                            answer_Xpos = [210,310]
                            answer_Ypos = [370,395]
                        elif correct != 2:
                            answer2 = font.render("(2) %d" %a2, True, (100,100,100))
                        if correct==3:  #정답의 번호가 3번일 경우 3번자리에 들어갈 내용, 아닐 경우 들어갈 내용 정해준다
                            answer3 = font.render("(3) %d" %q_answer, True, (100,100,100))
                            answer_Xpos = [210,310]
                            answer_Ypos = [420,445]
                        elif correct != 3:
                            answer3 = font.render("(3) %d" %a3, True, (100,100,100))
                        if correct==4: #정답의 번호가 4번일 경우 4번자리에 들어갈 내용, 아닐 경우 들어갈 내용 정해준다
                            answer4 = font.render("(4) %d" %q_answer, True, (100,100,100))
                            answer_Xpos = [210,310]
                            answer_Ypos = [470,495]
                        elif correct != 4:
                            answer4 = font.render("(4) %d" %a4, True, (100,100,100))
                        
                        screen.blit(answer1,(210,320))
                        screen.blit(answer2,(210,370)) 
                        screen.blit(answer3,(210,420)) 
                        screen.blit(answer4,(210,470)) #정답텍스트들 위치 지정해서 불러오기

                        pygame.display.update()

                        for event in pygame.event.get(): #클릭이벤트시 일어날 내용들.
                            if event.type == pygame.QUIT:
                                quit()
                            
                            if event.type == pygame.MOUSEBUTTONUP: #마우스 버튼이 눌렸다 떨어질시 이미지가 잠시 변경되었다가 다음 문제로 넘어간다
                                mouse = pygame.mouse.get_pos()
                                if mouse[0] in range (answer_Xpos[0],answer_Xpos[1]):
                                    if mouse[1] in range (answer_Ypos[0],answer_Ypos[1]):
                                        n=int(question_num)+1
                                        while True:
                                            screen.blit(egg_bg,(620,170))
                                            egg = pygame.image.load("image/egg2.png")
                                            screen.blit(egg,(620,170))
                                            pygame.display.update()
                                            time.sleep(0.3)
                                            break 
                                        if n>=4: #만약 3번째 문제였다면 다음문제로 넘어가지 않고 1스테이지를 마무리한다
                                            stage1_end()
                                        stage1_question("%d"%n)
                #1스테이지를 마무리하는 내용.
                def stage1_end():
                    while True:
                        screen.fill(BG)

                        bubble_s("계란을 그릇에 성공적으로 담았네요~!", 200)
                        explain("화면을 클릭할 시 다음 스테이지로 넘어갑니다.", 230)
                        bowl= pygame.image.load("image/bowl_egg3.png")
                        screen.blit(bowl,(260,280))
                        screen.blit(student_i,(700,25))
                        pygame.display.update()

                        for event in pygame.event.get(): #클릭이벤트시 2스테이지로 넘어간다.
                            if event.type == pygame.QUIT:
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                stage2()
                             
                
                stage1_question("1")

        def stage2():
            while True:
                screen.fill(BG)
                clock.tick(30)
                bubble_s("그럼 이제 계란을 섞어봅시다~!", 180)
                explain("클릭 시 다음 대사로 넘어갑니다.", 250)
                

                bowl = pygame.image.load("image/bowl_egg3.png")
                spoon = pygame.image.load("image/spoon.png")
                
                screen.blit(bowl,(260,280))
                screen.blit(spoon,(320,230))
                screen.blit(student_i,(700,25))
                pygame.display.update()
                
                remainNum = 30 #스페이스연타해야하는횟수
                def clear(): #스테이지 클리어시 나올 내용.
                    screen.fill(BG)
                    screen.blit(student_i,(700,25))
                    screen.blit(bowl,(260,280))
                    screen.blit(spoon,(320,230))
                    bubble_s("우와~ 성공이네요!", 240)
                    explain("클릭 시 다음 스테이지로 넘어갑니다.", 250)
                    pygame.display.update()
                    
                   
    
                for event in pygame.event.get(): #클릭 시 이벤트
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        while True:
                    
                            def basic(): #연타시 기본으로 떠있을 내용
                                screen.fill(BG)
                                screen.blit(student_i,(700,25))
                                screen.blit(bowl,(260,280))
                                screen.blit(spoon,(320,230))
                                bubble_s("열심히 휘저어주세요!", 240)
                                explain("스페이스바를 30회 연타해주세요!", 230)
                                remain_num()
                                pygame.display.update()

                            def remain_num(): #남은 횟수를 띄워주는 창
                                number = pygame.image.load("image/number.png")
                                screen.blit(number,(680,270))
                                
                                font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
                                text = font.render(str(remainNum), True, (20,30,80))
                                screen.blit(text,(755,335))   
                                pygame.display.update()
                
                
                                

                            basic()
                            remain_num()
                        
                            if remainNum<=15: #남은횟수가 15이하일때 이미지를 변경해준다
                                bowl = pygame.image.load("image/eggBowl1.png")
                                screen.blit(bowl,(260,280))
                                screen.blit(spoon,(320,230))
                                
                            for event in pygame.event.get(): #스페이스 눌렀을 시의 이벤트. (도구이미지변경, 남은횟수차감)
                                if event.type == pygame.QUIT:
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        while True:
                                            screen.blit(bowl,(260,280))
                                            w_spoon= pygame.image.load("image/w_spoon.png")
                                            screen.blit(w_spoon,(325,225))
                                            
                                            pygame.display.update()
                                            time.sleep(0.1)
                                            break
                                        
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_SPACE:
                                        remainNum-=1
                                        print(remainNum)
                                        remain_num()
                                        basic()
                                        
                            if remainNum<=0: #남은 횟수가 0회일 때의 이벤트.
                                while True:
                                    clear()
                                    bowl = pygame.image.load("image/eggBowl2.png")
                                    screen.blit(bowl,(260,280))
                                    screen.blit(spoon,(320,230))
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            stage3()    

        def stage3():
            screen.fill(BG)
            tray = pygame.image.load("image/tray.png")
            bread = pygame.image.load("image/bread_egg.png")
            left = pygame.image.load("image/key_left.png")
            right = pygame.image.load("image/key_right.png")
            up = pygame.image.load("image/key_up.png")
            down = pygame.image.load("image/key_down.png")
            dip_bg = pygame.image.load("image/egg_bg.png")
            dip_bg = pygame.transform.scale(dip_bg, (197, 236)) #이미지 요소들 불러오기

            bubble_s("그럼 이제 빵을 계란에 적셔보아요!", 200)
            explain("화면에 뜨는 방향키를 따라누르면 빵이 계란에 적셔집니다!", 200)
            screen.blit(student_i,(700,25))
            screen.blit(tray,(530,350))
            def key_input(input_num): #키보드누르는 이벤트함수
                if input_num>=4: #방향키성공횟수4번넘을 경우 다음 함수 실행
                    stage3_end()
                list_random= random.randrange(0,3) #랜덤으로 방향정할 수 있도록 랜덤함수사용
                if list_random==0: #각 숫자별로 방향 정해주고 해당 이미지 불러오도록설정
                    print("왼쪽!")
                    screen.blit(left,(80,230))
                elif list_random==1:
                    print("오른쪽!")
                    screen.blit(right,(80,230))
                elif list_random==2:
                    print("위!")
                    screen.blit(up,(80,230))
                elif list_random==3:
                    print("아래!")
                    screen.blit(down,(80,230))

                if input_num==1: #횟수별로 빵 이미지 추가되도록 설정한다.
                    screen.blit(bread,(640,370))
                    pygame.display.update()
                elif input_num==2:
                    screen.blit(bread,(730,390))
                    pygame.display.update()
                elif input_num==3:
                    screen.blit(bread,(580,435))
                    pygame.display.update()
                elif input_num==4:
                    screen.blit(bread,(670,460))
                    pygame.display.update()

                while True: #키보드이벤트설정용 while문
                    dip = pygame.image.load("image/dip1.png")
                    screen.blit(dip_bg,(380,170))
                    screen.blit(dip,(380,170))
                    pygame.display.update()

                   

                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT: #종료이벤트시 종료.
                            quit()
                        if event.type == pygame.KEYDOWN: 
                            if list_random==0:
                                if event.key == pygame.K_LEFT: #왼쪽키 눌렀을시 이미지잠시 변경, 키보드누른횟수 +1
                                    dip = pygame.image.load("image/dip2.png")
                                    screen.blit(dip_bg,(380,170))
                                    screen.blit(dip,(380,170))
                                    pygame.display.update()
                                    time.sleep(0.3)
                                    n= input_num+1
                                    key_input(n)
                            elif list_random==1:
                                if event.key == pygame.K_RIGHT: #오른쪽키눌렀을시
                                    dip = pygame.image.load("image/dip2.png")
                                    screen.blit(dip_bg,(380,170))
                                    screen.blit(dip,(380,170))
                                    pygame.display.update()
                                    time.sleep(0.3)
                                    n= input_num+1
                                    key_input(n)
                            elif list_random==2: #윗키눌렀을시
                                if event.key == pygame.K_UP:
                                    dip = pygame.image.load("image/dip2.png")
                                    screen.blit(dip_bg,(380,170))
                                    screen.blit(dip,(380,170))
                                    pygame.display.update()
                                    time.sleep(0.3)
                                    n= input_num+1
                                    key_input(n)
                            elif list_random==3:
                                if event.key == pygame.K_DOWN: #아래키눌렀을시
                                    dip = pygame.image.load("image/dip2.png")
                                    screen.blit(dip_bg,(380,170))
                                    screen.blit(dip,(380,170))
                                    pygame.display.update()
                                    time.sleep(0.3)
                                    n= input_num+1
                                    key_input(n)
            #키보드누르는 이벤트 이후 나올 내용.
            def stage3_end():
                while True:
                    screen.fill(BG)
                    screen.blit(student_i,(700,25))
                    bubble_s("우와 대단해요!! 너무 잘하시는데요?!", 170)
                    explain("화면을 클릭할 시 다음 스테이지로 넘어갑니다.", 200)
                    screen.blit(tray,(530,350))
                    screen.blit(bread,(640,370))
                    screen.blit(bread,(730,390))
                    screen.blit(bread,(580,435))
                    screen.blit(bread,(670,460))
                    pygame.display.update()
                    for event in pygame.event.get(): #클릭이벤트시 4스테이지로 넘어간다.
                        if event.type == pygame.QUIT:
                            quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            stage4()


            key_input(0) 
        
        def stage4():
            while True:
                for i in range(3): #이미지가 0.5초에 한번씩 위치가 이동되도록한다.(흔들리는것처럼보이게)(3번반복)
                    student = pygame.image.load("image/student.png")
                    desk = pygame.image.load("image/desk.png")
                    effect = pygame.image.load("image/effect.png")
                    fire = pygame.image.load("image/fire.png")
                    skillet = pygame.image.load("image/skillet.png")
                    screen.fill(BG)
                    screen.blit(student,(320,80))
                    screen.blit(desk,(260,320))
                    screen.blit(skillet,(380,300))
                    screen.blit(fire,(425,330))
                    screen.blit(effect,(100,100))
                    pygame.display.update()

                    time.sleep(0.5)
                    screen.fill(BG)
                    screen.blit(student,(320,85))
                    screen.blit(desk,(260,320))
                    screen.blit(skillet,(382,300))
                    screen.blit(fire,(423,332))
                    screen.blit(effect,(650,160))
                    pygame.display.update()
                    time.sleep(0.5)
                    for event in pygame.event.get(): 
                            if event.type == pygame.QUIT:
                                quit()
                final_stage()  #3번반복이끝나면 마지막스테이지로넘어간다.
        
        def final_stage(): 
            finish = pygame.image.load("image/toast.png")
            shine = pygame.image.load("image/shine.png")
            while True:
                screen.fill(BG)
                screen.blit(student_i,(700,25))
                screen.blit(finish,(250,250))
                screen.blit(shine,(100,210))
                screen.blit(shine,(700,400))
                bubble_s("우와~ 맛있는 프렌치 토스트가 완성됐어요~!", 110)
                explain("화면을 누르면 메인화면으로 돌아갑니다.", 230)
                pygame.display.update() 
                for event in pygame.event.get(): #클릭이벤트
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        main()
                
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                while True:
                    stage1()

#메인에서 달고나커피 버튼을 누를 시 실행될 함수
def play_dal():
    while True:
        screen.fill(BG) #배경채우기
        clock.tick(60)
        student_i = pygame.image.load("image/student_icon.png") #스크립트용이미지 불러요기
        bubble = pygame.image.load("image/bubble.png")
        screen.blit(student_i,(700,25))

        #말풍선+게임설명용 함수 생성.
        def bubble_s(script,x):
            screen.blit(bubble,(50,50))
            font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
            text = font.render(script, True, (20,30,80))
            screen.blit(text,(x,85))

        def explain(script,x):
            font = pygame.font.Font("NanumBarunGothicBold.ttf", 15)
            text = font.render(script, True, (120,120,150))
            screen.blit(text,(x,127))
        
        
        #1스테이지 함수
        def stage1(): 
            bubble_s("우선 재료를 그릇에 담아볼까요?", 200)
            explain("방향키를 눌러 재료를 그릇위치로 이동시켜주세요!", 225)
            bowl = pygame.image.load("image/bowl.png")
            coffee = pygame.image.load("image/coffee.png")
            sugar = pygame.image.load("image/sugar.png")
            water = pygame.image.load("image/water.png") #필요한 이미지들 불러오기

            bowl_position = bowl.get_rect(topleft=(170,200)) #bowl 위치

            def move_coffee():
                bowl = pygame.image.load("image/bowl.png") 
                screen.blit(bowl,bowl_position) #bowl 배치
                coffee_position = coffee.get_rect(topleft=(600,250)) #coffee 위치
                screen.blit(coffee,coffee_position) #coffee 배치
                pygame.display.update()

                coffee_toX = 0 #coffee그림이 이동할 좌표 초기화.
                coffee_toY = 0
                
                while True: #키보드 누를 시 coffee가 어디로 몇만큼 이동할지 정해준다
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: #종료이벤트시 종료.
                            quit()
                        if event.type == pygame.KEYDOWN: 
                            if event.key == pygame.K_LEFT:
                                coffee_toX -= 5
                            elif event.key == pygame.K_RIGHT:
                                coffee_toX += 5
                            elif event.key == pygame.K_UP:
                                coffee_toY -= 5
                            elif event.key == pygame.K_DOWN:
                                coffee_toY += 5
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                coffee_toX = 0
                            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                coffee_toY = 0
                
                    screen.fill(BG)  #이동 전의 이미지를 지우기 위해 배경을 다시 채워준다
                    bubble_s("우선 재료를 그릇에 담아볼까요?", 200)
                    explain("방향키를 눌러 재료를 그릇위치로 이동시켜주세요!", 225)
                    screen.blit(bowl, bowl_position)
                    screen.blit(student_i,(700,25)) #그 외 요소 다시 불러준다

                    screen.blit(coffee,coffee_position) 
                    pygame.display.update()
                    coffee_position[0] += coffee_toX
                    coffee_position[1] += coffee_toY #이동한 만큼 위치 더해준다.
                    
                    #coffee가 화면밖으로 나가지 않도록 경계값을 정해준다.
                    if coffee_position[0] < 0:
                        coffee_position[0] = 0
                    elif coffee_position[0] > 900 - 110:
                        coffee_position[0] = 900 - 110
                    if coffee_position[1] < 0 :
                        coffee_position[1]= 0
                    elif coffee_position[1] > 600 - 118:
                        coffee_position[1] = 600 - 118
                    pygame.display.update() 

                    if coffee_position[0] in range (270,418): 
                        if coffee_position[1] in range (250,414): #coffee가 지정한 위치에(bowl위치) 도착했을 시 아래 내용실행.
                            while True:
                                bowl = pygame.image.load("image/filledBowl_1.png")
                                screen.fill(BG)
                                bubble_s("잘했어요!", 300)
                                explain("클릭 시 다음으로 넘어갑니다.", 250)
                                screen.blit(student_i,(700,25))
                                screen.blit(bowl,bowl_position)
                                pygame.display.update()

                                for event in pygame.event.get(): 
                                    if event.type == pygame.QUIT:
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONDOWN: #클릭 이벤트 시 아래내용 실행
                                        move_sugar()

            def move_sugar():
                bowl = pygame.image.load("image/filledBowl_1.png")
                screen.blit(bowl,bowl_position) #그릇이미지 불러오기
                sugar_position = sugar.get_rect(topleft=(600,225))
                #screen.blit(coffee,coffee_position)
                pygame.display.update()

                sugar_toX = 0 #sugar가 이동할 좌표 초기화.
                sugar_toY = 0
                
                while True: #키보드 누를 시 sugar가 어디로 몇만큼 이동할지 정해준다
                    for event in pygame.event.get(): 
                        if event.type == pygame.QUIT:
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                sugar_toX -= 5
                            elif event.key == pygame.K_RIGHT:
                                sugar_toX += 5
                            elif event.key == pygame.K_UP:
                                sugar_toY -= 5
                            elif event.key == pygame.K_DOWN:
                                sugar_toY += 5
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                sugar_toX = 0
                            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                sugar_toY = 0
                 
                    screen.fill(BG) #이동 전의 이미지를 지우기 위해 배경을 다시 채워준다
                    bubble_s("다음 재료도 그릇에 담아볼까요?", 200)
                    explain("방향키를 눌러 재료를 그릇위치로 이동시켜주세요!", 225)
                    screen.blit(bowl, bowl_position)
                    screen.blit(student_i,(700,25)) #그 외 요소 다시 불러준다

                    screen.blit(sugar,sugar_position)
                    pygame.display.update()
                    sugar_position[0] += sugar_toX
                    sugar_position[1] += sugar_toY #이동한 만큼 위치 더해준다.
                    
                    #sugar가 화면밖으로 나가지 않도록 경계값을 정해준다.
                    if sugar_position[0] < 0:
                        sugar_position[0] = 0
                    elif sugar_position[0] > 900 - 110:
                        sugar_position[0] = 900 - 110
                    if sugar_position[1] < 0 :
                        sugar_position[1]= 0
                    elif sugar_position[1] > 600 - 118:
                        sugar_position[1] = 600 - 118
                    pygame.display.update() 

                    if sugar_position[0] in range (270,418):
                        if sugar_position[1] in range (200,464):
                            while True:
                                bowl = pygame.image.load("image/filledBowl_2.png")
                                screen.fill(BG)
                                bubble_s("잘했어요!", 300)
                                explain("클릭 시 다음으로 넘어갑니다.", 250)
                                screen.blit(student_i,(700,25))
                                screen.blit(bowl,bowl_position)
                                pygame.display.update()

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        move_water()
                            
            def move_water():
                bowl = pygame.image.load("image/filledBowl_2.png")
                screen.blit(bowl,bowl_position)  #bowl 배치
                water_position = water.get_rect(topleft=(600,225))
                screen.blit(water, water_position)  #water 배치
                pygame.display.update()

                water_toX = 0  #water가 이동할 좌표 초기화.
                water_toY = 0
                
                while True:
                    for event in pygame.event.get(): #키보드 누를 시 water가 어디로 몇만큼 이동할지 정해준다
                        if event.type == pygame.QUIT:
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                water_toX -= 5
                            elif event.key == pygame.K_RIGHT:
                                water_toX += 5
                            elif event.key == pygame.K_UP:
                                water_toY -= 5
                            elif event.key == pygame.K_DOWN:
                                water_toY += 5
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                water_toX = 0
                            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                water_toY = 0
                
                    screen.fill(BG) #이동 전의 이미지를 지우기 위해 배경을 다시 채워준다
                    bubble_s("마지막 재료도 그릇에 담아볼까요?", 200)
                    explain("방향키를 눌러 재료를 그릇위치로 이동시켜주세요!", 225)
                    screen.blit(bowl, bowl_position)
                    screen.blit(student_i,(700,25)) #그 외 요소 다시 불러준다

                    screen.blit(water,water_position)
                    pygame.display.update()
                    water_position[0] += water_toX
                    water_position[1] += water_toY #이동한 만큼 위치 더해준다.
                    
                    #water가 화면밖으로 나가지 않도록 경계값을 정해준다.
                    if water_position[0] < 0:
                        water_position[0] = 0
                    elif water_position[0] > 900 - 110:
                        water_position[0] = 900 - 110
                    if water_position[1] < 0 :
                        water_position[1]= 0
                    elif water_position[1] > 600 - 118:
                        water_position[1] = 600 - 118
                    pygame.display.update() 

                    if water_position[0] in range (270,418):
                        if water_position[1] in range (200,464): #water가 지정한 위치에(bowl위치) 도착했을 시 아래 내용실행.
                            while True:
                                bowl = pygame.image.load("image/filledBowl.png")
                                screen.fill(BG)
                                bubble_s("우와 성공했네요~!! 대단해요!", 200)
                                explain("클릭 시 다음 화면으로 넘어갑니다.", 250)
                                screen.blit(student_i,(700,25))
                                screen.blit(bowl,bowl_position)
                                pygame.display.update()

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONDOWN: #클릭시 stage2()로 넘어간다.
                                        stage2() 
                            
            move_coffee() #move_coffee() 부터 실행!
            


        def stage2():
            while True:
                screen.fill(BG) #배경 다시 채워서 화면 비우기
                screen.blit(student_i,(700,25))
                bubble_s("재료를 섞을 도구를 선택해봅시다~", 200)
                explain("도구를 마우스로 클릭하세요~!", 250)
                
                spoon = pygame.image.load("image/spoon.png")
                whisk = pygame.image.load("image/whisk.png")
                electricwhisk = pygame.image.load("image/electricwhisk.png") #사용할 이미지 불러오기
                
                spoon_pos = spoon.get_rect(topleft=(70,220))
                screen.blit(spoon, spoon_pos)

                whisk_pos = whisk.get_rect(topleft=(300,220))
                screen.blit(whisk, whisk_pos)

                electricwhisk_pos = electricwhisk.get_rect(topleft=(567,220))
                screen.blit(electricwhisk, electricwhisk_pos)
                
                pygame.display.update()

                for event in pygame.event.get(): #버튼이벤트
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()

                        if spoon_pos.collidepoint(mouse):
                            print("도구로 숟가락을 선택했군요!")
                            stage3_a()

                        elif whisk_pos.collidepoint(mouse):
                            print("도구로 거품기를 선택했군요!")
                            stage3_b()
                            
                        elif electricwhisk_pos.collidepoint(mouse):
                            print("도구로 전동거품기를 선택했군요!")
                            stage3_c()

        def stage3_a():
            while True:
                screen.fill(BG)
                clock.tick(30)
                bubble_s("도구로 숟가락을 선택하셨군요...?", 180)
                explain("클릭 시 다음 대사로 넘어갑니다.", 250)

                filledBowl = pygame.image.load("image/filledBowl.png")
                spoon = pygame.image.load("image/spoon.png")
                
                screen.blit(filledBowl,(260,280))
                screen.blit(spoon,(320,230))
                
                screen.blit(student_i,(700,25))

                pygame.display.update()
                
                remainNum = 80 #스페이스연타해야하는횟수
                def clear(): #스테이지 클리어시 나올 내용.
                    screen.fill(BG)
                    screen.blit(student_i,(700,25))
                    screen.blit(filledBowl,(260,280))
                    screen.blit(spoon,(320,230))
                    bubble_s("우와~ 성공이네요!", 260)
                    explain("클릭 시 다음 스테이지로 넘어갑니다.", 250)
                    pygame.display.update()
                    
                   
    
                for event in pygame.event.get(): #클릭 시 이벤트
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        while True:
                    
                            def basic(): #연타시 기본으로 떠있을 내용
                                screen.fill(BG)
                                screen.blit(student_i,(700,25))
                                screen.blit(filledBowl,(260,280))
                                screen.blit(spoon,(320,230))
                                bubble_s("..그럼 재료를 섞어봅시다! 열심히 휘저어주세요!", 110)
                                explain("스페이스바를 80회 연타해주세요! 화이팅!", 230)
                                remain_num()
                                pygame.display.update()

                            def remain_num(): #남은 횟수를 띄워주는 창
                                number = pygame.image.load("image/number.png")
                                screen.blit(number,(680,270))
                                
                                font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
                                text = font.render(str(remainNum), True, (20,30,80))
                                screen.blit(text,(755,335))   
                                pygame.display.update()
                
                
                                

                            basic()
                            remain_num()
                        
                            if remainNum<=60: #남은횟수가 60이하일때 이미지를 변경해준다
                                filledBowl = pygame.image.load("image/bowl_init.png")
                                screen.blit(filledBowl,(260,280))
                                screen.blit(spoon,(320,230))
                                
                            if remainNum<=20: #남은횟수가 20이하일때 이미지를 변경해준다
                                filledBowl = pygame.image.load("image/bowl_mid.png")
                                screen.blit(filledBowl,(260,280))
                                screen.blit(spoon,(320,230))



                            for event in pygame.event.get(): #스페이스 눌렀을 시의 이벤트. (도구이미지변경, 남은횟수차감)
                                if event.type == pygame.QUIT:
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        while True:
                                            screen.blit(filledBowl,(260,280))
                                            w_spoon= pygame.image.load("image/w_spoon.png")
                                            screen.blit(w_spoon,(325,225))
                                            
                                            pygame.display.update()
                                            time.sleep(0.1)
                                            break
                                        
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_SPACE:
                                        remainNum-=1
                                        print(remainNum)
                                        remain_num()
                                        basic()
                                        
                            if remainNum<=0: #남은 횟수가 0회일 때의 이벤트.
                                while True:
                                    clear()
                                    filledBowl = pygame.image.load("image/bowl_final.png")
                                    screen.blit(filledBowl,(260,280))
                                    screen.blit(spoon,(320,230))
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            stage4()
                             
        def stage3_b():
            while True:
                screen.fill(BG)
                clock.tick(30)
                bubble_s("도구로 거품기를 선택하셨군요?", 180)
                explain("클릭 시 다음 대사로 넘어갑니다.", 250)

                filledBowl = pygame.image.load("image/filledBowl.png")
                whisk = pygame.image.load("image/whisk.png")
                
                screen.blit(filledBowl,(260,280))
                screen.blit(whisk,(320,200))
                
                screen.blit(student_i,(700,25))

                pygame.display.update()
                
                remainNum = 40
                def clear(): #스테이지 클리어시 나올 내용.
                    screen.fill(BG)
                    screen.blit(student_i,(700,25))
                    screen.blit(filledBowl,(260,280))
                    screen.blit(whisk,(320,200))
                    bubble_s("우와~ 성공이네요!", 260)
                    explain("클릭 시 다음 스테이지로 넘어갑니다.", 250)
                    pygame.display.update()
                    
                   
    
                for event in pygame.event.get(): #클릭시 아래내용실행
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        while True:
                    
                            def basic(): #연타시 기본으로 떠있을 내용
                                screen.fill(BG)
                                screen.blit(student_i,(700,25))
                                screen.blit(filledBowl,(260,280))
                                screen.blit(whisk,(320,200))
                                bubble_s("그럼 재료를 섞어봅시다, 열심히 휘저어주세요!", 110)
                                explain("스페이스바를 40회 연타해주세요!", 230)
                                remain_num()
                                pygame.display.update()

                            def remain_num(): #남은 횟수를 띄워주는 창
                                number = pygame.image.load("image/number.png")
                                screen.blit(number,(680,270))
                                
                                font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
                                text = font.render(str(remainNum), True, (20,30,80))
                                screen.blit(text,(755,335))   
                                pygame.display.update()
                

                            basic()
                            remain_num()
                        
                            if remainNum<=30:  #남은횟수가 30이하일때 이미지를 변경해준다
                                filledBowl = pygame.image.load("image/bowl_init.png")
                                screen.blit(filledBowl,(260,280))
                                screen.blit(whisk,(320,200))
                                
                            if remainNum<=10:  #남은횟수가 10이하일때 이미지를 변경해준다
                                filledBowl = pygame.image.load("image/bowl_mid.png")
                                screen.blit(filledBowl,(260,280))
                                screen.blit(whisk,(320,200))



                            for event in pygame.event.get(): #스페이스 눌렀을 시의 이벤트. (도구이미지변경, 남은횟수차감)
                                if event.type == pygame.QUIT:
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        while True:
                                            screen.blit(filledBowl,(260,280))
                                            w_whisk= pygame.image.load("image/w_whisk.png")
                                            screen.blit(w_whisk,(325,205))
                                            pygame.display.update()
                                            time.sleep(0.1)
                                            break
                                        
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_SPACE:
                                        remainNum-=1
                                        print(remainNum)
                                        remain_num()
                                        basic()
                                        
                            if remainNum<=0: #남은 횟수가 0회일 때의 이벤트.
                                while True:
                                    clear()
                                    filledBowl = pygame.image.load("image/bowl_final.png")
                                    screen.blit(filledBowl,(260,280))
                                    screen.blit(whisk,(320,200))
                                    pygame.display.update()
                                    
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            stage4()
  
        def stage3_c():
            while True:
                screen.fill(BG)
                clock.tick(30)
                bubble_s("도구로 전동거품기를 선택하셨군요?!!", 180)
                explain("클릭 시 다음 대사로 넘어갑니다.", 250)

                filledBowl = pygame.image.load("image/filledBowl.png")
                electricwhisk = pygame.image.load("image/electricwhisk.png")
                
                screen.blit(filledBowl,(260,280))
                screen.blit(electricwhisk,(320,200))
                
                screen.blit(student_i,(700,25))

                pygame.display.update()
                
                remainNum = 20 #스페이스연타해야하는횟수
                def clear(): #스테이지 클리어시 나올 내용.
                    screen.fill(BG)
                    screen.blit(student_i,(700,25))
                    screen.blit(filledBowl,(260,280))
                    screen.blit(electricwhisk,(320,200))
                    bubble_s("우와~ 성공이네요!", 260)
                    explain("클릭 시 다음 스테이지로 넘어갑니다.", 250)
                    pygame.display.update()
                    
                   
    
                for event in pygame.event.get(): #클릭시 이벤트
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        while True:
                     
                            def basic(): #연타시 기본으로 떠있을 내용
                                screen.fill(BG)
                                screen.blit(student_i,(700,25))
                                screen.blit(filledBowl,(260,280))
                                screen.blit(electricwhisk,(320,200))
                                bubble_s("그럼 재료를 섞어봅시다~! 열심히 휘저어주세요!", 110)
                                explain("스페이스바를 20회 연타해주세요!", 230)
                                remain_num()
                                pygame.display.update()

                            def remain_num(): #남은 횟수를 띄워주는 창
                                number = pygame.image.load("image/number.png")
                                screen.blit(number,(680,270))
                                
                                font = pygame.font.Font("NanumBarunGothicBold.ttf", 25)
                                text = font.render(str(remainNum), True, (20,30,80))
                                screen.blit(text,(755,335))   
                                pygame.display.update()
                
                
                                

                            basic()
                            remain_num()
                        
                            if remainNum<=10: #남은횟수가 10이하일때 이미지를 변경해준다
                                filledBowl = pygame.image.load("image/bowl_init.png")
                                screen.blit(filledBowl,(260,280))
                                screen.blit(electricwhisk,(320,200))
                                
                            if remainNum<=5: #남은횟수가 5이하일때 이미지를 변경해준다
                                filledBowl = pygame.image.load("image/bowl_mid.png")
                                screen.blit(filledBowl,(260,280))
                                screen.blit(electricwhisk,(320,200))



                            for event in pygame.event.get(): #스페이스 눌렀을 시의 이벤트. (도구이미지변경, 남은횟수차감)
                                if event.type == pygame.QUIT:
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        while True:
                                            screen.blit(filledBowl,(260,280))
                                            w_electricwhisk= pygame.image.load("image/w_electricwhisk.png")
                                            screen.blit(w_electricwhisk,(325,205))
                                            pygame.display.update()
                                            time.sleep(0.1)
                                            break
                                        
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_SPACE:
                                        remainNum-=1
                                        print(remainNum)
                                        remain_num()
                                        basic()
                                        
                            if remainNum<=0: #남은 횟수가 0회일 때의 이벤트.
                                while True:
                                    clear()
                                    filledBowl = pygame.image.load("image/bowl_final.png")
                                    screen.blit(filledBowl,(260,280))
                                    screen.blit(electricwhisk,(320,200))
                                    pygame.display.update()
                                    
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            stage4()

        def stage4():
            while True:
                screen.fill(BG)
                bubble_s("그럼 이제 커피를 완성시켜 볼까요?", 190)
                explain("클릭 시 다음 대사로 넘어갑니다.", 250)
                screen.blit(student_i,(700,25))
                pygame.display.update()

                glass = pygame.image.load("image/glass_empty.png")
                milk = pygame.image.load("image/milk.png")
                dal = pygame.image.load("image/bowl_final.png")
                straw = pygame.image.load("image/straw.png") #필요 이미지 불러오기
                glass_position = glass.get_rect(topleft=(230,150))
                dal = pygame.transform.scale(dal, (232, 176))

                def move_milk():
                    glass = pygame.image.load("image/glass_empty.png")
                    screen.blit(glass,glass_position) #컵이미지 불러오기
                    milk_position = milk.get_rect(topleft=(600,280))
                    screen.blit(milk,milk_position) 
                    pygame.display.update()

                    toX = 0
                    toY = 0 #그림이 이동할 좌표 초기화.
                    
                    while True: #키보드 누를 시 이미지가 어디로 몇만큼 이동할지 정해준다
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    toX -= 5
                                elif event.key == pygame.K_RIGHT:
                                    toX += 5
                                elif event.key == pygame.K_UP:
                                    toY -= 5
                                elif event.key == pygame.K_DOWN:
                                    toY += 5
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    toX = 0
                                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    toY = 0
                    
                        screen.fill(BG) #이동 전의 이미지를 지우기 위해 배경을 다시 채워준다
                        bubble_s("우유를 컵에 부어줍시다~", 200)
                        explain("방향키를 눌러 우유를 컵 위치로 이동시켜주세요!", 225)
                        screen.blit(glass, glass_position)
                        screen.blit(student_i,(700,25)) #그 외 요소 다시 불러준다

                        screen.blit(milk,milk_position)
                        pygame.display.update()
                        milk_position[0] += toX
                        milk_position[1] += toY #이동한 만큼 위치 더해준다.
                        
                        #이미지가 화면밖으로 나가지 않도록 경계값을 정해준다.
                        if milk_position[0] < 0:
                            milk_position[0] = 0
                        elif milk_position[0] > 900 - 110:
                            milk_position[0] = 900 - 110
                        if milk_position[1] < 0 :
                            milk_position[1]= 0
                        elif milk_position[1] > 600 - 118:
                            milk_position[1] = 600 - 118
                        pygame.display.update() 

                        #이미지가 지정한 위치에 도착했을 시 아래 내용실행.
                        if milk_position[0] in range (230,387):
                            if milk_position[1] in range (150,530):
                                while True:
                                    glass = pygame.image.load("image/glass_milk.png")
                                    screen.fill(BG)
                                    bubble_s("잘했어요!", 300)
                                    explain("클릭 시 다음으로 넘어갑니다.", 250)
                                    screen.blit(student_i,(700,25))
                                    screen.blit(glass,glass_position)
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            move_dal()
                def move_dal():
                    glass = pygame.image.load("image/glass_milk.png")
                    screen.blit(glass,glass_position) #컵이미지 불러오기
                    dal_position = dal.get_rect(topleft=(600,280))
                    screen.blit(dal,dal_position)
                    pygame.display.update()

                    toX = 0
                    toY = 0 #그림이 이동할 좌표 초기화.
                    
                    while True: #키보드 누를 시 이미지가 어디로 몇만큼 이동할지 정해준다
                        for event in pygame.event.get(): 
                            if event.type == pygame.QUIT:
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    toX -= 5
                                elif event.key == pygame.K_RIGHT:
                                    toX += 5
                                elif event.key == pygame.K_UP:
                                    toY -= 5
                                elif event.key == pygame.K_DOWN:
                                    toY += 5
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    toX = 0
                                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    toY = 0
                    
                        screen.fill(BG)  #이동 전의 이미지를 지우기 위해 배경을 다시 채워준다
                        bubble_s("달고나를 컵에 부어줍시다~", 200)
                        explain("방향키를 눌러 달고나를 컵 위치로 이동시켜주세요!", 225)
                        screen.blit(glass, glass_position) 
                        screen.blit(student_i,(700,25)) #그 외 요소 다시 불러준다

                        screen.blit(dal,dal_position)
                        pygame.display.update()
                        dal_position[0] += toX
                        dal_position[1] += toY  #이동한 만큼 위치 더해준다.
                        
                        #이미지가 화면밖으로 나가지 않도록 경계값을 정해준다.
                        if dal_position[0] < 0:
                            dal_position[0] = 0
                        elif dal_position[0] > 900 - 232:
                            dal_position[0] = 900 - 232
                        if dal_position[1] < 0 :
                            dal_position[1]= 0
                        elif dal_position[1] > 600 - 176:
                            dal_position[1] = 600 - 176
                        pygame.display.update() 

                        #이미지가 지정한 위치에 도착했을 시 아래 내용실행.
                        if dal_position[0] in range (230,387):
                            if dal_position[1] in range (150,530):
                                while True:
                                    glass = pygame.image.load("image/glass_dal.png")
                                    screen.fill(BG)
                                    bubble_s("잘했어요!", 300)
                                    explain("클릭 시 다음으로 넘어갑니다.", 250)
                                    screen.blit(student_i,(700,25))
                                    screen.blit(glass,glass_position)
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            move_straw()
                def move_straw():
                    glass = pygame.image.load("image/glass_dal.png")
                    screen.blit(glass,glass_position) #컵이미지 불러오기
                    straw_position = straw.get_rect(topleft=(600,280))
                    screen.blit(straw,straw_position)
                    pygame.display.update()

                    toX = 0
                    toY = 0 #그림이 이동할 좌표 초기화.
                    
                    while True: #키보드 누를 시 이미지가 어디로 몇만큼 이동할지 정해준다
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    toX -= 5
                                elif event.key == pygame.K_RIGHT:
                                    toX += 5
                                elif event.key == pygame.K_UP:
                                    toY -= 5
                                elif event.key == pygame.K_DOWN:
                                    toY += 5
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    toX = 0
                                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                    toY = 0
                    
                        screen.fill(BG) #이동 전의 이미지를 지우기 위해 배경을 다시 채워준다
                        bubble_s("빨대를 컵에 꽂아줍시다~", 200)
                        explain("방향키를 눌러 빨대를 컵 위치로 이동시켜주세요!", 205)
                        screen.blit(glass, glass_position)
                        screen.blit(student_i,(700,25))  #그 외 요소 다시 불러준다

                        screen.blit(straw,straw_position)
                        pygame.display.update()
                        straw_position[0] += toX
                        straw_position[1] += toY #이동한 만큼 위치 더해준다.
                        #이미지가 화면밖으로 나가지 않도록 경계값을 정해준다.
                        if straw_position[0] < 0:
                            straw_position[0] = 0
                        elif straw_position[0] > 900 - 99:
                            straw_position[0] = 900 - 99
                        if straw_position[1] < 0 :
                            straw_position[1]= 0
                        elif straw_position[1] > 600 - 231:
                            straw_position[1] = 600 - 231
                        pygame.display.update() 

                        #이미지가 지정한 위치에 도착했을 시 아래 내용실행.
                        if straw_position[0] in range (230,387):
                            if straw_position[1] in range (150,530):
                                while True:
                                    glass = pygame.image.load("image/glass_straw.png")
                                    screen.fill(BG)
                                    bubble_s("우와 대단해요~!", 250)
                                    explain("클릭 시 다음으로 넘어갑니다.", 250)
                                    screen.blit(student_i,(700,25))
                                    screen.blit(glass,glass_position)
                                    pygame.display.update()

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            quit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            final_stage()

                for event in pygame.event.get(): #클릭시 이벤트
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        move_milk()
        def final_stage(): 
            finish = pygame.image.load("image/glass_straw.png")
            shine = pygame.image.load("image/shine.png")
            while True:
                screen.fill(BG)
                screen.blit(student_i,(700,25))
                screen.blit(finish,(370,170))
                screen.blit(shine,(100,210))
                screen.blit(shine,(700,400))
                bubble_s("우와~ 맛있는 달고나커피가 완성됐어요~!", 110)
                explain("화면을 누르면 메인화면으로 돌아갑니다.", 230)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        main()
        
        bubble_s("이번엔 달고나 커피를 만들어 볼 거예요!",150)
        explain("클릭 시 다음 대사로 넘어갑니다.", 250)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                while True:
                    stage1()
                


main()
