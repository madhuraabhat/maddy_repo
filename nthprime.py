maddy_repo
==========
#!/usr/bin/python

def nthprime() :
        n=1
        i=3
        while n!=10001 :
                j=2
                while j<i :
                        if i%j==0 :
                                break;
                        else :
                                j+=1
                        if i==j :
                                n+=1
                i+=1
        print i-1


nthprime()
