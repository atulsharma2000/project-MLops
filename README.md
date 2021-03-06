# 𝐈𝐧𝐭𝐞𝐠𝐫𝐚𝐭𝐢𝐨𝐧 𝐨𝐟 𝐌𝐋 𝐰𝐢𝐭𝐡 𝐃𝐞𝐯𝐎𝐩𝐬 𝐮𝐬𝐢𝐧𝐠 𝐎𝐒-𝐥𝐞𝐯𝐞𝐥 𝐯𝐢𝐫𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧
                            
![my woo](https://user-images.githubusercontent.com/41663027/88486344-af3ac900-cf9a-11ea-90b0-77c5b6245e2d.png)

- What is Machine learning?
Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

- What is DevOps?
DevOps is a set of practices that combines software development and information-technology operations which aims to shorten the systems development life cycle and provide continuous delivery with high software quality.

- What are container technology and 𝐎𝐒-𝐥𝐞𝐯𝐞𝐥 𝐯𝐢𝐫𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧?
Container technology is a method of packaging an application so it can be run with isolated dependencies, and they have fundamentally altered the development of software today due to their compartmentalization of a computer system.
OS-level virtualization refers to an operating system paradigm in which the kernel allows the existence of multiple isolated user-space instances.

- What is MLOps? How it's important?
MLOps is a practice for collaboration and communication between data scientists and operations professionals to help manage the production of ML lifecycle. MLOps is the only way to scale machine learning into production.
There are a number of barriers that prevent organizations from successfully implementing ML across the enterprise, including difficulties with Deployment and automation, Reproducibility of models and predictions, Diagnostics, Governance, regulatory compliance, Scalability, Collaboration, and Business uses. A standard practice, such as MLOps takes into account each of the aforementioned areas, which can help enterprises optimize workflows and avoid issues during implementation.


# 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧
- The aim is to automate a machine learning architecture and to predict only if accuracy is more than 90%. If accuracy is less than 90%, then it will tweak the machine learning model architecture automatically. Jenkins will be checking GitHub repositories every second for any changes. So as soon as a developer commits and pushes, Jenkins will start its jobs.
- Tech n Tools: ML libraries(TensorFlow, Keras, NumPy, Pandas, etc) to create a prediction model and Docker image for further automation, Jenkins(a great DevOps tool for automation), Docker for OS-level virtualization(to create images and containers on RHEL8), Red Hat Enterprise Linux 8, VMware(to run RHEL8 on our host operating system).


# 𝐄𝐱𝐩𝐥𝐚𝐧𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐈𝐦𝐩𝐥𝐞𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧:
(1) Install VMware on your host operating system. In VMware install the RHEL8 operating system. In RHEL8 install Docker(first you have to install all the requirements of Linux and configure yum and then install docker on RHEL8)
(2) After completion of the docker installation on Linux, create a docker image for the machine learning model to run and predict using a container. So make a directory and create a Dockerfile inside that directory and then use the docker build command to create the required image. (it will download and install everything) Command: docker build -t mlopsimg:v1 .
![1](https://user-images.githubusercontent.com/41663027/88486594-63891f00-cf9c-11ea-810e-fa058ae9730d.PNG)

(3) after the creation of the image install Jenkins on RHEL8 and start Jenkins services. Jenkins needs java to start services, so install java first. After installation, start Jenkins and copy-paste the IP of Linux on the browser with port 8080(Jenkins work on the port 8080) to access Jenkins GUI. example: 192.162.152.123:8080
- sudo yum install jenkins java-1.8.0-openjdk-devel   
- sudo yum install jenkins 
- sudo systemctl start jenkins

(4) Now create account on github and make a repository. Give anyname, i have given Project-MLops. Also make a folder in your windows or any os where you are working on machine learning code and paste all the required files in the same folder so that we can connect it with our github repository and push our updated work when ever we want.
wer have created three files here...
![333](https://user-images.githubusercontent.com/41663027/88486978-2d996a00-cf9f-11ea-85c7-a55f373b0236.PNG)
![4](https://user-images.githubusercontent.com/41663027/88486984-3722d200-cf9f-11ea-9d82-a34df58729f0.PNG)
![42](https://user-images.githubusercontent.com/41663027/88486992-4275fd80-cf9f-11ea-952c-4f254b2bef5a.PNG)
![4545](https://user-images.githubusercontent.com/41663027/88486996-4bff6580-cf9f-11ea-893c-e1d491884588.PNG)
- now adding, commiting and pushing our files on the github repository.
![gittt](https://user-images.githubusercontent.com/41663027/88487040-9c76c300-cf9f-11ea-8bcc-3efdab670522.PNG)
- this is the repository i made and pushed all the files for my ML project.
![22](https://user-images.githubusercontent.com/41663027/88487076-c8924400-cf9f-11ea-820b-157be490c295.PNG)

(5) In Jenkins create JOB-1. It will Pull the Github repo automatically whenever the developer commits and pushes the repository to Github. This job will copy all the repository files in a directory /root/mlops_code/ in our RHEL8 operating system.
- here i used POLL SCM , "Poll SCM" polls the SCM periodically for checking if any changes/ new commits were made and shall build the project if any new commits were pushed since the last build.
![j1](https://user-images.githubusercontent.com/41663027/88487172-6554e180-cfa0-11ea-94a2-056e977751bb.PNG)
- all the repository files are now pasted in our RhEL folder.(neglect the other files for a while)
![2](https://user-images.githubusercontent.com/41663027/88487233-d5636780-cfa0-11ea-963f-5bcb32e15cbc.PNG)

(6) JOB-2: it will only trigger after the completion of job1. Job2 will run a container from ml_py_img image we created and it also copy-pastes the mlops_code repository files from RHEL8 to container's /root/mlops_code directory. And as soon as the command runs, it will start executing the Training_model.py file.
This .py file will create a result.txt file which will be contaning the accuracy of the model.
![jjj2](https://user-images.githubusercontent.com/41663027/88487277-3e4adf80-cfa1-11ea-9be9-283c26f54fd0.PNG)
![j2222](https://user-images.githubusercontent.com/41663027/88487344-e496e500-cfa1-11ea-9a9a-48319f09b1f0.PNG)

(7) JOB-3:  this job will check the accuracy from the file result.txt. If the accuracy is less than the required accuracy then this job will automatically start adding the combination of the layers to increase the accuracy of the  model.
![j33](https://user-images.githubusercontent.com/41663027/88487426-a948e600-cfa2-11ea-8cc7-df6b08040fa0.PNG)
- here accuracy is already 98% so tweaking will not be done.
![jttjttjt](https://user-images.githubusercontent.com/41663027/88487446-c7aee180-cfa2-11ea-8168-65c5e160fa26.PNG)
- as our accuracy is good, so it will send a mail by executing sendmail.py file to the devloper
![maill](https://user-images.githubusercontent.com/41663027/88487523-76532200-cfa3-11ea-9340-2cd4ccade77e.PNG)


(8) JOB-4: it will monitor the container fails . If containers fails then this job will re run the containers and will start traning the model again. SO we will add a post buil as Job:2.

![dhdhjadh](https://user-images.githubusercontent.com/41663027/88487738-5e7c9d80-cfa5-11ea-937d-d36810739172.PNG)

- Build pipeline to watch the execution of the jobs 
![otupup](https://user-images.githubusercontent.com/41663027/88487759-8b30b500-cfa5-11ea-8b2a-650af4a5c16e.PNG)

𝐂𝐨𝐧𝐜𝐥𝐮𝐬𝐢𝐨𝐧:
Automated the Machine Learning architecture using Jenkins, now as soon as Developer commits and pushes the files on the GitHub, a docker container will be created with all the required machine learning libraries and model will train automatically with above required accuracy.

# video link
https://drive.google.com/file/d/1eEGapVk0IzwfyZgkYItfm6EnLTfit-lv/view?usp=sharing

