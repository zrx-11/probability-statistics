#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第 E 批：第三章 3.6 条件期望与回归、3.7 特征函数，以及总复习"""

CH_E = r"""
<section class="chapter" id="regression-char">
  <div class="breadcrumb"></div>
  <h2><span class="num">25</span>条件期望、回归与特征函数</h2>
  <p class="lead">本节收尾第三章。前半把条件期望推到连续情形，说明"回归"就是条件期望，并证明它是最小平方误差意义下的最优预测。后半引入特征函数——把分布变换成一个函数，让独立变量的相加变成乘法。</p>

  <div class="callout callout-warn">
    <div class="callout-title">前置与后续</div>
    前置：条件密度（第 22 节）、条件分布列与条件期望（第 18 节）、期望方差（第 24 节）、e 的级数（第 3 节）。后续：大数定律、中心极限定理，以及数理统计里的参数估计。
  </div>

  <h3>25.1 连续型的条件分布与条件期望</h3>
  <p>分布函数形式：$F_{\eta|\xi}(y\mid x)=P(\eta\le y\mid\xi=x)=\int_{-\infty}^{y}p_{\eta|\xi}(v\mid x)\,dv$，其中 $p_{\eta|\xi}(v\mid x)=\frac{p(x,v)}{p_\xi(x)}$。</p>
  <p>条件期望就是把条件密度当普通密度算期望：</p>
  <div class="formula">$$E(\eta\mid\xi=x)=\int_{-\infty}^{+\infty}y\,p_{\eta|\xi}(y\mid x)\,dy$$</div>
  <p>注意它是 x 的函数：不同的 x 给出不同的条件密度，算出的平均值也不同。把这个函数记作 $m(x)=E(\eta\mid\xi=x)$，就叫 η 对 ξ 的<b>回归函数</b>。</p>

  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">三角形区域上的回归</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>沿用第 22 节的例子：$p(x,y)=2$，区域 $0\lt y\lt x\lt1$。已算出 $p_\xi(x)=2x$。</p>
        <p>条件密度：$p_{\eta|\xi}(y\mid x)=\frac{2}{2x}=\frac1x$，y 的范围 $(0,x)$。即给定 x 后，η 在 $(0,x)$ 上均匀。</p>
        <p>条件期望：$E(\eta\mid\xi=x)=\int_0^x y\cdot\frac1x dy=\frac{x}{2}$。</p>
        <p>所以回归函数是 $m(x)=x/2$。看图就明白：给定竖线 x 后，y 在 0 到 x 之间均匀铺开，平均值自然是中点 x/2。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">全期望公式（连续版）</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>第 18 节用求和证过 $E\eta=E[E(\eta\mid\xi)]$。连续版把求和换成积分：</p>
        <p>$E\eta=\int y\,p_\eta(y)dy=\int y\left[\int p(x,y)dx\right]dy$。</p>
        <p>交换积分次序：$=\int\left[\int y\,p(x,y)dy\right]dx$。这一步是二重积分的性质：先对 y 积再对 x 积，和反过来积，结果一样，因为累加的还是同一批"小块面积×密度"。</p>
        <p>内层：$\int y\,p(x,y)dy=\int y\,p_\xi(x)p_{\eta|\xi}(y|x)dy=p_\xi(x)\cdot E(\eta\mid\xi=x)$。</p>
        <p>外层：$\int m(x)p_\xi(x)dx$，这正是 $E[m(\xi)]=E[E(\eta\mid\xi)]$。得证。</p>
        <p>验证上例：$E[m(\xi)]=\int_0^1\frac{x}{2}\cdot2x\,dx=\int_0^1x^2dx=\frac13$。直接算 $E\eta=\iint y\cdot2\,dxdy=\int_0^1\left[\int_0^x2y\,dy\right]dx=\int_0^1x^2dx=\frac13$。一致。</p>
      </div>
    </div>
  </div>

  <h3>25.2 回归：用条件期望做预测</h3>
  <p>给定联合分布时，"第一类回归"是 ξ 对 η 的回归函数 $E(\xi\mid\eta=y)$，"第二类回归"是 η 对 ξ 的回归函数 $E(\eta\mid\xi=x)$。这两个名字只是方向不同。</p>
  <p>关键是第二类回归的一个性质：它是所有"用 ξ 的函数预测 η"的方案里，平方误差最小的那个。</p>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">最优预测为什么是条件期望</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>设我们用 $g(\xi)$ 去预测 η，误差是 $\eta-g(\xi)$，评价标准是均方误差 $E[\eta-g(\xi)]^2$。要找让这个数最小的 g。</p>
        <p>分解：$\eta-g(\xi)=[\eta-m(\xi)]+[m(\xi)-g(\xi)]$，其中 $m(\xi)=E(\eta\mid\xi)$。</p>
        <p>平方展开求期望，得三项：$E[\eta-m(\xi)]^2+2E\{[\eta-m(\xi)][m(\xi)-g(\xi)]\}+E[m(\xi)-g(\xi)]^2$。</p>
        <p>看中间那一项。用全期望公式，先对 ξ 条件化：$E\{[\eta-m(\xi)][m(\xi)-g(\xi)]\}=E\{E[\eta-m(\xi)\mid\xi]\cdot[m(\xi)-g(\xi)]\}$。第二个因子在给定 ξ 时是常数，可以提到条件期望外面。</p>
        <p>而 $E[\eta-m(\xi)\mid\xi]=E(\eta\mid\xi)-m(\xi)=m(\xi)-m(\xi)=0$。所以交叉项是 0。</p>
        <p>于是 $E[\eta-g(\xi)]^2=E[\eta-m(\xi)]^2+E[m(\xi)-g(\xi)]^2$。</p>
        <p>第一项与 g 无关，第二项非负且只在 $g=m$ 时为 0。所以取 $g(\xi)=E(\eta\mid\xi)$ 时均方误差最小。</p>
        <p>含义：任何用 ξ 做的预测，误差都可以拆成"η 自身的条件波动"（第一项，无法消除）加上"预测函数偏离条件期望"（第二项，可以消除）。</p>
      </div>
    </div>
  </div>
  <div class="callout callout-key">
    <div class="callout-title">回归就是条件平均</div>
    给定 x 后 η 还会波动，问"平均是多少"，这个平均就是回归值。第 25.1 例子里 $m(x)=x/2$ 是一条直线，画出来是散点图的中间线。若条件期望是 x 的线性函数，就是线性回归；一般情形不限于线性。
  </div>

  <h3>25.3 特征函数</h3>
  <div class="callout callout-tip">
    <div class="callout-title">复数没学过，只需要三件事</div>
    第一，i 是一个记号，规定 $i^2=-1$，于是 $i^3=-i$、$i^4=1$，四次一循环，像钟表走一圈。第二，$e^{it}$ 理解成"单位圆上转过 t 弧度的那一点"，横坐标是 $\cos t$、纵坐标是 $\sin t$，这就是欧拉公式 $e^{it}=\cos t+i\sin t$。第三，本课不真去算虚部，只用"指数相乘等于指数相加"这条代数规则，最后靠唯一性定理回到分布，全程不需要复变函数。你只要会两件事：把两个指数乘开、把指数上的项相加。
  </div>
  <p>定义：</p>
  <div class="formula">$$\varphi(t)=E\left(e^{it\xi}\right)=E(\cos t\xi)+i\,E(\sin t\xi),\quad t\in\mathbb R$$</div>
  <p>i 是虚数单位，$i^2=-1$。它把分布在每个点上的"权重"乘上一个旋转相位后再累加。</p>

  <div class="callout callout-tip">
    <div class="callout-title">为什么要引入复数</div>
    两个分布相加，密度要用卷积算，很麻烦。而 $e^{it(\xi+\eta)}=e^{it\xi}\cdot e^{it\eta}$，指数函数的乘法把"相加"变成了"相乘"。独立时期望也能乘开，于是卷积变成普通乘法。这是一个纯粹的技术动机：找一个能把加法变成乘法的变换。
  </div>

  <p><b>离散型</b>：$\varphi(t)=\sum_k p_k e^{itx_k}$。</p>
  <p><b>连续型</b>：$\varphi(t)=\int_{-\infty}^{+\infty}p(x)e^{itx}\,dx$。这个积分叫 p 的傅里叶变换。</p>

  <h4>基本性质</h4>
  <p><b>（1）$\varphi(0)=1$。</b>代入 t=0，$e^0=1$，期望是 1。</p>
  <p><b>（2）$|\varphi(t)|\le1$。</b>$|E(e^{it\xi})|\le E|e^{it\xi}|=E(1)=1$，因为 $|e^{it\xi}|=1$。</p>
  <p><b>（3）独立时相乘。</b>$\varphi_{\xi+\eta}(t)=E(e^{it(\xi+\eta)})=E(e^{it\xi}e^{it\eta})=E(e^{it\xi})E(e^{it\eta})=\varphi_\xi(t)\varphi_\eta(t)$。这一步用到独立。</p>
  <p><b>（4）唯一性。</b>分布函数和特征函数一一对应，知道 $\varphi$ 就能还原 F。这条保证了"算出特征函数就等于确定了分布"。</p>

  <h4>正态的特征函数与可加性证明</h4>
  <div class="derive-steps">
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">第 23 节留下的作业</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>$\xi\sim N(\mu,\sigma^2)$ 的特征函数是 $\varphi(t)=\exp\left(i\mu t-\frac{\sigma^2t^2}{2}\right)$。这个结果由积分 $\int p(x)e^{itx}dx$ 配方算出，过程较长，此处直接引用。</p>
        <p>设 $\xi\sim N(\mu_1,\sigma_1^2)$、$\eta\sim N(\mu_2,\sigma_2^2)$ 独立。按性质（3）：</p>
        <p>$\varphi_{\xi+\eta}(t)=e^{i\mu_1t-\sigma_1^2t^2/2}\cdot e^{i\mu_2t-\sigma_2^2t^2/2}$。</p>
        <p>指数相加：$=e^{i(\mu_1+\mu_2)t-(\sigma_1^2+\sigma_2^2)t^2/2}$。</p>
        <p>这个式子正是 $N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ 的特征函数。按唯一性（4），ξ+η 的分布就是它。证完。</p>
        <p>对比一下卷积那条路：要把两个高斯函数乘起来再配方，篇幅是这里的三倍。特征函数的价值就在这。</p>
      </div>
    </div>
    <div class="derive-step">
      <div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">0-1 分布的特征函数</span><span class="derive-step-arrow">▶</span></div>
      <div class="derive-step-body">
        <p>ξ 取 1 的概率 p、取 0 的概率 q=1-p。$\varphi(t)=q\cdot e^{0}+p\cdot e^{it}=q+pe^{it}$。</p>
        <p>验证 $\varphi(0)=q+p=1$。$|\varphi(t)|$ 最大在 t=0，因为两项同向相加。</p>
        <p>用它可以快速算 n 个独立 0-1 之和（二项分布）的特征函数：$(q+pe^{it})^n$，展开后系数正是二项概率。这条和第 12 节的二项分布殊途同归。</p>
      </div>
    </div>
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 若 η 与 ξ 独立，$E(\eta\mid\xi=x)$ 等于什么？</div>
    <div class="qa-a">等于 $E\eta$，与 x 无关。独立意味着知道 ξ 不提供任何关于 η 的信息。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 为什么均方误差最小的预测是条件期望，而不是均值？</div>
    <div class="qa-a">均值只用了 η 自己的信息。条件期望还用上了 ξ 的信息：给定 x 后 η 的分布已经变了，用它的平均更准。只有 ξ 对 η 毫无信息（独立）时，两者才相同。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q3. 特征函数为什么必须带 i？</div>
    <div class="qa-a">i 让 $e^{it\xi}$ 的模恒为 1，保证 $|\varphi|\le1$；也让"相加变相乘"成立。若换成实指数 $e^{t\xi}$，独立时也能相乘，但 t 稍大积分就发散，很多分布压根不存在。</div>
  </div>

  <div class="chapter-nav"></div>
</section>

<section class="chapter" id="summary">
  <div class="breadcrumb"></div>
  <h2><span class="num">26</span>全景回顾与自测</h2>
  <p class="lead">三章共 20 节，主线只有一条：怎么把"可能发生什么"量化。这一节把整条链压成一张图、几张表，再给一份自测清单。</p>

  <h3>26.1 一条主线的三层结构</h3>
  <div class="knowledge-tree">
    <div class="kt-level">
      <div class="kt-label">第一层：概率本身</div>
      <div class="kt-node" data-goto="event-space">随机事件与样本空间</div>
      <div class="kt-node" data-goto="frequency-prob">频率与三公理</div>
      <div class="kt-node" data-goto="classical-geom">古典概型与几何概型</div>
      <div class="kt-node" data-goto="conditional">条件概率</div>
      <div class="kt-node" data-goto="total-bayes">全概率与贝叶斯</div>
      <div class="kt-node" data-goto="independence">独立性</div>
    </div>
    <div class="kt-level">
      <div class="kt-label">第二层：用变量描述</div>
      <div class="kt-node" data-goto="discrete-rv">离散型与分布列</div>
      <div class="kt-node" data-goto="discrete-2d">二维离散</div>
      <div class="kt-node" data-goto="discrete-func">离散型函数分布</div>
      <div class="kt-node" data-goto="dist-func">分布函数</div>
      <div class="kt-node" data-goto="continuous-density">连续型与密度</div>
      <div class="kt-node" data-goto="continuous-2d">二维连续</div>
      <div class="kt-node" data-goto="continuous-func">连续型函数分布</div>
    </div>
    <div class="kt-level">
      <div class="kt-label">第三层：用几个数概括</div>
      <div class="kt-node" data-goto="expectation">期望</div>
      <div class="kt-node" data-goto="variance">方差</div>
      <div class="kt-node" data-goto="cond-expect">条件期望</div>
      <div class="kt-node" data-goto="numeric-features">协方差与切比雪夫</div>
      <div class="kt-node" data-goto="regression-char">回归与特征函数</div>
    </div>
  </div>
  <p>三层之间有明确的依赖：第二层要算概率，所以用第一层的公理和公式；第三层要算积分求和，所以用第二层的密度和分布列。反过来不成立——不会有人用方差去定义概率。</p>

  <h3>26.2 公式速查</h3>
  <div class="table-wrap">
  <table>
    <tr><th>主题</th><th>核心公式</th><th>节</th></tr>
    <tr><td>条件概率</td><td>$P(A\mid B)=\dfrac{P(AB)}{P(B)}$</td><td>10</td></tr>
    <tr><td>全概率</td><td>$P(A)=\sum_iP(B_i)P(A\mid B_i)$</td><td>11</td></tr>
    <tr><td>贝叶斯</td><td>$P(B_i\mid A)=\dfrac{P(B_i)P(A\mid B_i)}{\sum_jP(B_j)P(A\mid B_j)}$</td><td>11</td></tr>
    <tr><td>二项概率</td><td>$P(\xi=k)=C_n^kp^kq^{n-k}$</td><td>12</td></tr>
    <tr><td>泊松逼近</td><td>$P(\xi=k)\approx\dfrac{\lambda^k}{k!}e^{-\lambda}$</td><td>13</td></tr>
    <tr><td>分布函数</td><td>$F(x)=P(\xi\le x)$</td><td>19</td></tr>
    <tr><td>密度与概率</td><td>$P(a\lt\xi\le b)=\int_a^bp(x)dx$</td><td>20</td></tr>
    <tr><td>正态密度</td><td>$p(x)=\dfrac{1}{\sqrt{2\pi}\sigma}e^{-(x-\mu)^2/(2\sigma^2)}$</td><td>21</td></tr>
    <tr><td>边缘密度</td><td>$p_\xi(x)=\int p(x,y)dy$</td><td>22</td></tr>
    <tr><td>卷积</td><td>$p_{\xi+\eta}(z)=\int p_\xi(x)p_\eta(z-x)dx$</td><td>23</td></tr>
    <tr><td>方差展开</td><td>$D\xi=E\xi^2-(E\xi)^2$</td><td>17</td></tr>
    <tr><td>和的方差</td><td>$D(\xi+\eta)=D\xi+D\eta+2\mathrm{Cov}$</td><td>24</td></tr>
    <tr><td>切比雪夫</td><td>$P(|\xi-E\xi|\ge\varepsilon)\le\dfrac{D\xi}{\varepsilon^2}$</td><td>24</td></tr>
    <tr><td>特征函数</td><td>$\varphi(t)=E(e^{it\xi})$</td><td>25</td></tr>
  </table>
  </div>

  <h3>26.3 自测清单</h3>
  <p>每条都要能不看前面章节、自己从头写出推导。写不出来就回到对应节。</p>
  <div class="qa-item">
    <div class="qa-q">1. 三个事件两两独立，能推出相互独立吗？</div>
    <div class="qa-a">不能。第 12 节给了 110/101/011/000 的反例。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">2. 从 5 个球里摸 2 个，有放回和无放回的概率为什么不同？</div>
    <div class="qa-a">有放回时两次独立，各有 5 种；无放回时第二次只剩 4 种。分母从 25 变成 20。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">3. 体检阳性率 99%，为什么真病概率只有 4.6%？</div>
    <div class="qa-a">因为基础患病率低，大量健康人的假阳性把阳性样本池稀释了。第 11 节算过。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">4. 离散型的分布函数为什么是阶梯？</div>
    <div class="qa-a">概率集中在可列个点上，每过一个点累积值跳一次。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">5. 连续型取单点的概率为什么是 0？</div>
    <div class="qa-a">用区间概率夹逼，F 连续所以两端都趋于同一个值。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">6. 密度能大于 1 吗？</div>
    <div class="qa-a">能。约束是曲线下面积为 1，不是高度。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">7. 指数分布的无记忆性怎么推？</div>
    <div class="qa-a">用尾概率 $P(\xi\gt x)=e^{-\lambda x}$，条件概率的比值里 $e^{-\lambda s}$ 约掉。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">8. 正态密度前的系数怎么来的？</div>
    <div class="qa-a">两次换元把指数部分化成高斯积分，得 $\sigma\sqrt{2\pi}$，取倒数做系数。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">9. $\eta=\xi^2$ 的密度为什么是两项相加？</div>
    <div class="qa-a">正负两支都映射到同一个 y，两条分支的密度都要计入。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">10. 两个 $U(0,1)$ 相加为什么是三角形？</div>
    <div class="qa-a">卷积的被积区间长度随 z 变化，中间最长两端变零。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">11. 协方差为 0 说明什么？说明不了什么？</div>
    <div class="qa-a">说明没有线性同步，说明不了独立。$\eta=\xi^2$ 是反例。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">12. 切比雪夫不等式的证明关键一步是什么？</div>
    <div class="qa-a">在尾部区域上 $(x-E\xi)^2/\varepsilon^2\ge1$，用它放大被积函数，再把积分扩到全轴。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">13. 为什么条件期望是最优平方预测？</div>
    <div class="qa-a">误差平方展开后的交叉项为 0，只剩两项，第二项非负且仅在 $g=m$ 时为 0。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">14. 特征函数怎么把卷积变成乘法？</div>
    <div class="qa-a">$e^{it(\xi+\eta)}=e^{it\xi}e^{it\eta}$，独立时期望也拆开相乘。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">15. 正态可加性为什么用特征函数证最快？</div>
    <div class="qa-a">指数上的二次型直接相加，比卷积积分配方短得多。</div>
  </div>

  <h3>26.4 五个反复踩的误区</h3>
  <p>（1）<b>互斥当独立。</b>互斥是"不能同时发生"，独立是"发生与否互不影响"。两个概率都为正的互斥事件一定不独立。</p>
  <p>（2）<b>$P(A\mid B)$ 与 $P(B\mid A)$ 颠倒。</b>前者以 B 为分母，后者以 A 为分母。基础率谬误的根源就在这里。</p>
  <p>（3）<b>密度当概率。</b>密度要乘区间长度（或积分）才是概率，且可以大于 1。</p>
  <p>（4）<b>不相关当独立。</b>只有正态分布时两者才等价，其他分布不成立。</p>
  <p>（5）<b>方差当平均偏差。</b>方差是偏差平方的平均，单位是原来的平方。要回到原单位得开根号，得到标准差。</p>

  <div class="callout callout-key">
    <div class="callout-title">这门课之后往哪走</div>
    这三章是概率论的公理与描述部分。往下是极限理论：大数定律说样本均值收敛到期望（切比雪夫不等式是它的证明工具），中心极限定理说和的分布趋于正态（正态可加性加特征函数是它的证明工具）。再往后进入数理统计：参数估计、假设检验，都需要这里的分布函数、密度和数字特征。
  </div>

  <h3>思考题</h3>
  <div class="qa-item">
    <div class="qa-q">Q1. 这 26 节里，哪几节是纯工具、哪几节是主干？</div>
    <div class="qa-a">第 1 到 5 节是工具（集合、计数、求和、微积分）。第 6 到 12 节是概率主干。第 13 到 18 节是离散型，第 19 到 25 节是连续型。第 26 节是回顾。</div>
  </div>
  <div class="qa-item">
    <div class="qa-q">Q2. 如果只能记住三个公式，记哪三个？</div>
    <div class="qa-a">条件概率的除法、全概率公式、方差展开 $D\xi=E\xi^2-(E\xi)^2$。前两个是几乎所有计算的入口，第三个是从定义推一切方差性质的起点。</div>
  </div>

  <div class="chapter-nav"></div>
</section>
"""
