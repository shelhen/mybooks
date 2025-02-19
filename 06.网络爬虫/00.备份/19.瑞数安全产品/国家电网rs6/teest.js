// 检测node.js的指纹环境
delete __dirname
delete __filename


all_content = "arg1_content"


function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        console.log("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}
proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'aaa', 'target']

setTimeout = function () {
}
setInterval = function () {
}
div = {
    getElementsByTagName: function (res) {
        console.log('div中getElementsByTagName的参数为：', res)
        if (res === "i") {
            return []
        }
    }
}
script = [
    {
        getAttribute: function (res) {
            if (res === "r") {
                return "m"
            }
        },
        parentElement: {
            removeChild: function (res) {
                console.log(res)
            }
        }
    },
    {
        getAttribute: function (res) {
            if (res === "r") {
                return "m"
            }
        },
        parentElement: {
            removeChild: function (res) {
                console.log(res)
            }
        }
    }
]
meta = [
    {
        "http_equiv":"Content-Type",
        getAttribute: function (res) {
            console.log('meta中getAttribute接收到的参数为：', res)
            if (res === "r") {
                return "m"
            }
        },
        content: 'text/html; charset=utf-8'
    },
    {
        "http_equiv":"Content-Type",
        getAttribute: function (res) {
            console.log('meta中getAttribute接收到的参数为：', res)
            if (res === "r") {
                return "m"
            }
        },
        content: all_content,
        parentNode: {
            removeChild: function (res) {
                console.log('meta中parentNode中removeChild所接受的参数为：')
            }
        }
    }
]
base = []
navigator = {
    appCodeName: "Mozilla",
    webdriver:false,
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    language: "zh-CN",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    vendor: "Google Inc.",
    vendorSub: "",
    platform: "Win32",
    languages:["zh-CN"],
    mimeTypes:{},
    product: "Gecko",
    webkitPersistentStorage:{},
    productSub: "20030107",
    connection:{
        downlink: 2.5,
        effectiveType: "4g",
        onchange: null,
        rtt: 100,
        saveData: false
    }
}
obj1 = {
    E: 2.718281828459045,
    LN2: 0.6931471805599453,
    LN10: 2.302585092994046,
    LOG2E: 1.4426950408889634,
    LOG10E: 0.4342944819032518,
    PI: 3.141592653589793,
    SQRT1_2: 0.7071067811865476,
    SQRT2: 1.4142135623730951
}
html1 = {}
location = {
    hash: "",
    host: "www.sgcc.com.cn",
    hostname: "www.sgcc.com.cn",
    href: "http://www.sgcc.com.cn/html/sgcc/col2022121225/column_2022121225_2.shtml",
    origin: "http://www.sgcc.com.cn",
    pathname: "/html/sgcc/col2022121225/column_2022121225_2.shtml",
    port: "",
    protocol: "http:",
    search: ""
}
history = {
    length: 2,
    scrollRestoration: "auto",
    state: null,
    replaceState:function (res) {
        console.log('history中replaceState参数：',res)
    }
}




// window补环境
window = global;
window.top = window
window.self = window
window.navigator = navigator
window.name = ''
window.ActiveXObject=undefined
window.$_ts = window['$_ts'];
            if (!$_ts)
                $_ts = {};
            $_ts.nsd = 62113;
            $_ts.cd = "qJwqrSAlouWqck9EWaqZqOakmfGZq19mHqAuJqVuqkacck9YEaaErr0ZES30quWqHqAZrp33HqqKJcquqkaDHqQKDkalkq9lokaOmOAkHqANckWqHqEZqS33DA3KJqWZrkamkGatrr0uqr9rHq3KDkWqck9hWaqEiAaKqqGyksaqHqlikq7lDuWqDAEZqS33WaqZqsaDmfGuqr9lHqVKDkackqalDkWqHq3RrS33WaqZrsacmfGZqp30xuaDkq0lDkWqHqEZqS33HcWKJqWuqkalHqVKDkac9ctFqsVSqGVSWyLOqU.tb5vM4.cfQQwHuphFsohGYWLNMpXlboUORSsGZV9krkWora8MhqtwKUa2WZLCKKNgV2JO5CYzMbfDtKop1UxsQnVeUHpCMC9XFUx.ePezQDy.tCvBMCZNMox.F4Rzwb2XKP726KrTYTJ5Km1PYoJeMYTrAzSPYbJTpPVeaKTCFKg.FUhCMne.wCz.tdpCMC9XFUx.ePezQDy.KPXgsVLawbYXV7r0MTR_39NTL6miQ0TSRPKGKDTaMb7.F8eBMn27Qbz.zbTCFKg.FUhCMne.wCz.K.3fVbzKFbTqLuYaQKl5I9U7MlfLADy6w.GyKDz6FC7.eoRBF1yNQbBChCTaMb7.F8eBMn27Qbz.SnZfUumsVb.kpVxoRKZ0YzrxplG0sTJs5nlyUbSnFCXCMURNMPzNQBRBhCz6FC7.eoRBF1yNQbBCUPZvF0Ji3wfmJ1zJJDRNnbmW19fOMkMcQPldKK2nFd3BMUrXFnzN4CeBtKSnFCXCMURNMPzNQBRBUP9GMKNHdCfGJVezFC.ysVNTpsg6s7xl3PQgUD2nebZBF6w.FnB0wbeNhb2nFd3BMUrXFnzN4CeBKoZ.FUhCMTgHqaw5WHfp3UVyUCelL2pfH935YToXplZ5YCqnIww4iDR43l0Z6mrAp0riFuMHRo2vskrxHty13YJCp9J2eleYsDlZs9hzM6r7MUqZRhpm80egAkE66cT23CWSJDFPhK2CiKWNA8xx8VE6J0lNdDYPWumbHnvaQkfThlmds8rlJOYltKmf5uVaRkLNMU1fRPTk89TeAtZup1zLwkSzusq_3of2VmILikw61lmPWIrJsuqawuSAg2R9WofuAC.uiDpbhlmds8rlJOYltKmf5uVaRkLNMU1fRDQ.poeJIw0CW0W73Kmb.krPH1SzwkueQnTk89TeAtZup1z93K3SjKE4tCf0ra8FqOWmqulomIx6w6VgJsA6jO3aWkA5JuCPWaWkRDmbWF2Pqa30WkWo9kEuHslCWk_jJuWmrsZ0Hj9SWOWcm5tLMonCBRGIQU5XIDLFMOlom5Nc6OmNf9P5vR9qrGQmqqcFES9zExfi833_2603tVk1gK9oeMYGZZZGswBDttWQ1OFkqaa_WOQu.OqSJulorO8FcsEnWOgTWtLnJuachDe6aOmU1DRtAVBWJURp3o00W829V9pYFKyf6YmVHsNKAOijw63.3C2SAe3kqaVkWaQDjGWcWGHaWoCC3bxbhbRjwMRPQDGXRvmXzbmPMPy2RviC3KyThbYXFMRGhCROR1z9_UqBRvmStCsTMPebQvQ.3dz6hCmXFnzOeKqB3KTutCHT3o7NR6ePtde7wn29FC3.dDeGtKpLF1BZMoQNRDfNQ4R9RCQX3DyfzbpytKYBFcBnM6WNFvw6tdx63c2.RDG.ZCTjtKzN31BuMUqNF6pLtdrahCeOw1zz_bABM6xP3cBaQDS.hbTbQI7BMCSGtCzLd1eXMD3.Fv8XhCyT3nzjWd7BMvVStCN6d1eXMvA.FbO5hCyjwczjMBQBMvYntCN0ZneXwKwGtCOgF1ej3UZ.FHT9hCNXR1zLeb3BFvRft6IOh6JZ31z6RX9BQCxBt6w6eneuwUl.w6IXh6JfRcz6w5y4h6Y73cz6ZCqBwKyXt6INRne0FCl.wXy4h6wOt6YjzvmPFcyTFvogh6mGR1zT3X9BQUm9t6Yb_ceaFPy0RKXCQDYehvpaR.RawDWXwomGzvr_wPyuRvKCwCxdhvJX3MR6FbJ9t6JL_ombF63.Q6dXh6wSRczSwHgBwURSt6m041eTIK3.QDOZR1enMKmfJMR0MvWXQDNbzvpPQnyaw61C8CmLhve6F.R4M63XICz0gPe4wbg.IC.Ch69N8Dy6tdzuFc2nFCy04PejwKWora88UcwFWGQkKhgvwGVDKcWO5AWoKPRbsq83WsAmqkgdry7uqaAu";
            if ($_ts.lcd)
                $_ts.lcd();
window.addEventListener = function (res) {
    console.log('window中addEventListener接收到的参数为：', res)
}
window.sessionStorage = {
    length: 0
}
window.indexedDB = {}
window._$_p = function (res) {
    console.log('window中_$_p参数：',res)
}
window.localStorage = {
    "$_YVTX": "Wq",
    "_$rc": "P8HI1BFqpnkVski3VyTZh4Zw62kB18QeEy1hxDmnRLPRu12pIaJm.f_rNybc6Eh_yvbQHKFdTCVf8NCnxBYJAaRBg8JHV1BWLjxcn5aVAaF9A9XyLwNhKJM3viHR4C2Oby6RitUBfwkJOSMCRouvUcxF6FDoJu10APhp7BUqxzckytCovMutw.qmpzm.h8cgSuFblRqlE1tf60zj9vVrmafLgKHE7AA4HbeC_Ec95wYNMOCtnWq5fzaxws_CY_WC04hCtA.lMUb4fm.k52YaUqmAQGlFGkOEpWp8hmCtdpBBxeqJ3j5mjmr4s.p1G.pgSstrpM_p_Pu3A4vS34zLX2fanZzsJlRNYeBm_w_5X.RxLt68UWo4aJ5wjzcHK5lXKs09xh9Tt2YoF23nVIp.XM3ikhPzJItI4IGxE37qR8qtQ01AWfQhmQPT4eoMqHN0.M0WORkx9x937d7aegZ2YiL_tX9ZAK3fXZsOiTacxKuvLgaMeFJEo2r4T3grmSLqvO0DzQoWLBbqQQoU5TFKWwbdg6o8RXpVgZl45piaaPgSoFFehdyQ5wzJwDuY5lMjHgZJq_JlG3MivVGAmseZVg1.4hoYy.uVSN8RxHdc3twJwgyJTI9c1hjTXJ3pXSk4AJ0vurjpW_8sb6Qz82Wm5Jtyel4m3pDe0obvUvegcNQDCCxm2Cfnj8gCcJjDvPwWOM4DuPLeyRR87B1lOXGlVyjp5p5B2n8KDbXhdwaJV_tI9zrA9R4AMnl137Ef.QLVNSqi8yLmT9Ig6itl",
    "__#classType": "localStorage",
    "$_YWTU": "BdLbC4vbH8nz5apNnJm6H_2WTxep.NLfoAZujpmu7MG"
}
window.open = function (res) {
    console.log('window中open的参数为：',res)
}
window.setTimeout = function () {
}
window.setInterval = function () {
}
window.DOMParser = function (res) {
    console.log('window中DOMParser参数：',res)
}
window._$bJ = function (res) {
    console.log('window中_$bJ参数：',res)
}
window._$az = function (res) {
    console.log('window中_$az参数：',res)
}
window.XMLHttpRequest = function (res) {
    console.log('window中XMLHttpRequest参数：',res)
}
window.chrome = {
    loadTimes: function (res) {console.log(res)},
    csi: function (res) {console.log(res)}
}
window.clientInformation = navigator
window.TEMPORARY = 0
window.webkitRequestFileSystem = function (res) {
    console.log('window中webkitRequestFileSystem参数：',res)
}
window.MutationObserver = function (res) {
    console.log('window中MutationObserver参数：',res)
    return {
        "observe":function (res) {
            console.log('window中MutationObserver中observe参数：',res)
            if (typeof res==='object'){
                return undefined
            }
        }
    }
}



//document补环境
document = {}
document.createElement = function (res) {
    console.log('document中createElement接收到的参数为：', res)
    if (res === "div") {
        return div
    }
}
document.getElementsByTagName = function (res) {
    console.log('document中getElementsByTagName接收到的参数为：', res)
    if (res === "script") {
        return script
    }
    if (res === "meta") {
        return meta
    }
    if (res === "base") {
        return base
    }
}
document.visibilityState = 'visible'
document.setTimeout = function () {
}
document.setInterval = function () {
}
document.getElementById = function (res) {
    console.log('document中getElementById参数：', res)
    if (res === "root-hammerhead-shadow-ui") {
        return null
    }
}
document.addEventListener = function (res) {
    console.log('document中addEventListener属性：', res)
}
document.appendChild = function (res){
    console.log('document中appendChild参数：',res)
}
document.removeChild = function (res) {
    console.log('document中removeChild参数：',res)
}
document.documentElement = {'style': {}}
document.all = [
    {'style': {}},
    {},
    meta[0],
    meta[0],
    script[0],
    script[0]
]
document.createExpression = function (res) {
    console.log('document中createExpression参数：',res)
    if (res==='//html'){
        return html1
    }
}


get_enviroment(proxy_array)

'arg2_function';

require("./test1")

function go() {
    console.log(document.cookie)
    return document.cookie
}
go()
// console.log(document.cookie)




