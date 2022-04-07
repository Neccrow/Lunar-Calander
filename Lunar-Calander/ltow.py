import sys
import io
import ltowmd
import ltowmd2
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
q = input('서력에서 천간력을 입력하시려면 "w", 천간력에서 서력으로 입력하시려면 "e" 를 입력하시오!\n')
if q == 'w':
    wy = int(input('서력 년도를 입력하세요.\n'))
    ltowmd.wl(wy)
elif q == 'e':
    gj = input('천간력을 입력하세요!(한자!)\n')
    sty = int(input('기준 년도를 입력하세요!\n'))
    ltowmd2.gw(gj,sty)
else:
    print('잘못된 입력값 입니다!\n')
print("")
print("")
print("")
print("")
print("")


print("엔터키를 눌러서 종료하십시요...")
input()
