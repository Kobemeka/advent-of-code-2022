with open("./1.txt") as f:
    print(max(list(map(lambda x: eval(x.replace("\n","+")), f.read().split("\n\n")))))