## Gensim学习笔记

### 一、基础概念

`Document`：文档

```python
document = "Human machine interface for lab abc computer applications"
```

`Corpus`：语料库，文档的列表集

```python
corpus=[
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    ...
]
```

语料库可以作为训练模型的输入数据，模型通过训练来寻找常见的 themes 和 topics，初始化其内部模型参数。

再训练后，一个主题模型可以被用来从新的文档中提取主题。此类语料集可以建立索引并通过语义相似性或聚类做作相似性查询。

再继续处理之前，我们希望将语料库中的每个单词与唯一的整数ID相关联，也就是建立词典。

`dictionary`：词典，`dictionary`本质上是一个包括很多单词的列表，但其中所有单词都是唯一的且具有不变的顺序，用来构建坐标系。

```python
from gensim import corpora

dictionary = corpora.Dictionary(corpus)
```

`Vector`：向量：文档的数学表达形式，向量化文档。

根据词典坐标系，为了推断语料库中的潜在结构，将每个文档用一系列数字表示，这些数字构成了一个向量，对于同于一个词典，同一个系列词对应的向量相同。如`(1, 0.0), (2, 2.0), (3, 5.0)`

为了节省内存，向量通常由许多零值组成。 Gensim 省略了所有值为 0.0 的向量元素。 这就是**稀疏矩阵**或是**词袋向量**。在这种稀疏表达形式中所有缺失的特征值被明确的解析为零。

另一种向量化表示文档的方法是**词袋模型**。在词袋模型下，每个文档都由一个向量表示，该向量包含字典中每个单词的频数。比如，假设我们有一个包含单词[‘coffee’, ‘milk’, ‘sugar’, ‘spoon’]的词典，一篇文档由字符串“coffee milk coffee”组成的字符串则会被表示成[2,1,0,0]，向量的长度就是字典中的条目数。词袋模型的主要特征之一就是它完全忽略了文档中单词出现的顺序，这也是“词袋”名称的来源。

**文档和向量的区别是前者是文本，后者是数学上更方便的文本表示形式。有时人们说的“文本”其实就是指“向量表示的文本”**

**两个不同的文本可能会有相同的向量表示（译者注：如词袋模型下“I like apple but don’t like banana”和“I like banana but don’t like apple”向量表示相同）**

`Model`：模型，

变换（transformation）指的是把文档的从一种表达形式变成另一种表达形式。在gensim中，文档由向量组成，所以变换（transformation）可以理解成两个向量空间间的映射函数。

`tf-idf`就是一个模型，tf-idf模型把词袋化的向量转化为语料集中频数由相对稀有度加权处理的向量空间。

```python
from gensim import models

# 训练模型，输入是文档稀疏表达的元祖二维列表。
tfidf = models.TfidfModel(bow_corpus)

# 转化 "system minors" 字符串
words = "system minors".lower().split()
print(tfidf[dictionary.doc2bow(words)])

# [(5, 0.5898341626740045), (11, 0.8075244024440723)]
```

tfidf模型返回一个元祖列表，第一条是词典ID，第二条是tf-idf权重。gensim提供了多种多样的模型和转换方法，我们也可以自行训练模型。

