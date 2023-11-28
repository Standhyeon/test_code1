print('사전 프로그램 시작... 종료는 q를 입력')
dictionary = {}

while True:
    st = input('$ ')
    command = st[0]
    if command == '<':
        st = st[1:]
        input_str = st.split(':')
        if len(input_str) < 2:
            print('입력 오류가 발생했습니다.')
        else:
            dictionary[input_str[0].strip()] = input_str[1].strip()
            
    elif command == '>':
        st = st[1:]
        input_str = st.strip()
        if input_str in dictionary:
            print(dictionary[input_str])
        else:
            print(f'{input_str}가 사전에 없습니다.')
            
    elif command == 'v':
        if dictionary == {}:
            print('영어 사전에 등록되어 있는 단어가 없습니다.')
        else:
            print('영어 사전에 있는 단어와 뜻을 출력합니다.')
            for i, j in dictionary.items():
                print(f'{i} : {j}')
        
    
    elif command == 'q':
        break
    
    else:
        print('입력 오류가 발생했습니다.')
        
print('사전 프로그램을 종료합니다.')
