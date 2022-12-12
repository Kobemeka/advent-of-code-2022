with open("./1.txt") as f:
    print(sum(sorted(list(map(lambda x: eval(x.replace("\n","+")), f.read().split("\n\n"))))[-1:-4:-1]))