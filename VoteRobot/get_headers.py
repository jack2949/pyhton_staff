import random
class Urls():
    lagouwang_urls=[
    'https://www.lagou.com/zhaopin/.NET/',
    'https://www.lagou.com/zhaopin/WP/',
    'https://www.lagou.com/zhaopin/Java/',
    'https://www.lagou.com/zhaopin/C%2B%2B/',
    'https://www.lagou.com/zhaopin/PHP/',
    'https://www.lagou.com/zhaopin/shujuwajue/',
    'https://www.lagou.com/zhaopin/sousuosuanfa/',
    'https://www.lagou.com/zhaopin/jingzhuntuijian/',
    'https://www.lagou.com/zhaopin/C/',
    'https://www.lagou.com/zhaopin/C%23/',
    'https://www.lagou.com/zhaopin/quanzhangongchengshi/',
    'https://www.lagou.com/zhaopin/Hadoop/',
    'https://www.lagou.com/zhaopin/Python/',
    'https://www.lagou.com/zhaopin/Delphi/',
    'https://www.lagou.com/zhaopin/VB/',
    'https://www.lagou.com/zhaopin/Perl/',
    'https://www.lagou.com/zhaopin/Ruby/',
    'https://www.lagou.com/zhaopin/Node.js/',
    'https://www.lagou.com/zhaopin/go/',
    'https://www.lagou.com/zhaopin/asp/',
    'https://www.lagou.com/zhaopin/shell/',
    'https://www.lagou.com/zhaopin/houduankaifaqita/',
    'https://www.lagou.com/zhaopin/HTML5/',
    'https://www.lagou.com/zhaopin/Android/',
    'https://www.lagou.com/zhaopin/iOS/',
    'https://www.lagou.com/zhaopin/yidongkaifaqita/',
    'https://www.lagou.com/zhaopin/webqianduan/',
    'https://www.lagou.com/zhaopin/Flash/',
    'https://www.lagou.com/zhaopin/html51/',
    'https://www.lagou.com/zhaopin/JavaScript/',
    'https://www.lagou.com/zhaopin/U3D/',
    'https://www.lagou.com/zhaopin/COCOS2D-X/',
    'https://www.lagou.com/zhaopin/qianduankaifaqita/',
    'https://www.lagou.com/zhaopin/shenduxuexi/',
    'https://www.lagou.com/zhaopin/jiqixuexi/',
    'https://www.lagou.com/zhaopin/tuxiangchuli/',
    'https://www.lagou.com/zhaopin/tuxiangshibie/',
    'https://www.lagou.com/zhaopin/yuyinshibie/',
    'https://www.lagou.com/zhaopin/jiqishijue/',
    'https://www.lagou.com/zhaopin/suanfagongchengshi/',
    'https://www.lagou.com/zhaopin/ziranyuyanchuli/',
    'https://www.lagou.com/zhaopin/ceshigongchengshi/',
    'https://www.lagou.com/zhaopin/zidonghuaceshi/',
    'https://www.lagou.com/zhaopin/gongnengceshi/',
    'https://www.lagou.com/zhaopin/xingnengceshi/',
    'https://www.lagou.com/zhaopin/ceshikaifa/',
    'https://www.lagou.com/zhaopin/youxiceshi/',
    'https://www.lagou.com/zhaopin/baiheceshi/',
    'https://www.lagou.com/zhaopin/huiheceshi/',
    'https://www.lagou.com/zhaopin/heiheceshi/',
    'https://www.lagou.com/zhaopin/shoujiceshi/',
    'https://www.lagou.com/zhaopin/yingjianceshi/',
    'https://www.lagou.com/zhaopin/ceshijingli2/',
    'https://www.lagou.com/zhaopin/ceshiqita/',
    'https://www.lagou.com/zhaopin/yunweigongchengshi/',
    'https://www.lagou.com/zhaopin/yunweikaifagongchengshi/',
    'https://www.lagou.com/zhaopin/wangluogongchengshi/',
    'https://www.lagou.com/zhaopin/xitonggongchengshi/',
    'https://www.lagou.com/zhaopin/ITzhichi/',
    'https://www.lagou.com/zhaopin/idc/',
    'https://www.lagou.com/zhaopin/cdn/',
    'https://www.lagou.com/zhaopin/f5/',
    'https://www.lagou.com/zhaopin/xitongguanliyuan/',
    'https://www.lagou.com/zhaopin/bingdufenxi/',
    'https://www.lagou.com/zhaopin/webanquan/',
    'https://www.lagou.com/zhaopin/wangluoanquan/',
    'https://www.lagou.com/zhaopin/xitonganquan/',
    'https://www.lagou.com/zhaopin/yunweijingli/',
    'https://www.lagou.com/zhaopin/yunweiqita/',
    'https://www.lagou.com/zhaopin/MySQL/',
    'https://www.lagou.com/zhaopin/SQLServer/',
    'https://www.lagou.com/zhaopin/Oracle/',
    'https://www.lagou.com/zhaopin/DB2/',
    'https://www.lagou.com/zhaopin/MongoDB/',
    'https://www.lagou.com/zhaopin/etl/',
    'https://www.lagou.com/zhaopin/hive/',
    'https://www.lagou.com/zhaopin/shujucangku/',
    'https://www.lagou.com/zhaopin/dbaqita/',
    'https://www.lagou.com/zhaopin/jishujingli/',
    'https://www.lagou.com/zhaopin/jishuzongjian/',
    'https://www.lagou.com/zhaopin/jiagoushi/',
    'https://www.lagou.com/zhaopin/CTO/',
    'https://www.lagou.com/zhaopin/yunweizongjian/',
    'https://www.lagou.com/zhaopin/jishuhehuoren/',
    'https://www.lagou.com/zhaopin/xiangmuzongjian/',
    'https://www.lagou.com/zhaopin/ceshizongjian/',
    'https://www.lagou.com/zhaopin/anquanzhuanjia/',
    'https://www.lagou.com/zhaopin/gaoduanjishuzhiweiqita/',
    'https://www.lagou.com/zhaopin/xiangmujingli/',
    'https://www.lagou.com/zhaopin/xiangmuzhuli/',
    'https://www.lagou.com/zhaopin/yingjian/',
    'https://www.lagou.com/zhaopin/qianrushi/',
    'https://www.lagou.com/zhaopin/zidonghua/',
    'https://www.lagou.com/zhaopin/danpianji/',
    'https://www.lagou.com/zhaopin/dianlusheji/',
    'https://www.lagou.com/zhaopin/qudongkaifa/',
    'https://www.lagou.com/zhaopin/xitongjicheng/',
    'https://www.lagou.com/zhaopin/fpgakaifa/',
    'https://www.lagou.com/zhaopin/dspkaifa/',
    'https://www.lagou.com/zhaopin/armkaifa/',
    'https://www.lagou.com/zhaopin/pcbgongyi/',
    'https://www.lagou.com/zhaopin/mujusheji/',
    'https://www.lagou.com/zhaopin/rechuandao/',
    'https://www.lagou.com/zhaopin/cailiaogongchengshi/',
    'https://www.lagou.com/zhaopin/jingyigongchengshi/',
    'https://www.lagou.com/zhaopin/shepingongchengshi/',
    'https://www.lagou.com/zhaopin/yingjiankaifaqita/',
    'https://www.lagou.com/zhaopin/shishigongchengshi/',
    'https://www.lagou.com/zhaopin/shouqiangongchengshi/',
    'https://www.lagou.com/zhaopin/shouhougongchengshi/',
    'https://www.lagou.com/zhaopin/bigongchengshi/',
    'https://www.lagou.com/zhaopin/qiyeruanjianqita/',
    'https://www.lagou.com/zhaopin/chanpinjingli1/',
    'https://www.lagou.com/zhaopin/wangyechanpinjingli/',
    'https://www.lagou.com/zhaopin/yidongchanpinjingli/',
    'https://www.lagou.com/zhaopin/chanpinzhuli/',
    'https://www.lagou.com/zhaopin/shujuchanpinjingli/',
    'https://www.lagou.com/zhaopin/dianshangchanpinjingli/',
    'https://www.lagou.com/zhaopin/youxicehua/',
    'https://www.lagou.com/zhaopin/chanpinshixisheng/',
    'https://www.lagou.com/zhaopin/wangyechanpinshejishi/',
    'https://www.lagou.com/zhaopin/wuxianchanpinshejishi/',
    'https://www.lagou.com/zhaopin/chanpinbujingli/',
    'https://www.lagou.com/zhaopin/chanpinzongjian/',
    'https://www.lagou.com/zhaopin/youxizhizuoren/',
    'https://www.lagou.com/zhaopin/shijueshejishi/',
    'https://www.lagou.com/zhaopin/wangyeshejishi/',
    'https://www.lagou.com/zhaopin/Flashshejishi/',
    'https://www.lagou.com/zhaopin/APPshejishi/',
    'https://www.lagou.com/zhaopin/UIshejishi/',
    'https://www.lagou.com/zhaopin/pingmianshejishi/',
    'https://www.lagou.com/zhaopin/meishushejishi%EF%BC%882D3D%EF%BC%89/',
    'https://www.lagou.com/zhaopin/guanggaoshejishi/',
    'https://www.lagou.com/zhaopin/duomeitishejishi/',
    'https://www.lagou.com/zhaopin/yuanhuashi/',
    'https://www.lagou.com/zhaopin/youxitexiao/',
    'https://www.lagou.com/zhaopin/youxijiemianshejishi/',
    'https://www.lagou.com/zhaopin/youxichangjing/',
    'https://www.lagou.com/zhaopin/youxijiaose/',
    'https://www.lagou.com/zhaopin/youxidongzuo/',
    'https://www.lagou.com/zhaopin/jiaohushejishi1/',
    'https://www.lagou.com/zhaopin/wuxianjiaohushejishi/',
    'https://www.lagou.com/zhaopin/wangyejiaohushejishi/',
    'https://www.lagou.com/zhaopin/yingjianjiaohushejishi/',
    'https://www.lagou.com/zhaopin/shujufenxishi/',
    'https://www.lagou.com/zhaopin/yonghuyanjiuyuan/',
    'https://www.lagou.com/zhaopin/youxishuzhicehua/',
    'https://www.lagou.com/zhaopin/shejijinglizhuguan/',
    'https://www.lagou.com/zhaopin/shejizongjian/',
    'https://www.lagou.com/zhaopin/shijueshejijinglizhuguan/',
    'https://www.lagou.com/zhaopin/shijueshejizongjian/',
    'https://www.lagou.com/zhaopin/jiaohushejijinglizhuguan/',
    'https://www.lagou.com/zhaopin/jiaohushejizongjian/',
    'https://www.lagou.com/zhaopin/yonghuyanjiujinglizhuguan/',
    'https://www.lagou.com/zhaopin/yonghuyanjiuzongjian/',
    'https://www.lagou.com/zhaopin/yonghuyunying/',
    'https://www.lagou.com/zhaopin/chanpinyunying/',
    'https://www.lagou.com/zhaopin/shujuyunying/',
    'https://www.lagou.com/zhaopin/neirongyunying/',
    'https://www.lagou.com/zhaopin/huodongyunying/',
    'https://www.lagou.com/zhaopin/shangjiayunying/',
    'https://www.lagou.com/zhaopin/pinleiyunying/',
    'https://www.lagou.com/zhaopin/youxiyunying/',
    'https://www.lagou.com/zhaopin/wangluotuiguang/',
    'https://www.lagou.com/zhaopin/yunyingzhuanyuan/',
    'https://www.lagou.com/zhaopin/wangdianyunying/',
    'https://www.lagou.com/zhaopin/xinmeitiyunying/',
    'https://www.lagou.com/zhaopin/haiwaiyunying/',
    'https://www.lagou.com/zhaopin/yunyingjingli/',
    'https://www.lagou.com/zhaopin/fuzhubian/',
    'https://www.lagou.com/zhaopin/neirongbianji/',
    'https://www.lagou.com/zhaopin/wenancehua/',
    'https://www.lagou.com/zhaopin/jizhe/',
    'https://www.lagou.com/zhaopin/shouqianzixun/',
    'https://www.lagou.com/zhaopin/shouhoukefu/',
    'https://www.lagou.com/zhaopin/taobaokefu/',
    'https://www.lagou.com/zhaopin/kefujingli/',
    'https://www.lagou.com/zhaopin/zhubian/',
    'https://www.lagou.com/zhaopin/yunyingzongjian/',
    'https://www.lagou.com/zhaopin/COO/',
    'https://www.lagou.com/zhaopin/kefuzongjian/',
    'https://www.lagou.com/zhaopin/shichangyingxiao1/',
    'https://www.lagou.com/zhaopin/shichangcehua/',
    'https://www.lagou.com/zhaopin/shichangguwen/',
    'https://www.lagou.com/zhaopin/shichangtuiguang/',
    'https://www.lagou.com/zhaopin/SEO/',
    'https://www.lagou.com/zhaopin/SEM/',
    'https://www.lagou.com/zhaopin/shangwuqudao/',
    'https://www.lagou.com/zhaopin/shangyeshujufenxi/',
    'https://www.lagou.com/zhaopin/huodongcehua/',
    'https://www.lagou.com/zhaopin/wangluoyingxiao/',
    'https://www.lagou.com/zhaopin/haiwaishichang/',
    'https://www.lagou.com/zhaopin/zhengfuguanxi/',
    'https://www.lagou.com/zhaopin/meijiejingli/',
    'https://www.lagou.com/zhaopin/guanggaoxiediao/',
    'https://www.lagou.com/zhaopin/pinpaigongguan/',
    'https://www.lagou.com/zhaopin/xiaoshouzhuanyuan/',
    'https://www.lagou.com/zhaopin/xiaoshoujingli/',
    'https://www.lagou.com/zhaopin/kehudaibiao/',
    'https://www.lagou.com/zhaopin/dakehudaibiao/',
    'https://www.lagou.com/zhaopin/BDjingli/',
    'https://www.lagou.com/zhaopin/shangwuqudao1/',
    'https://www.lagou.com/zhaopin/qudaoxiaoshou/',
    'https://www.lagou.com/zhaopin/dailishangxiaoshou/',
    'https://www.lagou.com/zhaopin/xiaoshouzhuli/',
    'https://www.lagou.com/zhaopin/dianhuaxiaoshou/',
    'https://www.lagou.com/zhaopin/xiaoshouguwen/',
    'https://www.lagou.com/zhaopin/shangpinzhuli/',
    'https://www.lagou.com/zhaopin/wuliu/',
    'https://www.lagou.com/zhaopin/cangchu/',
    'https://www.lagou.com/zhaopin/caigouzhuanyuan/',
    'https://www.lagou.com/zhaopin/caigoujingli/',
    'https://www.lagou.com/zhaopin/shangpinjingli/',
    'https://www.lagou.com/zhaopin/fenxishi/',
    'https://www.lagou.com/zhaopin/touziguwen/',
    'https://www.lagou.com/zhaopin/touzijingli/',
    'https://www.lagou.com/zhaopin/shichangzongjian/',
    'https://www.lagou.com/zhaopin/xiaoshouzongjian/',
    'https://www.lagou.com/zhaopin/shangwuzongjian/',
    'https://www.lagou.com/zhaopin/CMO/',
    'https://www.lagou.com/zhaopin/gongguanzongjian/',
    'https://www.lagou.com/zhaopin/caigouzongjian/',
    'https://www.lagou.com/zhaopin/touzizongjian/',
    'https://www.lagou.com/zhaopin/renliziyuan1/',
    'https://www.lagou.com/zhaopin/zhaopin/',
    'https://www.lagou.com/zhaopin/HRBP/',
    'https://www.lagou.com/zhaopin/renshiHR/',
    'https://www.lagou.com/zhaopin/peixunjingli/',
    'https://www.lagou.com/zhaopin/xinzifulijingli/',
    'https://www.lagou.com/zhaopin/jixiaokaohejingli/',
    'https://www.lagou.com/zhaopin/yuangongguanxi/',
    'https://www.lagou.com/zhaopin/zhuli/',
    'https://www.lagou.com/zhaopin/qiantai/',
    'https://www.lagou.com/zhaopin/xingzheng1/',
    'https://www.lagou.com/zhaopin/zongzhu/',
    'https://www.lagou.com/zhaopin/wenmi/',
    'https://www.lagou.com/zhaopin/kuaiji/',
    'https://www.lagou.com/zhaopin/chuna/',
    'https://www.lagou.com/zhaopin/caiwu1/',
    'https://www.lagou.com/zhaopin/jiesuan/',
    'https://www.lagou.com/zhaopin/shuiwu/',
    'https://www.lagou.com/zhaopin/shenji/',
    'https://www.lagou.com/zhaopin/fengkong/',
    'https://www.lagou.com/zhaopin/fawu2/',
    'https://www.lagou.com/zhaopin/lvshi/',
    'https://www.lagou.com/zhaopin/zhuanli/',
    'https://www.lagou.com/zhaopin/xingzhengzongjianjingli/',
    'https://www.lagou.com/zhaopin/caiwuzongjianjingli/',
    'https://www.lagou.com/zhaopin/HRDHRM/',
    'https://www.lagou.com/zhaopin/CFO/',
    'https://www.lagou.com/zhaopin/ceo/',
    'https://www.lagou.com/zhaopin/jinrongtouzijingli/',
    'https://www.lagou.com/zhaopin/jinrongfenxishi/',
    'https://www.lagou.com/zhaopin/touzizhuli/',
    'https://www.lagou.com/zhaopin/rongzi/',
    'https://www.lagou.com/zhaopin/binggou/',
    'https://www.lagou.com/zhaopin/hangyeyanjiu/',
    'https://www.lagou.com/zhaopin/touzizheguanxi/',
    'https://www.lagou.com/zhaopin/zichanguanli/',
    'https://www.lagou.com/zhaopin/licaiguwen/',
    'https://www.lagou.com/zhaopin/jiaoyiyuan/',
    'https://www.lagou.com/zhaopin/jinrong3fengkong/',
    'https://www.lagou.com/zhaopin/zixinpinggu/',
    'https://www.lagou.com/zhaopin/heguijicha/',
    'https://www.lagou.com/zhaopin/jinronglvshi/',
    'https://www.lagou.com/zhaopin/jinrongshenji/',
    'https://www.lagou.com/zhaopin/jinrongfawu/',
    'https://www.lagou.com/zhaopin/jinrongkuaiji/',
    'https://www.lagou.com/zhaopin/jinrongqingsuan/',
    'https://www.lagou.com/zhaopin/jinrongtouzizongjian/',
    'https://www.lagou.com/zhaopin/rongzizongjian/',
    'https://www.lagou.com/zhaopin/binggouzongjian/',
    'https://www.lagou.com/zhaopin/fengxiankongzhizongjian/',
    'https://www.lagou.com/zhaopin/zongcaifuzongcai/'
]



class GetHeaders():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
       ]

    def getHeaders(self):
        headers={
         "Accept": "application/json, text/javascript, */*; q=0.01",
         "Accept-Encoding": "gzip, deflate, br",
         "Accept-Language": "zh-CN,zh;q=0.8",
         "Host": "www.xicidaili.com",
         "Connection": "keep-alive",
         "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWFmOWI4ZWZlNjFmZjk2NmMwMzJlMWExMDYzZjViM2M0BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXh0SVduY1MvN3ZoR0xVbVJnbU8zM2RkdlNvSm9MM1FodTFsSGdjOXV6ZDA9BjsARg%3D%3D--8ece30259597c8d38fd952268f88d7962412607f; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1551335565; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1551409989",
         "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
         'User-Agent':random.choice(self.user_agent_list),
         'Referer':"https://www.xicidaili.com/wt/"
        }
        return headers
