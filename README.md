# 中文糖尿病问题分类评测 2023
## 1. 任务内容
中文糖尿病问题分类评测任务旨在自动为患者提出的有关糖尿病问题进行分类。糖尿病作为一种典型慢性疾病已成为全球重大公共卫生挑战之一。随着互联网的快速发展，庞大的二型糖尿病患者和高危人群对糖尿病专业信息获取的需求日益突出，糖尿病自动问答服务对患者和高危人群的日常健康服务也发挥着越来越重要的作用。该任务将有助于增强搜索结果的性能并推动糖尿病自动问答服务的发展。

该任务数据集包含的中文糖尿病问题一共分为6类，参赛者需要预测测试集中糖尿病问题对应的分类。预测完成后仅需将测试数据集空缺的分类数据填充，评价环节仅对填充的数据进行误差分析，得出预测表现得分。请不要更改数据集中其他部分的信息，如数据的长度、数据集文件名称等。

## 2. 评价标准
该任务使用准确率（Acc，Accuracy）作为评价指标，公式如下：

$准确率(Accuracy) = \frac{预测正确的样本数}{预测总样本数}$

## 3. 评测数据规模与分布

<table><tr><th>训练集</th><th>开发集</th><th>测试集</th><th>总计</th></tr><tr><td>6000</td><td>1000</td><td>1000</td><td>8000</td></tr></table>

## 4. 评测赛程

<table><tr><th>时间</th><th>事项</th></tr><tr><td>12月15日 ~3月10日</td><td>开放报名</td></tr><tr><td>12月20日</td><td>发布训练集和开发集</td></tr><tr><td>2月15日</td><td>发布测试集，开始提交测试集结果</td></tr><tr><td>3月15日</td><td>截止提交测试集结果</td></tr><tr><td>4月1日</td><td>获奖名单公布</td></tr></tr><tr><td>4月30日</td><td>邀稿截止</td></tr><tr><td>5月14日</td><td>竞赛论文接收</td></tr></table>

## 5. 报名方式
参赛者请在[报名表](https://github.com/yuni-bobo/Chinese-DQC/blob/main/Registration-Form.docx)下载报名表，按照规定要求填写后，以附件形式发送邮件到邮箱: ncaa2023classify@163.com 进行报名。

## 6. 提交方式
参赛者请将代码和填充好分类的测试集文件以附件形式发送至邮箱： ncaa2023classify@163.com 
