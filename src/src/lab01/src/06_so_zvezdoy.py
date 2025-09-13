import sys
sys.stdout.reconfigure(encoding='utf-8')

N = int(input())
in_person = 0
remote = 0
for _ in range(N):
    line = input().strip()
    parts = line.split()
    format_participation = parts[3].lower() == 'true'
    if format_participation:
        in_person += 1
    else:
        remote += 1
print(f"{in_person} {remote}")
