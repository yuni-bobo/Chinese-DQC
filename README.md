# 中文糖尿病问题分类评测 2023
## 获奖名单公布
<table><tr><th>Team Name</th><th>Score</th><th>Rank</th></tr>
  <tr><td>永升队</td><td>89.9</td><td>1</td></tr>
  <tr><td>biubiu</td><td>89.6</td><td>2</td></tr>
  <tr><td>雨打芭蕉队</td><td>89.1</td><td>3</td></tr>
  <tr><td>只会梭哈</td><td>89.1</td><td>3</td></tr>
</table>

## 1. 任务内容
中文糖尿病问题分类评测任务旨在自动为患者提出的有关糖尿病问题进行分类。糖尿病作为一种典型慢性疾病已成为全球重大公共卫生挑战之一。随着互联网的快速发展，庞大的二型糖尿病患者和高危人群对糖尿病专业信息获取的需求日益突出，糖尿病自动问答服务对患者和高危人群的日常健康服务也发挥着越来越重要的作用。该任务将有助于增强搜索结果的性能并推动糖尿病自动问答服务的发展。

该任务数据集包含的中文糖尿病问题一共分为6类。参赛者需要预测测试集中糖尿病问题对应的分类，预测完成后需将测试数据集空缺的类别标签数据进行填充。评价环节仅对填充的数据进行误差分析，得出预测表现得分。

## 2. 评价标准
该任务使用准确率（Acc，Accuracy）作为整体排名标准，公式如下：

$准确率(Accuracy) = \frac{预测正确的样本数}{预测总样本数}$

## 3. 评测数据规模与分布

<table><tr><th>类别</th><th>训练集</th><th>验证集</th><th>测试集</th><th>总计</th></tr>
  <tr><td>诊断</td><td>527</td><td>103</td><td>87</td><td>717</td></tr>
  <tr><td>治疗</td><td>1501</td><td>260</td><td>265</td><td>2026</td></tr>
  <tr><td>常识</td><td>1226</td><td>212</td><td>217</td><td>1655</td></tr>
  <tr><td>健康生活方式</td><td>1702</td><td>251</td><td>273</td><td>2226</td></tr>
  <tr><td>流行病学</td><td>599</td><td>118</td><td>90</td><td>807</td></tr>
  <tr><td>其他</td><td>445</td><td>56</td><td>68</td><td>569</td></tr>
  <tr><td>总计</td><td>6000</td><td>1000</td><td>1000</td><td>8000</td></tr>
</table>

## 4. 评测赛程

<table><tr><th>时间</th><th>事项</th></tr>
<tr><td>12月20日</td><td>发布训练集和验证集</td></tr>
<tr><td>2月15日</td><td>发布测试集，开始提交测试集结果</td></tr>
<tr><td>3月25日</td><td>截止提交测试集结果</td></tr>
<tr><td>4月1日</td><td>获奖名单公布</td></tr>
</tr><tr><td>4月30日</td><td>邀稿截止</td></tr>
<tr><td>5月14日</td><td>竞赛论文接收</td></tr>
</table>

## 5. 报名方式
参赛者请在[报名表](https://github.com/yuni-bobo/Chinese-DQC/blob/main/Registration-Form.docx)下载报名表，按照规定要求填写后，以附件形式发送邮件到邮箱: ncaa2023classify@163.com 进行报名。

**注意**: **每位参赛队员只能报名参加一个队伍**

## 6. 提交方式
参赛者请按照以下示例要求填充好测试集对应的“label”列，“question”与“label”之间使用“\t”作为分隔符。最后将文件保存为“test.txt”格式发送至邮箱：ncaa2023classify@163.com 

注意：参赛选手的实时排名可在[LeaderBoard](https://yuni-bobo.github.io/leaderboard.html)查看,LeaderBoard每日21:00更新队伍实时成绩排名。
<table><tr><th>question</th><th>\t</th><th>label</th></tr><tr><td>糖尿病患者可以吃西瓜吗</td><td>\t</td><td>3</td></tr></table>
