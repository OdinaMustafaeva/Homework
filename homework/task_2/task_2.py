with open("subjects.txt", "r+") as txt:
    def generation():
        rea = txt.readlines()
        for i in rea:
            yield i


    run_it = generation()
    for read in run_it:
        print(read)
