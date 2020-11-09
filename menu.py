import os
import webbrowser


def menu():
	os.system("tput setaf 3")
	print("\t\t1 for date")
	print("\t\t2 for time")
	print("\t\t3 for calendar")
	print("\t\t4 for Hadoop Services")
	print("\t\t5 for AWS Services")
	print("\t\t6 for docker services")
	print("\t\t7 to Check your IP")
	print("\t\t8 to change execution type")
	os.system("tput setaf 7")
def HadoopMenu():
	os.system("tput setaf 10")
	print("\t\t---WELCOME TO HADOOP SERVICES---")
	print("\t\t1.Configure this node as a Master")
	print("\t\t2.Configure this as a Slave")
	print("\t\t3.Configure this as a Client")
	print("\t\t4.Start Namenode")
	print("\t\t5.start Datanode")
	print("\t\t6.Stop Namenode")
	print("\t\t7.stop Datanode")
	print("\t\t8.See all the files")
	print("\t\t9.Create a file in your cluster")
	print("\t\t10.Delete a file in your cluster")
	print("\t\t11.Upload a file to  your cluster")
	print("\t\t12.Read a file in your cluster")
	print("\t\t13.change block size and upload a file to your cluster")
	print("\t\t14.Goto WebUI of your Hadoop Cluster")
	os.system("tput setaf 7")
	
def AWS_EC2Menu() :
	print("1.To launch instance")
	print("2.To describe your instance")
def s3menu():
	print("1.Create a bucket")
	print("2.Upload objects to your bucket")

def AWSMenu():
	os.system("tput setaf 10")
	print("\t\tLogin with your credentials")
	#os.system("aws configure")
	print("\t\t1.EC2")
	print("\t\t2.S3")
	os.system("tput setaf 7")
def DockerMenu():
	os.system("tput setaf 10")
	while True:
		print("\t\t1.See all images available")
		print("\t\t2.see all containers")
		print("\t\t3.Delete an image")
		print("\t\t4.Launch existing Containers")
		print("\t\t5.launch new container")
		print("\t\t6.Download/pull image")
		inp=int(input("enter your choice press 0 to exit "))
		if inp==1:
			os.system("docker images")
		if inp==2:
			os.system("docker ps -a")
		elif inp==3:
			x=input("enter the os image : ")
			os.system("docker -rmi {}".format(x))
		elif inp==4:
			x=input("enter the container name : ")
			os.system("docker start {}".format(x))
			os.system("docker attach {}".format(x))
		elif inp==5:
			x=input("enter the container name : ")
			y=input("osversion : ")
			os.system("docker run -it --name {} {}".format(x,y))
		elif inp==6:
			x=input("enter the container that to be downloaded : ")
			os.system("docker pull {}".format(x))
		elif inp==0:
			os.system("tput setaf 7")
			break
	


def local():
	while True:
				menu()
				choice = input("Enter your choice : ")
				choice = int(choice)
				if choice == 1 :
					os.system("date +%x")
				elif choice == 2:
					os.system("date +%r")
				elif choice == 3 :
					os.system("cal")




				elif choice == 4 :
					HadoopMenu()
					HadoopChoice = input("Enter your choice : ")
					HadoopChoice = int(HadoopChoice)
					if HadoopChoice == 1: 
						print("Configuring this as a master node")
						file = open("/etc/hadoop/core-site.xml", "r")
						lines = file.readlines()
						lines.insert(6, "<property>/n<name>fs.default.name</name>/n<value>hdfs://0.0.0.0:9001</value>/n</property>")
						file = open("/etc/hadoop/core-site.xml", "w")
						file.writelines(lines)
						file.close()
						os.system("mkdir /nn")
						file = open("/etc/hadoop/hdfs-site.xml", "r")
						lines = file.readlines()
						lines.insert(6, "<property>/n<name>dfs.name.dir</name>/n<value>/nn</value>/n</property>")
						file = open("/etc/hadoop/hdfs-site.xml", "w")
						file.writelines(lines)
						file.close()
						print("-------CONFIG DONE------")
					elif HadoopChoice == 2:
						print("Configuring this as a slave node")
						mast_ip = input("Enter master IP :")
						file = open("/etc/hadoop/core-site.xml", "r")
						lines = file.readlines()
						lines.insert(6, "<property>/n<name>fs.default.name</name>/n<value>hdfs://{}:9001</value>/n</property>".format(mast_ip))
						file = open("/etc/hadoop/core-site.xml", "w")
						file.writelines(lines)
						file.close()
						os.system("mkdir /dn")
						file = open("/etc/hadoop/hdfs-site.xml", "r")
						lines = file.readlines()
						lines.insert(6, "<property>/n<name>dfs.name.dir</name>/n<value>/dn</value>/n</property>")
						file = open("/etc/hadoop/hdfs-site.xml", "w")
						file.writelines(lines)
						file.close()
						print("-------CONFIG DONE------")

					elif HadoopChoice == 3:
						print("Configuring this as a client node")
						mast_ip = input("Enter master IP :")
						file = open("/etc/hadoop/core-site.xml", "r")
						lines = file.readlines()
						lines.insert(6, "<property>/n<name>fs.default.name</name>/n<value>hdfs://{}:9001</value>/n</property>".format(mast_ip))
						file = open("/etc/hadoop/core-site.xml", "w")
						file.writelines(lines)
						file.close()
						print("-------CONFIG DONE------")
					elif HadoopChoice == 4:
						print("Starting Namenode")
						os.system("hadoop-daemon.sh start namenode")
						print("Status : ")
						os.system("jps")
					elif HadoopChoice == 5:
						print("Starting Datanode")
						os.system("hadoop-daemon.sh start datanode")
						print("Status : ")
						os.system("jps")
					elif HadoopChoice == 6:
						print("Stopping Namenode")
						os.system("hadoop-daemon.sh stop namenode")
						print("Status : ")
						os.system("jps")
					elif HadoopChoice == 7:
						print("Stopping Datanode")
						os.system("hadoop-daemon.sh stop datanode")
						print("Status : ")
						os.system("jps")
					elif HadoopChoice == 8:
						print("Entered into Filesystem -- contents are : \n")
						os.system("hadoop fs -ls /")
					elif HadoopChoice == 9:
						print("Creating a file in your cluster : ")
						filename = input("Enter filename to create :")
						os.system("hadoop fs -touchx /{}".format(filename))
					elif HadoopChoice == 10:
						print("Deleting a file in your cluster : ") 
						try :
							filename = input("Filename you wish to delete :")
							os.system("hadoop fs -rm /{}".format(filename))
						except :
							print("File Error ! Such file not present !")
					elif HadoopChoice == 11:
						print("Uploading a file in your cluster :")
						filename = input("Enter filename to upload :")
						os.system("hadoop fs -put {} /".format(filename))
					elif HadoopChoice == 12:
						print("Reading a file in your cluster : ")
						filename = input("Enter filename to read :")
						os.system("hadoop fs -cat /{}".format(filename))
					elif HadoopChoice == 13:
						print("Changing block size in your cluster(Please upload a file) : ")
						filename = input("Enter Filename to upload :")
						BZise = int(input("Enter block size in Bytes (default 64MB)"))
						os.system("hadoop fs -Ddfs.block.size={} -put {} /".format(BZise, filename))


					elif HadoopChoice == 14:
						mast_ip = input("Enter master IP : ")
						print("Redirecting you to Hadoop - WebUI : ")
						webbrowser.open("hdfs://{}:50070".format(mast_ip))

					else:
						print("Something wrong I can feel it.")







				elif choice == 5 :
					AWSMenu()
					AWSChoice = input("Enter your choice : ")
					AWSChoice = int(AWSChoice)

					if AWSChoice == 1:
						print("Welcome to EC2 Services in AWS ")
						key_yes_no = str(input("Do you have a keypair ready ? (y/n)"))

						if('n' in key_yes_no or  'no' in key_yes_no or 'N' in key_yes_no or 'NO' in key_yes_no):
							key_create = input("Enter a keypair to create(mandatory to launch an instance)")
							os.system("aws ec2 create-key-pair --key-name {}".format(key_create))

						elif ('y' in key_yes_no or  'yes' in key_yes_no or 'Y' in key_yes_no or 'YES' in key_yes_no):
							AWS_EC2Menu()
							choice = input("Select your option : ")
							choice = int(choice)
							if choice == 1:
								print("---LAUCHING EC2 INSTANCE---")
								image_id = input("Enter image-id : ")
								instance_type = input("Enter instance type :")
								sec_group = input("Enter Security group id : ")
								count= input("How many instance(input number) : ")
								keyname = input("Enter your key-pair name ")
								os.system("aws ec2 run-instances --image-id {} --instance-type {} --security-group-ids {} --count {} --key-name {} ".format(image_id, instance_type, sec_group,count, keyname))
							elif choice ==2 :
								print("---Describing your instances---")
								os.system("aws ec2 describe-instances")
							else:
								exit()


					elif AWSChoice == 2 :
						print("Welcome to S3 Services ")
						s3menu()
						s3choice = int(input("Enter your choice : "))
						if s3choice == 1:
							print("---Creating S3 Bucket---")
							bucket_name = input("Enter your bucket name (UNIQUE) : ")
							region = input("Enter region name :")
							os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocalConstraint={}".format(bucket_name, region, region))

						elif s3choice == 2:
							print("---Uploading objects---")
							file_loc = input("File source : (Better copy & paste your file location)")
							bucket = input("Your bucket name :")
							os.system("aws s3 cp {} s3://{} --acl public-read-write".format(file_loc, bucket))
						else :
							exit()

					else:
						print("Something wrong I can feel it.")	




				elif choice == 6 :
					DockerMenu()
					




				elif choice == 7 :
					try:
						os.system("ifconfig wlo1")
					except:
						os.system("ifconfig enp0s3")




				elif choice == 8:
					remote()




				else :
					exit()
def remote():
	ssh_ip = input("Enter Target IP :")
	while True:
				menu()
				choice = input("Enter your choice : ")
				choice = int(choice)
				if choice == 1 :
					os.system("ssh {}date +%x".format(ssh_ip))
				elif choice == 2:
					os.system("ssh {} date +%r".format(ssh_ip))
				elif choice == 3 :
					os.system("ssh {} cal".format(ssh_ip))




				elif choice == 4 :
					print("Hadoop Services need to be local")




				elif choice == 5 :
					AWSMenu()
					AWSChoice = input("Enter your choice : ")
					AWSChoice = int(AWSChoice)

					if AWSChoice == 1:
						print("Welcome to EC2 Services in AWS ")
						key_yes_no = str(input("Do you have a keypair ready ? (y/n)"))

						if('n' in key_yes_no or  'no' in key_yes_no or 'N' in key_yes_no or 'NO' in key_yes_no):
							key_create = input("Enter a keypair to create(mandatory to launch an instance)")
							os.system("ssh {}aws ec2 create-key-pair --key-name {}".format(ssh_ip,key_create))

						elif ('y' in key_yes_no or  'yes' in key_yes_no or 'Y' in key_yes_no or 'YES' in key_yes_no):
							AWS_EC2Menu()
							choice = input("Select your option : ")
							choice = int(choice)
							if choice == 1:
								print("---LAUCHING EC2 INSTANCE---")
								image_id = input("Enter image-id : ")
								instance_type = input("Enter instance type :")
								sec_group = input("Enter Security group id : ")
								count= input("How many instance(input number) : ")
								keyname = input("Enter your key-pair name ")
								os.system("ssh {}aws ec2 run-instances --image-id {} --instance-type {} --security-group-ids {} --count {} --key-name {} ".format(ssh_ip,image_id, instance_type, sec_group,count, keyname))
							elif choice ==2 :
								print("---Describing your instances---")
								os.system("ssh {} aws ec2 describe-instances".format(ssh_ip))
							else:
								exit()


					elif AWSChoice == 2 :
						print("Welcome to S3 Services ")
						s3menu()
						s3choice = int(input("Enter your choice : "))
						if s3choice == 1:
							print("---Creating S3 Bucket---")
							bucket_name = input("Enter your bucket name (UNIQUE) : ")
							region = input("Enter region name :")
							os.system("ssh {} aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocalConstraint={}".format(ssh_ip,bucket_name, region, region))

						elif s3choice == 2:
							print("---Uploading objects---")
							file_loc = input("File source : (Better copy & paste your file location)")
							bucket = input("Your bucket name :")
							os.system("ssh {} aws s3 cp {} s3://{} --acl public-read-write".format(ssh_ip,file_loc, bucket))
						else :
							exit()

					else:
						print("Something wrong I can feel it.")	




				elif choice == 6 :
					os.system("tput setaf 10")
					while True:
						print("\t\t1.See all images available")
						print("\t\t2.see all containers")
						print("\t\t3.Delete an image")
						print("\t\t4.Launch existing Containers")
						print("\t\t5.launch new container")
						print("\t\t6.Download/pull image")
						inp=int(input("enter your choice press 0 to exit "))
						if inp==1:
							os.system("ssh {} docker images".format(ssh_ip))
						if inp==2:
							os.system("ssh {} docker ps -a".format(ssh_ip))
						elif inp==3:
							x=input("enter the os image : ")
							os.system("ssh {} docker -rmi {}".format(ssh_ip,x))
						elif inp==4:
							x=input("enter the container name : ")
							os.system("ssh {} docker start {}".format(ssh_ip,x))
							os.system("ssh {} docker attach {}".format(ssh_ip,x))
						elif inp==5:
							x=input("enter the container name : ")
							y=input("osversion : ")
							os.system("ssh {} docker run -it --name {} {}".format(ssh_ip,x,y))
						elif inp==6:
							x=input("enter the container that to be downloaded : ")
							os.system("ssh {} docker pull {}".format(ssh_ip, x))
						elif inp==0:
							os.system("tput setaf 7")
							break
									




				elif choice == 7 :
					try:
						os.system("ssh {} ifconfig wlo1")
					except:
						os.system("ssh {} ifconfig enp0s3")




				elif choice == 8:
					remote()




				else :
					exit()

	
print("\t\t1 - Local Execuion\n\t\t2 - Remote Execution")
choice = input("Enter your choice :")
if int(choice) == 1:
		local()
					
elif int(choice) == 2:
		remote()

