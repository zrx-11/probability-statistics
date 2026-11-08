#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 C 批：第二章 离散型随机变量"""

CH_C = r"""
<section class="chapter" id="discrete-rv">
  <div class="breadcrumb"></div>
  <h2><span class="num">12</span>随机变量与分布列</h2>
  <p class="lead">第一章的事件是文字描述（"至少一个正面"）。第二章把每个试验结果映射成一个数，用数来算，这就是随机变量。离散型的取值可数，用一张概率表记录全部信息。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：样本空间（第 5 节）、概率性质（第 7 节）、二项概率（第 11 节）。后续：常见分布（第 13 节）、期望（第 16 节）、分布函数（第 19 节）。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    骰子的面本来没有数，标上 1 到 6 之后才能算"点数之和"。随机变量干的就是这件事：把结果翻译成数，于是可以用加减乘除、求和、求平均。
  </div>

  <h3>12.1 随机变量的定义</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">定</span><span class="derive-step-title">ξ 是样本空间上的一个函数</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $\Omega$ 是样本空间。若对每个 $\omega\in\Omega$，都有一个实数 $\xi(\omega)$ 与之对应，就说 $\xi$ 是一个随机变量，记 $\xi\equiv\xi(\omega):\Omega\to\mathbb R$。</p>
        <p>它本质是一个函数，定义域是样本空间，值域是实数。</p>
        <p>如果 $\xi$ 只取有限个或可列个值，就叫离散型随机变量。可列的意思是能排成一列 $x_1,x_2,\dots$，每个都能数到，包括"无限但可数"（比如 1,2,3,…）。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">为什么用 ξ 而不用 x</div>
    课件记号里 $\xi$ 表示随机变量，x 表示它取到的某个具体数值。这个区分很重要：$\xi$ 是"还没掷的骰子"，x 是"掷出来的 3"。$P(\xi=x_k)=p_k$ 说的是随机变量落在具体值 $x_k$ 上的概率。本课全程沿用课件记号，随机变量用 $\xi,\eta$，不用常见的 X、Y。
  </div>

  <h3>12.2 分布列：把概率列成表</h3>
  <p>离散型随机变量 $\xi$ 的取值是 $x_1,x_2,\dots$，每个值对应一个概率 $p_k=P(\xi=x_k)$。这串概率构成分布列，记作</p>
  <div class="table-wrap">
  <table>
    <tr><th>$\xi$</th><th>$x_1$</th><th>$x_2$</th><th>$\cdots$</th><th>$x_k$</th><th>$\cdots$</th></tr>
    <tr><td>$P$</td><td>$p_1$</td><td>$p_2$</td><td>$\cdots$</td><td>$p_k$</td><td>$\cdots$</td></tr>
  </table>
  </div>
  <p>课件也给矩阵写法：$\begin{pmatrix}x_1&x_2&\cdots&x_k&\cdots\\ p_1&p_2&\cdots&p_k&\cdots\end{pmatrix}$，第一行取值，第二行概率，上下对齐。两种写法等价。</p>
  <p>分布列必须满足两条，来自公理：</p>
  <div class="formula">$$p_k\ge0,\qquad \sum_{k}p_k=1$$</div>
  <p>第一条是非负性。第二条是规范性：取值互斥且拼满样本空间，按可列可加性，概率之和等于 $P(\Omega)=1$。</p>

  <div class="callout callout-key">
    <div class="callout-title">为什么分布列就"完整描述"了 ξ</div>
    知道分布列，就能算任何关于 $\xi$ 的事件的概率。比如"$\xi$ 落在集合 B 里"的概率，就是把 B 里那些 $x_k$ 对应的 $p_k$ 加起来：$P(\xi\in B)=\sum_{x_k\in B}p_k$。各取值互斥，可加性保证这个加法合法。后面所有计算都从分布列出发。
  </div>

  <h3>12.3 从试验翻译成分布列</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">掷一颗均匀骰子</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Omega=\{1,\dots,6\}$，令 $\xi(\omega)=\omega$，就是点数本身。取值 1 到 6，每点概率 $1/6$。</p>
        <p>校验 $\sum p_k=6\times1/6=1$。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">抛 3 枚硬币，数正面个数</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\Omega$ 有 8 个样本点。令 $\xi$=正面个数，取值 0、1、2、3。</p>
        <p>$\xi=0$：只有（反反反）1 个点，$1/8$。$\xi=1$：$C_3^1=3$ 个点，$3/8$。$\xi=2$：$3/8$。$\xi=3$：$1/8$。</p>
        <p>校验：$1/8+3/8+3/8+1/8=1$。这就是 $B(3,1/2)$，第 13 节给名字。</p>
      </div>
    </div>
  </div>

  <h3>12.4 规范性是一道保险</h3>
  <p>如果某张表写着 $p_1=0.4$、$p_2=0.4$、$p_3=0.4$，加起来 1.2，这不是分布列。它违反公理 2，不可能对应任何真实随机变量。做题时算出概率之和不是 1，一定是中间算错或者漏了取值，回头查。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 掷骰子，令 $\xi=1$ 表示点数为奇数，$\xi=0$ 表示偶数。写出分布列。</div>
    <div class="qa-a">$P(\xi=1)=3/6=1/2$，$P(\xi=0)=3/6=1/2$，和为一。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么说 ξ 是函数，不是变量？</div>
    <div class="qa-a">它给每个样本点 $\omega$ 指定一个数值 $\xi(\omega)$，符合函数定义。叫"变量"是历史习惯，强调取值随结果而变。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 分布列里能出现负概率吗？</div>
    <div class="qa-a">不能，违反非负公理。概率一定在 0 到 1 之间。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="common-discrete">
  <div class="breadcrumb"></div>
  <h2><span class="num">13</span>常见离散分布</h2>
  <p class="lead">五个反复出现的分布：0-1 分布、二项分布、泊松分布、几何分布、超几何分布。每个都从实际场景推出来，不背公式。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：分布列（第 12 节）、二项概率（第 11 节）、e 与级数（第 3 节）。后续：期望方差（第 16、17 节）、泊松定理的应用。
  </div>

  <h3>13.1 0-1 分布</h3>
  <p>只做一次试验，只关心成不成。$\xi=1$ 表示成功，概率 p；$\xi=0$ 表示失败，概率 $q=1-p$。分布列：</p>
  <div class="table-wrap">
  <table>
    <tr><th>$\xi$</th><th>0</th><th>1</th></tr>
    <tr><td>$P$</td><td>$1-p$</td><td>$p$</td></tr>
  </table>
  </div>
  <p>它是一切离散分布的零件：二项分布就是 n 个 0-1 分布加起来。</p>

  <h3>13.2 二项分布 $B(n,p)$</h3>
  <p>第 11 节推过：n 重独立试验，每次成功概率 p，恰好成功 k 次的概率</p>
  <div class="formula">$$P(\xi=k)=C_n^k p^k q^{n-k},\quad k=0,1,\dots,n,\ q=1-p$$</div>
  <p>记 $\xi\sim B(n,p)$，读作"ξ 服从参数 n、p 的二项分布"。</p>
  <p>规范性用二项式定理验证：$\sum_{k=0}^n C_n^k p^kq^{n-k}=(p+q)^n=1$。这就是第 2 节讲二项式定理的用处。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">10 道选择题四选一，全靠蒙，答对 6 题以上</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$p=1/4$，$q=3/4$，$n=10$，要求 $P(\xi\ge6)=\sum_{k=6}^{10}C_{10}^k(0.25)^k(0.75)^{10-k}$。</p>
        <p>逐项：k=6 得 $210\times0.0002441\times0.17798\approx0.01622$；k=7 得 $120\times0.0000610\times0.23730\approx0.00174$；k=8 得 $45\times0.00001526\times0.31640\approx0.000217$；k=9 得 $10\times0.00000381\times0.42188\approx0.0000161$；k=10 得 $0.000000954$。</p>
        <p>相加约 $0.0180$。全靠蒙拿到 6 题以上的机会不到 2%。（以上为按二项公式逐项手算的结果。）</p>
      </div>
    </div>
  </div>

  <h3>13.3 泊松分布 $P(\lambda)$</h3>
  <p>场景：一段时间内电话呼入次数、一页书的错字数、一定面积内的粒子数。特点是发生次数多、每次概率小、彼此独立。分布列：</p>
  <div class="formula">$$P(\xi=k)=\frac{\lambda^k}{k!}e^{-\lambda},\quad k=0,1,2,\dots,\ \lambda\gt0$$</div>
  <p>$\lambda$ 是平均发生次数。这个公式从二项分布的极限推出来。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">让 $n\to\infty$、$np\to\lambda$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设 $np=\lambda$ 固定，则 $p=\lambda/n$，$q=1-\lambda/n$。第 k 项是 $C_n^k(\lambda/n)^k(1-\lambda/n)^{n-k}$。</p>
        <p>拆三块：$C_n^k(\lambda/n)^k=\frac{\lambda^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}$。</p>
        <p>后面那串有 k 个因子，每个都趋于 1，留下 $\frac{\lambda^k}{k!}$。</p>
        <p>第二块 $(1-\lambda/n)^{-k}\to1$。第三块 $(1-\lambda/n)^n\to e^{-\lambda}$，是第 3 节 e 的极限定义的变形。</p>
        <p>三块相乘得 $\frac{\lambda^k}{k!}e^{-\lambda}$。</p>
        <p>规范性：$\sum_{k\ge0}\frac{\lambda^k}{k!}e^{-\lambda}=e^\lambda\cdot e^{-\lambda}=1$，用的是第 3 节的 $e^x$ 级数，取 x=λ。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">为什么要有泊松分布</div>
    二项分布要指定 n 和 p 两个参数，但很多场景只知道"平均几次"，不知道总试验次数。比如一小时内的电话呼入，"潜在呼入次数"根本数不清。泊松分布只要一个平均数 $\lambda$，就覆盖了这类场景。数学上它是二项分布在 n 很大、p 很小时的极限。
  </div>

  <h3>13.4 几何分布 $Ge(p)$</h3>
  <p>场景：反复试验直到第一次成功，问总共做了几次。第 k 次才成功，意味着前 k-1 次全失败、第 k 次成功。各次独立，概率连乘：</p>
  <div class="formula">$$P(\xi=k)=q^{k-1}p,\quad k=1,2,3,\dots$$</div>
  <p>规范性：$\sum_{k\ge1}q^{k-1}p=\frac{p}{1-q}=\frac{p}{p}=1$，用的是等比级数（第 3 节）。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">无记忆性</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>问：已经失败了 m 次，再等 k 次的概率是多少？也就是求 $P(\xi=m+k\mid\xi\gt m)$。</p>
        <p>先算分子：$\{\xi=m+k\}$ 与 $\{\xi\gt m\}$ 有交集吗？$\xi=m+k$ 一定大于 m，所以交集就是 $\{\xi=m+k\}$ 本身。分子 $P(\xi=m+k)=q^{m+k-1}p$。</p>
        <p>分母：$P(\xi\gt m)$ 是"前 m 次全失败"，$=q^m$。</p>
        <p>比值：$\frac{q^{m+k-1}p}{q^m}=q^{k-1}p=P(\xi=k)$。</p>
        <p>结论：已经失败了 m 次，对"还要再等几次"的分布没有任何影响。几何分布"忘掉"了已经失败的历史。这叫无记忆性。</p>
      </div>
    </div>
  </div>
  <p>无记忆性反直觉：抛硬币连出 10 次反面，第 11 次正面的概率还是 1/2（若 p=1/2）。硬币没有记忆，不会"觉得该出正面了"。</p>

  <h3>13.5 超几何分布 $H(N,M,n)$</h3>
  <p>场景：N 件产品里有 M 件次品，不放回抽 n 件，其中恰好 k 件次品。总数用组合算：分母 $C_N^n$，分子"从 M 件次品里取 k 件、从 N-M 件正品里取 n-k 件"：</p>
  <div class="formula">$$P(\xi=k)=\frac{C_M^k C_{N-M}^{n-k}}{C_N^n},\quad k=0,1,\dots,\min(n,M)$$</div>
  <p>它与二项分布的区别：二项是有放回（各次独立），超几何是无放回（各次不独立）。N 很大、n 相对很小时，两者数值非常接近，实务中常用二项近似超几何。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">10 件产品 3 件次品，抽 2 件，恰有 1 件次品</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>分母 $C_{10}^2=45$。分子 $C_3^1C_7^1=3\times7=21$。概率 $21/45=7/15\approx0.4667$。</p>
        <p>用二项近似：$p=0.3$，$n=2$，$C_2^1\cdot0.3\cdot0.7=0.42$。差 0.047，因为 N=10 太小，近似不够好。</p>
      </div>
    </div>
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 某路口每分钟平均 2 辆车通过。求一分钟内恰好 3 辆的概率（按泊松）。</div>
    <div class="qa-a">$\lambda=2$，$P=\frac{2^3}{3!}e^{-2}=\frac{8}{6}\times0.1353\approx0.1804$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 投篮命中率 0.3，直到投进为止，求第 4 次才进的概率。</div>
    <div class="qa-a">$q^3p=0.7^3\times0.3=0.343\times0.3=0.1029$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 二项分布和泊松分布的关系是什么？</div>
    <div class="qa-a">泊松是二项在 n 大、p 小时的极限：固定 $np=\lambda$，让 $n\to\infty$。所以大量重复、单次概率很小的事件常用泊松。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="discrete-2d">
  <div class="breadcrumb"></div>
  <h2><span class="num">14</span>二维离散：联合、边缘与独立</h2>
  <p class="lead">两个随机变量一起看，需要一张二维表。行是 ξ 的取值，列是 η 的取值，格子是两者同时发生的概率。从这张表能读出各自的分布（边缘分布），也能判断两者是否独立。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：一维分布列（第 12 节）、独立性（第 11 节）。后续：第 15 节二元函数分布、第 16 节期望的线性性、第 23 节二维连续。
  </div>

  <h3>14.1 联合分布列</h3>
  <p>$(\xi,\eta)$ 的取值是有限或可列的格子 $(x_i,y_j)$，定义 $p_{ij}=P(\xi=x_i,\eta=y_j)$。把所有格子列成表：</p>
  <div class="table-wrap">
  <table>
    <tr><th>$\xi\backslash\eta$</th><th>$y_1$</th><th>$y_2$</th><th>$\cdots$</th><th>$y_j$</th><th>$\cdots$</th><th>行和</th></tr>
    <tr><td>$x_1$</td><td>$p_{11}$</td><td>$p_{12}$</td><td>$\cdots$</td><td>$p_{1j}$</td><td>$\cdots$</td><td>$p_{1\cdot}$</td></tr>
    <tr><td>$x_2$</td><td>$p_{21}$</td><td>$p_{22}$</td><td>$\cdots$</td><td>$p_{2j}$</td><td>$\cdots$</td><td>$p_{2\cdot}$</td></tr>
    <tr><td>$\vdots$</td><td>$\vdots$</td><td>$\vdots$</td><td></td><td>$\vdots$</td><td></td><td>$\vdots$</td></tr>
    <tr><td>$x_i$</td><td>$p_{i1}$</td><td>$p_{i2}$</td><td>$\cdots$</td><td>$p_{ij}$</td><td>$\cdots$</td><td>$p_{i\cdot}$</td></tr>
    <tr><td>列和</td><td>$p_{\cdot1}$</td><td>$p_{\cdot2}$</td><td>$\cdots$</td><td>$p_{\cdot j}$</td><td>$\cdots$</td><td>$1$</td></tr>
  </table>
  </div>
  <p>两条要求：$p_{ij}\ge0$，$\sum_i\sum_j p_{ij}=1$。这是二维版本的非负性与规范性。</p>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    一个班级的体检表：行是身高档，列是体重档，格子是"身高在这一档且体重在这一档"的人数比例。行和是身高分布，列和是体重分布，整张表加起来是 100%。联合分布表就是这个结构。
  </div>

  <h3>14.2 边缘分布：把另一维"抹掉"</h3>
  <p>只关心 $\xi$，不关心 $\eta$ 取什么。那就把同一行的所有格子加起来（固定 $\xi=x_i$，$\eta$ 可以是任何值，这些情况互斥）：</p>
  <div class="formula">$$p_{i\cdot}=P(\xi=x_i)=\sum_{j}p_{ij},\qquad p_{\cdot j}=\sum_{i}p_{ij}$$</div>
  <p>行和给 ξ 的边缘分布，列和给 η 的边缘分布。名字叫"边缘"，因为算出来的数正好写在这张表的右边和下边。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">为什么可以这样加</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>事件 $\{\xi=x_i\}$ 可以拆成 $\{\xi=x_i,\eta=y_1\}\cup\{\xi=x_i,\eta=y_2\}\cup\cdots$。</p>
        <p>不同的 $y_j$ 互斥，所以拆开的几块互斥。</p>
        <p>按可列可加：$P(\xi=x_i)=\sum_j P(\xi=x_i,\eta=y_j)=\sum_j p_{ij}$。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">一张两行两列的表</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$p_{11}=0.2$、$p_{12}=0.3$、$p_{21}=0.4$、$p_{22}=0.1$。总和 1.0。</p>
        <p>ξ 的边缘：$p_{1\cdot}=0.5$，$p_{2\cdot}=0.5$。η 的边缘：$p_{\cdot1}=0.6$，$p_{\cdot2}=0.4$。</p>
        <p>注意边缘分布与联合分布是两件事：知道边缘不能还原联合（这里可能还有别的表给出同样的边缘，见 14.4）。</p>
      </div>
    </div>
  </div>

  <h3>14.3 独立性：格子概率等于行和乘列和</h3>
  <p>ξ、η 独立，按第 11 节的定义，对任意 i、j 都有 $P(\xi=x_i,\eta=y_j)=P(\xi=x_i)P(\eta=y_j)$，即</p>
  <div class="formula">$$p_{ij}=p_{i\cdot}\cdot p_{\cdot j}$$</div>
  <p>用上面那张表检查：$p_{11}=0.2$，而 $p_{1\cdot}p_{\cdot1}=0.5\times0.6=0.3$，不等，所以不独立。而且只要有一个格子不满足，就不独立，不用检查全部。</p>

  <div class="callout callout-key">
    <div class="callout-title">独立性的判定顺序</div>
    先算边缘，再挑一个格子比对乘积。不相等就判不独立，可以提前结束。相等才需要继续检查剩下所有格子。判断"独立"比判断"不独立"费事，因为后者只要一个反例。
  </div>

  <h3>14.4 边缘相同、独立不同：一个反例</h3>
  <p>下面两张表边缘分布完全一样，但独立性不同。</p>
  <p>表一：$p_{11}=0.2$、$p_{12}=0.3$、$p_{21}=0.4$、$p_{22}=0.1$。边缘都是 0.5 和 0.6/0.4，不独立。</p>
  <p>表二：$p_{11}=0.3$、$p_{12}=0.2$、$p_{21}=0.3$、$p_{22}=0.2$。边缘也是 0.5、0.5 和 0.6、0.4，并且每个格子都等于 $p_{i\cdot}p_{\cdot j}$（例如 $0.5\times0.6=0.3$），独立。</p>
  <p>这说明边缘分布不携带"两者关系"的信息，联合分布才携带。这是一个必须记住的点。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 表：$p_{11}=0.1$、$p_{12}=0.2$、$p_{21}=0.3$、$p_{22}=0.4$。求边缘，判断独立。</div>
    <div class="qa-a">ξ 边缘 0.3、0.7；η 边缘 0.4、0.6。$p_{11}=0.1$，而 $0.3\times0.4=0.12$，不等，不独立。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么边缘分布不能还原联合分布？</div>
    <div class="qa-a">同一组边缘可以配出多张不同的联合表（见 14.4）。把行和列"摊平"的过程丢失了两者的关联信息。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="discrete-func">
  <div class="breadcrumb"></div>
  <h2><span class="num">15</span>随机变量函数的分布（离散）</h2>
  <p class="lead">已知 ξ 的分布，问 ξ 的函数 $\eta=g(\xi)$ 服从什么分布。离散情形只需做一件事：把映射到同一个 y 的那些 x 的概率全部加起来。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：分布列（第 12 节）、二维联合（第 14 节）。后续：第 24 节连续型的函数分布、第 26 节特征函数的变换思路。
  </div>

  <h3>15.1 为什么不能直接搬</h3>
  <p>如果 $g$ 是一一对应的（不同的 x 映射到不同的 y），那把每个 $p_k$ 搬到对应的 y 上就行，概率一个不少。</p>
  <p>问题出在"多对一"。比如 $\eta=\xi^2$，$\xi=-1$ 和 $\xi=1$ 都映射到 $\eta=1$。这时 $\eta=1$ 的概率不是其中一个，而是两个概率之和：这两个情况互斥，合起来才是"$\eta=1$"这个事件。</p>
  <div class="formula">$$p_\eta(y)=P(\eta=y)=P(g(\xi)=y)=\sum_{x_k:\,g(x_k)=y}p_k$$</div>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\xi$ 的分布与 $\eta=\xi^2$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>ξ 取值 $-1,0,1,2$，概率依次 $0.2,0.3,0.1,0.4$。校验：$0.2+0.3+0.1+0.4=1$。</p>
        <p>平方后取值：$(-1)^2=1$，$0^2=0$，$1^2=1$，$2^2=4$。所以 η 只取 0、1、4。</p>
        <p>$\eta=0$：只有 $\xi=0$，概率 0.3。</p>
        <p>$\eta=1$：$\xi=-1$ 与 $\xi=1$ 两个来源，概率 $0.2+0.1=0.3$。</p>
        <p>$\eta=4$：只有 $\xi=2$，概率 0.4。</p>
        <p>校验：$0.3+0.3+0.4=1$。分布列没有漏掉任何概率。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">同一张表上的 $\eta=|\xi|$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>绝对值后：$|-1|=1$、$|0|=0$、$|1|=1$、$|2|=2$。取值 0、1、2。</p>
        <p>$\eta=0$：0.3。$\eta=1$：$0.2+0.1=0.3$。$\eta=2$：0.4。</p>
        <p>与平方的例子结果一样（在这张表上巧合，因为正负对称的部分刚好相同）。换一张概率表结果就会不同，所以不能记结论，只能每次算。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">线性变换 $\eta=a\xi+b$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>线性变换一定是一一对应（$a\ne0$），所以每个概率直接搬：$P(\eta=ax_k+b)=p_k$。</p>
        <p>例如 $\xi$ 取 1、2、3，概率 0.2、0.5、0.3，则 $\eta=2\xi+1$ 取 3、5、7，概率仍是 0.2、0.5、0.3。取值变了，概率没变。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">"合并同值"是本节的唯一动作</div>
    后面第三章的连续情形会换一套工具（分布函数法、密度变换公式），但本质是同一件事：把映射到同一结果的概率"汇总"。离散能直接加，连续要积，区别在这里。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. ξ 取 $-2,-1,0,1,2$，概率各 0.2。求 $\eta=|\xi|$ 的分布列。</div>
    <div class="qa-a">$\eta=0$：0.2。$\eta=1$：$0.2+0.2=0.4$。$\eta=2$：$0.2+0.2=0.4$。和 1。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么线性变换不用合并同值？</div>
    <div class="qa-a">$a\ne0$ 时 $a x_1+b=a x_2+b$ 只有 $x_1=x_2$，不同取值不会撞在一起。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="expectation">
  <div class="breadcrumb"></div>
  <h2><span class="num">16</span>数学期望</h2>
  <p class="lead">期望就是"按概率加权的平均值"。它回答"长期做很多次，平均会得到多少"。本节从定义出发，把线性性、独立时的乘积性、以及几个常见分布的期望都推出来。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：分布列（第 12 节）、常见分布（第 13 节）、Σ 与级数（第 3 节）。后续：方差（第 17 节）、条件期望（第 18 节）、大数定律（第 25 节）。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    考试有 10% 概率拿 100 分、30% 拿 80 分、60% 拿 60 分。平均分不是 $(100+80+60)/3=80$，而是按概率加权：$100\times0.1+80\times0.3+60\times0.6=10+24+36=70$。这就是期望：概率大的分数权重更大。
  </div>

  <h3>16.1 定义</h3>
  <p>离散型随机变量 $\xi$ 取 $x_k$、概率 $p_k$。若级数 $\sum_k|x_k|p_k$ 收敛（保证不会加出无穷），定义</p>
  <div class="formula">$$E\xi=\sum_{k}x_k p_k$$</div>
  <p>读作"ξ 的数学期望"。加权平均的"权"就是概率。物理上它是质量的质心：把 $p_k$ 看成质量、$x_k$ 看成位置，$E\xi$ 就是重心。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">均匀骰子</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E\xi=\sum_{k=1}^6 k\cdot\frac16=\frac{1+2+3+4+5+6}{6}=\frac{21}{6}=3.5$。</p>
        <p>3.5 不是骰子能掷出的值。期望是"平均位置"，不必是取值之一。这一点初学者最容易搞混。</p>
      </div>
    </div>
  </div>

  <h3>16.2 线性性质</h3>
  <p>常数的期望是它本身：$E(c)=c$。更一般地：</p>
  <div class="formula">$$E(a\xi+b)=aE\xi+b$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">从定义出发，只做分配律</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E(a\xi+b)=\sum_k(ax_k+b)p_k$。</p>
        <p>拆成两项：$=\sum_k ax_kp_k+\sum_k bp_k$。</p>
        <p>第一项 $a\sum x_kp_k=aE\xi$，把常数 a 提出求和。第二项 $b\sum p_k=b\cdot1=b$，用规范性。</p>
        <p>合起来 $aE\xi+b$。</p>
      </div>
    </div>
  </div>

  <h3>16.3 和的期望等于期望的和</h3>
  <div class="formula">$$E(\xi+\eta)=E\xi+E\eta$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">用联合分布列，交换求和顺序</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E(\xi+\eta)=\sum_i\sum_j(x_i+y_j)p_{ij}$。</p>
        <p>拆成两个和：$\sum_i\sum_j x_ip_{ij}+\sum_i\sum_j y_jp_{ij}$。</p>
        <p>第一项里 $x_i$ 不含 j，先对 j 求和：$\sum_i x_i\left(\sum_j p_{ij}\right)=\sum_i x_ip_{i\cdot}=E\xi$。</p>
        <p>第二项同理，先对 i 求和得 $\sum_j y_jp_{\cdot j}=E\eta$。</p>
        <p>合起来 $E\xi+E\eta$。全程没有用到独立性，所以对任何两个随机变量都成立。</p>
      </div>
    </div>
  </div>
  <p>这条极强：不需要独立、不需要相关，加法永远可以拆。它是后面"用指示变量算期望"的全部基础。</p>

  <h3>16.4 独立时乘积的期望等于期望的乘积</h3>
  <div class="formula">$$E(\xi\eta)=E\xi\cdot E\eta\quad(\xi,\eta\text{ 独立})$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">把联合概率换成行列乘积</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E(\xi\eta)=\sum_i\sum_j x_iy_jp_{ij}$。</p>
        <p>独立给出 $p_{ij}=p_{i\cdot}p_{\cdot j}$，代入。</p>
        <p>此时被求和的式子分成"只含 i"和"只含 j"两部分：$\sum_i x_ip_{i\cdot}\sum_j y_jp_{\cdot j}$。</p>
        <p>两个因子分别是 $E\xi$ 和 $E\eta$，得乘积。注意这一步依赖独立，不独立时不能拆。</p>
      </div>
    </div>
  </div>
  <p>反例说明独立性不能省：$\xi$ 取 $-1,1$ 各 1/2，$\eta=\xi^2=1$ 恒为 1。$E\xi=0$，$E\eta=1$，$E\xi E\eta=0$。而 $E(\xi\eta)=E(\xi\cdot\xi^2)=E(\xi^3)$，$\xi^3$ 取 $-1,1$ 各 1/2，期望 0。这里凑巧相等，换 $\eta=\xi$ 试试：$E(\xi^2)=1\ne0$，确实是 0 对 1，不等。$\xi$ 与 $\xi$ 当然不独立。</p>

  <h3>16.5 常见分布的期望</h3>
  <p><b>0-1 分布</b>：$E\xi=0\cdot q+1\cdot p=p$。</p>
  <p><b>二项分布</b> $B(n,p)$：$E\xi=np$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">用 $kC_n^k=nC_{n-1}^{k-1}$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E\xi=\sum_{k=0}^n kC_n^kp^kq^{n-k}$。k=0 的项是 0，从 k=1 开始。</p>
        <p>用恒等式 $kC_n^k=nC_{n-1}^{k-1}$（含义：从 n 人里选 k 人，再指定一人当队长，等于先指定队长再从剩下 n-1 人选 k-1 个队员）。</p>
        <p>代入：$E\xi=n\sum_{k=1}^n C_{n-1}^{k-1}p^kq^{n-k}$。令 $j=k-1$，$p^k=p\cdot p^j$，$n-k=n-1-j$。</p>
        <p>$=np\sum_{j=0}^{n-1}C_{n-1}^jp^jq^{(n-1)-j}=np(p+q)^{n-1}=np$。</p>
      </div>
    </div>
  </div>
  <p><b>泊松分布</b> $E\xi=\lambda$：$E\xi=\sum_{k\ge0}k\frac{\lambda^k}{k!}e^{-\lambda}$。k=0 项为 0，从 k=1 起，用 $k/k!=1/(k-1)!$，得 $\lambda e^{-\lambda}\sum_{k\ge1}\frac{\lambda^{k-1}}{(k-1)!}=\lambda e^{-\lambda}e^{\lambda}=\lambda$。</p>
  <p><b>几何分布</b> $E\xi=1/p$：$\sum_{k\ge1}kq^{k-1}p=p\sum_{k\ge1}kq^{k-1}$。第 3 节讲过等比级数求导：$\sum_{k\ge1}kq^{k-1}=\frac{1}{(1-q)^2}=\frac{1}{p^2}$。所以 $E\xi=p\cdot\frac{1}{p^2}=\frac1p$。命中率 0.5 时，平均要投 2 次。</p>
  <p><b>超几何</b> $E\xi=n\frac{M}{N}$：把"第 i 件被抽中"写成一个 0-1 指示变量 $\xi_i$，它的期望是抽中概率 $M/N$。总数 $\sum\xi_i$ 的期望按线性性等于 $n\cdot M/N$，不需要考虑不独立。</p>

  <div class="callout callout-key">
    <div class="callout-title">指示变量法：把复杂问题拆成 0-1</div>
    凡是要算"有多少个满足某条件"的期望，都把每个个体拆成一个 0-1 变量，期望相加。因为加法不需要独立，所以哪怕个体之间高度相关（比如不放回抽样），答案照样对。这是期望比方差好算的根本原因。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. ξ 取值 $-1,0,1$，概率 0.3、0.4、0.3，求 Eξ 与 E(ξ²)。</div>
    <div class="qa-a">$E\xi=-0.3+0+0.3=0$。$E\xi^2=1\times0.3+0+1\times0.3=0.6$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 掷两颗骰子，点数之和的期望是多少？</div>
    <div class="qa-a">每颗期望 3.5，按线性性相加：7。不用算和的分布。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 期望一定是随机变量能取到的值吗？</div>
    <div class="qa-a">不一定。骰子期望 3.5，取不到。期望是长期平均位置，不是一次试验的结果。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="variance">
  <div class="breadcrumb"></div>
  <h2><span class="num">17</span>方差</h2>
  <p class="lead">期望只描述"中心在哪"，描述不了"散得多开"。两个班平均分都是 75，一个班都在 73 到 77 之间，另一个班 50 到 100 都有。方差就是量这个分散程度的数。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：期望及其性质（第 16 节）。后续：切比雪夫不等式（第 25 节）、协方差（第 25 节）、回归。
  </div>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    一班成绩 78、79、80、81、82，平均 80，大家都贴着平均。二班 60、70、80、90、100，平均也是 80，但离平均远得多。方差就是把"每个数与平均的距离"平方后求平均，二班的更大。
  </div>

  <h3>17.1 定义</h3>
  <div class="formula">$$D\xi=E(\xi-E\xi)^2=\sum_k(x_k-E\xi)^2p_k$$</div>
  <p>读作"ξ 的方差"。步骤：先算期望，再看每个取值偏离期望多少，平方（让正负都变正、并且放大远的偏差），按概率加权平均。</p>
  <p>为什么不直接取绝对值？因为平方可导，后面求最值、做代数变形方便；而且平方放大远端的偏差，更敏感。</p>
  <p>$\sqrt{D\xi}$ 叫标准差，单位和 ξ 一样，比方差好解释。</p>

  <h3>17.2 计算公式：$D\xi=E\xi^2-(E\xi)^2$</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">展开平方，逐项求和</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$D\xi=\sum_k(x_k-E\xi)^2p_k$。把平方展开：$(x_k-E\xi)^2=x_k^2-2x_kE\xi+(E\xi)^2$。</p>
        <p>三项分别求和：$\sum x_k^2p_k-2E\xi\sum x_kp_k+(E\xi)^2\sum p_k$。</p>
        <p>第一项是 $E\xi^2$。第二项里 $\sum x_kp_k=E\xi$，所以这一项是 $-2(E\xi)(E\xi)=-2(E\xi)^2$。第三项是 $(E\xi)^2\cdot1$。</p>
        <p>合起来：$E\xi^2-2(E\xi)^2+(E\xi)^2=E\xi^2-(E\xi)^2$。</p>
        <p>注意 $E\xi$ 是常数，可以提出求和号；$(E\xi)^2$ 也是常数。</p>
      </div>
    </div>
  </div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">两个班</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>一班取值 78、79、80、81、82，各概率 0.2。$E\xi=80$。偏差 $-2,-1,0,1,2$，平方 $4,1,0,1,4$。</p>
        <p>$D\xi=(4+1+0+1+4)\times0.2=10\times0.2=2$。标准差 $\sqrt2\approx1.41$。</p>
        <p>二班取值 60、70、80、90、100，各 0.2。$E\xi=80$。偏差 $-20,-10,0,10,20$，平方 $400,100,0,100,400$。</p>
        <p>$D\xi=(400+100+0+100+400)\times0.2=1000\times0.2=200$。标准差 $\sqrt{200}\approx14.1$，是一班的十倍。</p>
        <p>用另一条公式验算二班：$E\xi^2=(3600+4900+6400+8100+10000)\times0.2=6800$。$D\xi=6800-80^2=6800-6400=200$，一致。</p>
      </div>
    </div>
  </div>

  <h3>17.3 性质</h3>
  <p>常数的方差是 0：$D(c)=0$，因为常数离自己的距离恒为 0。</p>
  <div class="formula">$$D(a\xi+b)=a^2D\xi$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先算新期望，再套定义</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$a\xi+b$ 的期望是 $aE\xi+b$（第 16 节的线性性）。</p>
        <p>代入定义：$D(a\xi+b)=E\left[(a\xi+b)-(aE\xi+b)\right]^2$。</p>
        <p>方括号里 b 抵消：$=E\left[a(\xi-E\xi)\right]^2$。</p>
        <p>平方把 a 提出来变成 $a^2$：$=a^2E(\xi-E\xi)^2=a^2D\xi$。</p>
        <p>关键：平移 b 不改变分散程度（整班都加 5 分，差距不变），所以 b 不出现；乘以 a 把差距放大 a 倍，平方后变成 $a^2$。</p>
      </div>
    </div>
  </div>
  <p>注意 $D(\xi+\eta)$ 只有在独立时才等于 $D\xi+D\eta$。不独立时要多减两倍协方差，第 25 节会讲。</p>

  <h3>17.4 常见分布的方差</h3>
  <p><b>0-1 分布</b>：$D\xi=pq$。验算：$E\xi^2=p$（因为 $1^2=1$），$D=p-p^2=p(1-p)=pq$。</p>
  <p><b>二项分布</b> $D\xi=npq$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先算 Eξ²，再用公式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>把 $k^2$ 写成 $k(k-1)+k$，这样能用两次组合恒等式。</p>
        <p>$E\xi^2=\sum k(k-1)C_n^kp^kq^{n-k}+\sum kC_n^kp^kq^{n-k}$。</p>
        <p>第一项用 $k(k-1)C_n^k=n(n-1)C_{n-2}^{k-2}$，得 $n(n-1)p^2(p+q)^{n-2}=n(n-1)p^2$。</p>
        <p>第二项就是 $E\xi=np$。</p>
        <p>所以 $E\xi^2=n(n-1)p^2+np$，$D\xi=E\xi^2-(E\xi)^2=n(n-1)p^2+np-n^2p^2$。</p>
        <p>整理：$np[(n-1)p+1-np]=np(1-p)=npq$。</p>
      </div>
    </div>
  </div>
  <p><b>泊松分布</b> $D\xi=\lambda$。同样用 $k^2=k(k-1)+k$：$\sum k(k-1)\frac{\lambda^k}{k!}e^{-\lambda}=\lambda^2e^{-\lambda}\sum\frac{\lambda^{k-2}}{(k-2)!}=\lambda^2$。加 $E\xi=\lambda$，得 $E\xi^2=\lambda^2+\lambda$，$D=\lambda^2+\lambda-\lambda^2=\lambda$。均值方差相等，是泊松的标志。</p>
  <p><b>几何分布</b> $D\xi=\frac{q}{p^2}$。计算 $E\xi^2$ 要用 $\sum k^2q^{k-1}=\frac{1+q}{(1-q)^3}$，得 $E\xi^2=\frac{1+q}{p^2}$，减 $1/p^2$ 余 $q/p^2$。</p>

  <h3>17.5 标准化</h3>
  <p>把 ξ 变成 $\xi^*=\frac{\xi-E\xi}{\sqrt{D\xi}}$，则 $E\xi^*=0$、$D\xi^*=1$。验算：$E\xi^*=\frac{E\xi-E\xi}{\sqrt{D\xi}}=0$；$D\xi^*=\frac{D\xi}{D\xi}=1$。这叫标准化，正态分布查表前都要先做这一步。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. ξ 取值 0、1、2，概率 0.4、0.2、0.4。求 Eξ、Dξ。</div>
    <div class="qa-a">$E\xi=0+0.2+0.8=1$。$E\xi^2=0+0.2+1.6=1.8$。$D\xi=1.8-1=0.8$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么 $D(2\xi+3)=4D\xi$ 而不是 $2D\xi+3$？</div>
    <div class="qa-a">方差量的是"距离的平方"。乘 2 让每个偏差翻倍，平方后是 4 倍。加 3 只是整体平移，偏差不变。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 泊松分布的均值与方差有什么关系？</div>
    <div class="qa-a">都等于 λ。这是泊松分布的识别特征之一，做题看到"均值等于方差"可以反推是泊松。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="cond-expect">
  <div class="breadcrumb"></div>
  <h2><span class="num">18</span>条件分布与条件期望</h2>
  <p class="lead">把第一章的条件概率搬到二维随机变量上：给定 η 取某个值，ξ 的分布会变，这个新分布叫条件分布。在它上面算的期望叫条件期望。全期望公式把"分组平均"和"总平均"连起来。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：二维联合分布（第 14 节）、条件概率（第 9 节）、期望（第 16 节）。后续：第 26 节回归与条件期望、第 25 节全期望在方差分解里的用法。
  </div>

  <h3>18.1 条件分布列</h3>
  <p>给定 $\eta=y_j$（要求 $p_{\cdot j}\gt0$），ξ 的条件概率是 $P(\xi=x_i\mid\eta=y_j)=\frac{p_{ij}}{p_{\cdot j}}$。把 i 遍历一遍，得到一串新的概率：</p>
  <div class="formula">$$p_{i|j}=\frac{p_{ij}}{p_{\cdot j}},\qquad i=1,2,\dots$$</div>
  <p>校验它确实是分布列：非负显然；$\sum_i p_{i|j}=\frac{\sum_i p_{ij}}{p_{\cdot j}}=\frac{p_{\cdot j}}{p_{\cdot j}}=1$。第 9 节已经证明过条件概率满足三条公理，这里只是把它写成表。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">从 14.4 那张表读条件分布</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>表：$p_{11}=0.2$、$p_{12}=0.3$、$p_{21}=0.4$、$p_{22}=0.1$。η 的边缘 $p_{\cdot1}=0.6$、$p_{\cdot2}=0.4$。</p>
        <p>给定 $\eta=y_1$，ξ 的条件分布：$p_{1|1}=0.2/0.6\approx0.333$，$p_{2|1}=0.4/0.6\approx0.667$。和为一。</p>
        <p>给定 $\eta=y_2$：$p_{1|2}=0.3/0.4=0.75$，$p_{2|2}=0.1/0.4=0.25$。</p>
        <p>对比可见：η 取不同值，ξ 的分布明显不同（一个偏 0.667 走 y2，一个偏 0.75 走 y1）。这就是两者不独立的直观表现。</p>
      </div>
    </div>
  </div>

  <h3>18.2 条件期望</h3>
  <p>在条件分布上算期望，就是条件期望：</p>
  <div class="formula">$$E(\xi\mid\eta=y_j)=\sum_i x_i\,p_{i|j}$$</div>
  <p>它是"给定 η 这一列之后，ξ 的平均值"。注意它是 η 的函数：η 取哪个值，就有一个对应的数。所以 $E(\xi\mid\eta)$ 本身也是一个随机变量，随 η 变化。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">算</span><span class="derive-step-title">续上例，设 $x_1=0,\ x_2=1$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>给定 $\eta=y_1$：$E(\xi|\eta=y_1)=0\times0.333+1\times0.667=0.667$。</p>
        <p>给定 $\eta=y_2$：$E(\xi|\eta=y_2)=0\times0.75+1\times0.25=0.25$。</p>
        <p>两个值的差说明 η 携带了关于 ξ 的信息：知道 η 是 y1，ξ 更可能是 1。</p>
      </div>
    </div>
  </div>

  <h3>18.3 全期望公式</h3>
  <p>把各组的条件期望按 η 的概率加权，得到总的期望：</p>
  <div class="formula">$$E\xi=\sum_j E(\xi\mid\eta=y_j)\,P(\eta=y_j)=E\left[E(\xi\mid\eta)\right]$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">从两边分别展开同一个和</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>从 $E\xi$ 出发，按二维表写：$E\xi=\sum_i x_ip_{i\cdot}=\sum_i x_i\sum_j p_{ij}$。</p>
        <p>交换求和顺序：$=\sum_j\sum_i x_ip_{ij}$。</p>
        <p>把 $p_{ij}$ 拆成 $p_{i|j}p_{\cdot j}$：$=\sum_j\sum_i x_ip_{i|j}p_{\cdot j}$。</p>
        <p>$p_{\cdot j}$ 不含 i，提到内层求和外面：$=\sum_j p_{\cdot j}\left(\sum_i x_ip_{i|j}\right)$。</p>
        <p>括号里正是 $E(\xi|\eta=y_j)$，$p_{\cdot j}$ 是 $P(\eta=y_j)$。得证。</p>
      </div>
    </div>
  </div>
  <p>用上例验算：$E\xi=0\times0.5+1\times0.5=0.5$。分组加权：$0.667\times0.6+0.25\times0.4=0.4002+0.1=0.5002\approx0.5$（四舍五入误差）。一致。</p>

  <div class="callout callout-tip">
    <div class="callout-title">分组平均的例子</div>
    全校平均分，可以按年级分组算：各年级平均分 × 各年级人数占比，再加起来。这就是全期望公式。分组是为了利用"组内信息更集中"这个结构，算起来往往更容易。
  </div>

  <h3>18.4 两个常用的后续结论</h3>
  <p>第一，$E\left[E(\xi\mid\eta)\right]=E\xi$，就是上面的全期望公式的随机变量写法。</p>
  <p>第二，条件期望可以"提出来"：若 $f(\eta)$ 是 η 的函数，则 $E[\,f(\eta)\xi\mid\eta\,]=f(\eta)E(\xi\mid\eta)$。因为给定 η 之后，$f(\eta)$ 已经是确定值，可以当常数提出。这条在回归和特征函数里反复用。</p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 表中的条件分布 $p_{1|1}=0.4$、$p_{2|1}=0.6$，$\xi$ 取 0、2，求 $E(\xi|\eta=y_1)$。</div>
    <div class="qa-a">$0\times0.4+2\times0.6=1.2$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 全期望公式需要 ξ、η 独立吗？</div>
    <div class="qa-a">不需要。推导只用了联合分布与条件概率的定义，对任何两个随机变量都成立。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. $E(\xi\mid\eta)$ 是数还是随机变量？</div>
    <div class="qa-a">是随机变量。η 取不同值，它取不同的数。它的期望才是 $E\xi$。</div>
  </div>

  <div class="chapter-nav"></div>
</section>
"""

