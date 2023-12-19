formula = input()

flag = False

if formula[0] == '-':
    flag = True

is_minus = '-' in formula  # 일단 마이너스가 나오면 다 빼줘야 함
formula = formula.split('-')


if flag:  # 첫 번째 숫자가 음수
    formula = formula[1:]
    formula[0] = '-'+formula[0]

answer = 0
for i in range(len(formula)):
    if i == 0:
        answer += sum(map(int, formula[i].split('+')))
        continue
    if is_minus:
        answer -= sum(map(int, formula[i].split('+')))

print(answer)
