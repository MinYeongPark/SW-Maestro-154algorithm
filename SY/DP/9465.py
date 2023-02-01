import sys
input=sys.stdin.readline

for _ in range(int(input())):
	n=int(input())
	sticker=[list(map(int,input().split())) for _ in range(2)]
	dp=[[0]*n for _ in range(2)]
	dp[0][0]=sticker[0][0]
	dp[1][0]=sticker[1][0]

	for i in range(1,n):
		if i==1:
			dp[0][1]=sticker[1][0]+sticker[0][1]
			dp[1][1]=sticker[0][0]+sticker[1][1]
		else:
			dp[0][i]=max(dp[1][i-2],dp[1][i-1])+sticker[0][i]
			dp[1][i]=max(dp[0][i-2],dp[0][i-1])+sticker[1][i]

	print(max(dp[0][-1],dp[1][-1]))
