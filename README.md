# CSE100 Practice Questions & Answers

For so many reasons which includes complaints, inconsistencies, and lack of support on an application, CSE100.apk, I have taken the time to decompile the app and extract the questions in it for easy access for everyone and made the questions available in document formats(TXT and PDF).

And yes! including those that want to develop a new and better application. Credits of the content is due to the developer of the application.

Straight to business, below are the requirements and steps taken to extract the questions in the app:

## Requirements
- Apktool (How to install? Click [here](https://ibotpeaches.github.io/Apktool/install/))
- Python (Either versions would work)
- A few minute(s)
- And of course, your PC 😀 (you can't run these by your hands only)


## Extraction Steps

1. I'll assume you have the app (its also included in this repo). Nevertheless, clone this repo
```
git clone https://github.com/sawzeeyy/CSE100.git
```
2. Decompile the app using Apktool
```
./apktool -d CSE100.apk
```
3. After decompiling, a folder would be included on your PC with the name of the app, `../CSE100/CSE100`
4. The file containing the question is located at `../CSE100/assets/www/api/newQuestions.json`
![CSE100 File Structure](https://user-images.githubusercontent.com/32202226/41212800-993bea88-6d38-11e8-9817-765ae0a6643d.png)
5. Hurray! Its a JSON file and this has been included directly in this repo
6. Now, execute the python script, `extract.py`
```
python3 extract.py
```
7. You'll get loads of texts after execution
8. Those are the questions.

That's all! 🤓

In addition, there are two more files: the questions generated as from the tool which is in the formats `txt` (for those readers / students without a PDF software and others who want to make ammendments) and `pdf` (for all readers / students).


**Author: [@_sawzeeyy](https://www.twitter.com/_sawzeeyy)**


This is licensed under [MIT Licencse](https://github.com/sawzeeyy/CSE100/blob/master/LICENSE)