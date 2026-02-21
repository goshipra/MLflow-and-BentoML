# MLflow and BentoML Setup and IRIS data Experiment

# Objective
 
 - Setup an EC2 Instance where I setup mlflow for experiment tracking and BentoML for turning our machine learning model into production-ready API.


# Steps:
#### 1. Setup AWS EC2 Instance:
 I created an AWS EC2 Virtual Machine for this Project.

 - Go to AWS console > Search EC2 > Launch Instance > Choose instance type of your choice(I used t2.micro) > key pair > Security group > Launch Instance

 - Connect to created Instance by using ssh command from you AWS CLI from local terminal.

   
  
  ``` ssh -i "path/to/Key/KEYPAIR.pem" ec2-user@EC2INstance.compute-1.amazonaws.com ```



  ![alt text](image.png)


##### After loggedin to AWS Instance, we need to install necessary libraries:



```sudo yum update && sudo yum install python3-pip -y ```



<img width="1120" height="633" alt="Screenshot 2026-02-19 at 3 31 51 PM" src="https://github.com/user-attachments/assets/49fad6a2-8bef-4f73-a058-695ee33124f2" />

##### Install core dependencies


``` pip install mlflow bentoml scikit-learn pandas ```



<img width="939" height="332" alt="Screenshot 2026-02-19 at 3 33 10 PM" src="https://github.com/user-attachments/assets/bfe7da73-045f-408d-a490-c3e4608fb33f" />


#### 2. Train and Register with MLflow
We will use the Iris dataset for a simple classification model. This script trains the model, logs the metrics, and registers it in the MLflow Model Registry.

##### Create a folder and cd into the folder and Create a file named train.py:



  ``` vim train.py ```


  
<img width="603" height="62" alt="Screenshot 2026-02-19 at 3 53 05 PM" src="https://github.com/user-attachments/assets/962bd4d7-8863-4c41-a821-5106374d990a" />

 
###### you can copy the code from train.py file in this repository.
Then Excute the file using 



``` python3 train.py ```



<img width="800" height="484" alt="Screenshot 2026-02-19 at 3 55 03 PM" src="https://github.com/user-attachments/assets/ccd9815f-6968-426b-be3b-270b10a51b77" />

##### you can see mlruns directory created.

<img width="565" height="103" alt="Screenshot 2026-02-19 at 3 56 46 PM" src="https://github.com/user-attachments/assets/b0417aa7-acf5-4488-a0aa-f5e6bcbf20b0" />

##### create a file import_bento.py, you can copy the code from repository

<img width="682" height="56" alt="Screenshot 2026-02-19 at 4 00 57 PM" src="https://github.com/user-attachments/assets/770868e0-60af-40af-9a2e-32215be1409a" />


##### Execute it 

 ``` python3 import_bento.py ```

 <img width="682" height="56" alt="Screenshot 2026-02-19 at 4 00 57 PM" src="https://github.com/user-attachments/assets/dd2a580c-c9df-4847-80ed-9d3d938397af" />


 ##### you can see model being created 

 ``` bentoml models list ```

 <img width="738" height="119" alt="Screenshot 2026-02-19 at 4 01 35 PM" src="https://github.com/user-attachments/assets/a6f887fb-7dfe-476f-b8a9-4ce374effbae" />


 #### 3. Now we create service.py file, you can copy the code from repository

 ``` vim service.py ```

 ##### and run the service:

 ```  bentoml serve service:IrisService --reload --host 0.0.0.0 --port 3000 ```
 

 <img width="811" height="184" alt="Screenshot 2026-02-19 at 4 14 24 PM" src="https://github.com/user-attachments/assets/2c9826bd-be06-4048-889a-a52e42cfe58b" />

 #### 4. Access the UI of BentoML and MLflow

For BentoML UI on your browser, you need to enable port 3000 in inbound rules in Security groups in AWS : 

``` https://<Instance_Public_IP>:3000 ```
 
<img width="1011" height="726" alt="Screenshot 2026-02-19 at 4 17 02 PM" src="https://github.com/user-attachments/assets/7a6312e7-2dc6-4fd8-be54-a4f51acaf095" />

<img width="1011" height="726" alt="Screenshot 2026-02-19 at 4 17 02 PM" src="https://github.com/user-attachments/assets/b8594a76-fcd8-434e-9eea-ee2c7cbfb247" />

#####   
##### for MLflow UI, run below command on terminal: 

``` mlflow server --host 0.0.0.0 --port 5000 ```

and on your browser, you need to enable port 5000 in inbound rules in Security groups in AWS

``` https://<Instance_Public_IP>:5000 ```

<img width="1552" height="892" alt="Screenshot 2026-02-19 at 4 23 26 PM" src="https://github.com/user-attachments/assets/fdb721b1-92ec-4d47-8862-e490e3136655" />



























  

  
