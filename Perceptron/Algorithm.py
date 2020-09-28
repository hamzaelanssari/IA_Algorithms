def Perceptron(bais,learning_rate,epoches):
    w0=bais
    w1=0
    w2=0
    x=[2,0,3,1]
    y=[0,3,0,1]
    yt=[1,0,0,1]
    for i in range(epoches):
        j=0
        while j<4:
            new_y=w0+w1*x[j]+w2*y[j]
            if new_y>=0:
                sgn=1
            else:
                sgn=0;
            error=yt[j]-sgn
            if error!=0:
                w0=w0+learning_rate*error
                w1=w1+learning_rate*error*x[j]
                w2=w2+learning_rate*error*y[j]
            print("point(",x[j],",",y[j],") :","y'=",new_y,"sgn=",sgn,"w0=",w0,"w1=",w1,"w2=",w2,"Error=",error)
            j=j+1