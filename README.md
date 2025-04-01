# MindSpore-JSON

## 简介
MindSpore-JSON是一个基于MindSpore深度学习框架的机器学习模型集合，包含了多个常用的机器学习算法实现，如ResNet50、K-means聚类、线性回归、逻辑回归和决策树等。

## 安装

```bash
pip install mindspore-json
```

## 功能特点
- ResNet50图像分类模型
- K-means聚类算法
- 线性回归模型
- 逻辑回归分类器
- 决策树算法

## 使用示例
```python
from mindspore_json import resNet50
from mindspore_json import kmeans
from mindspore_json import linear
from mindspore_json import logistic
from mindspore_json import tree

# 更多使用示例请参考各模型的文档
```

## 依赖要求
- Python >= 3.7
- MindSpore >= 1.0.0
- NumPy >= 1.17.0
- EasyDict >= 1.9
- Matplotlib >= 3.3.0

## Usage

```
import json2

a = json2.load_file(r'/home/user/myjson.json')
json2.dump_file(r'/home/user/myjson.json', a)
```
