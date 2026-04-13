def plotlhs(infile,markersize=1,color='purple',ymax=2,figsize=[22,6],c=1.0):
    with open(infile) as fp:
        S=fp.readlines()
        S=[r.strip().split(",") for r in S]
        S=[r for r in S if float(r[0]) <= c]
    return scatter_plot(S,markersize=markersize,facecolor=color,edgecolor=color,ymin=-ymax,ymax=ymax,figsize=figsize)

def plotrhs(infile,markersize=1,color='green',ymax=2,figsize=[22,6],c=1.0):
    with open(infile) as fp:
        S=fp.readlines()
        S=[r.strip().split(",") for r in S]
        S=[r for r in S if float(r[0]) <= c]
    return line2d(S,markersize=markersize,color=color,xmin=0,xmax=c,ymin=-ymax,ymax=ymax,figsize=figsize)

def plot(lhs,rhs,outfile,title,markersize=1,ymax=2,figsize=[22,6],fontsize=12):
    X = plotlhs(lhs,markersize=markersize,ymax=ymax,figsize=figsize)
    Y = plotrhs(rhs,markersize=markersize,ymax=ymax,figsize=figsize)
    (X+Y).save(outfile,title=title,fontsize=fontsize)

def paperplots():
    plot("LHS_-1_28b.txt","RHS_-1_1e5_1e5.txt","fig1.png",title="",fontsize=16,ymax=5)
    plot("LHS_1_28b.txt","RHS_1_1e5_1e5.txt","fig2.png",title="",fontsize=16,ymax=2)
    plot("LHSp_-1_40b.txt","RHSp_-1_1e5_1e5.txt","fig3.png",title="",fontsize=16,ymax=4)
    plot("LHSpc_-1_30b.txt","RHSpc_-1_1e5_1e5.txt","fig4.png",title="",fontsize=16,ymax=3)
    plot("LHS_1b_28b.txt","RHS_1b_1e5_1e5.txt","fig5_2.png",title="P=2",fontsize=16,ymax=5)
    plot("LHS_2b_28b.txt","RHS_2b_1e5_1e5.txt","fig5_4.png",title="P=4",fontsize=16,ymax=5)
    plot("LHS_3b_28b.txt","RHS_3b_1e5_1e5.txt","fig5_8.png",title="P=8",fontsize=16,ymax=5)
    plot("LHS_4b_28b.txt","RHS_4b_1e5_1e5.txt","fig5_16.png",title="P=16",fontsize=16,ymax=5)

def webplots(delay=100):
    cnts = {16:5042,17:9014,18:15936,19:28138,20:50886,21:89570,22:159988,23:286254,24:508826,25:906302,26:1615826,27:2873164,28:5122428}
    pcnts = {30:4544,31:7909,32:13500,33:22867,34:39004,35:66799,36:114039,37:195027,38:334454,39:573010,40:987442}
    pccnts = {20:9628,21:16312,22:27561,23:46911,24:79371,25:135021,26:230107,27:392814,28:672341,29:1152499,30:1979932}
    for n in range(min(cnts),max(cnts)+1):
        plot("LHS_-1_%sb.txt"%(n),"RHS_-1_1e5_1e5.txt","fig1_%sb.png"%(n),title="Figure 1: X=2^%s, #{E: H(E)<=X}=%s"%(n,cnts[n]),ymax=5)
        print("fig1_%sb.png"%(n))
    sts = os.system('convert -delay %s -loop 1 '%(delay) + ' '.join(["fig1_%sb.png"%(n) for n in range(min(cnts),max(cnts)+1)]) + " fig1.gif")
    print("fig1.gif")
    for P in range(9):
        plot("LHS_%sb_28b.txt"%(P),"RHS_-1_1e5_1e5.txt","thm1_%sb_28b.png"%(P),title="Theorem 1: P=2^%s, X=2^28, #{E: H(E)<=X}=%s"%(P,cnts[28]),ymax=5)
        print("thm1_%sb_28b.png"%(P))
    sts = os.system('convert -delay %s -loop 1 '%(delay) + ' '.join(["thm1_%sb_28b.png"%(P) for P in range(9)]) + " thm1.gif")
    print("thm1.gif")
    for n in range(min(cnts),max(cnts)+1):
        plot("LHS_1_%sb.txt"%(n),"RHS_1_1e5_1e5.txt","fig2_%sb.png"%(n),title="Figure 2: X=2^%s, #{E: H(E)<=X}=%s"%(n,cnts[n]),ymax=2)
        print("fig2_%sb.png"%(n))
    sts = os.system('convert -delay %s -loop 1 '%(delay) + ' '.join(["fig2_%sb.png"%(n) for n in range(min(cnts),max(cnts)+1)]) + " fig2.gif")
    print("fig2.gif")
    for n in range(min(pcnts),max(pcnts)+1):
        plot("LHSp_-1_%sb.txt"%(n),"RHSp_-1_1e5_1e5.txt","fig3_%sb.png"%(n),title="Figure 3: X=2^%s, #{E: H(E)<=X, N(E) prime}=%s"%(n,pcnts[n]),ymax=4)
        print("fig3_%sb.png"%(n))
    sts = os.system('convert -delay %s -loop 1 '%(delay) + ' '.join(["fig3_%sb.png"%(n) for n in range(min(pcnts),max(pcnts)+1)]) + " fig3.gif")
    print("fig3.gif")
    for n in range(min(pccnts),max(pccnts)+1):
        plot("LHSpc_-1_%sb.txt"%(n),"RHSpc_-1_1e5_1e5.txt","fig4_%sb.png"%(n),title="Figure 4: X=2^%s, #{E: N(E)<=X, N(E) prime}=%s"%(n,pccnts[n]),ymax=3)
        print("fig4_%sb.png"%(n))
    sts = os.system('convert -delay %s -loop 1 '%(delay) + ' '.join(["fig4_%sb.png"%(n) for n in range(min(pccnts),max(pccnts)+1)]) + " fig4.gif")
    print("fig4.gif")
    for m in range(1,9):
        for n in range(min(cnts),max(cnts)+1):
            plot("LHS_%sb_%sb.txt"%(m,n),"RHS_%sb_1e5_1e5.txt"%(m),"fig5_%sb_%sb.png"%(m,n),title="Figure 5: P=%s, X=2^%s, #{E: H(E)<=X}=%s"%(2**m,n,cnts[n]),ymax=5)
            print("fig5_%sb_%sb.png"%(m,n))
        sts = os.system('convert -delay %s -loop 1 '%(delay) + ' '.join(["fig5_%sb_%sb.png"%(m,n) for n in range(min(cnts),max(cnts)+1)]) + " fig5_%sb.gif"%(m))
        print("fig5_%sb.gif"%(m))
    n=max(cnts)
    plot("LHS_1_%sb.txt"%(n),"RHS_1_1e5_1e5.txt","fig5_1_%sb.png"%(n),title="Figure 5: P=1, X=2^%s, #{E: H(E)<=X}=%s"%(n,cnts[n]),ymax=5)
    print("fig5_1_%sb.png"%(n))
    plot("LHS_-1_%sb.txt"%(n),"RHS_-1_1e5_1e5.txt","fig5_-1_%sb.png"%(n),title="Figure 5: P=oo, X=2^%s, #{E: H(E)<=X}=%s"%(n,cnts[n]),ymax=5)
    print("fig5_-1_%sb.png"%(n))
    sts = os.system('convert -delay %s -loop 1 '%(delay) +  'fig5_1_28b.png ' + ' '.join(["fig5_%sb_28b.png"%(m) for m in range(1,9)]) + ' fig5_-1_28b.png' + ' fig5.gif')
    print("fig5.gif")
