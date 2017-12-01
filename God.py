import Environment as env
import Visualizer as vis
import Model as mod
import Physics as phy

def main():
	world = env.World()
	world.addRoom('room1')
	print('Main exited.')

if __name__ == "__main__": main()

