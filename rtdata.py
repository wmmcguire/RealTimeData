import matplotlib.pyplot as plt 
from time import sleep
import numpy as np

plt.style.use('fivethirtyeight')
fig = plt.figure()
ax1=fig.add_subplot(1,1,1)
plt.title('Sin over Time')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(['Amplitude = 1'])

def main():
	fig.show()
	t = 0
	x, y = [], []


	while True:
		x.append(t)
		y.append(np.sin(np.pi*t))

		ax1.plot(x,y, 'r')

		fig.canvas.draw()

		ax1.set_xlim(left = t-5, right=t+5)

		sleep(0.1)
		t += 0.09
		

if __name__ == '__main__':
	main()