                                    𝐈𝐧𝐭𝐞𝐠𝐫𝐚𝐭𝐢𝐨𝐧 𝐨𝐟 𝐌𝐋 𝐰𝐢𝐭𝐡 𝐃𝐞𝐯𝐎𝐩𝐬 𝐮𝐬𝐢𝐧𝐠 𝐎𝐒-𝐥𝐞𝐯𝐞𝐥 𝐯𝐢𝐫𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧
                            
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


𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧
- The aim is to automate a machine learning architecture and to predict only if accuracy is more than 90%. If accuracy is less than 90%, then it will tweak the machine learning model architecture automatically. Jenkins will be checking GitHub repositories every second for any changes. So as soon as a developer commits and pushes, Jenkins will start its jobs.
- Tech n Tools: ML libraries(TensorFlow, Keras, NumPy, Pandas, etc) to create a prediction model and Docker image for further automation, Jenkins(a great DevOps tool for automation), Docker for OS-level virtualization(to create images and containers on RHEL8), Red Hat Enterprise Linux 8, VMware(to run RHEL8 on our host operating system).
