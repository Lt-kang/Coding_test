





#test case 입력
t = int(input())

#test case 만큼 반복
for i in range(t):
    #k층, n호 입력
    k = int(input())
    n = int(input())
    #0층 호수 방 인원을 리스트로 형성
    people = [i for i in range(1, n+1)]

    #k층이므로 k층만큼 반복
    for x in range(k):
        #n호실은 k-1층 1~n호수 까지 인원의 합이기 때문에 반복문 사용
        for y in range(1, n):
            #자신의 호수 + 자신 이전의 호수 = 자신의 층 +1의 호수
            people[y] += people[y-1]
    print(people[-1])


    
