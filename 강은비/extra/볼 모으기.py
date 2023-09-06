import sys

n = int(sys.stdin.readline())
ball = sys.stdin.readline().rstrip()
answer = []
answer.append(min(ball.count("R"), ball.count("B")))
answer.append(ball.rstrip(ball[-1]).count(ball[-1]))
answer.append(ball.lstrip(ball[0]).count(ball[0]))
print(min(answer))
