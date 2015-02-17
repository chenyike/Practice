def main():
    f = open("movies.txt")
    x=f.read()
    print len(x)
    x=f.read()
    print len(x)

    fout = open("movie.txt", "w")
    lst = f.readlines()
    lst.reverse()
    fout.writelines(lst)
    fout.close()     #fout reverse the list

    f.close()


    # r+ read and write
    f3 = open("movies.txt",'r+')
    lst = f3.readlines()
    lst.reverse()
    f3.writelines(lst)
    f3.close()

    
main()
