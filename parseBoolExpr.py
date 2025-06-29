def parseBoolExpr(exp):
    n=len(exp)
    st=[]
    i=n-1
    while i>=0:
        if exp[i]=="(":
            op=exp[i-1]
            print(st,i,op)
            if op=="|": 
                eva=False
                while st[-1]!=")":
                    eva|=st[-1]
                    print(eva)
                    st.pop()
                st.pop()
                st.append(eva)
            elif op=="&":
                eva=True
                while st[-1]!=")":
                    eva&=st[-1]
                    st.pop()
                st.pop()
                st.append(eva)
            elif op=="!":
                eva=not st[-1]
                st.pop()
                st.pop()
                st.append(eva)
            i-=2
        else:
            if exp[i]=="f":
                st.append(False)
            elif exp[i]=="t":
                st.append(True)
            elif exp[i]==")":
                st.append(")")
            i-=1
    return st[-1]
print(parseBoolExpr("!(&(f,t))"))
            
                
