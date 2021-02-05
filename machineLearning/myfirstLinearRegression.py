import matplotlib.pyplot as plt
import random as rd

x = [i+rd.uniform(-5, 5) for i in range(5,26)]
y = [i * 2 + rd.uniform(-5, 5) for i in x]

fig = plt.figure(figsize=(9, 7))
plt.subplots_adjust(wspace=0.4, hspace=0.6)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(223)

plt.subplot(2,2,1)
plt.title('Data Scatter')
plt.xlabel('x')
plt.ylabel('y')
ax1.scatter(x, y)
plt.subplot(2,2,3)
plt.title('Cost Function & Defferences')
plt.ylabel('defferences')
plt.xlabel('Variable')


def learn():
    randN = rd.randint(1, 10)
    current_defference = 0
    old_defference = 0
    plusFlug = True
    num = 1
    max_try = 100000
    try_num = 0
    datan = []
    datadefference = []
    while True:
        current_defference = 0
        if try_num > max_try:
            break
        for i, j in enumerate(x):
            current_defference += (y[i] - randN * j) * (y[i] - randN * j)

        if current_defference == 0:
            break
        if old_defference == 0:
            old_defference = current_defference
            continue

        if current_defference > old_defference:
            # 誤差が大きくなっていた場合
            num = num / 2
            if plusFlug:
                plusFlug = False
            else:
                plusFlug = True
        old_defference = current_defference
        datan.append(randN)
        datadefference.append(current_defference)
        if plusFlug:
            randN += num
        else:
            randN -= num
        try_num += 1
    d = {'num': randN ,'n': datan, 'defference': datadefference}
    return d
a = learn()
ax2.plot(a['n'], a['defference'], color=(0,0,1))
text = "X = {}".format(a["num"])
ax2.text(5, 10, text , size=10,
        horizontalalignment="center", verticalalignment="center")
plt.show()
