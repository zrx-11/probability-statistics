#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 B 批：第一章 事件与概率"""

CH_B = r"""
<section class="chapter" id="event-space">
  <div class="breadcrumb"></div>
  <h2><span class="num">5</span>随机事件与样本空间</h2>
  <p class="lead">做一次试验，把所有可能的结果装进一个集合，这个集合叫样本空间。每个结果叫样本点。我们关心的事情都是样本空间的一部分，叫事件。这一节把这三个词说清楚，再讲事件的运算。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：集合、并交补（第 1 节）。后续：公理化概率（第 6 节）、事件运算在概率公式里的翻译（第 7、9 节）。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    掷一颗骰子，结果有六种：1 到 6。把六个结果装进一个袋子 $\Omega=\{1,2,3,4,5,6\}$，这个袋子就是样本空间。问"点数大于 4"行不行，就是把袋子里的 5、6 挑出来组成小袋子 $A=\{5,6\}$，这个小袋子就是事件。
  </div>

  <h3>5.1 随机试验与样本空间</h3>
  <p>一件事满足三条就叫随机试验：可以在相同条件下重复做；每次可能的结果不止一个，且事先能列出全部可能；做完之前不知道会是哪一个。掷骰子、抛硬币、抽签、测量误差都算。</p>
  <p>试验的每个可能结果叫样本点，记作 $\omega$。全部样本点组成的集合叫样本空间，记作 $\Omega$。</p>
  <div class="table-wrap">
  <table>
    <tr><th style="width:30%">试验</th><th>样本空间</th></tr>
    <tr><td>掷一颗骰子</td><td>$\Omega=\{1,2,3,4,5,6\}$</td></tr>
    <tr><td>抛一枚硬币</td><td>$\Omega=\{\text{正},\text{反}\}$</td></tr>
    <tr><td>抛两枚硬币</td><td>$\Omega=\{(\text{正,正}),(\text{正,反}),(\text{反,正}),(\text{反,反})\}$</td></tr>
    <tr><td>等公交（0 到 10 分钟）</td><td>$\Omega=[0,10]$，区间里任何数都可能</td></tr>
    <tr><td>测量零件长度</td><td>$\Omega=(0,+\infty)$</td></tr>
  </table>
  </div>
  <p>前两行是有限个结果，后两行是连续区间。这两种 $\Omega$ 对应第二章的离散型和第三章的连续型，现在记住两种都有就行。</p>

  <h3>5.2 事件：样本空间的子集</h3>
  <p>事件就是样本空间的一个子集。"点数大于 4"是 $\{5,6\}$，"点数是偶数"是 $\{2,4,6\}$，"点数不超过 6"就是整个 $\Omega$。"点数等于 7"是空集 $\emptyset$，不可能发生。</p>
  <p>事件发生的意思是：这次试验的结果落在这个子集里。掷出 6，事件 $\{5,6\}$ 就发生了；掷出 3，没发生。</p>
  <p>两个特殊事件：$\Omega$ 叫必然事件，每次结果都在里面；$\emptyset$ 叫不可能事件。</p>

  <h3>5.3 事件的运算</h3>
  <p>事件是集合，集合运算原样搬过来，只换一种读法。</p>
  <div class="table-wrap">
  <table>
    <tr><th style="width:24%">运算</th><th>集合含义</th><th>事件含义</th></tr>
    <tr><td>$A\cup B$</td><td>并集</td><td>A、B 至少有一个发生</td></tr>
    <tr><td>$A\cap B$（也写 $AB$）</td><td>交集</td><td>A、B 同时发生</td></tr>
    <tr><td>$\bar A$</td><td>补集</td><td>A 不发生</td></tr>
    <tr><td>$A-B$</td><td>差集</td><td>A 发生而 B 不发生</td></tr>
  </table>
  </div>
  <p>$AB$ 是 $A\cap B$ 的简写，后面公式里经常用它。两个事件"互不相容"（也叫互斥）的意思是 $AB=\emptyset$：两个不能同时发生。</p>
  <p>德摩根律直接能用：$\overline{A\cup B}=\bar A\bar B$ 说"A、B 至少一个发生"的反面是"A、B 都不发生"；$\overline{AB}=\bar A\cup\bar B$ 说"A、B 同时发生"的反面是"至少一个不发生"。用日常语言读一遍就明白，不必重新证明。</p>

  <h3>5.4 σ-代数：能算概率的事件家族</h3>
  <p>样本空间的子集非常多，不是每个都需要算概率。概率论只挑一部分规整的子集来算，这一族子集要满足三条封闭性，叫 σ-代数，记作 $\mathcal F$。</p>
  <p>三条要求（课件 1.4 节原文）：</p>
  <p>（1）$\Omega\in\mathcal F$。整个样本空间必须在这族里，因为总得能给"必然发生"算概率。</p>
  <p>（2）若 $A\in\mathcal F$，则 $\bar A\in\mathcal F$。对取补封闭，A 能算概率，它的反面也得能算。</p>
  <p>（3）若 $A_1,A_2,\dots\in\mathcal F$，则 $\bigcup_{n=1}^\infty A_n\in\mathcal F$。对可列并封闭。</p>
  <p>满足三条的 $\mathcal F$ 叫 $\Omega$ 上的 σ-代数，$(\Omega,\mathcal F)$ 叫可测空间，$\mathcal F$ 中的元素叫事件。再配一个概率 P，三元组 $(\Omega,\mathcal F,P)$ 就叫概率空间。</p>

  <div class="callout callout-tip">
    <div class="callout-title">这三条的白话版</div>
    想象一份"能开发票的名单"：整笔生意要在名单上；退单也要能开；几张单子合并也要能开。σ-代数就是事件世界里能开发票的那份名单。有限样本空间里通常所有子集都算事件，三条自动满足。连续情形才会出现某些子集算不了概率，那是测度论的内容，本课不深入。
  </div>

  <div class="callout callout-key">
    <div class="callout-title">为什么要定义 σ-代数</div>
    如果要求概率对每个子集都有定义且满足可列可加，在实数区间上会引发矛盾，构造不出这样的概率。所以学界约定只对一部分规整子集定义概率，这套约定就是 σ-代数。课件走严格公理化路线，把这个前提摆出来，后面才能定义 P。由(2)(3)可以推出(1)：$\bar A\cup A=\Omega$ 在族里，所以 $\Omega$ 自动在。σ-代数又称 σ-域。
  </div>

  <h3>5.5 由样本点构造事件</h3>
  <p>抛两枚硬币，样本空间 4 个点。事件"至少一枚正面"是 $\{(正,正),(正,反),(反,正)\}$，它等于 $A_1\cup A_2$，其中 $A_1$ 是第一枚正面，$A_2$ 是第二枚正面。"两枚都正面"是 $A_1\cap A_2=\{(正,正)\}$。"两枚结果不同"等于 $(A_1\bar A_2)\cup(\bar A_1A_2)$：第一正第二反，或者第一反第二正。</p>
  <p>注意 $(A_1\bar A_2)$ 和 $(\bar A_1A_2)$ 互斥，一个人不可能既"第一正第二反"又"第一反第二正"。所以后面算概率时可以直接把两部分概率相加。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">"至少一枚正面"用两种写法核对</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p><b>写法一（并集）</b>：$A_1\cup A_2$。逐个数样本点：$A_1$ 含 (正,正)、(正,反)，$A_2$ 含 (正,正)、(反,正)。并起来是三个点，(正,正) 只算一次。</p>
        <p><b>写法二（补集）</b>：$\overline{A_1\cup A_2}=\bar A_1\bar A_2$。按德摩根，反面是"第一枚不正且第二枚不正"，只有 (反,反) 一个点。</p>
        <p>两种写法加起来应该覆盖全部 4 个点：3+1=4，对上了。</p>
        <p>若四点是等可能的，每点 1/4，则 $P(\text{至少一枚正面})=3/4$，而 $P(\text{两枚都反面})=1/4$。用补集算通常更快：先算"一个都没有"，再用 1 减。</p>
      </div>
    </div>
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 掷骰子，A=点数偶数，B=点数大于 4。写出 $A\cup B$、$AB$、$\bar A$。</div>
    <div class="qa-a">$A=\{2,4,6\}$，$B=\{5,6\}$，$A\cup B=\{2,4,5,6\}$，$AB=\{6\}$，$\bar A=\{1,3,5\}$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么 σ-代数里要求"可列并"而不是"任意并"？</div>
    <div class="qa-a">可列并够用了：可列可加性只对可数个事件要求。任意并（不可数）在实数区间上会遇到病态集合，无法一致定义概率。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. "今天下雨或刮风"的反面怎么说？</div>
    <div class="qa-a">今天不下雨且不刮风。这就是德摩根律 $\overline{A\cup B}=\bar A\bar B$。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="frequency-prob">
  <div class="breadcrumb"></div>
  <h2><span class="num">6</span>频率与公理化概率</h2>
  <p class="lead">概率到底是什么？一种说法是"做很多次，数频率"；另一种是"规定三条规则，满足规则的都叫概率"。课件用后一种。这节把两条路都走一遍，看它们如何衔接。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：样本空间与事件（第 5 节）、Σ 与级数（第 3 节）。后续：第 7 节概率的性质、第 8 节古典概型。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    抛硬币 10 次，正面可能 6 次；抛 100 次，约 50 次；抛 10000 次，约 5000 次。次数越多，频率越靠近 0.5。这个"越来越稳定"的现象，是概率最原始的来源。
  </div>

  <h3>6.1 频率：先数，再算比值</h3>
  <p>做 n 次同样的试验，事件 A 发生了 $n_A$ 次。频率定义为</p>
  <div class="formula">$$f_n(A)=\frac{n_A}{n}$$</div>
  <p>频率是算出来的，不是规定的。它有三个容易验证的性质：</p>
  <p>（1）非负：$f_n(A)\ge0$，次数不会为负。</p>
  <p>（2）规范：$f_n(\Omega)=n/n=1$，每次结果都在样本空间里。</p>
  <p>（3）有限可加：如果 A、B 互斥，A 发生 $n_A$ 次、B 发生 $n_B$ 次，合起来发生 $n_A+n_B$ 次（互斥保证没有一次同时算两边），所以 $f_n(A\cup B)=f_n(A)+f_n(B)$。</p>
  <p>这三条和后面的公理形态一样，差别只在"有限"与"全部"。</p>

  <h3>6.2 频率的稳定性与它的局限</h3>
  <div class="table-wrap">
  <table>
    <tr><th>试验</th><th>次数</th><th>正面频率</th></tr>
    <tr><td>抛硬币</td><td>10</td><td>0.6</td></tr>
    <tr><td>抛硬币</td><td>100</td><td>0.52</td></tr>
    <tr><td>抛硬币</td><td>1000</td><td>0.498</td></tr>
    <tr><td>抛硬币</td><td>10000</td><td>0.5004</td></tr>
  </table>
  </div>
  <p>（这组数是用来演示收敛趋势的示例，不是某次真实实验的记录。）</p>
  <p>趋势往 0.5 靠，但不是单调靠近，中间会来回晃。而且"次数越多越靠近"这件事本身要靠概率来证明（大数定律，第 25 节会提）。所以频率只能当直观来源，不能当定义。定义要用公理。</p>

  <h3>6.3 概率的公理化定义</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">定</span><span class="derive-step-title">概率的三条公理</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $(\Omega,\mathcal F)$ 是可测空间，对每个 $A\in\mathcal F$ 赋予实数 $P(A)$。如果满足：</p>
        <p><b>公理 1（非负性）</b> $P(A)\ge0$。</p>
        <p><b>公理 2（规范性）</b> $P(\Omega)=1$。</p>
        <p><b>公理 3（可列可加性）</b> 若 $A_1,A_2,\dots$ 两两互斥（$A_iA_j=\emptyset$，$i\ne j$），则 $P\left(\bigcup_{k=1}^{\infty}A_k\right)=\sum_{k=1}^{\infty}P(A_k)$。</p>
        <p>就称 $P(A)$ 为事件 A 的概率，$(\Omega,\mathcal F,P)$ 叫概率空间。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">公理 3 为什么要求互斥</div>
    互斥保证没有重复计数。两个事件有交集时直接相加，交集会被算两次。第 1 节的容斥公式 $|A\cup B|=|A|+|B|-|A\cap B|$ 就是在补这个重复。公理只对不重叠的情形要求相加，这是最省事也最有用的约定。
  </div>

  <h3>6.4 为什么只规定三条就够</h3>
  <p>三条公理没说"概率怎么算"，只说"概率必须遵守什么"。所有具体算法（古典概型、几何概型、分布列、密度）都是满足这三条的实例。定理只要从公理推出来，对所有实例都成立，不必一个个验证。</p>
  <p>类比：交通法规只规定"红灯停"，不规定每条路怎么走。各城市自己设计路网，只要遵守红灯停，就能安全运行。公理是概率世界的交规，具体分布是各城市的路网。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">验</span><span class="derive-step-title">具体骰子概率满足三条公理</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Omega=\{1,2,3,4,5,6\}$，对每个子集 A 规定 $P(A)=|A|/6$。</p>
        <p>非负：$|A|/6\ge0$。规范：$|\Omega|/6=1$。可列可加：互斥的 A、B 没有公共元素，$|A\cup B|=|A|+|B|$，两边除以 6 得 $P(A\cup B)=P(A)+P(B)$。三条全过。</p>
      </div>
    </div>
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 频率的三条性质与概率公理差在哪？</div>
    <div class="qa-a">可加性范围不同：频率只对有限个互斥事件相加成立，公理要求可列无限个也成立。频率是试验后算出的数，会随试验变；概率是定义出来的固定数。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. $P(A)=0.3$，$P(B)=0.4$，A、B 互斥，求 $P(A\cup B)$。</div>
    <div class="qa-a">互斥可直接加：$0.3+0.4=0.7$。不互斥就得减交集，见下一节加法公式。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="prob-properties">
  <div class="breadcrumb"></div>
  <h2><span class="num">7</span>概率的性质</h2>
  <p class="lead">从三条公理出发，把常用公式一条条推出来：空集概率为零、对立事件、减法公式、加法公式、单调性与连续性、次可加性。后面所有计算都用这些工具。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：三条公理（第 6 节）、集合运算（第 1 节）。后续：古典概型（第 8 节）、条件概率（第 9 节）、贝叶斯（第 10 节）。
  </div>

  <h3>7.1 空集的概率是 0</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">用公理 2 和公理 3</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Omega=\Omega\cup\emptyset$，而 $\Omega$ 与 $\emptyset$ 互斥（空集没有元素，不可能与 $\Omega$ 有交集）。</p>
        <p>按公理 3：$P(\Omega)=P(\Omega)+P(\emptyset)$。</p>
        <p>两边减去 $P(\Omega)$，得 $P(\emptyset)=0$。</p>
      </div>
    </div>
  </div>

  <h3>7.2 对立事件：和为 1</h3>
  <p>$A$ 与 $\bar A$ 互斥，并起来是整个 $\Omega$。所以 $P(A)+P(\bar A)=P(\Omega)=1$，即</p>
  <div class="formula">$$P(\bar A)=1-P(A)$$</div>
  <p>"至少"类题目最常用这条：算"至少一个"不好算，就算"一个都没有"再取 1 减。</p>

  <h3>7.3 有限可加与减法公式</h3>
  <p>公理 3 管可列个互斥事件，截到有限个同样成立，可以在后面补一堆空集：$P(A_1\cup\cdots\cup A_n)=P(A_1)+\cdots+P(A_n)$。</p>
  <div class="formula">$$P(A-B)=P(A)-P(AB)$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">拆成互斥的两块</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>A 拆成两块：在 B 里的部分 $AB$，和不在 B 里的部分 $A-B$。两块互斥，并起来是 A。</p>
        <p>$P(A)=P(AB)+P(A-B)$，移项得 $P(A-B)=P(A)-P(AB)$。</p>
        <p>若 $B\subseteq A$，此时 $AB=B$，公式退化成 $P(A-B)=P(A)-P(B)$。</p>
      </div>
    </div>
  </div>

  <h3>7.4 加法公式：容斥</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">把 $A\cup B$ 拆成互斥的三块</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$A\cup B$ 拆成：只在 A 的 $A-B$，只在 B 的 $B-A$，共同部分 $AB$。三块互斥。</p>
        <p>$P(A\cup B)=P(A-B)+P(B-A)+P(AB)$。</p>
        <p>用减法公式 $P(A-B)=P(A)-P(AB)$，$P(B-A)=P(B)-P(AB)$，代入：</p>
        <p>$P(A\cup B)=P(A)-P(AB)+P(B)-P(AB)+P(AB)=P(A)+P(B)-P(AB)$。</p>
      </div>
    </div>
  </div>
  <div class="formula">$$P(A\cup B)=P(A)+P(B)-P(AB)$$</div>
  <p>这是第 1 节容斥公式的概率版。三个事件版本按"单加、两两交减、三交加"展开。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$P(A)=0.5,\ P(B)=0.4,\ P(AB)=0.2$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$P(A\cup B)=0.5+0.4-0.2=0.7$。</p>
        <p>$P(\bar A\bar B)=P(\overline{A\cup B})=1-0.7=0.3$，这是"都不发生"。</p>
        <p>$P(A\bar B)=P(A)-P(AB)=0.5-0.2=0.3$，这是"只 A 发生"。</p>
        <p>四块加总：$0.3+0.2+0.2+0.3=1$，正好分解完。</p>
      </div>
    </div>
  </div>

  <h3>7.5 连续性：事件列的极限</h3>
  <p>若 $A_1\subseteq A_2\subseteq\cdots$（事件越滚越大），则 $\lim_{n\to\infty}P(A_n)=P\left(\bigcup_{n=1}^\infty A_n\right)$，这叫下连续。若 $A_1\supseteq A_2\supseteq\cdots$（越缩越小），则 $\lim P(A_n)=P\left(\bigcap A_n\right)$，叫上连续。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">把递增事件列拆成互斥的新增块</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>令 $B_1=A_1$，$B_2=A_2-A_1$，$B_3=A_3-A_2$，……。每块是"新长出来、以前没有的部分"，所以 $B_i$ 两两互斥。</p>
        <p>因为一层套一层，前 n 个事件的并 $A_n=B_1\cup\cdots\cup B_n$，新块刚好补满。</p>
        <p>按可列可加：$P\left(\bigcup A_n\right)=\sum P(B_k)$；而 $P(A_n)=\sum_{k=1}^nP(B_k)$ 是同一级数的部分和。</p>
        <p>部分和趋于级数和，两边取极限得证。</p>
      </div>
    </div>
  </div>

  <h3>7.6 次可加性</h3>
  <p>不要求互斥时，并的概率不超过概率之和：</p>
  <div class="formula">$$P\left(\bigcup_{k=1}^{n}A_k\right)\le\sum_{k=1}^{n}P(A_k)$$</div>
  <p>直观是"有重叠时直接相加会多算，加起来是个上界"。估界时常用。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $P(A)=0.6$，$P(B)=0.5$，$P(A\cup B)=0.8$，求 $P(AB)$。</div>
    <div class="qa-a">$P(AB)=P(A)+P(B)-P(A\cup B)=0.6+0.5-0.8=0.3$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 掷骰子，求"至少出现一个 1 或 2"的概率，用对立事件算。</div>
    <div class="qa-a">反面是"既没有 1 也没有 2"，只有 $\{3,4,5,6\}$ 四种，概率 $4/6$。答案是 $1-4/6=1/3$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 为什么 $P(A-B)=P(A)-P(AB)$ 比 $P(A)-P(B)$ 更通用？</div>
    <div class="qa-a">$P(A)-P(B)$ 要求 $B\subseteq A$，否则会出负数。$P(A)-P(AB)$ 只减交集，任何情况都对。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="classical-geom">
  <div class="breadcrumb"></div>
  <h2><span class="num">8</span>古典概型与几何概型</h2>
  <p class="lead">两种能直接算出概率的情形。古典概型数个数，几何概型量长度或面积。背后是同一个想法：总度量当分母，有利于事件的那部分当分子。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：排列组合（第 2 节）、公理与加法公式（第 6、7 节）。后续：第 13 节二项分布、第 21 节均匀分布。
  </div>

  <h3>8.1 古典概型：等可能 + 有限个结果</h3>
  <p>样本空间只有有限个样本点，且每个点发生的可能性相同，就叫古典概型。此时每点概率 $\frac{1}{|\Omega|}$，事件 A 里有 $|A|$ 个点：</p>
  <div class="formula">$$P(A)=\frac{|A|}{|\Omega|}=\frac{\text{有利于 A 的样本点数}}{\text{样本点总数}}$$</div>
  <p>验证三条公理：非负显然；$P(\Omega)=1$；互斥的 A、B 点数相加等于并的点数，可加。三条成立，确实是合法概率。</p>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    袋子里 10 个球，3 红 7 白。随机摸一个，红的概率 3/10。每个球被摸到的机会一样，红球占了 3 个位置，所以 3/10。古典概型就是"数位置"。
  </div>

  <h3>8.2 摸球：有放回与无放回</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">3 红 2 白，连摸两次</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>无放回。总情况：第一次 5 种，第二次 4 种，共 20 种。两次都红：第一次 3 种，第二次只剩 2 个红球，$3\times2=6$ 种。概率 $6/20=3/10$。</p>
        <p>用组合算同一题：总 $C_5^2=10$，两红 $C_3^2=3$，得 $3/10$。两种算法一致。用组合时把"先摸谁"的顺序抹掉了，分子分母都抹，比值不变。</p>
        <p>有放回。总情况 $5\times5=25$ 种，两次都红 $3\times3=9$ 种，概率 $9/25$。</p>
        <p>有放回的概率更大，原因很简单：无放回时第二次红球少了一个，机会变小。第二章会把这件事写成"不独立"。</p>
      </div>
    </div>
  </div>

  <h3>8.3 分房模型</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">3 个人进 4 个房间，机会均等</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>总情况：每人 4 种，共 $4^3=64$ 种。</p>
        <p>"三个人各住一间"：第一个人 4 种，第二个剩 3 种，第三个剩 2 种，共 $4\times3\times2=24$ 种。概率 $24/64=3/8$。</p>
        <p>"至少两人同房"用对立事件：$1-3/8=5/8$。正面算要分"恰好两人同房"和"三人都同房"两类，反而麻烦。</p>
      </div>
    </div>
  </div>

  <h3>8.4 生日问题：反直觉的例子</h3>
  <p>n 个人里至少两人生日相同。按对立事件算"所有人都不相同"：第一个人随便 365 天，第二个人避开前一个剩 364 天，第三个人 363 天，……第 n 个人剩 $365-n+1$ 天。</p>
  <div class="formula">$$P(\text{至少两人同生日})=1-\frac{365\times364\times\cdots\times(365-n+1)}{365^n}$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">n=23 与 n=50</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>n=23：分子是 365 乘到 343，除以 $365^{23}$ 约为 0.4927，所以概率约 0.5073，刚过半。</p>
        <p>n=50：比值约 0.0296，概率约 0.9704，几乎必然。</p>
        <p>直觉上觉得"要 366 人才一定重复"，但"至少一对重复"的门槛低得多。23 个人能组出 $C_{23}^2=253$ 对，每一对都有机会撞上，253 次机会累积起来就过半了。</p>
      </div>
    </div>
  </div>

  <h3>8.5 几何概型：等可能 + 连续度量</h3>
  <p>样本空间是一个区域，点等可能落在区域内任意位置，概率与区域的度量（长度、面积）成正比，与形状位置无关：</p>
  <div class="formula">$$P(A)=\frac{A\text{ 的度量}}{\Omega\text{ 的度量}}$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">等公交，0 到 10 分钟内车来，等不超过 3 分钟</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Omega=[0,10]$，长度 10。事件是 $[0,3]$，长度 3，概率 $3/10$。</p>
        <p>问"等 3 到 7 分钟"，长度 $7-3=4$，概率 $4/10$。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">约会问题：各在 0 到 60 分钟随机到，先到的等 15 分钟</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设到达时刻为 x、y，样本空间是 $60\times60$ 的正方形，面积 3600。能见面要求 $|x-y|\le15$。</p>
        <p>不满足的区域是两个三角形：$y\lt x-15$ 与 $y\gt x+15$。每个直角边 45，面积 $\frac12\cdot45^2=1012.5$，两个共 2025。</p>
        <p>满足的面积 $3600-2025=1575$，概率 $1575/3600=0.4375$。两个三角形一个在线上方一个在线下方，不重叠，可以直接相加。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">古典与几何是同一个公式</div>
    统一写法是 $P(A)=\frac{\mu(A)}{\mu(\Omega)}$，$\mu$ 是某种度量。第二章的分布列是离散情形的"点数"，第三章的密度是连续情形的"密度"，沿的都是这条线。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 5 个球（3 红 2 白）无放回摸 2 个，求一红一白。</div>
    <div class="qa-a">总 $C_5^2=10$，一红一白 $C_3^1C_2^1=6$，概率 $6/10=3/5$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 在 $[0,1]$ 上随机取一点，它恰好等于 0.5 的概率是多少？</div>
    <div class="qa-a">单点没有长度，概率为 0。这不代表不可能发生，只是概率为零。第三章会重点讲这个反直觉现象。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 几何概型为什么不能数样本点？</div>
    <div class="qa-a">样本点有不可数个，每个点概率为 0，数不了。改用长度面积这类连续度量当分母。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="conditional">
  <div class="breadcrumb"></div>
  <h2><span class="num">9</span>条件概率与乘法公式</h2>
  <p class="lead">已知某件事发生了，另一件事的概率要不要改？要改。条件概率把样本空间从"全部可能"缩到"已知发生的那部分"，把 100% 的概率重新分配。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：古典概型（第 8 节）、加法公式（第 7 节）。后续：全概率与贝叶斯（第 10 节）、独立性（第 11 节）、第二章条件分布。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    班里 40 人，男生 20 女生 20；男生里戴眼镜 10 人。随机抽一个，是戴眼镜男生的概率 10/40 = 1/4。若已告诉你"抽到的是男生"，分母从 40 变成 20，概率 10/20 = 1/2。信息缩小了范围，概率跟着变。
  </div>

  <h3>9.1 定义的推导：为什么是除法</h3>
  <p>已知 B 发生，样本空间从 $\Omega$ 缩成 B。在新世界里只有落在 B 里的点可能。事件 A 想发生，得同时落在 A 和 B 里，也就是 $AB$。</p>
  <p>新世界的总质量是 $P(B)$，其中 $AB$ 占的比例是 $\frac{P(AB)}{P(B)}$。所以定义</p>
  <div class="formula">$$P(A|B)=\frac{P(AB)}{P(B)},\quad P(B)\gt0$$</div>
  <p>读作"在 B 发生的条件下，A 发生的概率"。除以 $P(B)$ 的动作就是重新归一化，把 B 那部分的概率撑到 1。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">验</span><span class="derive-step-title">掷骰子：已知是偶数，求是 2 的概率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>B=偶数 $=\{2,4,6\}$，$P(B)=1/2$。A=点数为 2，$P(AB)=1/6$。</p>
        <p>$P(A|B)=\frac{1/6}{1/2}=\frac13$。直接想也对：在 2、4、6 里，2 占三分之一。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">条件概率本身也是一个概率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>固定 B，把 $P(\cdot|B)$ 当新概率函数，验证三条公理。</p>
        <p>非负：分子分母都非负。</p>
        <p>规范：$P(\Omega|B)=\frac{P(\Omega B)}{P(B)}=\frac{P(B)}{P(B)}=1$。</p>
        <p>可列可加：互斥的 $A_i$ 切开后 $A_iB$ 也互斥，且 $(\bigcup A_i)B=\bigcup(A_iB)$，所以 $P(\bigcup A_i|B)=\frac{\sum P(A_iB)}{P(B)}=\sum P(A_i|B)$。</p>
        <p>三条都过，所以第 7 节的对立事件、加法公式，换成条件版原样成立。</p>
      </div>
    </div>
  </div>

  <h3>9.2 乘法公式</h3>
  <p>把定义两边乘 $P(B)$：</p>
  <div class="formula">$$P(AB)=P(A|B)P(B)=P(B|A)P(A)$$</div>
  <p>两个顺序都对，因为 $P(AB)$ 对称。三个以上推广成连乘：</p>
  <div class="formula">$$P(A_1A_2\cdots A_n)=P(A_1)P(A_2|A_1)P(A_3|A_1A_2)\cdots P(A_n|A_1\cdots A_{n-1})$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">三项连乘怎么来</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$P(A_1A_2A_3)=P(A_1A_2)P(A_3|A_1A_2)$，把 $A_1A_2$ 当整体套两事件公式。</p>
        <p>再把 $P(A_1A_2)$ 展开成 $P(A_1)P(A_2|A_1)$。</p>
        <p>合起来是三项连乘。多一项就多除一次前面那串的概率，这叫链式法则。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">不放回抽球：三只都是红球</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>袋里 3 红 2 白共 5 只，不放回连抽 3 只。</p>
        <p>第一只红：$\frac35$。第二只在"第一只红"条件下：剩 2 红 2 白共 4 只，$\frac24$。第三只在前两只都红条件下：剩 1 红 2 白共 3 只，$\frac13$。</p>
        <p>连乘：$\frac35\cdot\frac24\cdot\frac13=\frac{6}{60}=\frac{1}{10}$。</p>
        <p>组合核对：$\frac{C_3^3}{C_5^3}=\frac{1}{10}$，一致。</p>
      </div>
    </div>
  </div>

  <h3>9.3 容易犯的错：混淆方向</h3>
  <p>$P(A|B)$ 与 $P(B|A)$ 一般不同。"得病的人里 95% 检测阳性"（$P(\text{阳}|\text{病})=0.95$）与"阳性的人里得病的比例"（$P(\text{病}|\text{阳})$）是两个数，后者还受患病率影响，可能低得多。第 10 节的贝叶斯公式专门处理这个转换。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $P(A)=0.5,\ P(B)=0.4,\ P(A|B)=0.5$，求 $P(AB)$ 与 $P(B|A)$。</div>
    <div class="qa-a">$P(AB)=P(A|B)P(B)=0.5\times0.4=0.2$。$P(B|A)=P(AB)/P(A)=0.2/0.5=0.4$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么条件概率要求 $P(B)\gt0$？</div>
    <div class="qa-a">分母不能是 0。从意义上讲，"已知一件概率为 0 的事发生了"这个前提没法对话，也不知道按什么比例重新分配。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 无放回抽球时，第二次摸到红球的概率受第一次影响吗？</div>
    <div class="qa-a">受影响，是条件概率。第一次红时第二次红概率 2/4，第一次白时是 3/4。第二章用"独立"来描述不受影响的情形（有放回）。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="total-bayes">
  <div class="breadcrumb"></div>
  <h2><span class="num">10</span>全概率公式与贝叶斯公式</h2>
  <p class="lead">条件概率最重要的两个用法。全概率把复杂事件的概率拆成"按来源分类相加"，贝叶斯反过来"看见结果推断来源"。推导只用乘法公式和可加性。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：条件概率与乘法公式（第 9 节）、互斥与可加性（第 7 节）。后续：第 12 节条件分布、第 18 节全期望公式、第 25 节线性回归。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    三家厂各产一部分零件：甲 50%、乙 30%、丙 20%，次品率分别 2%、3%、5%。随机取一个零件是次品的概率多少？按来源分三类算，再加起来。这就是全概率。
  </div>

  <h3>10.1 完备事件组：把样本空间切块</h3>
  <p>若 $B_1,B_2,\dots,B_n$ 两两互斥、并起来是整个 $\Omega$、每个概率大于 0，就叫完备事件组（样本空间的一个划分）。想成把场地切成几块，不重叠，拼满全场。</p>
  <p>任何事件 A 都能按这几块切开：$A=(AB_1)\cup(AB_2)\cup\cdots\cup(AB_n)$。$B_i$ 不重叠，切开后的 $AB_i$ 也不重叠，可以用可加性把概率相加。</p>

  <h3>10.2 全概率公式的推导</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">切开、相加、换乘法</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$P(A)=P\left(\bigcup_{i=1}^n AB_i\right)$，因为 $B_i$ 拼满 $\Omega$，A 必然全落在其中。</p>
        <p>切开后的 $AB_i$ 两两互斥，按有限可加：$P(A)=\sum_{i=1}^n P(AB_i)$。</p>
        <p>每块用乘法公式：$P(AB_i)=P(B_i)P(A|B_i)$。</p>
        <p>合起来：$P(A)=\sum_{i=1}^n P(B_i)P(A|B_i)$。</p>
      </div>
    </div>
  </div>
  <div class="formula">$$P(A)=\sum_{i=1}^{n}P(B_i)P(A|B_i)$$</div>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">三家厂的次品率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$P(\text{次})=0.5\times0.02+0.3\times0.03+0.2\times0.05=0.01+0.009+0.01=0.029$。</p>
        <p>约 2.9%。三个来源各贡献 1.0%、0.9%、1.0%，合计 2.9%。</p>
      </div>
    </div>
  </div>

  <h3>10.3 贝叶斯公式：反过来推来源</h3>
  <p>条件反了：已知抽到次品，求它来自甲厂的概率。工厂质检常用，找到问题零件来源才能追责。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">定义出发，分母换全概率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>要求的量 $P(B_i|A)=\frac{P(AB_i)}{P(A)}$。</p>
        <p>分子用乘法公式：$P(AB_i)=P(B_i)P(A|B_i)$。</p>
        <p>分母用全概率公式：$P(A)=\sum_j P(B_j)P(A|B_j)$。</p>
        <p>合成即得。</p>
      </div>
    </div>
  </div>
  <div class="formula">$$P(B_i|A)=\frac{P(B_i)P(A|B_i)}{\sum_{j=1}^{n}P(B_j)P(A|B_j)}$$</div>
  <p>分子是"这一路的贡献"，分母是"所有路的总贡献"，比值是这一路占的份额。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">次品来自甲厂的概率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>分子 $0.5\times0.02=0.01$，分母 $0.029$，得 $P(\text{甲}|\text{次})=0.01/0.029\approx0.345$。</p>
        <p>乙：$0.009/0.029\approx0.310$。丙：$0.01/0.029\approx0.345$。三个加起来 1，分完。</p>
        <p>甲产量最大（50%），丙次品率最高（5%），两者贡献打平。贝叶斯要把产量和次品率乘起来再比。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">体检：患病率 0.5%、灵敏度 95%、误报 10%</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>记 D=患病，+ =阳性。$P(D)=0.005$，$P(+|D)=0.95$，$P(+|\bar D)=0.10$。</p>
        <p>分子（真病人被检出）：$0.005\times0.95=0.00475$。</p>
        <p>分母：$0.00475+0.995\times0.10=0.00475+0.0995=0.10425$。</p>
        <p>$P(D|+)=0.00475/0.10425\approx0.0456$。</p>
        <p>阳性之后真患病概率只有 4.6%。原因是有病的人本来就少（0.5%），健康人占 99.5%，健康人里 10% 的误报，绝对数量远大于真病人检出。0.0995 是 0.00475 的二十多倍。</p>
        <p>这就是基础率谬误：只看检测准确率不看患病率，会把 4.6% 误读成 95%。</p>
      </div>
    </div>
  </div>

  <h3>10.4 先验与后验</h3>
  <p>贝叶斯的分子分母结构可以读成一次更新：$P(B_i)$ 是看到数据之前的先验，$P(B_i|A)$ 是看到 A 之后的后验，$P(A|B_i)$ 叫似然，是这一路产生该数据的证据强度。</p>
  <p>公式做的事就是把先验按似然加权，再重新归一化。体检那题里，先验 0.005 被 0.95 的似然拉高，同时被健康人 0.0995 的总证据摊薄，落到 0.046。</p>

  <div class="callout callout-key">
    <div class="callout-title">两个公式的关系</div>
    全概率是"由原因推结果"：知道各路来源与条件概率，算结果的总概率。贝叶斯是"由结果推原因"：知道结果发生了，反推来源。方向相反，共用同一个乘法公式。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 两台机器产同一种零件，甲占 60%、废品率 1%；乙占 40%、废品率 2%。求废品率，以及废品来自乙的概率。</div>
    <div class="qa-a">废品率 $0.6\times0.01+0.4\times0.02=0.014$。乙贡献 0.008，占 $0.008/0.014\approx0.571$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 体检那题，患病率升到 10%，阳性后患病概率变成多少？</div>
    <div class="qa-a">分子 $0.1\times0.95=0.095$，分母 $0.095+0.9\times0.1=0.185$，$0.095/0.185\approx0.514$。先验变大，后验涨到约 51%。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 全概率公式的划分为什么必须拼满全场？</div>
    <div class="qa-a">不拼满的话，A 有一部分落在没切的区域，$P(A)$ 就漏算，公式不成立。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="independence">
  <div class="breadcrumb"></div>
  <h2><span class="num">11</span>独立性与伯努利概型</h2>
  <p class="lead">"一件事发生不影响另一件事"怎么写成公式？写出来就是乘法。这节讲独立性的定义、多事件相互独立的条件、与互斥的区别，最后引出 n 重独立试验与二项概率，为第二章铺路。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：条件概率（第 9 节）、乘法公式。后续：第 13 节二项分布、第 14 节二维独立、第 22 节连续型独立。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    抛两次硬币，第一次不影响第二次。知道第一次正面，第二次正面概率仍是 1/2。这就是独立。而"今天下雨"和"路上堵车"不独立：下雨天堵车概率比晴天大。
  </div>

  <h3>11.1 定义：条件概率等于无条件概率</h3>
  <p>若 A 发不发生不影响 B 的概率，就是 $P(B|A)=P(B)$。展开 $\frac{P(AB)}{P(A)}=P(B)$，两边乘 $P(A)$：</p>
  <div class="formula">$$P(AB)=P(A)P(B)$$</div>
  <p>这个式子不需要 $P(A)\gt0$，所以直接拿它当定义。若满足，称 A、B 相互独立。</p>
  <p>配套的两条可以推出来：独立时 A 与 $\bar B$ 也独立，$\bar A$ 与 $\bar B$ 也独立。因为 $P(A\bar B)=P(A)-P(AB)=P(A)-P(A)P(B)=P(A)(1-P(B))=P(A)P(\bar B)$。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">验</span><span class="derive-step-title">抛两枚硬币</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$A$=第一枚正面 $=\{(正,正),(正,反)\}$，$P(A)=1/2$。$B$=第二枚正面 $=\{(正,正),(反,正)\}$，$P(B)=1/2$。$AB=\{(正,正)\}$，$P(AB)=1/4$。</p>
        <p>$P(A)P(B)=\frac14=P(AB)$，独立。</p>
      </div>
    </div>
  </div>

  <h3>11.2 互斥与独立：完全不同的两件事</h3>
  <p>互斥是"不能同时发生"：$AB=\emptyset$，$P(AB)=0$。独立是"互相不影响"：$P(AB)=P(A)P(B)$。两者不是一回事，甚至互相排斥。只要 $P(A),P(B)$ 都大于 0，互斥时 $P(AB)=0\ne P(A)P(B)\gt0$，必不独立；独立时乘积大于 0，$AB$ 非空，不互斥。</p>
  <p>举例：掷骰子，A=点数 1，B=点数 2。互斥，一次只能出一个点。它们当然不独立：知道 A 发生，B 就不可能发生，概率从 1/6 变成 0，影响极大。</p>

  <h3>11.3 三个事件相互独立</h3>
  <p>三个事件相互独立，需要两两独立再加一条三者乘积：</p>
  <div class="formula">$$P(AB)=P(A)P(B),\ P(AC)=P(A)P(C),\ P(BC)=P(B)P(C),\ P(ABC)=P(A)P(B)P(C)$$</div>
  <p>只有两两独立不够。反例：盒里 4 个球，编号 110、101、011、000。A=第一位是 1，B=第二位是 1，C=第三位是 1，每个概率都是 1/2。任取两个同时为 1 的只有 1 个球，$P(AB)=1/4=P(A)P(B)$，两两独立成立。三个同时为 1 的球一个都没有，$P(ABC)=0\ne1/8$，所以三者不相互独立。</p>

  <h3>11.4 伯努利概型与二项概率</h3>
  <p>n 次试验，每次只关心成功/失败两种结果，成功概率固定为 p，各次相互独立，这套设定叫 n 重伯努利概型。问 n 次里恰好成功 k 次的概率。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先定位置，再乘概率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先数 k 次成功出现在哪几次：从 n 次里选 k 次，$C_n^k$ 种位置组合。</p>
        <p>固定一种位置（前 k 次成功、后 n-k 次失败），这条具体路径的概率是 $p^k(1-p)^{n-k}$，各次独立，概率连乘。</p>
        <p>每种位置的路径概率都一样，不同位置互斥，所以总数是 $C_n^k p^k(1-p)^{n-k}$。</p>
      </div>
    </div>
  </div>
  <div class="formula">$$P(\text{恰好 k 次成功})=C_n^k p^k(1-p)^{n-k},\quad k=0,1,\dots,n$$</div>
  <p>记 $q=1-p$，常写成 $C_n^k p^k q^{n-k}$。这就是第二章二项分布 $B(n,p)$ 的分布列。这里已经推出来了，第二章只是给名字和记号。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">投篮 5 次，命中率 0.6，恰好中 3 次</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$C_5^3\cdot0.6^3\cdot0.4^2=10\times0.216\times0.16$。</p>
        <p>$0.216\times0.16=0.03456$，乘 10 得 $0.3456$。</p>
        <p>核对归一化：$\sum_{k=0}^5 C_5^k0.6^k0.4^{5-k}=(0.6+0.4)^5=1$，用二项式定理验证，成立。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">第一章到这里结束</div>
    骨架回顾：样本空间装结果 → 公理定规则 → 性质提供公式 → 三种算法（古典、几何、条件）→ 独立性让乘法成立。第二章开始把"结果"换成数字。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $P(A)=0.5$，$P(B)=0.6$，$P(AB)=0.3$。A、B 独立吗？</div>
    <div class="qa-a">$P(A)P(B)=0.3=P(AB)$，独立。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 独立时 $\bar A$ 与 $\bar B$ 也独立吗？</div>
    <div class="qa-a">$P(\bar A\bar B)=1-P(A)-P(B)+P(AB)=1-P(A)-P(B)+P(A)P(B)=(1-P(A))(1-P(B))$，成立。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 掷 4 次硬币，恰好 2 次的概率。</div>
    <div class="qa-a">$C_4^2(1/2)^2(1/2)^2=6\times1/16=3/8$。</div>
  </div>

  <div class="chapter-nav"></div>
</section>
"""
