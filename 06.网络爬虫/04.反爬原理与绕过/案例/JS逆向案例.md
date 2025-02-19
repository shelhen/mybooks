1. 逆向目标

- 目标网址:https://www.qimai.cn/rank/offline
- 接口:https://api.qimai.cn/rank/offline?analysis=ew8vECUSNA54ZX4XKQt8TygiLhI0LT9MfWMqHCxTdxwrHlgANBMFSHo3KRt3XDcMBQ9FRDoWHkUCCgoWWQMACwEWHDoWBQZaVlEAAVNTUVg4Wkk%3D&status=3&date=2023-12-21&sdate=2023-12-21&edate=2023-12-21&country=cn&genre=36&option=4&page=2

##### 2. 逆向分析

- 定位加密位置

- 尝试关键字搜索`analysis`

```JavaScript
// 搜索不到的原因
1. 代码有做混淆
2. 关键字做拼接  
```

- `hook`定位

```
(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("analysis") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();
```

![](./images/134.png)

- 可以看到他的数据在第三个栈已经生成好了,说明代码是在异步的过程中加密的数据,但是异步执行的代码在栈堆里面是看不到的,在异步生成的过程有两个原因,第一个可能是在单纯的异步代码生成加密的,另一种可能是在拦截器里面生成的
- 异步调试的方法,可以在发异步的位置下一个断点,先大致的过一点,先大致观察代码的执行的过程,前期可以先大致调试一下,大致知道数据在哪里生成之后就能精细化调整
- 拦截器,就能向上节课一样,向下调试找到响应拦截器,请求拦截器一般就是在响应拦截器的上面
- 加密位置
- e的值就是加密对应的数据

![](./images/135.png)

##### 3. 逆向代码

- JavaScript代码

```JavaScript
function o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function (n) {
            t += unescape("%u00" + n)
        });
    var t, e = t;
    return String[e](n)
}

function v(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });

    return btoa(t)

}

function h(n, t) {
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]('')
}


function get_analysis(a) {
    // var a = [1, '2023-12-21', '2023-12-21', '2023-12-21', 'cn', '36', 4, 3];
    a = a["sort"]()["join"]('')
    a = v(a)
    r = +new Date() - 4421027 - 1661224081041
    // r = 41932436257
    a = (a += "@#" + "/indexV2/getIndexRank") + ("@#" + r) + ("@#" + 3)
    console.log(a)
    var d = "xyz517cda96efgh"
    return v(h(a, d))
}

aa = get_analysis(['0', '6014'])

// console.log(aa)
```

- python代码

```python
import requests
import execjs

headers = {
    "origin": "https://www.qimai.cn",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://api.qimai.cn/indexV2/getIndexRank"
params = {
    "setting": "0",
    "genre": "6014"
}
with open('1111.js', encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
val = params.values()
analysis = js.call('get_analysis', list(val))
params['analysis'] = analysis
response = requests.get(url, headers=headers, params=params)

print(response.json())

```

