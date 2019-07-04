def incorrect(a,b) :
    correct = a - b
    last = correct % 10
    if last == 0 :
        return correct+1
    return correct-1

a,b = input().split()

print(incorrect(int(a),int(b)))
