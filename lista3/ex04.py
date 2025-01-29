def filtering(names):
    return list(filter(lambda x: len(x) >= 5, names))


names = ["lucas", "fernanda", "ana", "gabriel", "joao"]

fnames = filtering(names)

print(fnames)