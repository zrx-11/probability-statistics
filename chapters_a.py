#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 A 批：课程概览 + 数学地基四章"""

CH_A = r"""
<section class="chapter" id="intro" style="display:block">
  <div class="breadcrumb"></div>
  <h2><span class="num">0</span>课程概览：从初中数学到概率统计</h2>
  <p class="lead">本课把《概率统计》第一到三章（事件与概率、离散型随机变量、连续型随机变量）从初中数学开始逐层推导。凡是读懂后面要用到的前置知识，都在前面补上，不跳步。</p>

  <div class="callout callout-tip">
    <div class="callout-title">这门课怎么学</div>
    每一步都不跳过。所有公式都从初中的分数、面积、方程、配料式一步步推出来，每个新符号第一次出现都给白话解释。看不懂的地方展开折叠的推导步骤，连"两边同时除以 2"这种变化都写着。数值例子全部手算验证过，可以自己跟着算。
  </div>

  <h3>知识树：整门课的地图</h3>
  <p>整门课长在初中数学的根上。点击节点可跳到对应章节。</p>
  <div class="knowledge-tree">
    <div class="kt-level"><span class="kt-label root">根系（初中）</span>
      <a class="kt-node root" data-goto="foundation-set">四则运算</a>
      <a class="kt-node root" data-goto="foundation-set">大小比较与等号</a>
      <a class="kt-node root" data-goto="foundation-set">数数</a>
      <a class="kt-node root" data-goto="foundation-set">且·或·非</a>
      <a class="kt-node root" data-goto="foundation-calc">长度与面积</a>
    </div>
    <div class="kt-level"><span class="kt-label base">地基</span>
      <a class="kt-node base" data-goto="foundation-set">集合与计数</a>
      <a class="kt-node base" data-goto="foundation-count">排列组合</a>
      <a class="kt-node base" data-goto="foundation-series">数列·Σ·级数</a>
      <a class="kt-node base" data-goto="foundation-calc">函数·极限·积分</a>
    </div>
    <div class="kt-level"><span class="kt-label tool">第一章 工具</span>
      <a class="kt-node tool" data-goto="event-space">样本空间</a>
      <a class="kt-node tool" data-goto="frequency-prob">公理化</a>
      <a class="kt-node tool" data-goto="classical-geom">古典/几何概型</a>
      <a class="kt-node tool" data-goto="conditional">条件概率</a>
      <a class="kt-node tool" data-goto="total-bayes">贝叶斯</a>
      <a class="kt-node tool" data-goto="independence">独立性</a>
    </div>
    <div class="kt-level"><span class="kt-label tool">第二章 离散</span>
      <a class="kt-node tool" data-goto="discrete-rv">随机变量</a>
      <a class="kt-node tool" data-goto="common-discrete">常见分布</a>
      <a class="kt-node tool" data-goto="discrete-2d">二维离散</a>
      <a class="kt-node tool" data-goto="expectation">期望</a>
      <a class="kt-node tool" data-goto="variance">方差</a>
      <a class="kt-node tool" data-goto="cond-expect">条件期望</a>
    </div>
    <div class="kt-level"><span class="kt-label tool">第三章 连续</span>
      <a class="kt-node tool" data-goto="dist-func">分布函数</a>
      <a class="kt-node tool" data-goto="continuous-density">密度</a>
      <a class="kt-node tool" data-goto="common-continuous">常见连续分布</a>
      <a class="kt-node tool" data-goto="continuous-2d">二维连续</a>
      <a class="kt-node tool" data-goto="continuous-func">函数分布·卷积</a>
      <a class="kt-node tool" data-goto="numeric-features">协方差·切比雪夫</a>
      <a class="kt-node tool" data-goto="regression-char">回归·特征函数</a>
    </div>
    <div class="kt-level"><span class="kt-label">主干</span>
      <a class="kt-node main" data-goto="summary">公式全景与自测</a>
    </div>
  </div>

  <h3>三章在讲什么</h3>
  <p><b>第一章</b>讲"怎么给事件算概率"。先把一次试验的所有可能结果装进一个集合（样本空间），再把概率定义成一个满足三条规则的秤，最后学几种常用的算法：等可能计数、几何度量、条件收缩、全概率分解、贝叶斯反推。</p>
  <p><b>第二章</b>把"试验结果"从文字换成数字，也就是随机变量。离散型随机变量只能取可数的值，用一张分布表记录每个值对应的概率。然后学期望、方差、条件期望，这些数字特征把随机变量的整体信息压缩成几个数。</p>
  <p><b>第三章</b>把取值从"可数"放宽到"连续"。连续型随机变量取单个值的概率是 0，不能用表记录，改用密度函数描述"哪里概率密、哪里稀"。积分处理连续情形，卷积处理两个随机变量相加，特征函数把分布转到另一个空间看它的结构。</p>

  <h3>记号约定</h3>
  <div class="table-wrap">
  <table>
    <tr><th style="width:26%">符号</th><th>含义</th></tr>
    <tr><td>$\Omega$</td><td>样本空间，一次试验所有可能结果的集合</td></tr>
    <tr><td>$\omega$</td><td>样本点，一次试验的一个具体结果</td></tr>
    <tr><td>$A,B,C$</td><td>事件，样本空间的子集</td></tr>
    <tr><td>$P(A)$</td><td>事件 A 发生的概率，一个介于 0 和 1 之间的数</td></tr>
    <tr><td>$\xi,\eta$</td><td>随机变量，把每个结果映射成一个实数</td></tr>
    <tr><td>$p_k,\ p_{ij}$</td><td>分布列，离散型随机变量取各值的概率</td></tr>
    <tr><td>$F(x)$</td><td>分布函数，$F(x)=P(\xi\le x)$</td></tr>
    <tr><td>$p(x)$</td><td>密度函数，连续型的"概率密度"</td></tr>
    <tr><td>$E\xi,\ D\xi$</td><td>数学期望、方差</td></tr>
    <tr><td>$\mathrm{Cov}(\xi,\eta),\ \rho$</td><td>协方差、相关系数</td></tr>
  </table>
  </div>

  <div class="callout callout-warn">
    <div class="callout-title">学习顺序建议</div>
    地基四章不必一口气全学完。集合与计数、排列组合必须先过，后面古典概型全靠它；数列与级数在泊松分布、特征函数处会用到；函数极限积分在第三章密集使用。时间紧就先读前三章正文，遇到积分卡住再回来补地基四。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 为什么连续型随机变量取单个值的概率是 0，但整个区间上的概率可以大于 0？</div>
    <div class="qa-a">因为连续型的概率用面积表示。一条线没有面积，一个点的面积是 0；一段区间有宽度，面积可以大于 0。第三章会用密度函数把这个直觉写成严格的积分。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="foundation-set">
  <div class="breadcrumb"></div>
  <h2><span class="num">1</span>地基一：集合与计数</h2>
  <p class="lead">概率论的第一步是把"所有可能的结果"装进一个盒子里，这个盒子就是集合。本节从"一个班里有谁"讲起，把并、交、补三个运算和计数公式推出来。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：数数、大于小于、且或非。后续：第 5 节样本空间与事件运算、第 8 节古典概型的计数、第二章的联合分布。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    集合就是一个袋子。袋子里装的东西叫元素。一个班 40 个学生，就是装着 40 个人的袋子。"数学好的人"也是一个袋子，是从班级袋子里挑出来的一部分。概率要算的事，基本都是问"从袋子里随机摸一个，摸到某个小袋子的机会有多大"。
  </div>

  <h3>1.1 集合的写法与关系</h3>
  <p>把一些确定的对象放在一起，就构成一个集合。比如 $A=\{1,2,3\}$ 表示装着 1、2、3 三个数的袋子。$x\in A$ 读作"x 属于 A"，意思是 x 在这个袋子里；$x\notin A$ 就是不在。</p>
  <p>不含任何元素的集合叫空集，记作 $\emptyset$。全班没人及格的那次考试，及格者的集合就是空集。</p>
  <p>如果 B 里的每个元素都在 A 里，说 B 是 A 的子集，记作 $B\subseteq A$。比如"数学好的人"是"全班同学"的子集。空集是所有集合的子集，因为它没有元素可以被挑出来说不属于。</p>

  <h3>1.2 三个运算：并、交、补</h3>
  <p>设 A、B 是同一个大袋子里的两个小袋子。</p>
  <p><b>并</b> $A\cup B$：把两个袋子的东西倒在一起（重复的只算一次）。对应语言里的"或"，而且这个"或"是宽松的或：只要在 A 里或在 B 里，或者两边都在，都算数。</p>
  <p><b>交</b> $A\cap B$：两边都有的东西。对应"且"。</p>
  <p><b>补</b> $\bar A$：全班里不属于 A 的人。对应"非"。</p>
  <p><b>差</b> $A-B$：在 A 里但不在 B 里，等于 $A\cap\bar B$。</p>

  <div class="callout callout-key">
    <div class="callout-title">把集合语言翻译成事件语言</div>
    $A\cup B$：A、B 至少发生一个。$A\cap B$：两个同时发生。$\bar A$：A 不发生。$A-B$：A 发生而 B 不发生。后面所有概率公式，翻译成这句话就能读懂。
  </div>

  <h3>1.3 德摩根律：否定的分配</h3>
  <p>先看一句日常话。"不是（数学好并且体育好）"，等价于"数学不好，或者体育不好"。注意这里"并且"变成"或者"，两个否定变成两个肯定之外的取反。这就是德摩根律：</p>
  <div class="formula">$$\overline{A\cup B}=\bar A\cap\bar B,\qquad \overline{A\cap B}=\bar A\cup\bar B$$</div>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">逐点法证明第一条</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>要证两个集合相等，标准做法是证明"左边包含右边"且"右边包含左边"，也就是每个元素在左边当且仅当在右边。</p>
        <p>第一步，取任意 $x\in\overline{A\cup B}$。意思是 x 不在 $A\cup B$ 里。既然不在并集里，那它就不在 A 里，也不在 B 里。所以 $x\in\bar A$ 且 $x\in\bar B$，于是 $x\in\bar A\cap\bar B$。这证明了左边是右边的子集。</p>
        <p>第二步，反过来取 $x\in\bar A\cap\bar B$。意思是 x 既不在 A 又不在 B。那么 x 不可能出现在 $A\cup B$ 里，因为并集里的每个元素至少属于其中一个。所以 $x\in\overline{A\cup B}$。右边也是左边的子集。</p>
        <p>两边互相包含，集合相等。第二条把"且"和"或"对调，证明过程完全对称。</p>
      </div>
    </div>
  </div>

  <h3>1.4 数个数：容斥原理</h3>
  <p>概率的古典算法里，分子分母都在数个数。两个袋子倒在一起，里面一共有多少个不同的东西？直接相加会重复算交集里的人。</p>
  <div class="formula">$$|A\cup B|=|A|+|B|-|A\cap B|$$</div>
  <p>竖线表示集合里元素的个数。为什么减一次？逐点看：只属于 A 的人，在 $|A|$ 里算了 1 次，在 $|B|$ 里没算，总共 1 次，正确；只属于 B 的人同理 1 次；同时在 A 和 B 里的人，在 $|A|$ 里算了 1 次，$|B|$ 里又算了 1 次，重复了，所以减 1 次变回 1 次。三个人群各算对，公式成立。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">40 人的班：数学好 20 人，体育好 15 人，两样都好 8 人</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>至少一样好的人数：$|A\cup B|=20+15-8=27$ 人。</p>
        <p>两样都不好的人数：$40-27=13$ 人。</p>
        <p>只数学好的人数：$|A|-|A\cap B|=20-8=12$ 人。</p>
        <p>只体育好的人数：$15-8=7$ 人。核对：$12+7+8+13=40$，四类人刚好分完整个班。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">三个集合的容斥公式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>把 $A\cup B\cup C$ 先看成 $(A\cup B)\cup C$，套两次两集合公式：</p>
        <p>$|A\cup B\cup C|=|A\cup B|+|C|-|(A\cup B)\cap C|$</p>
        <p>$=(|A|+|B|-|A\cap B|)+|C|-|(A\cap C)\cup(B\cap C)|$</p>
        <p>最后一项再用一次两集合公式：$|(A\cap C)\cup(B\cap C)|=|A\cap C|+|B\cap C|-|A\cap B\cap C|$。</p>
        <p>合并得到：$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$。</p>
        <p>规律是加减交替：单个加，两两交减，三个交加。这个规律推广到任意有限个集合也对。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">为什么这节要学</div>
    概率的公理里有一条叫"可列可加性"，说的是互不重叠的事件，并起来的概率等于概率相加。互不重叠就是不交，也就是交集为空。讲清楚"并"和"交"的差别，公理才读得懂。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 全班 50 人，读过《红楼梦》的 30 人，读过《三国》的 25 人，两本都读过的 10 人。求至少读过一本的人数。</div>
    <div class="qa-a">$30+25-10=45$ 人。还剩 5 人两本都没读。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么 $\overline{A\cup B}=\bar A\cap\bar B$ 里"或"变成了"且"？</div>
    <div class="qa-a">"不在 A 或 B 里"要求两个都排除。只要还在其中一个里面，就属于并集。所以要同时满足"不在 A"和"不在 B"，用且连接。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="foundation-count">
  <div class="breadcrumb"></div>
  <h2><span class="num">2</span>地基二：排列组合</h2>
  <p class="lead">古典概型的分子分母都是"数个数"。这节把数个数的方法从"一条一条数"升级成公式，从选人排队和选人组队两个场景把排列与组合推出来。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：乘法、除法、集合。后续：第 8 节古典概型、第 13 节二项分布、第 14 节二项式定理的系数。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    从家到学校有 3 条路，学校到体育馆有 2 条路。从家经学校到体育馆共有几条路线？每走一条家到学校的路，都可以配 2 条去体育馆的路，所以 $3\times 2=6$ 条。分几步走，就把每步的选择数乘起来。
  </div>

  <h3>2.1 两条计数原理</h3>
  <p><b>乘法原理</b>：一件事分几步完成，第 1 步有 $m_1$ 种做法，第 2 步有 $m_2$ 种，……，第 k 步有 $m_k$ 种，那么整件事共有 $m_1\times m_2\times\cdots\times m_k$ 种做法。道理是每一条前序路线都要配上后面所有可能，形成"配对所有"。</p>
  <p><b>加法原理</b>：一件事可以用几种互不重叠的方式完成，第 1 类有 $n_1$ 种，第 2 类有 $n_2$ 种，……，那么共有 $n_1+n_2+\cdots$ 种。分类之间不能有重叠，否则会重复计数。</p>
  <p>两者的区别用一句话记：分步用乘，分类用加。</p>

  <h3>2.2 排列：选出来还要排队</h3>
  <p>从 5 个人里选 3 个，站在三个位置上（第一排、第二排、第三排），有多少种排法？</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">逐个位置填人</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>第一个位置：5 个人谁都可以，5 种。</p>
        <p>第二个位置：第一个人已经站上去了，剩下 4 个人挑，4 种。</p>
        <p>第三个位置：前面已占了 2 人，剩 3 人挑，3 种。</p>
        <p>三步是分步完成的，按乘法原理：$5\times4\times3=60$ 种。</p>
        <p>把人数换成 n、位置数换成 k，同样的推理：第一个位置 n 种，第二个 n-1 种，……，第 k 个 n-k+1 种。连乘得</p>
      </div>
    </div>
  </div>
  <div class="formula">$$A_n^k=n(n-1)(n-2)\cdots(n-k+1)=\frac{n!}{(n-k)!}$$</div>
  <p>$A_n^k$ 读作"从 n 个里取 k 个的排列数"。$n!$ 读作 n 的阶乘，表示 $n(n-1)(n-2)\cdots2\cdot1$，即从 n 乘到 1。分子分母约掉 $(n-k)!$，正好留下前面 k 个因子。</p>
  <p>规定 $0!=1$。理由是"一个都不排"只有一种做法，就是什么都不做。这个规定让公式在 k=n 时也成立：$A_n^n=n!/0!=n!$。</p>

  <h3>2.3 组合：选出来不管顺序</h3>
  <p>从 5 个人里选 3 个组队，队内不分位置，有多少种？</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先排后除以重复</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先把"组队"当成"排队"来数：$A_5^3=60$。这 60 种排法里，只要成员相同就算同一支队，但队伍内部 3 个人有 $3!=6$ 种站法。</p>
        <p>比如 {甲乙丙} 这一支队，排队时被数成了 甲乙丙、甲丙乙、乙甲丙、乙丙甲、丙甲乙、丙乙甲 六种。所以每支队被重复数了 6 次。</p>
        <p>把 60 除以 6，得 $60/6=10$ 支队。于是定义</p>
      </div>
    </div>
  </div>
  <div class="formula">$$C_n^k=\frac{A_n^k}{k!}=\frac{n!}{k!(n-k)!}$$</div>
  <p>$C_n^k$ 读作"从 n 个里取 k 个的组合数"，也写作 $\binom{n}{k}$。除以 $k!$ 就是在扣掉队内顺序造成的重复。</p>

  <div class="callout callout-key">
    <div class="callout-title">排列与组合怎么分</div>
    问顺序有关吗？排队、排名、密码、分配不同岗位，顺序有关，用 A。组队、选代表、抽出一把牌，顺序无关，用 C。
  </div>

  <h3>2.4 组合数的两个性质</h3>
  <p>第一条：$C_n^k=C_n^{n-k}$。选出的 k 个人确定后，剩下的 n-k 个人也确定了，选人和留人一一对应，所以数目相等。比如 $C_{10}^3=C_{10}^7$。</p>
  <p>第二条：$C_n^k=C_{n-1}^{k-1}+C_{n-1}^k$。把 n 个人里的某一位特殊人物拿出来（比如班长），所有选法分成两类：班长在队里，还要从剩下 n-1 人选 k-1 个；班长不在队里，从剩下 n-1 人选满 k 个。两类不重叠，按加法原理相加。这个递推就是杨辉三角每行的生成规则。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">数值验算</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$C_5^3=5!/(3!2!)=120/(6\times2)=10$，与前面组队的 10 对上。</p>
        <p>验第二条：$C_5^3=C_4^2+C_4^3=6+4=10$。对。</p>
        <p>验第一条：$C_5^3=C_5^2=10$，也对。</p>
      </div>
    </div>
  </div>

  <h3>2.5 二项式定理：组合数的另一个出口</h3>
  <p>把 $(a+b)^n$ 展开，各项的系数就是组合数。以 n=3 为例，先硬展开：</p>
  <p>$(a+b)^3=(a+b)(a+b)(a+b)$。乘开时，每个括号里要么选 a 要么选 b。三个括号都选 a，得 $a^3$；一个选 b 两个选 a，得 $a^2b$，而且这种情况有 $C_3^1=3$ 种（b 来自第几个括号）；两个选 b 得 $ab^2$，有 $C_3^2=3$ 种；三个都选 b 得 $b^3$。</p>
  <div class="formula">$$(a+b)^3=a^3+3a^2b+3ab^2+b^3$$</div>
  <p>一般地，$(a+b)^n$ 展开后，选 k 个括号出 b、n-k 个出 a，得项 $a^{n-k}b^k$，这样的选法有 $C_n^k$ 种：</p>
  <div class="formula">$$(a+b)^n=\sum_{k=0}^{n}C_n^k a^{n-k}b^k$$</div>
  <p>这就是二项式定理。第二章算二项分布的概率 $C_n^k p^k q^{n-k}$，系数就是从这里来的。</p>

  <div class="callout callout-key">
    <div class="callout-title">在概率里怎么用</div>
    古典概型 $P=\frac{有利于 A 的情况数}{所有情况数}$，分子分母都是组合数。考试里一道"从 52 张牌抽 5 张"的题，分母就是 $C_{52}^5=2598960$，这个数要会算：$52\times51\times50\times49\times48/(5\times4\times3\times2\times1)$。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 10 个人里选 3 个当班委，3 个职务不同，有多少种？</div>
    <div class="qa-a">$A_{10}^3=10\times9\times8=720$ 种。职务不同即顺序有关，用排列。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 10 个人里选 3 个去打扫卫生，有多少种？</div>
    <div class="qa-a">$C_{10}^3=120$ 种。打扫卫生不分职务，顺序无关，用组合。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 为什么 $0!=1$ 而不是 0？</div>
    <div class="qa-a">阶乘公式要满足 $A_n^n=n!/(n-n)!=n!$，必须有 $0!=1$。从含义上讲，什么都不排只有一种做法，也是 1。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="foundation-series">
  <div class="breadcrumb"></div>
  <h2><span class="num">3</span>地基三：数列、Σ 与级数</h2>
  <p class="lead">概率里到处是"把所有情况的概率加起来"，写起来就是一串求和。这节把求和记号 Σ、等差等比数列的求和公式、以及 e 这个常数的来历讲清楚。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：四则运算、乘方。后续：第 6 节可列可加、第 13 节泊松分布、第 16 节期望的定义、第 21 节指数分布、第 25 节特征函数的级数展开。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    存钱罐每天投一枚硬币，第 1 天 1 枚，第 2 天 2 枚，……，第 30 天 30 枚。一个月总共多少枚？不用一天一天加，用公式：$(1+30)\times30/2=465$。把长串相加压成一个公式，就是数列求和干的事。
  </div>

  <h3>3.1 Σ 记号：把加法写成一行</h3>
  <p>$\sum_{k=1}^{n}a_k$ 读作"k 从 1 到 n，把 $a_k$ 全部加起来"，意思是 $a_1+a_2+\cdots+a_n$。$\Sigma$ 是希腊字母，就是"求和"的意思。下面的 $k=1$ 是起点，上面的 n 是终点，k 是计数器。</p>
  <p>两个常用的求和结果，直接展开就能验证：</p>
  <div class="formula">$$\sum_{k=1}^{n}1=n,\qquad \sum_{k=1}^{n}k=\frac{n(n+1)}{2}$$</div>
  <p>第一个是把 1 加了 n 次。第二个下面推。</p>

  <h3>3.2 等差数列求和：倒序相加</h3>
  <p>相邻两项差固定的数列叫等差数列，公差记 d：$a_k=a_1+(k-1)d$。求和用一个小技巧。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">把和正着写一遍，倒着写一遍</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $S=a_1+a_2+\cdots+a_n$。</p>
        <p>倒过来写：$S=a_n+a_{n-1}+\cdots+a_1$。</p>
        <p>两式逐项相加。第一对 $a_1+a_n$，第二对 $a_2+a_{n-1}$。因为等差，$a_1+a_n=a_2+a_{n-1}=\cdots$ 每一对的和都相同，都等于首项加末项。</p>
        <p>一共有 n 对，所以 $2S=n(a_1+a_n)$，即</p>
      </div>
    </div>
  </div>
  <div class="formula">$$S_n=\frac{n(a_1+a_n)}{2}$$</div>
  <p>取 $a_1=1$、d=1，末项 $a_n=n$，得 $\sum_{k=1}^n k=n(n+1)/2$，就是上面那个公式。</p>

  <h3>3.3 等比数列求和：错位相减</h3>
  <p>相邻两项比值固定的数列叫等比数列，公比记 q：$a_k=a_1q^{k-1}$。求和。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">乘 q 再相减，错开一位</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$S_n=a_1+a_1q+a_1q^2+\cdots+a_1q^{n-1}$。</p>
        <p>两边乘 q：$qS_n=a_1q+a_1q^2+\cdots+a_1q^{n-1}+a_1q^n$。</p>
        <p>两式相减。中间的 $a_1q,\ a_1q^2,\dots,a_1q^{n-1}$ 全部成对抵消，只剩首尾：</p>
        <p>$S_n-qS_n=a_1-a_1q^n$。</p>
        <p>左边提取 $S_n$：$(1-q)S_n=a_1(1-q^n)$。当 $q\ne1$ 时两边除以 $1-q$，得</p>
      </div>
    </div>
  </div>
  <div class="formula">$$S_n=\frac{a_1(1-q^n)}{1-q}\quad(q\ne1)$$</div>

  <h3>3.4 无穷等比级数：加不完也能算出总数</h3>
  <p>项数无限多时，和还可能是有限的。比如 $1+\frac12+\frac14+\frac18+\cdots$，每次加一半，越加越少。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">让 n 趋于无穷</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>有限和是 $S_n=\frac{1(1-q^n)}{1-q}$。这里 $a_1=1$，$q=\frac12$。</p>
        <p>当 n 变大时，$q^n=(\frac12)^n$ 越来越接近 0：$(\frac12)^{10}\approx0.00098$，$(\frac12)^{20}\approx0.00000095$。</p>
        <p>所以 $S_n$ 越来越接近 $\frac{1}{1-\frac12}=2$。无穷和记作 2。</p>
        <p>一般地，$|q|\lt1$ 时 $q^n\to0$，$S=\frac{a_1}{1-q}$；$|q|\ge1$ 时和发散，没有有限值。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">在概率里的位置</div>
    离散型随机变量的所有概率加起来必须等于 1，就是一条级数等式。比如几何分布 $P(\xi=k)=q^{k-1}p$，$k=1,2,\dots$，全部加起来 $\sum q^{k-1}p=\frac{p}{1-q}=1$，正好用等比级数公式验证。
  </div>

  <h3>3.5 e：自然增长的常数</h3>
  <p>银行年利率 100%，存 1 元一年后得 2 元。如果改成半年结息一次，利率减半，第一次得 $1.5$ 元，第二次在这 1.5 上再乘 1.5，得 $1.5^2=2.25$ 元。结息越频繁，钱越多：</p>
  <div class="table-wrap">
  <table>
    <tr><th>结息次数</th><th>每次倍率</th><th>一年后</th></tr>
    <tr><td>1</td><td>2</td><td>2</td></tr>
    <tr><td>2</td><td>1.5</td><td>2.25</td></tr>
    <tr><td>12</td><td>1+1/12</td><td>约 2.613</td></tr>
    <tr><td>365</td><td>1+1/365</td><td>约 2.7146</td></tr>
    <tr><td>趋于无穷</td><td>—</td><td>约 2.71828</td></tr>
  </table>
  </div>
  <p>无限频繁结息时的极限值就是常数 e：</p>
  <div class="formula">$$e=\lim_{n\to\infty}\left(1+\frac1n\right)^n\approx2.718281828$$</div>
  <p>把 $(1+\frac1n)^n$ 用二项式定理展开，会得到另一个更有用的形式：</p>
  <div class="formula">$$e^x=\sum_{k=0}^{\infty}\frac{x^k}{k!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">从二项式定理到这个级数</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$(1+\frac{x}{n})^n=\sum_{k=0}^{n}C_n^k(\frac{x}{n})^k$。</p>
        <p>看第 k 项：$C_n^k(\frac{x}{n})^k=\frac{n(n-1)\cdots(n-k+1)}{k!}\cdot\frac{x^k}{n^k}=\frac{x^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}$。</p>
        <p>后面那一串分式，分子有 k 个因子，分母是 k 个 n。当 n 很大时每个因子 $\frac{n-j}{n}\to1$，整串趋于 1。</p>
        <p>所以第 k 项趋于 $\frac{x^k}{k!}$。对所有项求和，就得到 $e^x$ 的级数。取 x=1 得 $e=1+1+\frac12+\frac16+\frac1{24}+\cdots$。</p>
      </div>
    </div>
  </div>
  <p>这个级数在泊松分布里直接出现：$P(\xi=k)=\frac{\lambda^k}{k!}e^{-\lambda}$，那个 $k!$ 和 $e^{-\lambda}$ 就是为了让所有概率加起来等于 1。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 计算 $1+2+3+\cdots+100$。</div>
    <div class="qa-a">$100\times101/2=5050$。倒序相加：首尾配对，每对 101，共 50 对。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. $0.3+0.03+0.003+\cdots$ 等于多少？</div>
    <div class="qa-a">首项 0.3，公比 0.1，和 $=0.3/(1-0.1)=1/3$。这也解释了 0.333… 为什么等于 1/3。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 为什么几何分布的所有概率加起来等于 1？</div>
    <div class="qa-a">$P(\xi=k)=q^{k-1}p$ 是首项 p、公比 q 的等比数列，和 $=p/(1-q)$。因为 $p+q=1$，所以等于 1。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="foundation-calc">
  <div class="breadcrumb"></div>
  <h2><span class="num">4</span>地基四：函数、极限、积分</h2>
  <p class="lead">第三章连续型随机变量整章建立在积分上。这节从"面积"讲起，把极限、导数、定积分、换元、分部、反常积分、高斯积分、Γ 函数一次补齐。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：函数图像、面积、四则运算。后续：第 20 节密度的归一化、第 21 节指数与正态的分布函数、第 24 节卷积、第 26 节特征函数。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    积分就是求不规则图形的面积。把图形切成很多细条，每条近似当成长方形，宽乘高再全部加起来。切得越细，结果越准。极限就是"切到无限细"这个动作。
  </div>

  <h3>4.1 函数与连续</h3>
  <p>函数就是一个"输入一个数、输出一个数"的规则，记作 $y=f(x)$。把输入和输出画成点，连起来就是图像。</p>
  <p>连续的意思是图像一笔画得下来，中间不断。严格说法是：x 靠近 a 时，f(x) 靠近 f(a)。</p>

  <h3>4.2 极限：靠近的过程</h3>
  <p>$\lim_{x\to a}f(x)=L$ 读作"x 趋于 a 时 f(x) 的极限是 L"，意思是 x 无限接近 a（但不一定等于 a），f(x) 就无限接近 L。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">用数表看 $f(x)=x^2$ 在 x=1 的极限</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$x=1.1$：$1.1^2=1.21$。$x=1.01$：$1.0201$。$x=1.001$：$1.002001$。</p>
        <p>x 越来越靠近 1，$x^2$ 就越来越靠近 1。所以 $\lim_{x\to1}x^2=1$，正好等于函数在 1 处的值，这说明 $x^2$ 在 1 处连续。</p>
      </div>
    </div>
  </div>

  <h3>4.3 导数：瞬间的变化速度</h3>
  <p>汽车开 2 小时走 120 公里，平均速度 60 公里每小时。但仪表盘显示的是"这一秒的速度"，不是平均。要算瞬时速度，就让时间差越来越小。</p>
  <p>定义导数：</p>
  <div class="formula">$$f'(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$$</div>
  <p>分子是函数值的改变量，分母是自变量的改变量，比值是平均变化率，取极限得瞬时变化率。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">求 $f(x)=x^2$ 的导数</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>第一步代入：$\frac{(x+\Delta x)^2-x^2}{\Delta x}$。</p>
        <p>第二步展开平方：$(x+\Delta x)^2=x^2+2x\Delta x+(\Delta x)^2$。</p>
        <p>第三步相减：分子变成 $2x\Delta x+(\Delta x)^2$。</p>
        <p>第四步除以 $\Delta x$：得 $2x+\Delta x$。</p>
        <p>第五步取极限：$\Delta x\to0$，剩下 $2x$。所以 $(x^2)'=2x$。</p>
      </div>
    </div>
  </div>
  <p>常用的导数公式，后面会反复用：</p>
  <div class="table-wrap">
  <table>
    <tr><th>函数</th><th>导数</th><th>函数</th><th>导数</th></tr>
    <tr><td>$x^n$</td><td>$nx^{n-1}$</td><td>$e^x$</td><td>$e^x$</td></tr>
    <tr><td>$\ln x$</td><td>$1/x$</td><td>$\sin x$</td><td>$\cos x$</td></tr>
    <tr><td>$\cos x$</td><td>$-\sin x$</td><td>$e^{kx}$</td><td>$ke^{kx}$</td></tr>
  </table>
  </div>

  <h3>4.4 定积分：把面积切成竖条</h3>
  <p>求曲线 $y=f(x)$ 在区间 $[a,b]$ 下方的面积。办法是切条：把 $[a,b]$ 分成 n 段，每段宽 $\Delta x=\frac{b-a}{n}$，第 i 条取高度 $f(x_i)$，面积约为 $f(x_i)\Delta x$。全部加起来，再让 n 趋于无穷：</p>
  <div class="formula">$$\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i)\Delta x$$</div>
  <p>记号 $\int$ 是一个拉长的 S，表示求和；dx 表示"宽度趋于 0"。</p>
  <p>算面积不用每次都切条。牛顿-莱布尼茨公式把它转成"找原函数再代端点"：如果 $F'(x)=f(x)$，那么</p>
  <div class="formula">$$\int_a^b f(x)\,dx=F(b)-F(a)$$</div>
  <p>基本积分表：</p>
  <div class="table-wrap">
  <table>
    <tr><th>被积函数</th><th>原函数</th><th>被积函数</th><th>原函数</th></tr>
    <tr><td>$x^n\ (n\ne-1)$</td><td>$\frac{x^{n+1}}{n+1}$</td><td>$e^x$</td><td>$e^x$</td></tr>
    <tr><td>$1/x$</td><td>$\ln x$</td><td>$e^{-x}$</td><td>$-e^{-x}$</td></tr>
    <tr><td>$\sin x$</td><td>$-\cos x$</td><td>$\cos x$</td><td>$\sin x$</td></tr>
  </table>
  </div>

  <h3>4.5 换元法：把复杂的换成简单的</h3>
  <p>由复合函数求导的链式法则 $[F(g(x))]'=f(g(x))g'(x)$，反过来读：如果被积函数长成 $f(g(x))g'(x)$ 的样子，就可以把 $g(x)$ 整体换成 u。</p>
  <div class="formula">$$\int f(g(x))g'(x)\,dx=\int f(u)\,du,\quad u=g(x)$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\int 2x e^{x^2}dx$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>观察到 $2x$ 正好是 $x^2$ 的导数。令 $u=x^2$，$du=2x\,dx$。</p>
        <p>原式变成 $\int e^u du=e^u+C=e^{x^2}+C$。</p>
        <p>验证：$(e^{x^2})'=e^{x^2}\cdot2x$，正好是被积函数。</p>
      </div>
    </div>
  </div>

  <h3>4.6 分部积分：乘积的积分</h3>
  <p>由乘积求导法则 $(uv)'=u'v+uv'$，移项再积分，得到</p>
  <div class="formula">$$\int u\,dv=uv-\int v\,du$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\int x e^{-x}dx$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>取 $u=x$，$dv=e^{-x}dx$，则 $du=dx$，$v=-e^{-x}$。</p>
        <p>代入公式：$\int x e^{-x}dx=-xe^{-x}-\int(-e^{-x})dx=-xe^{-x}+\int e^{-x}dx$。</p>
        <p>而 $\int e^{-x}dx=-e^{-x}+C$，所以结果 $=-xe^{-x}-e^{-x}+C=-(x+1)e^{-x}+C$。</p>
        <p>验证求导：$[-(x+1)e^{-x}]'=-e^{-x}+(x+1)e^{-x}=xe^{-x}$，对。</p>
      </div>
    </div>
  </div>

  <h3>4.7 反常积分：积到无穷远</h3>
  <p>积分上限是无穷时，先积到有限上限 b，再让 b 趋于无穷：$\int_0^\infty f(x)dx=\lim_{b\to\infty}\int_0^b f(x)dx$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\int_0^\infty e^{-x}dx$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先积到 b：$\int_0^b e^{-x}dx=[-e^{-x}]_0^b=-e^{-b}+1$。</p>
        <p>b 趋于无穷时，$e^{-b}$ 趋于 0（$e^{-10}\approx0.0000454$）。所以极限为 1。</p>
        <p>这个结果 1 是后面指数分布密度归一化的基础。</p>
      </div>
    </div>
  </div>

  <h3>4.8 高斯积分：$\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$</h3>
  <p>这个积分在正态分布里必须用到，因为正态密度的系数 $\frac{1}{\sqrt{2\pi}\sigma}$ 就是靠它凑出 1 的。它没法用初等原函数算，用一个巧办法。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先平方，再换极坐标</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $I=\int_{-\infty}^{\infty}e^{-x^2}dx$。要算 $I$，先算 $I^2$。两个积分相乘，因为积分变量名字可以随便换，把第一个里的 x 改成 x，第二个里的 x 改成 y：</p>
        <p>$I^2=\left(\int e^{-x^2}dx\right)\left(\int e^{-y^2}dy\right)=\iint e^{-(x^2+y^2)}dx\,dy$。这一步成立是因为两个积分各自独立，可以合并成二重积分。</p>
        <p>现在换极坐标：$x=r\cos\theta$，$y=r\sin\theta$。此时 $x^2+y^2=r^2$。面积元的换算：极坐标下一小块矩形边长是 dr 和 $r\,d\theta$，面积 $dx\,dy=r\,dr\,d\theta$（那个 r 是第 3 章会讲的雅可比）。</p>
        <p>代入：$I^2=\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta$。</p>
        <p>先算里面：$\int_0^\infty e^{-r^2}r\,dr$。令 $u=r^2$，$du=2r\,dr$，即 $r\,dr=\frac12du$。积分变成 $\frac12\int_0^\infty e^{-u}du=\frac12\cdot1=\frac12$。</p>
        <p>再算外面：$\int_0^{2\pi}\frac12 d\theta=\frac12\cdot2\pi=\pi$。</p>
        <p>所以 $I^2=\pi$，$I=\sqrt\pi$（取正，因为被积函数恒正）。</p>
      </div>
    </div>
  </div>

  <h3>4.9 Γ 函数：阶乘的连续版</h3>
  <p>阶乘 $n!=n(n-1)\cdots1$ 只对整数有定义。能不能推广到分数？用积分定义一个函数：</p>
  <div class="formula">$$\Gamma(s)=\int_0^\infty x^{s-1}e^{-x}\,dx,\quad s\gt0$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$\Gamma(s+1)=s\Gamma(s)$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>把 $\Gamma(s+1)=\int_0^\infty x^{s}e^{-x}dx$ 分部积分。取 $u=x^s$，$dv=e^{-x}dx$，则 $du=sx^{s-1}dx$，$v=-e^{-x}$。</p>
        <p>$\Gamma(s+1)=[-x^se^{-x}]_0^\infty+\int_0^\infty sx^{s-1}e^{-x}dx$。</p>
        <p>第一项：x 趋于无穷时，$x^se^{-x}\to0$（指数压过多项式）；x=0 时当 $s\gt0$，$0^s\cdot1=0$。所以第一项为 0。</p>
        <p>第二项是 $s\int_0^\infty x^{s-1}e^{-x}dx=s\Gamma(s)$。得递推式 $\Gamma(s+1)=s\Gamma(s)$。</p>
        <p>配合 $\Gamma(1)=\int_0^\infty e^{-x}dx=1$，递推得 $\Gamma(2)=1\cdot\Gamma(1)=1$，$\Gamma(3)=2\cdot1=2$，$\Gamma(n+1)=n!$。阶乘确实是它的整数特例。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$\Gamma(\frac12)=\sqrt\pi$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Gamma(\frac12)=\int_0^\infty x^{-1/2}e^{-x}dx$。令 $x=t^2$，则 $dx=2t\,dt$，$x^{-1/2}=1/t$。</p>
        <p>代入：$\int_0^\infty \frac{1}{t}e^{-t^2}2t\,dt=2\int_0^\infty e^{-t^2}dt$。</p>
        <p>偶函数，$\int_0^\infty e^{-t^2}dt=\frac12\int_{-\infty}^\infty e^{-t^2}dt=\frac{\sqrt\pi}{2}$。</p>
        <p>所以 $\Gamma(\frac12)=2\cdot\frac{\sqrt\pi}{2}=\sqrt\pi$。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">这一节的四个结果，后面在哪用</div>
    定积分 → 第 20 节 $F(x)=\int_{-\infty}^x p(y)dy$ 的定义；换元 → 第 21 节指数分布换元、第 24 节卷积；高斯积分 → 第 21 节正态密度系数；Γ 函数 → 第 26 节特征函数与第 21 节 $\Gamma$ 型分布。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 求 $\int_0^1 x^2dx$。</div>
    <div class="qa-a">原函数 $x^3/3$，代端点 $1/3-0=1/3$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么高斯积分要平方，而不是直接求原函数？</div>
    <div class="qa-a">$e^{-x^2}$ 的原函数写不成初等函数，牛顿-莱布尼茨公式用不上。平方后变成二维，换极坐标后 $e^{-r^2}$ 能积出来。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. $\Gamma(4)$ 等于多少？</div>
    <div class="qa-a">$\Gamma(4)=3!=6$。按递推 $\Gamma(4)=3\Gamma(3)=3\cdot2\Gamma(2)=3\cdot2\cdot1=6$。</div>
  </div>

  <div class="chapter-nav"></div>
</section>
"""
