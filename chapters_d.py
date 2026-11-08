#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 D 批：第三章 连续型随机变量（前半）"""

CH_D = r"""
<section class="chapter" id="dist-func">
  <div class="breadcrumb"></div>
  <h2><span class="num">19</span>分布函数</h2>
  <p class="lead">离散型用分布列，但连续型的单个取值概率都是 0，表写不出来。换一个记录方式：不问"等于某个值的概率"，问"不超过 x 的概率"。这就是分布函数，离散和连续都能用它描述。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：分布列（第 12 节）、概率的单调性与加法公式（第 7 节）。后续：密度（第 20 节）、分布函数法求函数分布（第 23 节）。
  </div>

  <h3>19.1 定义</h3>
  <div class="formula">$$F(x)=P(\xi\le x),\quad x\in\mathbb R$$</div>
  <p>读作"ξ 的分布函数"。它把每个实数 x 对应到"ξ 落在 $(-\infty,x]$ 里"的概率。x 从负无穷往正无穷走，F(x) 就逐渐累积所有概率，这也是"累积分布函数"这个名字的来源。</p>

  <div class="callout callout-tip">
    <div class="callout-title">生活直觉</div>
    全班身高的累积分布：问"身高不超过 170 的人占多少比例"，这个比例随阈值升高而增大。170 时 60%，175 时 85%，180 时 97%，190 时 100%。这条随阈值单调上升的曲线就是分布函数。
  </div>

  <h3>19.2 四条性质</h3>
  <p><b>（1）单调不减。</b>若 $x_1\lt x_2$，则 $F(x_1)\le F(x_2)$。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">用集合包含与减法公式</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$x_1\lt x_2$ 时，事件 $\{\xi\le x_1\}$ 是 $\{\xi\le x_2\}$ 的子集：前者包含的样本点都在后者里。</p>
        <p>按第 7 节的减法公式，$P(\xi\le x_2)-P(\xi\le x_1)=P(x_1\lt\xi\le x_2)\ge0$。</p>
        <p>所以 $F(x_2)\ge F(x_1)$。</p>
      </div>
    </div>
  </div>
  <p><b>（2）右连续。</b>$F(x+0)=\lim_{t\to x^+}F(t)=F(x)$。直觉：事件 $\{\xi\le x\}$ 可以由 $\{\xi\le x+1/n\}$ 不断缩小交出来，按上连续性（7.5 节）取极限，概率也收敛到 $F(x)$。</p>
  <p><b>（3）$F(-\infty)=0$、$F(+\infty)=1$。</b>前者是"ξ 小于负无穷"，不可能；后者是"ξ 小于正无穷"，必然。</p>
  <p><b>（4）$P(a\lt\xi\le b)=F(b)-F(a)$。</b>这就是上一条减法公式，只是换了字母。这个区间概率后面算密度积分时反复出现。</p>

  <h3>19.3 离散型的分布函数：阶梯</h3>
  <p>离散型 ξ 取 $x_1\lt x_2\lt\cdots$，F(x) 在每两个相邻取值之间保持不变，到了 $x_k$ 处向上跳一格，跳跃高度正好是 $p_k$：</p>
  <div class="formula">$$F(x)=\sum_{x_k\le x}p_k$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">均匀骰子的 F(x)</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$x\lt1$ 时，没有任何取值不超过 x，F=0。</p>
        <p>$1\le x\lt2$ 时，只有 1 不超过 x，F=1/6。</p>
        <p>$2\le x\lt3$ 时，1、2 都不超过，F=2/6。</p>
        <p>依次往上，每跨过一个整数跳 1/6。$x\ge6$ 时 F=1。</p>
        <p>图形是六级台阶，每级宽 1、高 1/6。注意在整数点上，F 取的是"跳上去之后"的值，这体现了右连续。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">问</span><span class="derive-step-title">$P(2\lt\xi\le5)$ 用 F 怎么算</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F(5)-F(2)=5/6-2/6=3/6=1/2$。</p>
        <p>核对：2 到 5 之间的整数是 3、4、5，共 3 个，每个 1/6，合计 1/2。一致。</p>
        <p>注意左端是开区间：$2\lt\xi$ 排除了 2。若写成 $2\le\xi\le5$，就得用 $F(5)-F(2-0)$，把跳跃点扣掉。</p>
      </div>
    </div>
  </div>

  <h3>19.4 分布函数能反推分布列</h3>
  <p>离散型时，$p_k=F(x_k)-F(x_k-0)$，也就是跳跃点处"跳上去的高度"。所以分布列和分布函数携带的信息完全一样，只是换了一种排版。连续型没有跳跃，于是没法从 F 读出单点概率，这也预告了下一节的密度。
  </p>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 若 F 在 x=2 处跳了 0.3，说明什么？</div>
    <div class="qa-a">说明 ξ 取 2 的概率是 0.3。离散型的跳跃高度就是该点的概率。</div>
  </div>
    <div class="qa-item">
    <div class="qa-q">Q2. 为什么分布函数要求右连续，而不是左连续？</div>
    <div class="qa-a">因为定义用的是 $\xi\le x$（包含等号），x 增大时把该点也纳入进来。包含方式决定了跳点取右侧值。若定义改成 $\xi\lt x$，就会变成左连续，但那样不常用。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="continuous-density">
  <div class="breadcrumb"></div>
  <h2><span class="num">20</span>连续型与概率密度</h2>
  <p class="lead">连续型的分布函数是光滑曲线，没有台阶，所以取单点的概率是 0。要描述"哪里概率密、哪里稀"，需要一个密度函数。本节把密度的定义、归一化和区间概率说清楚。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：分布函数（第 19 节）、定积分与反常积分（第 4 节）。后续：均匀、指数、正态（第 21 节）、连续型二维（第 22 节）、卷积（第 23 节）。
  </div>

  <h3>20.1 定义</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">定</span><span class="derive-step-title">密度是分布函数的导数</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>若存在非负函数 p(x)，使对任意 x 都有</p>
        <p>$F(x)=P(\xi\le x)=\int_{-\infty}^{x}p(y)\,dy$，</p>
        <p>就说 ξ 是连续型随机变量，p(x) 叫它的概率密度函数（简称密度）。</p>
        <p>反过来，若 F 可导，则 $p(x)=F'(x)$。这和第 4 节的牛顿-莱布尼茨公式是一回事：密度是分布函数的"变化率"，分布函数是密度的累积面积。</p>
      </div>
    </div>
  </div>

  <h3>20.2 密度不是概率</h3>
  <p>p(x) 本身不是概率，它是"单位长度上的概率"。概率是密度在区间上的积分：</p>
  <div class="formula">$$P(a\lt\xi\le b)=\int_a^b p(x)\,dx$$</div>
  <p>由此得两条：</p>
  <p>（1）$p(x)\ge0$ 且 $\int_{-\infty}^{+\infty}p(x)dx=1$。后者是规范性：总概率为 1，等于整条密度曲线下的面积。</p>
  <p>（2）密度可以大于 1。比如在 $[0,0.5]$ 上的均匀分布，密度是 $1/0.5=2$。面积约束的是"总面积为 1"，不是"高度不超过 1"。这一点和离散概率完全不同，初学者常卡在这里。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">取单点的概率为什么是 0</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>取 $P(\xi=c)$。用区间概率逼近：对任意 $\varepsilon\gt0$，$\{\xi=c\}\subseteq\{c-\varepsilon\lt\xi\le c\}$。</p>
        <p>所以 $P(\xi=c)\le P(c-\varepsilon\lt\xi\le c)=F(c)-F(c-\varepsilon)$。</p>
        <p>连续型的 F 连续（因为它是密度的积分，积分上限连续变动时积分值连续），所以 $\varepsilon\to0$ 时右边趋于 $F(c)-F(c)=0$。</p>
        <p>而概率非负，夹在 0 和 0 之间，只能是 0。</p>
        <p>结论：连续型随机变量取任何单点的概率都是 0。</p>
      </div>
    </div>
  </div>

  <div class="callout callout-key">
    <div class="callout-title">概率为 0 不等于不可能</div>
    在 $[0,1]$ 上均匀取点，取到 0.5 的概率是 0，但 0.5 是一个完全可能的点。区别在于：概率衡量的是"机会的比例"，单点没有长度，比例是 0；但"能不能发生"是另一个问题。同样，"概率为 1"也不等于必然。这是连续型最反直觉的地方，接受它就好。
  </div>

  <h3>20.3 连续型与离散型的对照</h3>
  <div class="table-wrap">
  <table>
    <tr><th>对比项</th><th>离散型</th><th>连续型</th></tr>
    <tr><td>描述工具</td><td>分布列 $p_k$</td><td>密度 p(x)</td></tr>
    <tr><td>单点概率</td><td>$p_k$ 可能大于 0</td><td>恒为 0</td></tr>
    <tr><td>区间概率</td><td>求和</td><td>积分</td></tr>
    <tr><td>分布函数</td><td>阶梯，有跳跃</td><td>连续曲线，无跳跃</td></tr>
    <tr><td>归一化</td><td>$\sum p_k=1$</td><td>$\int p=1$</td></tr>
  </table>
  </div>
  <p>课件注释里特别说明：连续型的分布函数一定连续，但密度未必连续（可以有断点）；离散型的分布函数一定不连续（有台阶）。这三句话是判断类型最快的办法。</p>

  <h3>20.4 由密度求分布函数，再求区间概率</h3>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$p(x)=2x$（$0\lt x\lt1$），其余为 0</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先验归一化：$\int_0^1 2x\,dx=[x^2]_0^1=1$。合法。</p>
        <p>求 F：$x\lt0$ 时 0；$0\le x\lt1$ 时 $\int_0^x2y\,dy=x^2$；$x\ge1$ 时 1。</p>
        <p>求 $P(0.3\lt\xi\le0.7)=F(0.7)-F(0.3)=0.49-0.09=0.40$。</p>
        <p>也可以直接积分：$\int_{0.3}^{0.7}2x\,dx=0.49-0.09=0.40$，一样。</p>
      </div>
    </div>
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 密度 p(x)=c 在 [0,2] 上，求 c。</div>
    <div class="qa-a">$\int_0^2 c\,dx=2c=1$，得 $c=0.5$。这就是 [0,2] 上的均匀分布。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 密度能等于 3 吗？</div>
    <div class="qa-a">能，只要它所在的区间足够短。比如 [0,1/3] 上均匀分布密度是 3，面积仍是 1。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 为什么连续型的分布函数一定连续？</div>
    <div class="qa-a">它是密度的变上限积分，积分上限连续变动时积分值也连续。没有跳跃，就没有断点。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="common-continuous">
  <div class="breadcrumb"></div>
  <h2><span class="num">21</span>常见连续分布</h2>
  <p class="lead">三个必须掌握的连续分布：均匀、指数、正态。每个都从密度出发，验证归一化，再算分布函数与期望方差。正态的归一化要用第 4 节的高斯积分。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：密度（第 20 节）、积分与高斯积分（第 4 节）、级数 e（第 3 节）。后续：二维连续（第 22 节）、数字特征（第 24 节）、中心极限定理。
  </div>

  <h3>21.1 均匀分布 $U(a,b)$</h3>
  <div class="formula">$$p(x)=\begin{cases}\dfrac{1}{b-a},&a\lt x\lt b\\[4pt]0,&\text{其他}\end{cases}$$</div>
  <p>密度在区间内是常数，意思是"每一点的机会密度相同"。归一化：$\int_a^b\frac{1}{b-a}dx=\frac{b-a}{b-a}=1$。</p>
  <p>分布函数：$x\lt a$ 时 0；$a\le x\lt b$ 时 $\frac{x-a}{b-a}$；$x\ge b$ 时 1。是一条从 (a,0) 斜升到 (b,1) 的直线段。</p>
  <p>期望与方差：$E\xi=\frac{a+b}{2}$（区间中点）；$D\xi=\frac{(b-a)^2}{12}$。第 24 节会算。</p>
  <p>应用：第 8 节几何概型的"等公交"就是 $U(0,10)$。计算机生成的随机数通常是 $U(0,1)$。</p>

  <h3>21.2 指数分布 $Exp(\lambda)$</h3>
  <div class="formula">$$p(x)=\begin{cases}\lambda e^{-\lambda x},&x\ge0\\0,&x\lt0\end{cases},\quad \lambda\gt0$$</div>
  <p>场景：等待下一次事件发生的时间（电话呼入间隔、元件寿命、公交到站等待）。$\lambda$ 是单位时间内平均发生的次数，越大表示越频繁。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">验</span><span class="derive-step-title">归一化</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\int_0^\infty\lambda e^{-\lambda x}dx$。令 $u=\lambda x$，$du=\lambda dx$，积分变成 $\int_0^\infty e^{-u}du$。</p>
        <p>第 4 节算过，这个反常积分等于 1。合法。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">分布函数与尾概率</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F(x)=\int_0^x\lambda e^{-\lambda y}dy=[-e^{-\lambda y}]_0^x=1-e^{-\lambda x}$（$x\ge0$）。</p>
        <p>尾概率 $P(\xi\gt x)=1-F(x)=e^{-\lambda x}$。这个式子比 F 更好用，因为它只有一个指数项。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">无记忆性</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>问：已经等了 s 分钟，再等 t 分钟的概率。即 $P(\xi\gt s+t\mid\xi\gt s)$。</p>
        <p>分子：$\{\xi\gt s+t\}$ 与 $\{\xi\gt s\}$ 的交集就是 $\{\xi\gt s+t\}$（前者更小）。概率 $e^{-\lambda(s+t)}$。</p>
        <p>分母：$P(\xi\gt s)=e^{-\lambda s}$。</p>
        <p>比值：$\frac{e^{-\lambda s}e^{-\lambda t}}{e^{-\lambda s}}=e^{-\lambda t}=P(\xi\gt t)$。</p>
        <p>结论：已经等了多久，都不影响"还要再等多久"的分布。指数分布和几何分布一样，没有记忆。这也解释了一个常见误解：公交"已经等了 10 分钟，车该来了"是错的，如果等待时间服从指数分布，从第 10 分钟重新计时，分布和刚来时一模一样。</p>
      </div>
    </div>
  </div>

  <h3>21.3 正态分布 $N(\mu,\sigma^2)$</h3>
  <div class="formula">$$p(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right],\quad -\infty\lt x\lt+\infty$$</div>
  <p>记 $\xi\sim N(\mu,\sigma^2)$。参数：$\mu$ 是中心位置，$\sigma$ 是宽度（$\sigma$ 越大越扁平）。图形是钟形，以 $\mu$ 为对称轴。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">验证归一化：系数从哪来</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>要证 $\int_{-\infty}^\infty p(x)dx=1$。先把系数提出来，只需要算 $\int_{-\infty}^\infty e^{-(x-\mu)^2/(2\sigma^2)}dx$。</p>
        <p>换元 $y=\frac{x-\mu}{\sigma}$，则 $x=\mu+\sigma y$，$dx=\sigma dy$。积分变成 $\sigma\int_{-\infty}^\infty e^{-y^2/2}dy$。</p>
        <p>再换元 $z=\frac{y}{\sqrt2}$，$dy=\sqrt2\,dz$，$e^{-y^2/2}=e^{-z^2}$。积分变成 $\sigma\sqrt2\int_{-\infty}^\infty e^{-z^2}dz$。</p>
        <p>第 4 节已经算出高斯积分 $=\sqrt\pi$。代入得 $\sigma\sqrt2\sqrt\pi=\sigma\sqrt{2\pi}$。</p>
        <p>乘回系数 $\frac{1}{\sqrt{2\pi}\sigma}$，得 1。这就是系数里那个 $\sqrt{2\pi}$ 的来历，它不是随便写的。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">标准化与查表</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>令 $\xi^*=\frac{\xi-\mu}{\sigma}$。按第 17 节的标准化，$E\xi^*=0$，$D\xi^*=1$，且它仍服从正态，所以 $\xi^*\sim N(0,1)$，叫标准正态。</p>
        <p>标准正态的分布函数记 $\Phi(x)$。任意正态的概率都转成它：$P(a\lt\xi\le b)=\Phi\left(\frac{b-\mu}{\sigma}\right)-\Phi\left(\frac{a-\mu}{\sigma}\right)$。</p>
        <p>推导只需一步：$P(\xi\le b)=P\left(\xi^*\le\frac{b-\mu}{\sigma}\right)=\Phi\left(\frac{b-\mu}{\sigma}\right)$。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">用</span><span class="derive-step-title">三倍标准差规则</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>查表得：$P(|\xi-\mu|\le\sigma)\approx0.6827$，$P(|\xi-\mu|\le2\sigma)\approx0.9545$，$P(|\xi-\mu|\le3\sigma)\approx0.9973$。</p>
        <p>含义：正态分布里，99.7% 的值都落在中心两侧三倍标准差内。超出 3σ 的概率不到 0.3%，所以工程上常把"3σ 之外"当作异常信号。这是"六西格玛"管理方法的概率基础。</p>
      </div>
    </div>
  </div>
  <p><b>期望与方差</b>：$E\xi=\mu$，$D\xi=\sigma^2$。参数就是这么命名的。计算在第 24 节：期望靠对称性（密度以 $\mu$ 为轴左右对称，重心落在 $\mu$），方差靠换元后算 $\int z^2e^{-z^2/2}dz$（分部积分得 $\sqrt{2\pi}$）。</p>

  <div class="callout callout-key">
    <div class="callout-title">三个分布的记忆锚点</div>
    均匀：一条平的线，参数是两端。指数：从高处往下掉的曲线，参数是"多快掉完"。正态：钟形，两个参数各管位置和宽度。看到题目问"等待时间"用指数，问"测量误差/身高/成绩"用正态，问"完全不知道落在哪、只知道范围"用均匀。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $U(0,4)$ 的密度和 $P(1\lt\xi\le3)$。</div>
    <div class="qa-a">密度 $1/4=0.25$。概率 $(3-1)/4=1/2$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. $Exp(2)$ 的均值是多少？平均等多久？</div>
    <div class="qa-a">$1/\lambda=0.5$，平均等 0.5 个单位时间。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 正态分布为什么系数里有 √(2π)？</div>
    <div class="qa-a">为了让整条曲线下面积为 1。高斯积分 $\int e^{-x^2}=\sqrt\pi$，换元两次后带出 $\sigma\sqrt{2\pi}$，系数正好是它的倒数。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="continuous-2d">
  <div class="breadcrumb"></div>
  <h2><span class="num">22</span>二维连续：联合、边缘、条件与独立</h2>
  <p class="lead">两个连续型随机变量一起看，用一块曲面描述"概率密度在地图上的分布"。把一维的求和换成二重积分，其余逻辑与离散情形一一对应。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：密度（第 20 节）、二维离散的边缘与独立（第 14 节）、二重积分。后续：卷积（第 23 节）、协方差（第 24 节）、条件期望与回归（第 25 节）。
  </div>

  <h3>22.1 联合密度</h3>
  <div class="callout callout-tip">
    <div class="callout-title">先说清二重积分怎么算</div>
    二重积分就是"算两次一维积分"。写成 $\int_a^b\left[\int_c^d p(x,y)\,dy\right]dx$，方括号里的内层是把 x 冻成常数、只让 y 从 c 扫到 d，积完得到一个只含 x 的式子；再拿这个式子对 x 积一遍。几何上 $dx\,dy$ 是一小块矩形的面积，整个积分就是把每小块上的"密度×面积"累加起来。先对谁积不影响结果，这和第 4 节里"求和可以换顺序"是同一个道理。
  </div>
  <p>$(\xi,\eta)$ 的联合密度 p(x,y) 满足 $p(x,y)\ge0$，且 $\iint_{\mathbb R^2}p(x,y)dxdy=1$。联合分布函数：</p>
  <div class="formula">$$F(x,y)=P(\xi\le x,\eta\le y)=\int_{-\infty}^{x}\int_{-\infty}^{y}p(u,v)\,dv\,du$$</div>
  <p>落在区域 D 内的概率就是密度在 D 上的二重积分：$P((\xi,\eta)\in D)=\iint_D p(x,y)dxdy$。面积越大概率越大，这是"密度×面积"的连续版。</p>

  <h3>22.2 边缘密度：把另一维积掉</h3>
  <div class="formula">$$p_\xi(x)=\int_{-\infty}^{+\infty}p(x,y)\,dy,\qquad p_\eta(y)=\int_{-\infty}^{+\infty}p(x,y)\,dx$$</div>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">先写边缘分布函数，再求导</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F_\xi(x)=P(\xi\le x)=P(\xi\le x,\eta\lt+\infty)$。η 取任何值都行，所以把 y 积到正无穷：</p>
        <p>$F_\xi(x)=\int_{-\infty}^{x}\left[\int_{-\infty}^{+\infty}p(u,y)dy\right]du$。</p>
        <p>对 x 求导。由牛顿-莱布尼茨，变上限积分求导等于把上限代入被积函数：</p>
        <p>$p_\xi(x)=F_\xi'(x)=\int_{-\infty}^{+\infty}p(x,y)dy$。</p>
        <p>离散版是"行和"，连续版是"对另一维积分"，同一个动作。</p>
      </div>
    </div>
  </div>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">单位正方形上的均匀分布</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$p(x,y)=1$（$0\lt x\lt1,\ 0\lt y\lt1$），其余 0。总面积 $1\times1=1$，合法。</p>
        <p>边缘：$p_\xi(x)=\int_0^1 1\,dy=1$（$0\lt x\lt1$）；$p_\eta(y)=1$。两者都是 $U(0,1)$。</p>
        <p>联合等于边缘乘积：$1=1\times1$，独立。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$p(x,y)=2$ 在三角形 $0\lt y\lt x\lt1$ 上</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先验归一化：三角形面积 $1/2$，密度 2，二重积分 $2\times\frac12=1$，合法。</p>
        <p>边缘 $p_\xi(x)=\int_0^x 2\,dy=2x$（$0\lt x\lt1$）。边缘 $p_\eta(y)=\int_y^1 2\,dx=2(1-y)$（$0\lt y\lt1$）。</p>
        <p>判断独立：$p(x,y)=2$，而 $p_\xi(x)p_\eta(y)=2x\cdot2(1-y)=4x(1-y)$，不相等，不独立。</p>
        <p>这个例子说明"联合密度是常数"不代表独立。均匀只说明"在定义域内均匀"，定义域的形状（三角形）本身携带了两者的关联：x 大时 y 的取值范围也大。</p>
      </div>
    </div>
  </div>

  <h3>22.3 独立性判定</h3>
  <p>连续型独立的条件和离散版形状一样，只是把概率换成密度（严格说要求"几乎处处"相等，即除个别点外都相等，个别点的差异不影响积分）：</p>
  <div class="formula">$$p(x,y)=p_\xi(x)\,p_\eta(y)$$</div>
  <p>若密度能分解成"只含 x 的函数乘只含 y 的函数"，并且定义域是矩形，通常就独立。定义域不是矩形（比如三角形）基本不独立。</p>

  <h3>22.4 条件密度</h3>
  <p>给定 $\eta=y$，ξ 的条件密度定义为</p>
  <div class="formula">$$p_{\xi|\eta}(x\mid y)=\frac{p(x,y)}{p_\eta(y)},\quad p_\eta(y)\gt0$$</div>
  <p>和条件概率的除法完全同构：联合除以边缘，把"η 那一列"重新归一化成 1。验证：$\int p_{\xi|\eta}(x|y)dx=\frac{\int p(x,y)dx}{p_\eta(y)}=\frac{p_\eta(y)}{p_\eta(y)}=1$。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">三角形例子里给定 $y=0.5$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$p_\eta(0.5)=2(1-0.5)=1$。</p>
        <p>$p_{\xi|\eta}(x|0.5)=\frac{2}{1}=2$，x 的范围是 $0.5\lt x\lt1$。</p>
        <p>即给定 y=0.5 后，x 在 (0.5,1) 上均匀。这也说明条件化会把定义域切一刀。</p>
      </div>
    </div>
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $p(x,y)=e^{-(x+y)}$（$x,y\gt0$）。求边缘，判断独立。</div>
    <div class="qa-a">$p_\xi(x)=e^{-x}\int_0^\infty e^{-y}dy=e^{-x}$，同理 $p_\eta(y)=e^{-y}$。乘积 $e^{-(x+y)}$ 等于联合，独立。两个都是 $Exp(1)$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么边缘密度要积分而不是求和？</div>
    <div class="qa-a">连续型的"另一维"有不可数个取值，求和换成积分。逻辑一样：把另一维的所有可能性都累加。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="continuous-func">
  <div class="breadcrumb"></div>
  <h2><span class="num">23</span>随机变量函数的分布（连续）</h2>
  <p class="lead">已知 ξ 的密度，求 $\eta=g(\xi)$ 的密度。离散情形是"合并同值概率"，连续情形没有概率可加，改用分布函数法：先求 $F_\eta(y)$，再求导得密度。这一节的三个结果（线性变换、平方、卷积）都要会推。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：密度（第 20 节）、分布函数（第 19 节）、二维联合（第 22 节）。后续：正态可加性、特征函数（第 25 节）、中心极限定理的证明思路。
  </div>

  <h3>23.1 分布函数法：万能套路</h3>
  <p>要求 $\eta=g(\xi)$ 的密度，按三步走：</p>
  <p>第一步，写 $F_\eta(y)=P(\eta\le y)=P(g(\xi)\le y)$。这是要解的不等式。</p>
  <p>第二步，把不等式化成关于 ξ 的区间，用 $F_\xi$ 表示。</p>
  <p>第三步，对 y 求导，得 $p_\eta(y)$。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">线性变换 $\eta=a\xi+b$（$a\ne0$）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>先设 $a\gt0$。$F_\eta(y)=P(a\xi+b\le y)=P\left(\xi\le\frac{y-b}{a}\right)=F_\xi\left(\frac{y-b}{a}\right)$。</p>
        <p>求导，用链式法则：$p_\eta(y)=p_\xi\left(\frac{y-b}{a}\right)\cdot\frac{1}{a}$。</p>
        <p>若 $a\lt0$，不等式方向翻转：$a\xi+b\le y$ 变成 $\xi\ge\frac{y-b}{a}$，所以 $F_\eta(y)=1-F_\xi\left(\frac{y-b}{a}\right)$。</p>
        <p>求导得 $p_\eta(y)=-p_\xi\left(\frac{y-b}{a}\right)\cdot\frac1a$。因为 a 是负数，$-\frac1a=\frac{1}{|a|}$。</p>
        <p>统一写成 $p_\eta(y)=\frac{1}{|a|}p_\xi\left(\frac{y-b}{a}\right)$。</p>
        <p>含义：密度横向拉伸压缩 $|a|$ 倍，面积要保持 1，所以高度除以 $|a|$。b 只是平移，不影响高度。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$\eta=\xi^2$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>y 必须大于 0，否则 $F_\eta(y)=0$。</p>
        <p>$F_\eta(y)=P(\xi^2\le y)=P(-\sqrt y\le\xi\le\sqrt y)=F_\xi(\sqrt y)-F_\xi(-\sqrt y)$。</p>
        <p>求导，两个变上限都要用链式法则：$p_\eta(y)=p_\xi(\sqrt y)\cdot\frac{1}{2\sqrt y}-p_\xi(-\sqrt y)\cdot\left(-\frac{1}{2\sqrt y}\right)$。</p>
        <p>合并：$p_\eta(y)=\frac{p_\xi(\sqrt y)+p_\xi(-\sqrt y)}{2\sqrt y}$，$y\gt0$。</p>
        <p>为什么加号：x 与 -x 两条分支都映射到同一个 y，两条分支的密度贡献相加，正是离散"合并同值"的连续版。</p>
        <p>例：$\xi\sim N(0,1)$ 时，$p_\eta(y)=\frac{2\varphi(\sqrt y)}{2\sqrt y}=\frac{\varphi(\sqrt y)}{\sqrt y}$（因为标准正态密度是偶函数），$y\gt0$。这是自由度为 1 的卡方分布。</p>
      </div>
    </div>
  </div>

  <h3>23.2 卷积公式：两个独立变量相加</h3>
  <p>$\xi,\eta$ 独立，求 $Z=\xi+\eta$ 的密度。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">在平面上积出 $x+y\le z$ 的区域</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$F_Z(z)=P(\xi+\eta\le z)=\iint_{x+y\le z}p_\xi(x)p_\eta(y)\,dx\,dy$。这里用了独立，联合密度等于乘积。</p>
        <p>把二重积分写成一重套一重。固定 x，y 的条件是 $y\le z-x$：</p>
        <p>$=\int_{-\infty}^{+\infty}\left[\int_{-\infty}^{z-x}p_\eta(y)dy\right]p_\xi(x)\,dx$。</p>
        <p>对 z 求导。内层积分是变上限 $z-x$ 的函数，求导得 $p_\eta(z-x)$：</p>
        <p>$p_Z(z)=\int_{-\infty}^{+\infty}p_\xi(x)\,p_\eta(z-x)\,dx$。</p>
        <p>这个式子叫卷积。含义：把所有"x 加上 $z-x$ 恰好等于 z"的配对方式的密度相乘再累加。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">两个 $U(0,1)$ 相加，得三角分布</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$p_\xi(x)=1$（$0\lt x\lt1$），$p_\eta$ 同理。$p_Z(z)=\int p_\xi(x)p_\eta(z-x)dx$。</p>
        <p>被积函数为 1 的条件是两个因子都在定义域里：$0\lt x\lt1$ 且 $0\lt z-x\lt1$，后者等价于 $z-1\lt x\lt z$。</p>
        <p>所以积分区间是 $(0,1)$ 与 $(z-1,z)$ 的交，长度就是答案。</p>
        <p>$0\lt z\lt1$ 时交集 $(0,z)$，长度 z。$1\le z\lt2$ 时交集 $(z-1,1)$，长度 $2-z$。其余 0。</p>
        <p>密度是三角形：从 0 升到 1（z=1 处最高），再降回 0。积分验算 $\int_0^1 z\,dz+\int_1^2(2-z)dz=0.5+0.5=1$。</p>
      </div>
    </div>
  </div>

  <h3>23.3 正态分布的可加性</h3>
  <p>若 $\xi\sim N(\mu_1,\sigma_1^2)$、$\eta\sim N(\mu_2,\sigma_2^2)$ 且独立，则</p>
  <div class="formula">$$\xi+\eta\sim N(\mu_1+\mu_2,\ \sigma_1^2+\sigma_2^2)$$</div>
  <p>结论可以硬用卷积积分算出来（把两个高斯函数乘起来配方，结果仍是高斯），但计算很长。第 25 节的特征函数给了一条更短的证明：特征函数相乘，指数上的二次项直接相加。这里先记住结论，第 25 节补证明。</p>
  <p>这条性质是中心极限定理的基石：大量独立同分布随机变量相加，分布趋于正态，原因就是"正态加正态还是正态"，而非正态的分布相加会越来越像正态。</p>

  <div class="callout callout-key">
    <div class="callout-title">连续函数分布的三条经验</div>
    一一映射（线性变换）：套公式 $\frac{1}{|a|}$。多对一（平方、绝对值）：各分支密度相加。两个变量相加：卷积。遇到别的函数，回到分布函数法三步走，不要硬套公式。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $\xi\sim U(0,1)$，求 $\eta=2\xi+1$ 的密度。</div>
    <div class="qa-a">$a=2\gt0$，$p_\eta(y)=\frac12p_\xi\left(\frac{y-1}{2}\right)$。$p_\xi$ 在 (0,1) 上为 1，所以 $0\lt\frac{y-1}{2}\lt1$ 即 $1\lt y\lt3$ 时密度 $0.5$。是 $U(1,3)$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 卷积公式要求独立吗？</div>
    <div class="qa-a">推导时用 $p(x,y)=p_\xi p_\eta$，所以要求独立。不独立时要用联合密度：$p_Z(z)=\int p(x,z-x)dx$。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 为什么两个均匀相加得到三角形而不是平的？</div>
    <div class="qa-a">和为某个 z 的配对方式数量不同。z=0.5 附近配对小，z=1 时配对最多（从 0+1 到 1+0 整体都能配），所以中间高两头低。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="numeric-features">
  <div class="breadcrumb"></div>
  <h2><span class="num">24</span>数字特征、协方差与切比雪夫不等式</h2>
  <p class="lead">连续型的期望和方差把求和换成积分。两个变量一起看时，还需要协方差来描述"同向变化的程度"。最后用方差推出切比雪夫不等式，它是大数定律的入口。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：密度（第 20 节）、常见连续分布（第 21 节）、二维连续（第 22 节）、离散型期望方差（第 16、17 节）。后续：条件期望与回归（第 25 节）、大数定律与中心极限定理。
  </div>

  <h3>24.1 连续型的期望与方差</h3>
  <p>把求和的每一项"概率"换成"密度×微小宽度"，求和就变成积分：</p>
  <div class="formula">$$E\xi=\int_{-\infty}^{+\infty}x\,p(x)\,dx,\qquad D\xi=\int_{-\infty}^{+\infty}(x-E\xi)^2p(x)\,dx$$</div>
  <p>第 17 节那条 $D\xi=E\xi^2-(E\xi)^2$ 仍然成立，因为推导只用了求和的线性性，换成积分同样合法。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">均匀 $U(a,b)$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E\xi=\int_a^b x\cdot\frac{1}{b-a}dx=\frac{1}{b-a}\left[\frac{x^2}{2}\right]_a^b=\frac{b^2-a^2}{2(b-a)}=\frac{a+b}{2}$。</p>
        <p>最后一步用平方差公式：$b^2-a^2=(b-a)(b+a)$，约掉 $(b-a)$。</p>
        <p>$E\xi^2=\frac{1}{b-a}\left[\frac{x^3}{3}\right]_a^b=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}$。这里用了立方差公式 $b^3-a^3=(b-a)(a^2+ab+b^2)$。</p>
        <p>$D\xi=\frac{a^2+ab+b^2}{3}-\frac{(a+b)^2}{4}$。通分：$\frac{4(a^2+ab+b^2)-3(a^2+2ab+b^2)}{12}=\frac{a^2-2ab+b^2}{12}=\frac{(b-a)^2}{12}$。</p>
        <p>验算 $U(0,1)$：均值 0.5，方差 $1/12\approx0.0833$。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">指数 $Exp(\lambda)$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E\xi=\int_0^\infty x\lambda e^{-\lambda x}dx$。分部积分，取 $u=x$、$dv=\lambda e^{-\lambda x}dx$，则 $du=dx$、$v=-e^{-\lambda x}$。</p>
        <p>$=[-xe^{-\lambda x}]_0^\infty+\int_0^\infty e^{-\lambda x}dx$。</p>
        <p>第一项在无穷处 $xe^{-\lambda x}\to0$（指数压过多项式），在 0 处为 0，所以是 0。</p>
        <p>第二项 $=\left[-\frac1\lambda e^{-\lambda x}\right]_0^\infty=\frac1\lambda$。</p>
        <p>方差：同样分部两次，$E\xi^2=\int_0^\infty x^2\lambda e^{-\lambda x}dx=\frac{2}{\lambda^2}$。所以 $D\xi=\frac2{\lambda^2}-\frac1{\lambda^2}=\frac1{\lambda^2}$。</p>
        <p>均值与标准差都等于 $1/\lambda$，这是指数分布的一个特征。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">正态 $N(\mu,\sigma^2)$ 的期望</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$E\xi=\int x p(x)dx$。换元 $y=\frac{x-\mu}{\sigma}$，$x=\mu+\sigma y$，$dx=\sigma dy$。</p>
        <p>密度带系数 $\frac{1}{\sqrt{2\pi}\sigma}$，乘上 $dx=\sigma dy$ 后系数变成 $\frac{1}{\sqrt{2\pi}}$。</p>
        <p>积分变成 $\frac{1}{\sqrt{2\pi}}\int(\mu+\sigma y)e^{-y^2/2}dy$。</p>
        <p>拆两项：$\mu\frac{1}{\sqrt{2\pi}}\int e^{-y^2/2}dy$ 加 $\sigma\frac{1}{\sqrt{2\pi}}\int y e^{-y^2/2}dy$。</p>
        <p>第一项是 $\mu\cdot1=\mu$，因为标准正态密度积分为 1。</p>
        <p>第二项：被积函数 $ye^{-y^2/2}$ 是奇函数（y 变 -y 时值变号），在对称区间上积分等于 0。</p>
        <p>所以 $E\xi=\mu$。方差同理：换元后要算 $\frac{1}{\sqrt{2\pi}}\int y^2e^{-y^2/2}dy$，分部积分得 1，所以 $D\xi=\sigma^2$。</p>
      </div>
    </div>
  </div>

  <div class="table-wrap">
  <table>
    <tr><th>分布</th><th>期望</th><th>方差</th></tr>
    <tr><td>$U(a,b)$</td><td>$(a+b)/2$</td><td>$(b-a)^2/12$</td></tr>
    <tr><td>$Exp(\lambda)$</td><td>$1/\lambda$</td><td>$1/\lambda^2$</td></tr>
    <tr><td>$N(\mu,\sigma^2)$</td><td>$\mu$</td><td>$\sigma^2$</td></tr>
  </table>
  </div>

  <h3>24.2 协方差：两个变量同向变化的程度</h3>
  <p>把一个变量的偏差和另一个变量的偏差乘起来再求期望：</p>
  <div class="formula">$$\mathrm{Cov}(\xi,\eta)=E\left[(\xi-E\xi)(\eta-E\eta)\right]=E(\xi\eta)-E\xi\,E\eta$$</div>
  <p>含义：两者同时偏大或同时偏小时，乘积为正；一个偏大一个偏小时，乘积为负。所以协方差为正说明"同向变化"，为负说明"反向变化"，接近 0 说明没有明显的线性同步。</p>
  <p>第二个等号的推导：展开 $E[(\xi-E\xi)(\eta-E\eta)]=E(\xi\eta)-E\xi E\eta-E\eta E\xi+E\xi E\eta=E(\xi\eta)-E\xi E\eta$。</p>
  <p>协方差带单位（ξ 的单位乘 η 的单位），不方便比较。除以两个标准差，得到相关系数：</p>
  <div class="formula">$$\rho=\frac{\mathrm{Cov}(\xi,\eta)}{\sqrt{D\xi}\sqrt{D\eta}}\in[-1,1]$$</div>
  <p>$\rho=\pm1$ 表示严格线性关系，$\rho=0$ 叫不相关。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">$D(\xi+\eta)=D\xi+D\eta+2\mathrm{Cov}$</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$D(\xi+\eta)=E[(\xi+\eta)-E(\xi+\eta)]^2$。期望拆开：$E(\xi+\eta)=E\xi+E\eta$。</p>
        <p>方括号里是 $(\xi-E\xi)+(\eta-E\eta)$，记作 $a+b$。</p>
        <p>平方展开：$E(a+b)^2=Ea^2+Eb^2+2E(ab)$。</p>
        <p>$Ea^2=D\xi$，$Eb^2=D\eta$，$E(ab)=\mathrm{Cov}(\xi,\eta)$。</p>
        <p>合起来得公式。独立时协方差为 0，退化成 $D\xi+D\eta$。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">辨</span><span class="derive-step-title">不相关不等于独立</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>独立一定不相关（因为 $E\xi\eta=E\xi E\eta$），但不相关不能推出独立。</p>
        <p>反例：$\xi\sim U(-1,1)$，$\eta=\xi^2$。显然 η 完全由 ξ 决定，不独立。</p>
        <p>但 $E\xi=0$（对称），$E(\xi\eta)=E(\xi^3)=0$（奇函数在对称区间积分为 0），所以 $\mathrm{Cov}=0-0=0$，不相关。</p>
        <p>这说明协方差只捕捉"线性"关系，捕捉不到"平方"这种非线性依赖。看散点图能一眼看出，算相关系数会得到 0。</p>
      </div>
    </div>
  </div>

  <h3>24.3 切比雪夫不等式</h3>
  <div class="formula">$$P(|\xi-E\xi|\ge\varepsilon)\le\frac{D\xi}{\varepsilon^2},\quad \varepsilon\gt0$$</div>
  <p>读法：随机变量偏离均值超过 ε 的概率，不超过方差除以 $\varepsilon^2$。方差越小，越集中，这个上界越小。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">只在"远处"积分</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设连续型。$P(|\xi-E\xi|\ge\varepsilon)=\int_{|x-E\xi|\ge\varepsilon}p(x)dx$。积分区域是远离中心的两个尾巴。</p>
        <p>在这块区域上，$|x-E\xi|\ge\varepsilon$，所以 $(x-E\xi)^2\ge\varepsilon^2$，于是 $\frac{(x-E\xi)^2}{\varepsilon^2}\ge1$。</p>
        <p>用这个 1 去放大被积函数：$\int_{|x-E\xi|\ge\varepsilon}p(x)dx\le\int_{|x-E\xi|\ge\varepsilon}\frac{(x-E\xi)^2}{\varepsilon^2}p(x)dx$。</p>
        <p>右边的积分区域是全部实轴的一个子集，而被积函数非负，所以整体积分不超过在全实轴上的积分。</p>
        <p>全实轴积分正是 $\frac{D\xi}{\varepsilon^2}$。得证。</p>
        <p>离散型把积分换成求和，推理一字不改。</p>
      </div>
    </div>
  </div>
  <p>取 $\varepsilon=k\sqrt{D\xi}$，不等式变成 $P(|\xi-E\xi|\ge k\sigma)\le\frac{1}{k^2}$。k=3 时给 1/9，比正态的 0.003 松得多。切比雪夫对任何分布都成立，代价是界很粗糙。</p>

  <div class="callout callout-key">
    <div class="callout-title">为什么需要这么粗的界</div>
    因为它不要求知道具体分布，只知道期望和方差就能用。实际工程里常常只知道均值和方差，这时切比雪夫是唯一能给出保证的工具。它也是大数定律的证明工具：样本均值偏离总体均值的概率被方差/ε² 压住，样本越多方差越小，概率趋于 0。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. $E\xi=10$，$D\xi=4$，用切比雪夫估计 $P(|\xi-10|\ge6)$ 的上界。</div>
    <div class="qa-a">$4/36\approx0.111$。即偏离 6 以上的概率不超过约 11.1%。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 独立时 $D(\xi+\eta)$ 等于什么？</div>
    <div class="qa-a">$D\xi+D\eta$，因为协方差为 0。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. $\mathrm{Cov}(\xi,\eta)=0$ 能说明独立吗？</div>
    <div class="qa-a">不能。$\xi\sim U(-1,1)$、$\eta=\xi^2$ 是反例：协方差 0 但 η 完全依赖 ξ。</div>
  </div>

  <div class="chapter-nav"></div>
</section>
"""
