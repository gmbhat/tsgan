import os

print("enter command: ")
command = input()

if "-i all" in command:
	command1 = command.replace("-i all", "-i stretch_missing_train.csv")
	command1 = "cmd /k python gain.py " + command1
	print("-------------- running stretch_missing_train.csv --------------")
	os.system(command1)
	print("-------------- done running stretch_missing_train.csv --------------")




	command2 = command.replace("-i all", "-i accel_z_missing_train.csv")
	command2 = "cmd /k python gain.py " + command2
	print("-------------- running accel_z_missing_train --------------")
	os.system(command2)
	print("-------------- done running accel_z_missing_train.csv --------------")





	command3 = command.replace("-i all", "-i accel_y_missing_train.csv")
	command3 = "cmd /k python gain.py " + command3
	print("-------------- running accel_y_missing_train.csv --------------")
	os.system(command3)
	print("-------------- done running accel_y_missing_train.csv --------------")





	command4 = command.replace("-i all", "-i accel_x_missing_train.csv")
	command4 = "cmd /k python gain.py " + command4
	print("-------------- running accel_x_missing_train.csv --------------")
	os.system(command4)
	print("-------------- done running accel_x_missing_train.csv --------------")

else:
	command5 = "cmd /k python gain.py " + command
	os.system(command5)