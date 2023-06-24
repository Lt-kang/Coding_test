def solution(binomial):
    if "+" in binomial: answer = int(binomial.split("+")[0])+int(binomial.split("+")[1])
    if "-" in binomial: answer = int(binomial.split("-")[0])-int(binomial.split("-")[1])
    if "*" in binomial: answer = int(binomial.split("*")[0])*int(binomial.split("*")[1])
    return answer