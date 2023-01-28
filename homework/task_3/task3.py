with open("only_name", "r+") as o_name:
    def generation():
        rea = o_name.readlines()
        for i in rea:
            if i[0:4] == 'name':
                yield i[7:]


    run_it = generation()
    for read in run_it:
        print(read)
