![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSfK19QQJTeEkm7iaRicsbNhZic1FafyNLZfJFxg91eXokCwiauk1SI7IjWfx8Pq92KZzibiconLoVoy8NIhBVxO32EWTnyMqUbNradpU/0?wx_fmt=jpeg)

#  SemiAnalysis的创始人：AI到底赚不赚钱？为什么说内存是这轮最硬的主线？（视频+原文解读）

原创  AI未来课代表  AI未来课代表  [ AI未来课代表 ](javascript:void\(0\);)

_2026年07月13日 16:41_ __ _ _ _ _ _ 上海  _

在小说阅读器读本章

去阅读

课代表

本期是WisdomTree播客《The Next Big Thing》首期，嘉宾Dylan
Patel是半导体与AI研究机构SemiAnalysis的创始人。这66分钟，他其实在回答几个躲不开的问题——  
1\. 天天有人喊AI是泡沫，可Anthropic到底赚没赚到钱？  
2\. 为什么说内存是这轮最硬的投资主线，逼得明年iPhone都得涨价？  
3\. 都说电力是AI的终极瓶颈，他凭什么说"它也不是瓶颈"？  
整理成中文七个话题，分享给同样想看懂AI基建这盘棋的你。

📖 阅读说明 ｜  本文正文是 **本期访谈内容** ；凡涉及外部资料的对照、背景或另一种说法，一律放在这样的 **灰色虚线框** 里，并标注
**【外部分析 · 非本次访谈】+ 来源 + 日期** ，请勿与Dylan本期的原话混为一谈。

⚡ 30秒读懂

01\.  AI到底赚不赚钱？Dylan的答案是  「已经在印钞」
——Anthropic四月、五月已盈利且自由现金流为正，经常性收入破500亿美元ARR、毛利率70%+。

02\.  硬币另一面：SemiAnalysis自己一年AI支出从去年11月的不到10万美元，飙到今天的  1100万美元
（峰值1400万），一家90人公司，AI花费已是薪资的三分之一还多。

03\.  省钱的反直觉真相：  用最新最贵的模型，反而最便宜  。同质量下AI成本每年降约60倍，DeepSeek两年内比GPT-4便宜了600倍。

04\.  内存超级周期是这轮最硬的主线
——产能每年只增20–30%，需求却在翻倍，价格已涨约4倍、还要再涨2–3倍。代价：明年iPhone、MacBook必须涨价。

05\.  CPU从「三年没人提」到「今年满世界喊」，但Dylan泼冷水：  卖方把CPU/GPU比例吹过头了
，大头的钱仍流向AI算力和内存，这只是补涨小周期。

06\.  电力才是终极瓶颈——  但「也不是瓶颈，看你愿意疯到什么程度」
：把卡车发动机改成发电机堆几百台，两年后光伏+储能比燃气还便宜，再极端就是把数据中心发射到太空。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSdky1dj1JSdzTO57UVIt8QiagISVoX57SGgM6DibLy2Eb73AkbVDndJLkibiajTMZM8DNKoQaX3FfAnicCG0TiaE66ljgZwjoZzdBDZA/640?wx_fmt=jpeg&from=appmsg)

贯穿全篇的一把尺子 ｜  Dylan判断供应链任一环节能不能涨、涨多少，反复用同一套框架： **需求传导率**
（AI每花1美元，落到这个环节是1分钱还是5分钱）× **市场结构** （垄断、寡头还是大宗商品）× **价格弹性**
（TSMC只涨5–10%，内存能上下摆2–3倍）。一句话记住这期：  几乎所有东西都在缺货，问题不再是能不能拿到货，而是要等多久。

01\.

从「网上发癫」到90人研究帝国：SemiAnalysis是怎么炼成的

要听懂后面所有判断，得先知道Dylan是谁——一个把技术、供应链、金融、地缘揉在一起看的人，和一家靠5000万美元捐赠硬件天天跑基准测试、连黄仁勋都得在台上回应的研究机构。

一个从十几岁就在论坛「发癫」的人

SemiAnalysis的起点，用Dylan自己的话说就是「在网上发癫」。他十几岁出头就在发关于芯片、手机SOC、屏幕的帖子，还没拥有第一部智能手机就已经痴迷；
**12岁**
就在管理Android、Apple、Intel、NVIDIA、AMD相关的论坛和Reddit板块。「我一直是个爱发帖的人」——现在他手下90人的公司里，市场部同事求他别再回复网上那些路人，但他就是有那种「一有人批评我就非回不可」的冲动。

他在美国Georgia州农村的一家汽车旅馆里长大，父母开旅馆、后来还开加油站，从小就懂生意、对「东西是怎么造出来的」有种天分。做过两年quant，2020年幻灭辞职——「钱是能赚到，但真没那么光鲜」——然后用真名在自己搭的WordPress上写技术、商业、金融、供应链混在一起的东西。

成名作很能说明他的方法论：Huawei被禁用TSMC时，美国市场都以为赢家是Qualcomm，他第一篇文章却判断真正的大赢家是台湾的
**MediaTek** ——因为地缘上，刚被美国封了的中国，更愿意从台湾公司买而不是美国公司。  「这种拐点，我总能在华尔街任何对冲基金之前先喊出来。」

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSfMF0QRtDfldFlLRYBd1RycyNsXUQ1PpdNA7PrI7fbXM4OYkzq947YSaaYbdOPkjuDwGQkngUJDgjo7KnjQ6HOrGBwiauIv9CYo/640?wx_fmt=jpeg&from=appmsg)

四年跑160场大会，滚出一支「疯狂人才密度」的队伍

有四年时间他满世界跑，一年参加 **40场大会**
，从NeurIPS、ICML这样的顶级AI研究会议，一直跑到只有300人、除了5个人全说日语的半导体化学品原料小会。「一个会去三次，你就懂那套行话、认识那些人了。」把整个产业链上上下下跑遍，哪儿出现拐点，他立刻知道它在供应链和金融层面会往哪走。团队也像雪球一样越滚越大：

时间  |  团队规模  
---|---  
2023 → 2024  |  2 → 7人  
2024 → 2025初  |  7 → 20人  
2025 → 2026  |  20 → 60人  
今年  |  90人（一年新增30）  
  
人才密度是他最得意的地方：来自ASML、Applied Materials、LAM
Research这些晶圆设备公司，一直到Intel、TSMC、NVIDIA、Microsoft、Amazon，还有在OpenAI做过模型、在Tesla做过FSD、在Cohere干过的人——甚至有个成员在哈萨克斯坦建过一座发电厂。「大概一半人是在这个行业做过工程的，另一半要么是前对冲基金的，要么就是我在Twitter、Discord上发现的、超有热情的聪明人。」

从「内存是最大输家」到卖数据服务

2022年Substack越做越大后他开始招人，头两个是Discord上认识多年的技术朋友，第三个Myron来自对冲基金。招Myron的方式很「Dylan」：2023年初他发了一篇文章，判断
**「内存是AI浪潮里最大的输家」**
——因为AI服务器用的内存比普通服务器少得多（普通服务器的物料成本里约一半是内存，AI服务器里这个比例低得多，部分因为NVIDIA的利润率实在太高），然后在付费板块末尾附了一句「我在招人」。Myron就这么找上门，成了公司第一个对冲基金背景的雇员（前两个都是技术出身）。

他一加入，团队就开始做各种模型，把业务从「写newsletter」转向 **卖信息服务、卖报告、卖数据集** ——雪球从此滚下山坡。
有意思的是，这个「内存是输家」的判断后来彻底反转  ：NVIDIA下一代芯片的内存用量暴增，内存从「最大输家」一路变成了本文第4章的「超级周期主角」。

$50M硬件实验室，和黄仁勋「藏了后手」的名场面

SemiAnalysis有一批工程师专做开源基准测试。OpenAI、Microsoft、Amazon、Google、CoreWeave、Nebius、Crusoe、Oracle等云厂商累计捐了
**超过5000万美元** 的硬件——8种GPU（H100、H200、Blackwell、AMD各款）外加Google TPU、Amazon
Trainium。他们每晚都在最新的CUDA、PyTorch、vLLM、SGLang上跑一遍基准，覆盖「token吐得多快 ×
性价比多高」的整条曲线。这套东西叫 **InferenceX** 。

名场面就出在这里。Blackwell发布时，黄仁勋声称性能提升 **25倍**
，没人信——Dylan当时觉得顶多15–20倍，还有一堆人喊「也就3倍」。结果InferenceX实测：在DeepSeek
V3上，Blackwell在某些区间比Hopper快了整整 **30倍**
。Dylan拿到结果立刻给黄仁勋发邮件认错：「你2024年说25倍大家都喷你，连我也喷了，但我错了，你其实是留了后手。」

他没想到黄仁勋会把这段搬上GTC舞台。5.5万人看直播、2万人在场馆里，黄仁勋当众点名Dylan，花了整整5分钟讲「Dylan说我藏着掖着，但我没有」——
讲他的时间比讲全场任何人都长。  SemiAnalysis还做了一条印着「Inference
King」的WWE冠军腰带，寄给NVIDIA、AMD、SGLang、vLLM这些合作方，黄仁勋直接把腰带举上了PPT。

一个从论坛发帖起家的人，如今成了连全球最大公司CEO都要在台上回应的「基准裁判」。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSd4QyWM1xPWYNP14WYh1LLZK1ptyHZDdX4OUFiaG3p8hc2ZibOfvicZwmEc45Oa9apFuF4nK9RW8AgmG79v8ncrFicnZwK9KD1iaNGo/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSfau1s4YhTp1seMyG8fNiarib9AjuxVFk4m6LZZEmSfDX2VJHJQvDeDfvMLwxW1Gv9kjXxIliaSBiaIvBC1licp5BzCUmnXHGvQkZ7w/640?wx_fmt=jpeg&from=appmsg)

02\.

AI到底赚不赚钱？一面在印钞，一面在疯狂烧钱

投资者最大的疑问就是ROI：这些公司到底有没有从AI上赚到钱？Dylan把它拆成硬币的两面——卖AI的人已经在印钞，买AI的人则在经历支出的指数级爆炸。

卖AI的一面：Anthropic已经在「印钞」

这是Dylan甩出的第一个、也是最重要的事实：  Anthropic在Q2是盈利的，自由现金流为正。
不是画饼——四月关账时就已经盈利且自由现金流为正，五月同样，六月看起来也一样（还没完全关账）。三个月里至少两个月做到了盈利 + 自由现金流为正。

Anthropic指标  |  数值  
---|---  
经常性收入（ARR）  |  突破500亿美元  
毛利率  |  70%+  
盈利 / 自由现金流  |  Q2已转正（4、5月确认）  
  
其他公司还没到「印钞」的程度，但都在接近：随着Codex采用度上升，OpenAI的收入也开始加速上扬。「这些公司都在变得越来越赚钱。」

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSfHULFvrPXU0Pf2GrpHhB1qs2K0rBGvUtxh4ia8hlboCwv3qotglBh7ml2E05wMQjpnkegym2E3JibmZ6pOzcmWxvYiaYjcjRNpZ8/640?wx_fmt=jpeg&from=appmsg)

买AI的一面：Dylan自曝家底，一年烧掉1100万

他自创了一个词——不是ARR（年度经常性收入），而是 **ARS（Annual Reoccurring Spend，年度经常性支出）**
。这条曲线堪称恐怖：

时间  |  年度AI支出（ARS）  
---|---  
去年11月（Claude Code之前）  |  < 10万美元  
今年1月底  |  400万美元  
今天  |  约1100万美元（峰值1400万）  
  
去年11月还只是给每个员工开一份200美元的ChatGPT订阅，总共不到10万；Claude Code随Opus
4.5、4.6起飞后，1月底冲到400万，今天约 **1100万美元** ——这还是一家只有90人的公司。  AI花费已经是员工薪资的三分之一还多
，年底可能到「一半对一半」。

📌【外部分析 · 非本次访谈】  来源：Dylan Patel做客《Invest Like the Best》播客 · 2026-04-23 ·
**性质：与本期交叉验证**  
他当时说SemiAnalysis的年化AI支出约 **700万美元**
、占薪资25%+；仅两三个月后的本期就更新到约1100万、峰值1400万、占比升到三分之一以上——正好印证他反复强调的「token需求几乎无上限」。

更值得玩味的两个细节：一个年薪30万美元的好开发者，花在AI上的钱正在 **逼近薪资的1:1** ；而SemiAnalysis内部花钱最多的，反而是
**不会写代码的人** ——他们只管告诉模型自己要什么，然后不断迭代直到拿到结果。

划重点 ｜  很多公司Q1、Q2就烧穿了全年AI预算，接下来是砍AI还是砍别处？Dylan观察到多数公司在砍其他SaaS、甚至裁员来保AI。
「压制AI使用的公司，会在生产力上被远远甩下。」

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSdMYXwZibmd5HBvJdSVQuTsUso5iaHxkMYKNdlKT2Q7ic4MHtaj3wAbymzAy6ON2DiajI90F67ia2OhxNmoXKd3M20Q2ZYDMYyS4Zqo/640?wx_fmt=jpeg&from=appmsg)

课代表锐评：
「AI是不是泡沫」这个问题，Dylan用一个最难反驳的事实回应——一家头部模型公司已经月度盈利、自由现金流为正、毛利率70%+。泡沫论者该换个问法了：不是「有没有价值」，而是「价值分给谁、每个环节能吃到多少」。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSeMRzMqdd1PCeoubVUcruXUQy6H9wzSrmQkHTelelibXDiaKIF83z3iahCEdsEAic1bjndN6xlOloD31xGyf5VQU3T89hQEwbrFsTM/640?wx_fmt=jpeg&from=appmsg)

03\.

省钱悖论：想降本，就得用最新、最贵的模型

很多人以为省钱=换便宜模型，Dylan说这是个误解。关键要先把AI工作负载分成两类，它们的降本逻辑正好相反。

第一类：集成进流程——达标即止，等它变便宜

比如「客户发来一份文档，我用模型检查其中某些内容」。这种场景只需要达到某个质量门槛，一旦达标就可以停止追求更强的模型，转而通过等更便宜的新模型来降本。这里的降本引擎快得惊人——
同一质量水平，AI成本每年大约降60倍。

当年大家对DeepSeek那么震惊，就是因为 **DeepSeek V3比GPT-4便宜了600倍**
——而它是在GPT-4发布约两年后出现的。按「每年降60倍」算两年该是3600倍，实际落在600倍，反正每年降本的幅度就在这条曲线上。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSd21KLkuq77iaQSUmoK6lUHpO5ZsTzDjmiaw63h0hWJmyBGJypZYamyBEU67AdXaevN4FDucJ4ia7VKhfLbhBmFUgyPdTB0J251u4/640?wx_fmt=jpeg&from=appmsg)

第二类：AI助手 / agentic——降本靠用最新模型

如果你在做日常智力工作，让模型帮你查、帮你想，成本优化的关键  恰恰不是切到更便宜的模型，而是用最新的模型  。因为新模型更聪明、更省token：

同一个任务  |  消耗  
---|---  
Claude 4.6 Opus  |  10万token + 来回好几轮 + 我10分钟  
Claude 4.8 Opus  |  2.5万token + 一个来回  
  
生成的token更少、我花的时间更少， **总成本反而更低**
。有意思的是升级后的规律：4.6换到4.7、4.7换到4.8，成本都是先跌一周左右，然后又飙回去——因为大家发现「原来的活干完了，那就再多干点」。所以必须把生产力和成本放在一起衡量。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSe2XQ0uVvIUjvTCCt4HP5Sg6cDdxiaiaSYkPlVia7sTaPIHdice8KvZvSCVzPvkNgVDfXwMsqlBVoNybrUQqzYdRDrvYwc445IkM6E/640?wx_fmt=jpeg&from=appmsg)

为什么SemiAnalysis仍是「majority Anthropic shop」

在AI助手这个场景里，token效率至关重要——这也是  Anthropic一直压OpenAI一头的原因：它的模型更省token。
OpenAI在顶尖科学、数学、代码的边缘任务上，往往能做Anthropic做不到的事，但要花3倍时间、4倍token，人机反馈循环也更慢，用户感知反而更差。

他举了个绝妙的类比：「你有四个小时做一个任务，是给模型发一次调用让它自己跑四小时好，还是分四次调用来回沟通好？」在人在环路（human in the
loop）的反馈循环里，Anthropic因为更省token反而快得多、好得多。所以大多数任务留给Claude
Code，只有那些「让它跑一整晚」的任务才交给OpenAI Codex。

在助手场景，最贵的模型往往是最便宜的选择——因为你买的不是token，是「一次做对」。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSe7TOGicz5kQUT7rRJXwWb2fAaQLh1b3wQoC2hG3YKG0tLIWqAK5t2iaAtQ3xrSJc0UK7nROHYkg0hjC8BjiaShYrVf2VkT1y34vU/640?wx_fmt=jpeg&from=appmsg)

04\.

内存超级周期：这轮最硬的投资主线

内存过去40年一直是典型的大宗商品：18–24个月上行、再18–24个月下行，周而复始。Dylan说这次不一样，而且他从2024年就喊对了这一波。

不是老周期：这次是「总支出翻倍、还要再翻倍」

周期不会消失，我们现在正处在一个「上行猛得离谱」的超级周期里。但关键区别在于：过去上行周期是终端市场涨50%，像内存这种有定价权、弹性大的大宗商品，股票能翻两三倍。
这次不是涨50%的事——仅过去几年，总支出已经翻了一倍，而且还要再翻一倍。

内存价格已经涨了大约4倍，接下来除了产能增长之外，价格还要再涨 **2到3倍** ；毛利率正朝着一个大宗商品本不该有的水平—— **85%到90%**
——狂奔。当然到顶之后又会腰斩回70多甚至更低，所以本质是「疯狂拉升，再回落」的高波动。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXScR20OTqeeR9iaJ3eiboDTJmcc0eX4IM8ugAJ5sqB4I0DsX6ic5aXVWjEdsuV2rB9VUHNXT5Y2GuEhjNcv1dlWcBc2MTuyASnQIk8/640?wx_fmt=jpeg&from=appmsg)

根因：reasoning引爆了KV cache

为什么内存需求会失控？Dylan把技术根因讲透了。做推理（inference）时，每生成一个token，都要把所有权重读进芯片，同时读进上下文（这个上下文缓存就叫
**KV cache** ）。从权重这边看，不管上下文是1000还是10万token，内存压力都一样；但从KV cache这边看——
读1000个token和读10万个token，内存需求差得离谱，而计算量几乎不变。

2024年12月，OpenAI发布o1（第一个reasoning模型），SemiAnalysis当即写下判断：pre-training scaling
law正在让位给reasoning scaling law，而reasoning会让KV cache爆炸式增长， **内存将是最大的赢家**
。到2026年1月，市场问「内存涨了50%是不是到顶了」，他们又发了一篇：「不不不，你们没搞懂——产能未来三年每年只增20–30%，需求却在翻倍，价格只能一直涨，直到把扛不住的用户挤出去。」

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSe0N2TZ5fohcgOykegRBoGS9h3WnElxlbdibgyUqxnw5w7DZ2WN5BeoiactY10TShLhwsU9qGX2PGb4gWqhKwZAnUCLUkwF58vdQ/640?wx_fmt=jpeg&from=appmsg)

代价：明年iPhone、MacBook必须涨价

价格一直涨，扛不住的用户就被挤出市场——智能手机、笔记本因为成本涨太多，会把内存产能全部让给AI。目前一些中低端中国手机厂商（如小米）出货已经
**下降40%** ，但高端市场还没受影响。Dylan判断：  明年iPhone、MacBook价格必须上涨
——现在涨100美元市场没啥反应，但内存会一直贵下去直到「AI吃饱」，所以手机涨价不会只涨100，得涨好几百美元，直到达到一个新的平衡点。

这里也体现了框架里的「弹性」差异：TSMC定价没弹性（对客户公道、讲长期，只涨5–10%），而内存是大宗商品，靠现货和合约市场调节，能上下摆2–3倍。同样的AI需求传导到不同环节，价格反应天差地别。

📌【外部分析 · 非本次访谈】  来源：Dylan Patel做客《Invest Like the Best》播客 · 2026-04-23 ·
**性质：背景补充**  
他当时就点过AI的三大结构性供给瓶颈—— **HBM内存、逻辑芯片、EUV光刻**
，判断会持续2–3年。本期他把「内存」这一条单独拎出来，讲透了背后的量价机制。

内存的短缺不是短期的，是要持续好几年的结构性短缺——这是Dylan押得最重的一注。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXScSuH6L76icibEBPHGM392vabqvGfI4y4gXULI1MnlAic6jUjzBAuE8y7oHfiaoyDCU5PEAVoCj3czkKM6pXicoic21ibZvq2OByl1NBc/640?wx_fmt=jpeg&from=appmsg)

05\.

CPU卷土重来——但别被卖方带偏

AI爆发的头三年，几乎没人提CPU；今年却满世界都在喊CPU。SemiAnalysis是最早点出这个拐点的，但Dylan也第一个出来泼冷水。

需求为什么起来：RL和agentic都在吃CPU

去年11月，OpenAI和Anthropic开始跟Amazon、Google、Microsoft谈，把它们机队里的CPU买下来或租下来——CPU需求从此一路往上拐。原因有两条：

1 ｜  **pre-training → 强化学习（RL）**
：RL要让模型生成推理链或合成数据，再丢进一个环境去校验——跑代码单元测试、模拟网站沙盒、模拟工程系统。这些环境校验需要大量CPU。

2 ｜  **chat → agentic** ：模型不停发tool
call（搜索、查数据库、问Python解释器、写代码编译部署），必须跟真实世界打交道，循环里的CPU越来越多。全球GitHub
commits同比翻了好几倍，大量代码被生成并部署到CPU上。

划重点 ｜  关键的转变是：以前是 **人** 跟模型交互——模型给个回复，我读完、复制粘贴到别处就完事，CPU闲着也无所谓；现在是
**模型自己跟互联网世界交互**
，每一次搜索、查数据库、调Python解释器验证、编译并部署代码，都是CPU在循环里来回跑。而部署出去的又多是网页爬虫、分析引擎、业务流程自动化这类「标准代码」，不挑最快的核、性价比核就够用——这就是CPU需求拐点的真正来源。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSePkbicnCfPBvGkUabta5ibI7A06Ms9HqnekricZ2XaLqusgN8S4alA7SoHibtlYeUUH4anhO5k89KNOiaRK0RPLtZMoI14WV3ksp5U/640?wx_fmt=jpeg&from=appmsg)

格局：从Intel/AMD双雄到五方混战，人人都能提价

两年前CPU市场还是Intel + AMD的天下，现在变成了五方混战——但奇特的是，Intel、AMD居然都还能 **提价** ：

玩家  |  看点  
---|---  
Amazon（Graviton）  |  领头羊，造出来是租不是卖，利润率惊人，订单大增  
NVIDIA（Vera）  |  从只卖搭配GPU到单独卖CPU，指引200亿美元营收  
ARM  |  新进入者，股价一路飙涨  
Intel / AMD  |  竞争中竟仍能提价，需求大涨  
  
要快核还是多核？同样是agentic，CPU需求分两种

先记一个CPU架构的取舍：把核做大一倍（核数减半），单核性能只提升约50%、而非翻倍。所以NVIDIA
Vera不到100核、但每核更快，AMD旗舰256核、但单核弱。到底该选哪种，取决于工作负载——而agentic其实分成两种截然不同的情况。

**第一种：算力会卡住等CPU。**
模型跑完，把结果交给CPU处理、自己在旁边干等——比如等一段代码在沙盒里跑完才能继续。这时几万美元的AI算力被卡住空转，代价极高，所以你宁愿要「核数少一半、但单核快50%」的CPU，让这一个任务尽快跑完。
这正是NVIDIA Vera的定位。

**第二种：算力不会浪费。**
我拿到回复去实施时，模型的算力立刻转去服务成千上万的其他用户——算力没闲着。这时CPU慢一点无所谓，只要核多、够便宜就行，Amazon
Graviton、AMD正合适。还有「部署AI生成的代码」这一路：全球GitHub commits同比 **翻了好几倍**
（不是涨10%、50%，是翻几倍），海量代码被生成、部署，跑的多是网页爬虫、分析引擎、业务自动化这类标准代码，用性价比核就够。
所以这是一条连续谱：NVIDIA站「最快单核」一端，AMD、Amazon、ARM站「多核便宜」一端。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSdSdhmLJkVvH2iaRygib2enuZQHrgdhGsTNSmU4zV8zeZY8qBicwHcvREI3Tb3DTNKicUQuDiby81GTTB71HSSuNh56jWQUSAFsC8L8/640?wx_fmt=jpeg&from=appmsg)

泼冷水：卖方把CPU/GPU比例吹过头了

自从SemiAnalysis点出这个拐点，ARM、Intel、NVIDIA、AMD的股票都暴涨。但Dylan说，那些「根本不懂技术的卖方分析师开始瞎编」——把CPU/GPU比例吹到「CPU比AI算力还占大头」的程度，
这是错的。  算笔账就明白：一颗满配Blackwell
5万多美元，按1:1配CPU也就5000美元——要卖3000亿到5000亿美元的Blackwell，只能带出300亿到500亿美元的CPU。

大头的钱仍然流向AI算力和内存。这轮CPU的真相是 **「补涨 + 比例修正」的小周期** ：过去三年出货了上千万颗GPU和AI
ASIC，基本都没配够CPU，现在是一次巨大的补涨加上比例本身上移；等把积压的缺口补齐，就只剩增量、进入稳态。  不是CPU需求会永远超过AI芯片。

CPU确实被低估过、现在定价更合理了——但把它当成下一个GPU来炒，就是被卖方带偏了。

课代表锐评：
这一章是整期最有「卖方vs买方研究」分野的地方——同一个CPU热点，卖方讲成长故事，Dylan用一颗芯片的美元拆分把叙事拉回地面。判断一个主题时，先问「每1美元AI支出到底落到它头上多少」，比听增速百分比靠谱得多。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSeEic3sNnz4cny3sbU6lb7cjuZ734xyZrzTpZKTc5QOHNNf10ias8atRNl91Msu6WjWbflq0AFWGZwrica3BNUaWBNHwj2PNSC2G8/640?wx_fmt=jpeg&from=appmsg)

06\.

光vs铜：市场对CPO太亢奋了

网络是这轮增速最快的环节，但Dylan在最热门的CPO（共封装光学）上给出了一个明确的反共识判断。

网络价值量在飙升

随着模型越来越大、集群越来越大，网络的增速比任何环节都快。在AI芯片相关支出里，网络占比正从
**不到10%涨到10%以上；到了CPO时代能到20%–30%** 。电信光（像Sienna股价一直飙）、data
com（芯片到芯片，铜和光并存）都在猛涨。

反共识：CPO要到2029才真正放量

CPO现在大家都认，但Dylan说「市场有点过于亢奋了」。他的时间表和主流不一样：

时间  |  CPO进度（Dylan判断）  
---|---  
2027  |  不可能落地  
2028年末  |  才开始起步  
2029  |  才是大规模放量的关键年  
  
原因是制造：产能、良率、芯片设计都没就绪，极难量产。所以大家能用铜就尽量用铜—— **Ruben全铜、Feynman（Ruben、Ruben
Ultra之后的下一代GPU）仍是铜**
，而Ruben现在都还没开始出货。交换机上的CPO会比GPU/ASIC更早，但就算不上CPO，集群越大每颗GPU需要的光模块和有源电缆也越多。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSfQGmSxuTria0GvbiaU6GafwS7t9oVDvYmofUJoCD9xM9JKw7qswCWribobVKFrfzMrkIJBN1O2Qr0axLKAOZ9JQtbzE3MdOItFPE/640?wx_fmt=jpeg&from=appmsg)

中期押注：看多铜 + 非CPO光模块，看空CPO

SemiAnalysis周一刚给机构订户发了一份note：技术上CPO终会到来、铜最终会被取代，但
中期维度上，他们非常看多铜和非CPO光模块、反而看空CPO  ——因为看到下游一些芯片延期（Feynman没全面上CPO）。做背板连接器和电缆的
**Amphenol** 这类铜相关公司，未来几年表现会比之前预期好很多（此前市场以为CPO会更早放量，如今被往后推了）。

为什么铜这么顽固？  归根到底，集成光器件比走电信号贵太多
——只有当你不得不走电、又走不了那么远时，才需要加中继器或上光。而铜产业本身还在大量创新，反过来又把CPO往后推。所以「能用铜就用铜」不是保守，是一笔实打实的成本账。SemiAnalysis跟WisdomTree一起做的，正是给「CPO光模块
/ 非CPO光模块 / 传统光收发 / 铜连接」各自该占多少权重做出判断。

光模块是「你今天闭上眼、五年后睁开会大得多」的赢家，但中间的局部错位，正是研究能赚钱的地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSfpZDAK8uQJmUAiafes5pXPtFK4iaf5dYSyNqbPIF0Xdb3r4Fcu4BVkbEYLHuz07Zpvl2EN5EVI26yOpNpOML1hH4KxiaoFIoIzSo/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSdbyuiaxWwSDS3xbricURhuAOjicSRwiabmPWdVfaibc0M42vjT2hCPlB8xhwR9ib0GTEumk1KUjObRlloLmYzv0ic8Au5HZyxmyeKW1s/640?wx_fmt=jpeg&from=appmsg)

07\.

电力：终极瓶颈，也「不是瓶颈」

聊完模型、GPU、CPU、内存、网络，绕不开每个数据中心里那头「房间里的大象」——电从哪来。而SemiAnalysis最大的研究板块，恰恰就是它。

数据中心增长曲线，和三段式拆解

今年部署 **20吉瓦（GW）** 数据中心，明年30GW（+50%），后年50GW。三大制约按难度排： **能源 > 政治 > 施工许可 **
。而能源又能拆成三段，各有各的机会与难处：

1 ｜ 发电  ：电网发电量在增，同时出现「专门为数据中心发电」的大趋势。

2 ｜ 输电  ： **最难看好** ——监管政治阻力大，本地公用事业垄断，建一条线成本要摊给所有用户。

3 ｜ 转换  ：把电网的电转成芯片能用的形态，一整条精彩的供应链（下文详述）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXSdnibGqoX92q7ibfDZpLOvcJl0KbFsdEEXS1YsecoDnMJ8Jq2mqwOpSpic7APEiabzhQ0pmViaZIJktISicxw7YPJzjicfVV2BVJ1arGs/640?wx_fmt=jpeg&from=appmsg)

表后自建电站大爆发：把卡车发动机改成发电机

最有意思的是「表后自建电站」（behind the meter）。Dylan预计再过几年，  数据中心新增用电的一半将在场内自发，而不是从电网输入。
主力是天然气（GE
Vernova、Mitsubishi、Siemens的双联合循环机组），但更疯的是——人们把火车、轮船、卡车的发动机拿来改烧天然气、反向驱动电动机发电。

美国一年能造上百万台往复式发动机，把柴油改成烧气很容易，就算继续烧柴油也行。 **10GW以上的数据中心会用这种方式来建**
：一个站堆上几百台，从汽修店雇一批机修工整天维护，中间配电池缓冲负载波动。审批仍有博弈（空气许可、天然气管道），Oracle的数据中心就遇到过。「很多人说这也太恶心、太不可靠了，但确实有人在这么干，而且它真能跑。」

再往远看是一条完整的谱系：约两年后 **光伏 + 储能会比燃气还便宜**
（得益于中国的制造能力和补贴），但要看你要几个9的可靠性——够撑一夜便宜，够撑连续三天下雨就贵了；最极端的是 **太空数据中心**
，连电池都不用，装块太阳能板扔上去就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Hl6n61hiaXScE63eiaymrrE7yYichPL0TWUyAGea7QK0D5RsHz6u3VE3J7tnfCdK9ibU71cYkSSAxb9VGThzuZIftLQ3Yo96peDGWFFvnrEMPao/640?wx_fmt=jpeg&from=appmsg)

SemiAnalysis最大的板块，竟不是半导体

你可能以为一家叫SemiAnalysis的公司，最大的数据集是半导体——其实是 **数据中心 + 能源 + 工业** （内部戏称DEI
team，Jeremy带队）。他们追踪每一个数据中心、每一座发电厂，能算出哪个项目延期、哪家公司这个季度有多少数据中心上线——「这是行业里没人能做到的事」。Google想知道Meta能部署多少、Meta想知道OpenAI，所有投资人都在盯。

而且这是个 **极度分散**
的市场：内存就3家、设备就几家，但数据中心/能源有几百家公司做着各种零碎部件，几十家在建数据中心，遍布台湾、日本、韩国——「散户根本不容易接触到」。转换环节同样精彩：IGBT、碳化硅、GaN氮化镓MOSFET，12V→54V→800V直流转换，固态变压器，UPS/蓄电池/超级电容平滑「脏电→干净电」。（NVIDIA把Kyber往后推、Ruben
Ultra Kyber不再上800V，供应链节奏也随之后移。）

越往供应链深处走，越是一堆不起眼、却真会缺货的小环节。Dylan举例：有好几个月他们一直在聊 **PCB钻头** （给电路板打孔用的钻头）、PCB上贴的
**铜箔** ，还有 **MLCC片式电容** ——这些环节同样会供需错位、股价大涨，但相关公司散落在台湾、日本、韩国上市，  散户根本接触不到。
「我们平时聊得多的都是内存、CPU、数据中心这些大环节，但真正深入供应链，会发现局部的痛点非常小、又非常多。」

「数据中心会继续是某种瓶颈，但也不会真成瓶颈——取决于你愿意疯到什么程度。」

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSccbkoRrS4cRueL0X7veDWqA4RyNeLbGNoZPVHshno2rQqSkicr48uvblMttqUJeC5p4jV7k3scMY6xPg9kxdKsROyZicySkTta0/640?wx_fmt=jpeg&from=appmsg)

08\.

课代表总结：3个不该被噪音淹没的判断

数字和公司名很多，但真正值得记下来的，是它们背后的3个判断。

判断一 · ROI之争已经结束，战场转向「谁分到钱」

当一家头部模型公司已经月度盈利、自由现金流为正、毛利率70%+，同时连一家90人研究机构自己都愿意一年掏1100万买token，
「AI有没有价值」这个问题就已经被事实回答了。  接下来真正的分歧，是需求会怎样传导——从模型一层层流向内存、CPU、光、电，每个环节能吃到多少。

泡沫论者该换个问法了。

判断二 · 用一把尺子量所有环节，别追单个热点

内存为什么最硬、CPU为什么被高估、CPO为什么被提前炒作——答案都出自同一把尺子： **需求传导率 × 市场结构 × 价格弹性**
。内存三者全占（需求翻倍、寡头、大宗商品弹性），所以是超级周期；CPU传导率有限（每10万美元GPU只带5000美元CPU），所以只是补涨小周期。
同样喊「缺货」，能不能涨、涨多久，得用这把尺子量，而不是听增速百分比。

卖方讲故事，买方研究拆美元。

判断三 · 瓶颈都是暂时的，就看愿意多「疯」

这期最反直觉的一句话是「电力是瓶颈，也不是瓶颈」。当解法可以疯到「把卡车发动机改成发电机堆几百台」「把数据中心发射到太空」，
真正的约束就不再是物理，而是「你愿意为算力付出多难看的代价」。  这也解释了为什么这波基建的天花板，比大多数人想的高得多。

供给的想象力，就是需求的天花板。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Hl6n61hiaXSeR2sm7xN1dXbuuYIuCvjIzLzEKR1icfQITCb5625g4qO7FNFib6KhsdqXufGiacenicSC85kmaqiaXOuog3ic0VBjxlwv9xibjkzGLP8/640?wx_fmt=jpeg&from=appmsg)

最 终 判 断

Dylan
Patel这66分钟，本质是把「AI是不是泡沫」这个宏大问题，翻译成了一张可操作的供应链地图：AI已经在印钞，需求几乎无上限地传导到每一个正在缺货的环节，但每个环节能吃到多少、涨多久，取决于它的市场结构和弹性。
**内存是这轮最硬的超级周期主线，CPU是被卖方高估的补涨小周期，CPO被市场提前亢奋、铜还有很长的路，而电力这个终极瓶颈「也不是瓶颈」。**
对投资者而言，价值不在于知道「AI很大」，而在于拿着这把「需求传导 × 市场结构 × 弹性」的尺子，去量每一个被喊成「下一个短缺」的名字。

本文内容翻译整理自WisdomTree播客《The Next Big
Thing》2026-07-09期原文，仅供学习交流，可能存在翻译偏差或遗漏。如有疑问欢迎对照英文原版收看，也欢迎业内专家在评论区指正与补充。内容仅供参考，不构成任何投资建议。

点击下方关注公众号，设个星标

才能及时接收最新推送

预览时标签不可点

微信扫一扫  
关注该公众号



微信扫一扫  
使用小程序

****



****



****



×  分析

__

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gOzB8yV5b0lodGDJuhPLRzjfibzOicMto5yIVQ0ibfGicSo8nhRhq8nIdo7fGjXjw0AdI8AacS1iay1oSlLmL3SHhOA/0?wx_fmt=png)

微信扫一扫可打开此内容，  
使用完整服务

：  ，  ，  ，  ，  ，  ，  ，  ，  ，  ，  ，  ，  。  视频  小程序  赞  ，轻点两下取消赞  在看  ，轻点两下取消在看
分享  留言  收藏  听过

