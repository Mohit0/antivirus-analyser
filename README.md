# Antivirus-Analyser
Installation: 
1. Install dependencies:
<br />Run ```$ pip install -r requirements.txt```
2. Add your yara rules to ***public/*** folder. 
3. Compile all added rules.
<br />Run ```$ python compile_rules.py```
>**Note: This is a required to to initialize project for first time or whenever new rules are added.**
<br />References for yara rules:
<br />1. https://github.com/InQuest/awesome-yara
<br />2. https://github.com/Neo23x0/signature-base
<br />3. https://github.com/Yara-Rules/rules
<br />

### To Scan files in AWS S3
1. Add your aws creds to ***~/.aws/credentials*** file. (Default credentials will be used)
2. Add your **bucket_name** and **remote_file name** in **aws_manager.py** file 
> You can also create **lamdba_functions** to directly run aws_manager.py to scan whenever new file uploads to the bucket
3. Run ```python aws_manager.py```
4. Scanned files will be added a tag in S3 to confirm results. 
![image](https://user-images.githubusercontent.com/17490996/235293213-6f650644-9235-40ea-85ef-02771424b789.png)


### To Scan via Web App
1. Run ```$ python api_flask_app.py```
<br />OR 
<br />**Create docker container:** 
<br />```$ docker build .```
<br />```$ docker run -it -p 5000:5000 <image>```
<img src='https://user-images.githubusercontent.com/17490996/235293344-dc0422f3-10d0-4bd4-85fb-41b010e3bf05.png' width=700 height=200>
<img src='https://user-images.githubusercontent.com/17490996/235293372-8292f50d-55ec-4e6d-a043-3f8262bbc7c9.png' width=700 height=400>
