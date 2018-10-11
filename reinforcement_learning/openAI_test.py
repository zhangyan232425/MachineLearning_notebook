import gym
import matplotlib.pyplot as plt
from matplotlib import animation
def plot_env(env):
	plot.figure()
	img = env.render(mode='rgb_array')
	plt.imshow(img)
	plt.show()
env = gym.make('MsPacman-v0')
frames = []
n_max_steps = 10
n_change_steps = 10
obs = env.reset()
a= 0
for step in range(n_max_steps):
	img = env.render('rgb_array')
	frames.append(img)
	if step % n_change_steps ==0:
		action = env.action_space.sample()
	obs,reward,done,info = env.step(action)
	print(action)
	if done:
		break
def update_scene(num,frames,patch): #num: the index of each fig, patch:
	patch.set_data(frames[num])
	return patch,
def plot_animation(frames,repeat=False,interval=40):
	plt.close()
	fig = plt.figure()
	patch = plt.imshow(frames[0])
	return animation.FuncAnimation(fig,update_scene,fargs=(frames,patch),frames=len(frames),repeat=repeat,interval=interval)
video = plot_animation(frames)
plt.show()