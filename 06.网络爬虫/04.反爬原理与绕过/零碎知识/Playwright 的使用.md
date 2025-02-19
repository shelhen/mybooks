Playwright 支持同步与异步两种模式，这里分开来进行讲解。

**同步**

使用 Playwright 时可以选择启动安装的三种浏览器（Chromium、Firefox 和 WebKit）中的一种。

```
from playwright.sync_api import sync_playwright

# 调用sync_playwright方法，返回浏览器上下文管理器
with sync_playwright() as p:
    # 创建谷歌浏览器示例，playwright默认启动无头模式，设置headless=False，即关闭无头模式
    browser = p.chromium.launch(headless=False)
    # 新建选项卡
    page = browser.new_page()
    # 跳转到目标网址
    page.goto("http://baidu.com")
    # 获取页面截图
    page.screenshot(path='example.png')
    # 打印页面的标题，也就是title节点中的文本信息
    print(page.title())
    # 关闭浏览器
    browser.close()
# 输出：百度一下，你就知道
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JonHruqhBA6oL7rVg2PnhkvmSH2iaveeQP61D0Ij7rd02S8t5kBWpjyIGx7sD7Tjmb62n3aibSXdQA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

可以看到，Playwright 的使用也比较简单，语法比较简洁，而且浏览器的启动速度以及运行速度也很快。

**异步**

异步代码的编写方法与同步基本一致，区别在于同步调用的是 sync_playwright，异步调用的是 async_playwright。最终运行效果与同步一致。

```
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://baidu.com")
        # 打印网页源代码
        print(await page.content())
        await browser.close()

asyncio.run(main())
```

**代码生成**

Playwright 提供了代码生成功能，这个功能可以对我们在浏览器上的操作进行录制并生成代码，它可以有效提高程序的编写效率。代码生成功能需要使用 Playwright 命令行中的 codegen实现，codegen 命令存在如下主要参数：

> -o ：将生成的脚本保存到指定文件
>
> -b ：要使用的浏览器，默认为 chromium
>
> --target ：生成的语言，默认为 Python
>
> --save-trace ：记录会话的跟踪并将其保存到文件中
>
> --timeout ：设置页面加载的超时时间
>
> --user-agent ：指定UA
>
> --viewport-size ：指定浏览器窗口大小

我们在命令行执行命令：`playwright codegen -o script.py`

执行命令后会弹出一个 chromium 浏览器与脚本窗口，当我们在浏览器上进行操作时，脚本窗口会根据我们的操作生成对应代码。当我们操作结束后，关闭浏览器，在当前目录下会生成一个 script.py 文件，该文件中就是我们在进行浏览器操作时，Playwright 录制的代码。我们运行该文件，就会发现它在复现我们之前的操作。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JonHruqhBA6oL7rVg2PnhkmJjllEudWzUg8edhibWeNXqAjwfOvqSkhplb8kfyaEuqeUVB0S7kgfQ/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

代码生成功能的实用性其实较为一般，它只能实现比较简单的操作，当遇到复杂操作时，生成的代码就容易出现问题。最好的方式是使用代码生成功能生成部分操作的代码，然后再手动去修改它生成的代码。

**隔离**

上一步中，我们使用代码生成功能生成了一段代码，我们会发现这段代码中使用到了一个 new_context 方法，通过这个方法创建了一个 content ，然后再去进行其它操作。这个 new_content 方法其实是为了创建一个独立的全新上下文环境，它的目的是为了防止多个测试用例并行时各个用例间不受干扰，当一个测试用例异常时不会影响到另一个。

```
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()
```

**定位器**

Playwright 提供了多种定位器来帮助开发中定位元素。

> page.get_by_role() ：通过显式和隐式可访问性属性进行定位。
>
> page.get_by_text() ：通过文本内容定位。
>
> page.get_by_label() ：通过关联标签的文本定位表单控件。
>
> page.get_by_placeholder() ：按占位符定位输入。
>
> page.get_by_alt_text() ：通过替代文本定位元素，通常是图像。
>
> page.get_by_title() ：通过标题属性定位元素。
>
> page.get_by_test_id() ：根据data-testid属性定位元素（可以配置其他属性）。
>
> page.locator()：拓展选择器，可以使用 CSS 选择器进行定位

使用定位器最好的方式就是上文中讲到的利用代码生成功能来生成定位代码，然后手动去修改，这里就不做尝试。

**选择器**

Playwright 支持 CSS、Xpath 和一些拓展选择器，提供了一些比较方便的使用规则。

**CSS 选择器**

```
# 匹配 button 标签
page.locator('button').click()
# 根据 id 匹配,匹配 id 为 container 的节点
page.locator('#container').click()
# CSS伪类匹配，匹配可见的 button 按钮 
page.locator("button:visible").click()
# :has-text 匹配任意内部包含指定文本的节点
page.locator(':has-text("Playwright")').click()
# 匹配 article 标签内包含 products 文本的节点
page.locator('article:has-text("products")').click()
# 匹配 article 标签下包含类名为 promo 的 div 标签的节点
page.locator("article:has(div.promo)").click()
```

**XPath**

```
page.locator("xpath=//button").click()
page.locator('xpath=//div[@class="container"]').click()
```

**其它**

```
# 根据文本匹配，匹配文本内容包含 name 的节点
page.locator('text=name').click()
# 匹配文本内容为 name 的节点
page.locator("text='name'").click()
# 正则匹配
page.locator("text=/name\s\w+word").click()
# 匹配第一个 button 按钮
page.locator("button").locator("nth=0").click()
# 匹配第二个 button 按钮
page.locator("button").locator("nth=-1").click()
# 匹配 id 为 name 的元素
page.locator('id=name')
```

**等待**

当进行 click 、fill 等操作时，Playwright 在采取行动之前会对元素执行一系列可操作性检测，以确保这些行动能够按预期进行。

如对元素进行 click 操作之前，Playwright 将确保：

> 元素附加到 DOM
>
> 元素可见
>
> 元素是稳定的，因为没有动画或完成动画
>
> 元素接收事件，因为没有被其他元素遮挡
>
> 元素已启用

即使 Playwright 已经做了充分准备，但是也并不完全稳定，在实际项目中依旧容易出现因页面加载导致事件没有生效等问题，为了避免这些问题，需要自行设置等待。



```
# 固定等待1秒
page.wait_for_timeout(1000)
# 等待事件
page.wait_for_event(event)
# 等待加载状态
page.get_by_role("button").click()
page.wait_for_load_state()
```

**事件**

```
from playwright.sync_api import sync_playwright


def print_request_sent(request):
    print("Request sent: " + request.url)


def print_request_finished(request):
    print("Request finished: " + request.url)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
 # 添加事件 发起请求时打印URL
    page.on("request", print_request_sent)
    # 请求完成时打印URL
    page.on("requestfinished", print_request_finished)
    page.goto("https://baidu.com")
    # 删除事件
    page.remove_listener("requestfinished", print_request_finished)
    browser.close()
```

**反检测**

在 Selenium 的使用中，我们讲到了自动化工具容易被网站检测，也提供了一些绕过检测的方案。这里我们介绍一下 Playwright 的反检测方案。

以 https://bot.sannysoft.com/ 为例，我们分别测试正常模式与无头模式下的检测结果。

**正常模式**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JonHruqhBA6oL7rVg2PnhkUkDWOEG97WfRFVNwV4DQGgTE0tiba6S9pAiczP8I4icXjUwStjZbye5UA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**无头模式**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JonHruqhBA6oL7rVg2PnhkeuBB6tFnkGbLEXCvWicUI9wVOLK27coAl26Fa5bw1DjOFWekhbTu6tw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

可以看到，正常模式下 WebDriver 一栏报红，而无头模式下更是惨不忍睹，基本上所有特征都被检测到了。这些还只是最基本的检测机制，自动化工具的弱点就暴露的很明显了。

与 Selenium 一样，绕过检测主要还是针对网站的检测机制来处理，主要就是在页面加载之前通过执行 JS 代码来修改一些浏览器特征。以无头模式为例：



```
from playwright.sync_api import sync_playwright

with open('./stealth.min.js', 'r') as f:
    js = f.read()

with sync_playwright() as p:
    browser = p.chromium.launch()
    # 添加 UserAgent
    page = browser.new_page(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    )
    # 执行 JS 代码
    page.add_init_script(js)
    page.goto("https://bot.sannysoft.com/")
    page.screenshot(path='example.png')
    browser.close()
```

这里与 Selenium 反检测方案一样，执行 **stealth.min.js** 来隐藏特征（ **stealth.min.js** 的来源与介绍参考上期文章）。最终结果如下图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JonHruqhBA6oL7rVg2Pnhk2qDqb9FfOvXjpEPPcJfobAFN3djN9LhKGyOib1yENOaNJpwDRKJ6AZw/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)





**启动**

以百度热搜榜为例：

```
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://top.baidu.com/board?tab=realtime')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

示例代码中使用 launch 方法创建了一个浏览器对象 browser ，设置了 headless=False 来关闭无头模式，这一行代码的作用相当于启动一个浏览器，await的作用就是等待浏览器启动完毕。

创建完浏览器后，使用到了 newPage 方法，创建了一个 Page 对象，这一步相当于打开了一个新的标签页，通过 await 等待标签页创建完毕，然后调用 goto 方法打开目标网址，最后使用 close 方法关闭浏览器。

**launch 详解**

launch 方法用于启动浏览器进程并返回浏览器实例，它包含了多个参数：

| **参数**                            | **描述**                                                     |
| :---------------------------------- | :----------------------------------------------------------- |
| `ignoreHTTPSErrors`（bool）         | 是否忽略HTTPS错误。默认为 `False`                            |
| `headless`（bool）                  | 是否开启无头模式。默认为`True`                               |
| `executablePath` （str）            | 可执行文件的路径，设置该参数可以指定已有的 Chrome 或 Chromium 浏览器。 |
| `slowMo` （int \| float）           | 传入指定时间（毫秒），用于延缓 Pyppeteer 的一些模拟操作。    |
| `args` （List [str]）               | 传递给浏览器的额外参数。                                     |
| `dumpio`（bool）                    | 是否将 Pyppeteer 的输出信息传给 `process.stdout`和`process.stderr`。默认为`False`。 |
| `userDataDir` （str）               | 用户数据文件夹。                                             |
| `env`（dict）                       | 浏览器环境。默认与 Python 进程相同。                         |
| `devtools`（bool）                  | 是否为每个标签页打开 DevTools 面板，默认为`False`,如果该参数为 `True`，则 `headless` 会被强制设置为 `False`。 |
| `logLevel`（int \| str）            | 日志级别。默认值与根记录器相同。                             |
| `autoClose`（bool）                 | 脚本完成时自动关闭浏览器进程。默认为`True`。                 |
| `loop`（asyncio.AbstractEventLoop） | 事件循环。                                                   |

**禁用提示条**

与 Selenium 一样，Pyppeteer 控制浏览器时会提示 Chrome 正受到自动测试软件的控制。可以通过 设置 launch 方法中的 args 参数来关闭提示。



```
browser = await launch(headless=False, args=['--disable-infobars'])
```

**用户数据持久化**

自动化工具如 Selenium 、Playwright 都有一个特点，就是每一次运行的时候创建的都是一个全新的浏览器，它不会记录用户之前的行为。如第一次运行时我登录了某个网站，而第二次运行时再次进入该网站时依旧需要登录。这是因为自动化工具没有记录用户行为信息。Pyppeteer 中，如果需要记录用户的行为信息，可以通过设置 launch 方法中的 userDataDir 方法来实现。

```
browser = await launch(headless=False, args=['--disable-infobars'], userDataDir='./userdata')
```

设置了用户数据文件夹后运行代码，会生成一个 userdata 文件夹，其中就存储着用户上次控制浏览器时记录的一些行为数据。

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JgRib0vaicRlfAouHSiaUCnzuAuoM1FSjs3MsRic6BF0eUaDjB0ku1PQp3agLfYuLxW8KoKhUXrH8DJA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**执行 JS 语句**

```
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://top.baidu.com/board?tab=realtime')
    dimensions = await page.evaluate('''() => {
           return {
               width: document.documentElement.clientWidth,
               height: document.documentElement.clientHeight,
               deviceScaleFactor: window.devicePixelRatio,
           }
       }''')
    print(dimensions)
    await browser.close()
# {'width': 783, 'height': 583, 'deviceScaleFactor': 1}
```

通过调用 Page 对象下的 evaluate 方法可以执行一段 JS 语句。

**反检测**

Pyppeteer 的反检测方式与 Selenium 和 Playwright 有些区别，但是思想是一样的。

首先需要安装 pyppeteer_stealth 库，它的作用就是用来隐藏特征。

```
pip install pyppeteer_stealth
```

以无头模式为例：

```
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth


async def main():
    browser = await launch()
    page = await browser.newPage()
    # 隐藏特征
    await stealth(page)
    
    await page.goto('https://bot.sannysoft.com/')
    await page.screenshot(path='page.png')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

隐藏特征前：

![](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JgRib0vaicRlfAouHSiaUCnzuJjibq9PEKGia7PHjYkzWjOxjsuslkVmZib72KHMNicHcO1RqiblRp4jaCFg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

隐藏特征后：

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabtD4jabia4JgRib0vaicRlfAouHSiaUCnzukjShjThypxfjBzkWXs7JcaHGDTRETOqlz6oKohicHtT74Tu06oJB4Ag/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**等待**

> waitForSelector ：等待符合条件的节点加载完成
>
> waitForFunction ：等待某个 JavaScript 方法执行完毕或返回结果
>
> waitForRequest ：等待某个特定的请求发出
>
> waitForResponse ：等待某个特定请求对应的响应
>
> waitForNavigation ：等待页面跳转，如果页面加载失败则抛出异常
>
> waitFor ：通用等待
>
> waitForXpath ：等待符合 Xpath 的节点加载出来

**选择器**

Pyppeteer 提供了一些比较有意思的选择器方法。

> J() ：返回匹配到的第一个节点，等同于 querySelector 方法。
>
> JJ() ：返回匹配到的所有节点，等同于 querySelectorAll 方法。
>
> JJeval() ：执行 JS 脚本并返回一个 JSON 对象，等同于 querySelectorAllEval 方法。
>
> Jeval() ：执行 JS 脚本并返回执行结果，等同于 querySelectorEval 方法。
>
> Jx() ：通过 Xpath 匹配符合条件的内容，等同于 xpath 方法。

```
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://top.baidu.com/board?tab=realtime')
    # 等待元素加载
    await page.waitForXPath('//div[@class="c-single-text-ellipsis"]')
    element_j = await page.J('.c-single-text-ellipsis')
    element_jj = await page.JJ('.c-single-text-ellipsis')
    # 打印元素的文本信息
    print(await (await element_j.getProperty('textContent')).jsonValue())
    for element in element_jj:
        # 打印元素的文本信息
        print(await (await element.getProperty('textContent')).jsonValue())

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
"""
运行结果：
青年强则国家强 
青年强则国家强 
乌代表举自家国旗挑衅暴揍俄代表 
英王加冕礼彩排：黄金钻石马车亮眼 
平凡岗位上的奋斗故事 
俞敏洪建议24节气都放假 
7人吃自助4小时炫300多个螃蟹 
  .
  .
  .
"""
```

