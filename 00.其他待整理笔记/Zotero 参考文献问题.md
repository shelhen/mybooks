

# Zotero 参考文献问题

一些处理过的参考文献格式

https://github.com/redleafnew/Chinese-std-GB-T-7714-related-csl

官方网站提供了可视化自定义工具：https://editor.citationstyles.org/visualEditor/

- 可以以可视化块的形式**快速对样式进行编辑**，实现个性需求。
- 可以检索到大量的样式，**迅速找到适合的模板**

知乎某人给的小教程：https://zhuanlan.zhihu.com/p/612655690

## CSL 1.0.2 规范

文档：https://docs.citationstyles.org/en/stable/specification.html

> 作者：Principal Authors Rintze M. Zelle, PhD, Brenton M. Wiernik, Frank G. Bennett, Jr., Bruce D’Arcus

引文样式语言 （CSL） 是一种基于 XML 的格式，用于描述 引文、注释和参考书目的格式，提供了开放格式、紧凑而坚固的样式、对样式要求的广泛支持、自动样式本地化、样式分发和更新的基础结构、数以千计的免费样式。

### 1.XML声明

每种样式或区域设置都应以 XML 声明开头，并指定 XML 版本和字符编码。在大多数情况下，声明将是：

```python
<?xml version="1.0" encoding="UTF-8"?>
```

### 2.样式结构

#### 2.1根元素

样式的根元素是`style`，一般具有如下属性：

`class`：确定样式是使用文本内引用（`in-text`）还是注释。

`default-locale`（可选）：设置样式本地化的默认区域设置。

`version`：样式的 CSL 版本，对于与 CSL 1.0 兼容的样式，必须为“1.0”。

此外，可以携带任何[全局选项](https://docs.citationstyles.org/en/stable/specification.html#global-options)和[可继承名称选项](https://docs.citationstyles.org/en/stable/specification.html#inheritable-name-options)。

```xml
<style xmlns="http://purl.org/net/xbiblio/csl" version="1.0" class="in-text" name-as-sort-order="all" sort-separator=" " demote-non-dropping-particle="never" initialize-with=" " initialize-with-hyphen="false" page-range-format="expanded" default-locale="zh-CN">
</style>
```

#### 2.2子元素

根元素内可以包含如下子元素，其结构基于 [Atom 联合格式](http://tools.ietf.org/html/rfc4287)。

##### （1）`cs:info`

必须显示为第一个子元素，其中包含关于样式的描述：样式名称、ID、作者等等。

- `author`和`contributor`（可选）：分别用于确认风格 作者和贡献者，可以多次使用，内部可以提供更多子元素，如`name`、`email`、`url`或其他自定义子元素。

- `category`（可选）：样式可以分配一个或多个类别，可以使用一次来描述文内引文的呈现方式，也可以多次与属性一起使用 set 到其中一个学科类别：

设置引用呈现方式：`citation-format`；

```python
“author-date” - e.g. “… (Doe, 1999)”
“author” - e.g. “… (Doe)”
“numeric” - e.g. “… [1]”
“label” - e.g. “… [doe99]”
“note” - note格式使用的是脚注格式：①：某个脚注。
```

设置学科类别：`field`

```python
['anthropology', 'astronomy', 'biology', 'botany', 'chemistry', 'communications', 'engineering', 'generic-base - used for generic styles like Harvard and APA', 'geography', 'geology', 'history', 'humanities', 'law', 'linguistics', 'literature', 'math', 'medicine', 'philosophy', 'physics', 'political_science', 'psychology', 'science', 'social_science', 'sociology', 'theology', 'zoology']
```

> **有两大类格式，分别是note和in-text，其中in-text又分为author-date和numeric格式。无论是什么格式，均需要定义文内引用和参考文献的格式。**

- `id`：必须出现的唯一标识符，过去或现有总是使用`URL`，未来建议使用`uuid`来保证稳定性和唯一性。

- `link`（可选）：可多次使用，用于提供引用或者相关其他链接，必须携带两个属性：`href` 和`rel`，前者通常为 URL，后者解释前者的作用。

```python
“self” - 样式 URI
“template” - 派生当前样式的样式的 URI
“documentation” - 样式文档的 URI
```

- `published`（可选）:内容必须为时间戳， 指示样式的初始创建或可用时间。

- `updated`：必须，给出更新时间，示例：`2024-01-21T19:31:01+08:00`

- `title`：必须出现一次，内容应该是有一定的可识别性的样式名。

- `title-short`（可选）：缩短 样式名称。

- `summary`（可选）：给出一个（简短的）描述。

- `rights`（可选）：指定样式文件被释放，该元素可以携带属性`rightslicense`指定许可证的 URI。

- `issn/eissn/issnl`（可选）：多次用于表示ISSN 编写样式的期刊的标识符。

例子：

```xml
<info>
    <!-- 名称，id可以设置为英文名称，最好有一定的可识别性 -->
    <title>GB/T 7714-2015 (著者-出版年, 双语)</title>
    <id>http://www.zotero.org/styles/gb-t-7714-2015-author-date-bilingual</id>
    <!-- 提供引用或者相关其他链接 -->
    <link href="http://www.zotero.org/styles/gb-t-7714-2015-author-date-bilingual" rel="self"/>
    <link href="http://www.zotero.org/styles/china-national-standard-gb-t-7714-2015-author-date" rel="template"/>
     <!-- 信息与文献 参考文献著录规则官网 -->
    <link href="https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D8055ED3A7E05397BE0A0AB82A" rel="documentation"/>
    <!-- 作者信息:内部标签随意 -->
    <author>
      <name>shelhen</name>
      <email>shelhen@163.com</email>
    </author>
    <!-- 合作者信息:内部标签随意 -->
    <contributor>
      <name>CaiGui</name>
      <email>CaiGui@163.com</email>
    </contributor>
    <!-- 类别信息:可以插入单标签 -->
    <category citation-format="author-date"/>
    <category field="generic-base"/>
    <!-- 摘要信息 -->
    <summary>按照语言显示“等”或“et al.”</summary>
    <!-- 时间信息 -->
    <updated>2024-01-21T19:31:01+08:00</updated>
    <!-- 版权信息 -->
    <rights license="http://creativecommons.org/licenses/by-sa/3.0/">This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 License</rights>
  </info>
```

##### （2）`cs:citation`

用于描述引用文献的格式，如：[编号] 作者1,作者2,日期,题目,页码,出版社,....,等等。

- `sort`：用于指定引文应该如何排序，一般可以放置在`layout`之前，详情请参考[排序](https://docs.citationstyles.org/en/stable/specification.html#sorting)。
- `layout`：必须的子元素，描述引文的结构和格式，该元素可携带[特定于引文的选项](https://docs.citationstyles.org/en/stable/specification.html#citation-specific-options)和[可继承选项的](https://docs.citationstyles.org/en/stable/specification.html#inheritable-name-options)属性。

```xml
<citation>
  <sort>
    <key variable="citation-number"/>
  </sort>
  <layout>
    <text variable="citation-number"/>
  </layout>
</citation>
```

##### （3）`cs:bibliography `（可选）

用于描述书目的格式， 其中列出了一个或多个书目来源。

- `layout`：必须的子项描述每个书目条目的格式，该元素携带[特定于参考书目的选项](https://docs.citationstyles.org/en/stable/specification.html#bibliography-specific-options)和[可继承选项](https://docs.citationstyles.org/en/stable/specification.html#inheritable-name-options)的属性。

- `sort`：用于指定书目应该如何排序，一般可以放置在`layout`之前，详情请参考[排序](https://docs.citationstyles.org/en/stable/specification.html#sorting)。

```xml
<bibliography>
  <sort>
    <key macro="author"/>
  </sort>
  <layout>
    <group delimiter=". ">
      <text macro="author"/>
      <text variable="title"/>
    </group>
  </layout>
</bibliography>
```

##### （4）`cs:macro`（可选）

使用元素定义的宏可以包含格式设置说明，宏可以被其他宏内部的`text`标签调用，也可以被`bibliography`或`citation`内部的`layout`标签调用或是`sort`标签内部的`key`调用。建议将`macro`放置在`locale`之后和`citation`之前。

宏标签必须包含一个`name`属性，并且其内部需要包含一个或多个[呈现 元素](https://docs.citationstyles.org/en/stable/specification.html#rendering-elements)。

合理的使用宏可以提高样式的可读性、紧凑性和 可维护性。建议通过以来依赖调用宏来保持项目类型（例如书籍、日记）的内容，为了便于代码重用，建议使用常用宏名称。在下面的示例中，引用由项目标题组成，当 项目类型为“book”：

```xml
<macro name="title">
    <choose>
      <if type="book">
        <text variable="title" font-style="italic"/>
      </if>
      <else>
        <text variable="title"/>
      </else>
    </choose>
  </macro>
  <citation>
    <layout>
      <text macro="title"/>
    </layout>
  </citation>
```

任何祖先分隔元素的分隔符不会应用于元素的输出中（请参阅[分隔符](https://docs.citationstyles.org/en/stable/specification.html#delimiter)）。`<text macro="...">`

##### （5）`cs:locale`（可选）

在文件内部定义的一些本地化数据，正常的数据应该来自`locales-xx-XX.xml`区域设置文件中，通过`locale`标签在内部重新定义或补充元素，这些元素应该是 直接放在`info`元素之后。

属性`xml:lang`必须被设置，以确定哪类语言最终会被影响，其值必须被设置为`xsd:language`的区域设置代码，请参阅区域设置回退。如下代码中，仅当语言为英文时才会生效。

```python
<locale xml:lang="en">
    <terms>
      <term name="editortranslator" form="short">
        <single>ed. &amp; trans.</single>
        <multiple>eds. &amp; trans.</multiple>
      </term>
    </terms>
  </locale>
```

### 3.元素渲染

指定书目片段或引文片段以何种顺序排列。

#### 3.1`cs:layout`：决定如何呈现一条引用

它必须包含`prefix`、`suffix`和`delimiter`属性，其中`prefix`与`suffix`定义了文内引用的前缀和后缀，`delimiter`定义了两条引用之间的符号。

```python
<layout prefix="(" suffix=")" delimiter="; ">
# (A.C. Smith, D. Williams. et al., 2002; W. Wallace, J. Snow, 1999)
<layout prefix="[" suffix="]" delimiter="@ ">
# [A.C. Smith, D. Williams. et al., 2002@ W. Wallace, J. Snow, 1999]
```

#### 3.2`cs:text`：决定呈现内容

- `variable`：呈现变量的文本内容。属性值必须是标准变量之一，可以伴随`form`属性来选择变量的“长”（默认）或“短”形式。
- `macro`：呈现宏的文本输出。属性值必须匹配元素属性的值。
- `term`：呈现一个术语。属性值必须是 [附录II - 术语](https://docs.citationstyles.org/en/stable/specification.html#appendix-ii-terms)中列出的术语之一。可能伴随`plural`属性选择术语的单数（“false”，默认）或复数（“true”）变体， 并通过`form`属性选择“long”（默认）、“short”， “动词”、“动词短”或“符号”形式变体
- `value`：呈现属性值本身。

还可以携带 [affixes](https://docs.citationstyles.org/en/stable/specification.html#affixes), [display](https://docs.citationstyles.org/en/stable/specification.html#display), [formatting](https://docs.citationstyles.org/en/stable/specification.html#formatting), [quotes](https://docs.citationstyles.org/en/stable/specification.html#quotes), [strip-periods](https://docs.citationstyles.org/en/stable/specification.html#strip-periods) and [text-case](https://docs.citationstyles.org/en/stable/specification.html#text-case) 属性。

（3）





### 3.区域设置









