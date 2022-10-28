from numpy import empty, ones, zeros
from matplotlib.pyplot import plot, show, axhline, ylim, title, legend, xlabel, ylabel, grid, subplots

N=int(input('Number of ions:'))
k=float(input('k:'))
a=range(N)
u=empty([2,N])
m=1.0772/3

for i in a:
    u[0,N-1-i]=m*N*(1-(2*i)/(N-1))
u[1,:]=zeros(N)

def f(m):
    f=empty(2)
    for n in a:
        if n!=m:
            f[:]+=(u[:,m]-u[:,n])/((u[0,m]-u[0,n])**2+(u[1,m]-u[1,n])**2)**(3/2)
    return u[:,m]-K[:]*f

def df(m):
    df=empty(2)
    for n in a:
        if n!=m:
            df[:]+=(((u[0,m]-u[0,n])**2+(u[1,m]-u[1,n])**2)-3*(u[:,m]-u[:,n])**2)/((u[0,m]-u[0,n])**2+(u[1,m]-u[1,n])**2)**(5/2)
    return ones(2)-K[:]*df

def u_eq(e):
    delta=ones(2)
    while abs(delta[0])>e:
        for m in range(N):
            delta=f(m)/df(m)
            u[:,m]-=delta
    return u
d=1
k1=0
while k1<=k:
    K=[1,k1]
    u_eq(1e-6)
    k1+=k/100

for i in a:
    for j in range(2):
        u[j,i]=float("{0:.5f}".format(u[j,i]))



print(u)
print(2*max(u[0,:])/(N-1))

%matplotlib qt
fig, ax = subplots()
ax.plot(u[0,:],u[1,:],'ro',label='equilibrium positions')#,linestyle='dashed', marker='s')
ax.axhline(0,label='trap axis')
ylim(-1,1)
grid()
#title('Equilibrium positions for N= ions and k_x=')
xlabel('z/l')
ylabel('x/l')
ax.set_aspect(1)
legend(loc=1)
ax.legend()
show()
