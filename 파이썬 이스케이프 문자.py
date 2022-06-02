# print()문에서 사용한다.

\n : 줄바꿈
\t : 탭
\\ : 역슬래시() 출력
\" : 따옴표(") 출력. 작은따옴표도 해당된다.
\b : 백스페이스. 바로 앞 문자가 지워진다.
⇒ 한글은 두 개를 써야 한 글자가 삭제되고, macOS와 리눅스 터미널에서만 정상작동된다고 한다. 테스트 해보니 맨 끝문장에 사용하는 경우에 작동을 안한다...

print('두 줄에\n나눠서 출력')
#두 줄에
#나눠서 출력
print('hello world!\nhello world!\bhello world!')
#hello world!
#hello worldhello world!
