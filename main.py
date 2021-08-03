import itertools

dnastring = ["accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtctgtgcggcattccac",
       "gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctggaggggtcgtgcgcta",
       "atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaaggctactgtgtagatccgta"
        ,"ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg"
             ]



t = 4
n = 78
l = 8



def score(dnastring, s):
    diffArr = ['a', 'c', 'g', 't']
    arr = find_matrix(dnastring, s)

    valueMatrix = initailize_value_matrix(diffArr)

    for i in range(len(diffArr)):
        for j in range(l):
            for k in range(t):
                if diffArr[i].lower() == arr[k][j].lower():
                    valueMatrix[i][j] += 1

    scoreSum = find_sum(valueMatrix)

    return scoreSum


def find_sum(valueMatrix):
    scoreSum = 0
    for i in range(l):
        maxValue = 0
        for j in range(len(valueMatrix)):
            if valueMatrix[j][i] > maxValue:
                maxValue = valueMatrix[j][i]
        scoreSum += maxValue
    return scoreSum


def initailize_value_matrix(diffArr):
    valueMatrix = []
    for i1 in range(len(diffArr)):

        temp = []
        for j1 in range(l):
            temp.append(0)
        valueMatrix.append(temp)
    return valueMatrix


def find_matrix(dnastring, s):
    arr = []
    k = 0
    for d in dnastring:
        tempArr = []
        for w in d[s[k]:s[k] + l]:
            tempArr.append(w)

        k += 1
        arr.append(tempArr)
    return arr


def brute_force(dnastring, t, n, l):

    data = itertools.product(range(n - l+1), repeat=t)

    bestScore = 0
    bestMotif = []
    for s in data:

        sco = score(dnastring, s)
        if sco > bestScore:
            bestMotif = s
            bestScore = sco

    print("Best Score: ", bestScore)
    print("Best Motif: ", bestMotif)

    return bestMotif


brute_force(dnastring, t, n, l)
