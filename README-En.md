# Chinese Diabetes Question Classification Evaluation 2023
## 1. Task content
The Chinese diabetes question classification Check task aims to automatically classify diabetes related questions raised by patients.As a typical chronic disease, diabetes has become one of the major global public healthchallenges. With the rapid development of the Internet, the huge group of type 2 diabetes patients and high-risk people has shown an increasing demand for specializedinformation on diabetes. The automated diabetes Question Answering (QA) services also play a vital role in providing daily health services for patients and high-risk people.This task will help to enhance the performance of search results and promote the development of diabetes automatic question answering service.

The Chinese diabetes questions included in the task dataset are divided into six categories. Participants need to predict the classification of diabetes questions in the test set.After the prediction is completed, you only need to fill in the missing classified data of the test data set. In the evaluation phase, we will analyze the error of the filled data to get the predicted performance score.Please do not change the information in other parts of the dataset, such as the length of the data, the name of the dataset file, etc.

## 2. Evaluation standard
The task uses the accuracy (Acc, Accuracy) as the evaluation index, and the formula is as follows

$Accuracy  = \frac{Predict\ the\ correct\ number\ of\ samples}{Total\ number\ of\ predicted\ samples}$

## 3. Scale and distribution of evaluation data

<table><tr><th>Categories</th><th>Training Set</th><th>Validation Set</th><th>Test Set</th><th>Total</th></tr>
  <tr><td>Diagnosis</td><td>527</td><td>103</td><td>87</td><td>717</td></tr>
  <tr><td>Treatment</td><td>1501</td><td>260</td><td>265</td><td>2026</td></tr>
  <tr><td>Common Knowledge</td><td>1226</td><td>212</td><td>217</td><td>1655</td></tr>
  <tr><td>Healthy Lifestyle</td><td>1702</td><td>251</td><td>273</td><td>2226</td></tr>
  <tr><td>Epidemiololgy</td><td>599</td><td>118</td><td>90</td><td>807</td></tr>
  <tr><td>Other</td><td>445</td><td>56</td><td>68</td><td>569</td></tr>
  <tr><td>Total</td><td>6000</td><td>1000</td><td>1000</td><td>8000</td></tr>
</table>

## 4. Evaluate the competition schedule

<table>
  <tr><th>Time</th><th>Event</th></tr>
  <tr><td>Dec 15，2022~Mar 10，2023</td><td>Open Registration</td></tr>
  <tr><td>Dec 20,2022</td><td>Publish training setand validation set</td></tr>
  <tr><td>Feb 15,2023</td><td>Publish test set and start to submit test set results</td></tr>
  <tr><td>Mar 15, 2023</td><td>Result submission due</td></tr>
  <tr><td>Apr 1,2023</td><td>Notification of final list</td></tr>
  <tr><td>Apr 30, 2023</td><td>Invited papers or presentations confirmation due</td></tr>
  <tr><td> May 16, 2023</td><td>Notification of acceptance or rejection</td></tr>
</table>

## 5. Registration method
Participants are invited to download the registration form at [Registration-Form](https://github.com/yuni-bobo/Chinese-DQC/blob/main/Registration-Form.docx) .After filling in the registration form, please send an email to the mailbox in the form of an attachment for registration: ncaa2023classify@163.com 

Note: Each Participant can only register for one team

## 6. Submission method
Participants should fill in the "label" column corresponding to the test set according to the following example requirements. " \t" is used as the separator between "question" and "label". Finally, save the file as "test. txt" and send it to the mailbox: ncaa2023classify@163.com

Note: The real-time ranking of Participants can be viewed in [leaderboard](leaderboard/README.md)
<table>
  <tr><th>question</th><th>\t</th><th>label</th></tr>
  <tr><td>糖尿病患者可以吃西瓜吗</td><td>\t</td><td>3</td></tr>
</table>
