# Faker文档

*Faker* 是一个 用于生成虚假数据的Python 包，广泛应用于压力测试与爬虫开发。

```
pip install Faker
```

## 1.本地化虚假

`faker.Faker`可以将语言环境作为参数，返回本地化 数据，默认为`en_US`。

```python
from faker import Faker

fake = Faker('zh_CN')
print(fake.name())  # 李雷
# 多区域设置
fake = Faker(['it_IT', 'en_US', 'ja_JP'])
```

可能用到的区域：

| 参数    | 含义                    | 参数    | 含义                   | 参数    | 含义                   | 参数    | 含义                    |
| ------- | ----------------------- | ------- | ---------------------- | ------- | ---------------------- | ------- | ----------------------- |
| `ar_EG` | `Arabic（埃及)`         | `en_GB` | `English（大不列颠)`   | `hu_HU` | `Hungarian（匈牙利）`  | `pl_PL` | `Polish（波兰）`        |
| `ar_PS` | `Arabic（巴勒斯坦)`     | `en_NZ` | `English（新西兰)`     | `hy_AM` | `Armenian（亚美尼亚）` | `pt_BR` | `Portuguese（巴西)`     |
| `ar_SA` | `Arabic（沙特阿拉伯)`   | `en_US` | `English（美国)`       | `it_IT` | `Italian（意大利）`    | `pt_PT` | `Portuguese（葡萄牙)`   |
| `bg_BG` | `Bulgarian（保加利亚）` | `es_ES` | `Spanish（西班牙)`     | `ja_JP` | `Japanese（日本）`     | `ro_RO` | `Romanian（罗马尼亚）`  |
| `bs_BA` | `Bosnian（波黑）`       | `es_MX` | `Spanish（墨西哥)`     | `ka_GE` | `Georgian（格鲁吉亚)`  | `ru_RU` | `Russian（俄罗斯）`     |
| `cs_CZ` | `Czech（捷克）`         | `et_EE` | `Estonian（爱沙尼亚）` | `ko_KR` | `Korean（韩国）`       | `sl_SI` | `Slovene（斯洛文尼亚）` |
| `de_DE` | `German（德国）`        | `fa_IR` | `Persian（伊朗)`       | `lt_LT` | `Lithuanian（立陶宛）` | `sv_SE` | `Swedish（瑞典）`       |
| `dk_DK` | `Danish（丹麦）`        | `fi_FI` | `Finnish（芬兰）`      | `lv_LV` | `Latvian（拉脱维亚）`  | `tr_TR` | `Turkish（土耳其）`     |
| `el_GR` | `Greek（希腊）`         | `fr_FR` | `French（法国）`       | `ne_NP` | `Nepali（尼泊尔）`     | `uk_UA` | `Ukrainian（乌克兰）`   |
| `en_AU` | `English（澳大利亚)`    | `hi_IN` | `Hindi（印度）`        | `nl_NL` | `Dutch（荷兰)`         | `zh_CN` | `Chinese（中国大陆）`   |
| `en_CA` | `English（加拿大)`      | `hr_HR` | `Croatian（克罗地亚）` | `no_NO` | `Norwegian（挪威）`    | `zh_TW` | `Chinese（中国台湾）`   |

## 2.可生成的虚假数据

### 1.人物相关

```python
fake.first_name()            # 名字
fake.first_name_female()     # 名字(女)
fake.first_name_male()       # 名字(男)
fake.first_romanized_name()  # 名字(罗马文)
fake.last_name()             # 姓
fake.last_name_female()      # 姓(女)
fake.last_name_male()        # 姓(男)
fake.last_romanized_name()   # 姓(罗马文)
fake.name()                  # 姓名
fake.name_female()           # 姓名(女)
fake.name_male()             # 姓名(男)
fake.prefix()                # 称谓
fake.prefix_female()         # 称谓(女)
fake.prefix_male()           # 称谓(男)
fake.romanized_name()        # 称谓(罗马文)
fake.suffix()                # 姓名后缀(中文不适用)
```

### 2.地址相关

```
fake.address()            # 地址
fake.building_number()    # 楼名    
fake.city()               # 完整城市名
fake.city_name()          # 城市名字(不带市县)
fake.city_suffix()        # 城市后缀名
fake.country()            # 国家名称
fake.district()           # 地区
fake.postcode()           # 邮编
fake.province()           # 省
fake.street_address()     # 街道地址
fake.street_name()        # 街道名称
fake.street_suffix()      # 街道后缀名
fake.country_code(representation="alpha-2")  # 国家编号
```

### 3.汽车相关

```
fake.license_plate() # 牌照
```

### 4.银行相关

```
ake.bank_country()           # 银行所属国家
fake.bban()                  # 基本银行账号
fake.iban()                  # 国际银行代码
```

### 5.条形码相关

```
fake.ean(length=13)    # EAN条形码
fake.ean13()           # EAN13条形码
fake.ean8()            # EAN8条形码
```

### 6.颜色相关

```
fake.color_name()        # 颜色名称
fake.hex_color()         # 颜色十六进制值
fake.rgb_color()         # 颜色RGB值
fake.rgb_css_color()     # CSS颜色值
fake.safe_color_name()   # 安全色
fake.safe_hex_color()    # 安全色十六进制值
```

### 7.公司相关

```
fake.bs()                 # 商业用词
fake.catch_phrase()       # 妙句(口号)
fake.company()            # 公司名称
fake.company_prefix()     # 公司名称前缀
fake.company_suffix()     # 公司名称后缀
```

### 8.信用卡相关

```
fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")    # 过期年月
fake.credit_card_full(card_type=None)            # 完整信用卡信息
fake.credit_card_number(card_type=None)          # 信用卡卡号
fake.credit_card_provider(card_type=None)        # 信用卡提供商
fake.credit_card_security_code(card_type=None)   # 信用卡安全码
```

### 9.货币相关

```
fake.cryptocurrency()           # 加密货币代码+名称
fake.cryptocurrency_code()      # 加密货币代码
fake.cryptocurrency_name()      # 加密货币名称
fake.currency()                 # 货币代码+名称
fake.currency_code()            # 货币代码
fake.currency_name()            # 货币名称
```

### 10.时间相关

```
fake.am_pm()        # AM或PM
fake.century()      # 世纪
fake.date(pattern="%Y-%m-%d", end_datetime=None)            # 日期字符串(可设置格式和最大日期)
fake.date_between(start_date="-30y", end_date="today")      # 日期(可设置限定范围)
fake.date_between_dates(date_start=None, date_end=None)     # 同上
fake.date_object(end_datetime=None)                         # 日期(可设置最大日期)
fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)    # 出生日期
fake.date_this_century(before_today=True, after_today=False)       # 本世纪日期
fake.date_this_decade(before_today=True, after_today=False)        # 本年代中的日期
fake.date_this_month(before_today=True, after_today=False)         # 本月中的日期
fake.date_this_year(before_today=True, after_today=False)          # 本年中的日期
fake.date_time(tzinfo=None, end_datetime=None)                     # 日期和时间
fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)    # 日期和时间(从001年1月1日到现在)
fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)    # 日期时间(可设置限定范围)
fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None)    # 同上
fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)     # 本世纪中的日期和时间
fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)      # 本年代中的日期和时间
fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)       # 本月中的日期和时间
fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)        # 本年中的日期和时间
fake.day_of_month()   # 几号
fake.day_of_week()    # 星期几
fake.future_date(end_date="+30d", tzinfo=None)        # 未来日期
fake.future_datetime(end_date="+30d", tzinfo=None)    # 未来日期和时间
fake.iso8601(tzinfo=None, end_datetime=None)          # iso8601格式日期和时间
fake.month()                                          # 第几月
fake.month_name()                                     # 月份名称
fake.past_date(start_date="-30d", tzinfo=None)        # 过去日期
fake.past_datetime(start_date="-30d", tzinfo=None)    # 过去日期和时间
fake.time(pattern="%H:%M:%S", end_datetime=None)      # 时间(可设置格式和最大日期时间)
fake.time_delta(end_datetime=None)                    # 时间间隔
fake.time_object(end_datetime=None)                   # 时间(可设置最大日期时间)
fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None)
fake.timezone()    # 时区
fake.unix_time(end_datetime=None, start_datetime=None)    # UNIX时间戳
fake.year()        # 某年
```

### 11.文件相关

```
fake.file_extension(category=None)                # 文件扩展名
fake.file_name(category=None, extension=None)     # 文件名
fake.file_path(depth=1, category=None, extension=None)    # 文件路径
fake.mime_type(category=None)                     # MIME类型
fake.unix_device(prefix=None)                     # UNIX设备
fake.unix_partition(prefix=None)                  # UNIX分区
```

### 12.坐标相关

```
fake.coordinate(center=None, radius=0.001)        # 坐标
fake.latitude()                                   # 纬度
fake.latlng()                                     # 经纬度
fake.local_latlng(country_code="US", coords_only=False)    # 返回某个国家某地的经纬度
fake.location_on_land(coords_only=False)                   # 返回地球上某个位置的经纬度
fake.longitude()                                   # 经度
```

### 13.网络相关

```
fake.ascii_company_email(*args, **kwargs)        # 企业邮箱(ascii编码)
fake.ascii_email(*args, **kwargs)                # 企业邮箱+免费邮箱(ascii编码)
fake.ascii_free_email(*args, **kwargs)           # 免费邮箱(ascii编码)
fake.ascii_safe_email(*args, **kwargs)           # 安全邮箱(ascii编码)
fake.company_email(*args, **kwargs)              # 企业邮箱
fake.domain_name(levels=1)                       # 域名
fake.domain_word(*args, **kwargs)                # 二级域名
fake.email(*args, **kwargs)                      # 企业邮箱+免费邮箱
fake.free_email(*args, **kwargs)                 # 免费邮箱
fake.free_email_domain(*args, **kwargs)          # 免费邮箱域名
fake.hostname(*args, **kwargs)                   # 主机名
fake.image_url(width=None, height=None)          # 图片URL
fake.ipv4(network=False, address_class=None, private=None)    # ipv4
fake.ipv4_network_class()  
fake.ipv4_private(network=False, address_class=None)          # 私有ipv4
fake.ipv4_public(network=False, address_class=None)           # 公共ipv4
fake.ipv6(network=False)                                      # ipv6
fake.mac_address()                            # MAC地址
fake.safe_email(*args, **kwargs)              # 安全邮箱
fake.slug(*args, **kwargs)                    # URL中的slug
fake.tld()                                    # 顶级域名
fake.uri()                                    # URI
fake.uri_extension()                          # URI扩展
fake.uri_page()                               # URI页
fake.uri_path(deep=None)                      # URI路径
fake.url(schemes=None)                        # URL
fake.user_name(*args, **kwargs)               # 用户名
```

### 14.图书相关

```
fake.isbn10(separator="-")        # ISBN-10图书编号
fake.isbn13(separator="-")        # ISBN-13图书编号
```

### 15.职位相关

```
fake.job()        # 职位
```

### 16.文本相关

```
fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)    # 单个段落
fake.paragraphs(nb=3, ext_word_list=None)                                         # 多个段落                                            
fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)    # 单个句子
fake.sentences(nb=3, ext_word_list=None)                                 # 多个句子
fake.text(max_nb_chars=200, ext_word_list=None)                          # 单个文本
fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)             # 多个文本
fake.word(ext_word_list=None)                                            # 单个词语
fake.words(nb=3, ext_word_list=None, unique=False)                       # 多个词语
```

### 17.编码相关

```
fake.binary(length=1048576)                # 二进制
fake.boolean(chance_of_getting_true=50)    # 布尔值
fake.md5(raw_output=False)                 # Md5
fake.null_boolean()                        # NULL+布尔值
fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)                           # 密码
fake.sha1(raw_output=False)                # SHA1
fake.sha256(raw_output=False)              # SHA256
fake.uuid4(cast_to=<class 'str'>)          # UUID4
```

### 18.电话相关

```
fake.msisdn()                # 完整手机号码(加了国家和国内区号)
fake.phone_number()          # 手机号
fake.phonenumber_prefix()    # 区号
```

### 19.档案相关

```
fake.profile(fields=None, sex=None)        # 档案(完整)
fake.simple_profile(sex=None)               # 档案(简单)
```

### 20.Python相关

```
fake.pybool()    # Python布尔值
fake.pydecimal(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)  # Python十进制数
fake.pydict(nb_elements=10, variable_nb_elements=True, *value_types)    # Python字典
fake.pyfloat(left_digits=None, right_digits=None, positive=False, min_value=None, max_value=None)        # Python浮点数
fake.pyint(min_value=0, max_value=9999, step=1)    # Python整型值
fake.pyiterable(nb_elements=10, variable_nb_elements=True, *value_types)    # Python可
fake.pylist(nb_elements=10, variable_nb_elements=True, *value_types)    # Python列表
fake.pyset(nb_elements=10, variable_nb_elements=True, *value_types)    # Python集合
fake.pystr(min_chars=None, max_chars=20)    # Python字符串
fake.pystruct(count=10, *value_types)       # Python结构
fake.pytuple(nb_elements=10, variable_nb_elements=True, *value_types)    # Python元组
```

### 21.身份证相关

```
fake.ssn(min_age=18, max_age=90)    # 身份证
```

22.用户代理相关

```
fake.android_platform_token()        # 安卓
fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)    # Chrome
fake.firefox()                       # FireFox
fake.internet_explorer()             # Ie
fake.ios_platform_token()            # ios
fake.linux_platform_token()          # Linux
fake.linux_processor()               # Linux处理器
fake.mac_platform_token()            # Mac
fake.mac_processor()                 # Mac处理器
fake.opera()                         # Opera
fake.safari()                        # Safari
fake.user_agent()                    # 随机用户代理
fake.windows_platform_token()        # Windows
```

