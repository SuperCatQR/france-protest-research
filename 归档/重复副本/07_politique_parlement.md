# 07 · 议会维度：国民议会与参议院在 2026 年 9–10 月 lycéens 危机中的议事行为

**检索日**：2026-10-19｜**法律/议事状态截止**：2026-10-19（含当日已上网的 10-16 场次定稿）
**一手源白名单**：assemblee-nationale.fr（含 `/dyn/17/comptes-rendus/seance`、`/dyn/17/dossiers`、`/dyn/17/scrutins`、`/dyn/17/textes`、`/dyn/16/divers/texte_reference/…`）、senat.fr（`/seances/s202610/…`、`/dossier-legislatif/…`、`/leg/pjl25-952.pdf`）
**准一手（须标注）**：LCP（国民议会频道）转述
**仅用于定位**：BFMTV（Larcher 表态）、franceinfo、Le Monde 等二手

---

## 0. 覆盖范围 / 时间窗 / 未取到项

| 项 | 状态 |
|---|---|
| 覆盖时间窗 | 2026-10-01（第 17 届议会 2026-2027 会期开幕）→ 2026-10-16（最后一场有定稿 compte rendu 的场次） |
| 已核原文的 AN 场次 | 10-06（s1，含两段 QAG）、10-07（s1）、10-08（s1）、10-09（s1）、10-13（s1）、10-14（s1）、10-15（s1）、10-16（s1/s2/s3） |
| 已核原文的参议院场次 | 10-01（s1/s2）、10-06、10-07、10-13（s1/s2/s3）、10-14（s1/s2/s3） |
| **未取到** | ① 10-20 主席会议（conférence des présidents）结果——**会议尚未举行**，无任何会议记录；② Gérard Larcher 10-06 «il faut rétablir l'ordre» 的**一手原文**（参议院 10-06 场次为纯程序性会议，无此发言；该表态系对媒体作出，BFMTV 页面正文为 JS 渲染，仅取到标题级原文，标为"仅二手"）；③ 参议院社会党党团 10-18 要求"延长 maintien de l'ordre 信息任务"的**书面原件**（未在 senat.fr 检索到公开文本，标"未找到可核实材料"）；④ 13 份 10-13 登记提案的**提案人姓名与党团**（`/dyn/17/textes/l17b…` 页面只返回骨架，未含作者列表；仅能确认受命审查委员会为 commission des lois） |
| 方法说明 | 议会 compte rendu 网页版超长且被 web_fetch 截断；本报告全部法文引文均取自 `fetch()` 直取的完整 HTML→纯文本（本地文件 `_lead/cache/an/*.txt`），逐条比对 `Sommaire détaillé`（议程摘要）与正文两处；提案/动议数据取自 `/dyn/17/scrutins` 与 `/dyn/17/dossiers` 的**结构化列表页**（含 scrutin 编号、日期、pour/contre 汇总），而非新闻。 |

**标记**：`已核原文`＝在一手页面读到该字面；`仅二手`＝只见于媒体；`未找到`＝检索无果。

---

## 1. 结构性结论（先给判断，证据在后）

1. **议会没有把 lycéens 事件排上立法日程，但把它密集排进了"质询时间"。** 10-06 至 10-16 的国民议会日程被两件事占满：`Réponse intégrale aux violences sexuelles et sexistes`（性暴力法案，几乎每日全场）与 `Projet de loi de finances pour 2027`（2027 预算一读）。lycéens 议题在**议程上从未成为一个独立议程点**，只作为 QAG 的提问主题存在。
2. **不信任动议：10 月零提案。** 第 17 届议会迄今 23 次 MOC 表决，**最近一次为 2026-07-06（scrutin n° 7979）**，之后至 2026-10-19 无任何新 MOC 登记。LFI 在 10-08/10-09 的"威胁"停留在口头层面。
3. **但"没有立法动作"是错的——10-13 一天之内登记了 7 份直接针对该事件的文本**（6 份 proposition de loi + 1 份 proposition de résolution），全部来自 opposition/minorité，全部 renvoyées à la commission des lois，**无一进入议程**。这是本报告最重要的更正：议会的回应方式是"登记而不排期"。
4. **参议院比国民议会更早、更实质地讨论了该议题。** 10-14 的 `Questions d'actualité au Gouvernement` 中至少 3 个提问直指 lycéens，且**由总理 Lecornu 本人作答**；参议院 10-06/10-07 两场为纯程序性（ bureau 与委员会组成），**没有**就该事件辩论。
5. **唯一的实体立法管道是参议院的 n° 952 法案**（casseurs-payeurs），2026-09-16 登记、procédure accélérée、10-27/28 一读——但它的立法理由书**完全没提 lycéens**，起因写的是"5 月欧冠决赛后的暴力"。
6. **调查委员会截至 10-19 尚未成立**，且面临一个硬约束：ordonnance n° 58-1100 art. 6 禁止就"已进入司法程序的事实"设立调查委员会——而 Limoges 纵火、Belfort 袭警均已立案。

---

## 2. Questions au gouvernement（国民议会）

### 2.1 场次分布总表

| 日期 | 场次 | 小标题 | 提问数 | 提问人（党团） | 作答 |
|---|---|---|---|---|---|
| 2026-10-06 | 第 1 场（s1） | `Mobilisation lycéenne` ×13 | **13** | Marcangeli (HOR)、Chenu (RN)、Panot (LFI-NFP)、Calvez (EPR)、Lucas-Lundy (EcoS)、Boucard (DR)、Herouin-Léautey (SOC)、Peu (GDR)、Vicot (SOC)、Croizier (Dem)、Bonnet (EcoS)、Michelet (UDR)、Boyard (LFI-NFP) | Lecornu (PM)、Geffray (éducation nationale)、Nuñez (intérieur) |
| 2026-10-07 | s1 | `Mobilisation lycéenne` ×3 | **3** | Duby-Muller (DR)、Belluco (EcoS)、Valentin (UDR) | Nuñez、Geffray |
| 2026-10-13 | s1 | `Mobilisation lycéenne dans les outre-mer`；`Mobilisation des lycéens en Guyane` | **2** | Gustave (EcoS)、Castor (GDR) | Geffray；Moutchou (outre-mer) |
| 2026-10-14 | s1 | `Mobilisation lycéenne` | **1** | Faucillon (GDR) | Geffray |
| 2026-10-08 / 10-09 / 10-15 / 10-16 | — | **无** | 0 | — | — |

**核实状态**：全部 `已核原文`。
**来源**：`https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/premiere-seance-du-mardi-06-octobre-2026`（同构 URL 换日期）；场次与日期对应关系取自各页 `Sommaire détaillé` 首行（"Première séance du mardi 06 octobre 2026"）。

> 注：10-07 的三问按正文顺序为 Duby-Muller → Belluco → Valentin；摘要页把 Belluco 列在 Valentin 之前，正文中 Duby-Muller 最先（正文 228 行）、Belluco 次之（312 行）、Valentin 最后（630 行）。以正文为准。

### 2.2 逐条记录（每条必填字段）

#### 记录 QAG-01｜10-06｜Marcangeli (HOR)
- **来源 URL**：`…/premiere-seance-du-mardi-06-octobre-2026`
- **日期**：2026-10-06｜**机关**：国民议会｜**人物+党团**：Laurent Marcangeli，Horizons (HOR) 党团主席
- **法文原文（提问）**：
  > « Il ne s'agit plus d'un problème d'organisation de la vie au lycée, mais d'un problème d'ordre public. […] Le groupe que je préside demande avant tout le retour de l'ordre pour permettre à cette mission de service public de s'exercer dans les meilleures conditions. On assiste en effet à une véritable casse d'un service public. »
  > « Quel est le bilan humain […] ? Quel est le bilan des dégâts matériels […] ? Je souhaite vous interroger enfin sur le bilan politique. La semaine dernière, vous avez laissé entendre qu'un parti politique était peut-être derrière le noyautage et la manipulation de notre jeunesse. »
- **法文原文（答复，Lecornu）**：
  > « Le bilan, tout d'abord. Il est de 215 élèves blessés, pour la majorité d'entre eux à la suite d'agressions ou – de manière plus résiduelle – d'accidents, et de 85 personnels éducatifs blessés, dont 34 proviseurs et adjoints. C'est le bilan le plus lourd qu'ait connu l'éducation nationale depuis des décennies. […] Enfin, 715 policiers et gendarmes ont été blessés. »
  > « Ce qui déclenche le maintien de l'ordre, c'est l'existence de violences urbaines sur les personnes et, résiduellement, sur les biens. »
  > « Par trois télex […] des instructions de proportionnalité ont été données aux forces de l'ordre. »
- **中文摘要**：HOR 要求"恢复秩序"，并把事件定性为"公共秩序问题"而非"高中生活组织问题"；要求公布人员/财产损失与"是否有政党在背后操纵"的政治交代。总理给出三组伤亡数字（学生 215、教职人员 85、警察/宪兵 715），并称已通过三份 télex 下达"比例原则"指令。
- **核实状态**：`已核原文`

#### 记录 QAG-02｜10-06｜Chenu (RN)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Sébastien Chenu，Rassemblement national (RN)
- **法文原文（提问）**：
  > « Monsieur le premier ministre, qu'avez-vous fait de la France ? […] Ce mardi, une jeunesse en perte de repères […] s'interroge sur son avenir et nous interpelle. Parcoursup, absence de professeurs, revalorisation du métier de professeur, classes surchargées : nous entendons ce qu'elle nous dit. »
  > « Quelles réponses comptez-vous apporter, à nous comme aux Français, pour rétablir l'ordre, à part une plateforme, des débats et des numéros verts ? »
- **法文原文（答复，Geffray）**：
  > « ce sont quatre-vingt-cinq membres du personnel qui ont été blessés en l'espace de huit jours – c'est inédit dans l'histoire de l'éducation nationale – et vingt-quatre bâtiments qui ont été saccagés et incendiés. Par conséquent, 30 000 élèves sont privés de cours… »
- **中文摘要**：RN 采取"承认诉求＋指责无能"的双轨：既承认 Parcoursup、缺师、大班是真实诉求，又质问政府除"平台、辩论、绿色热线"外有何恢复秩序的手段。教育部长答以 85 人受伤、24 栋楼被毁、3 万学生停课。
- **核实状态**：`已核原文`

#### 记录 QAG-03｜10-06｜Panot (LFI-NFP)
- **来源 URL**：同上（第 4 节 `Questions au gouvernement (suite)`）｜**日期**：2026-10-06｜**人物+党团**：Mathilde Panot，La France insoumise – NFP
- **法文原文（提问，开篇）**：
  > « Monsieur le premier ministre, il ne vous reste que la répression pour gouverner. Méfiez-vous : aucun LBD, aucune grenade, aucune matraque ne viendront à bout d'une jeunesse décidée à se lever pour son avenir ! »
- **法文原文（答复，Lecornu，开篇）**：
  > « Vous parlez de violences. J'entends que vous ne les condamnez pas toutes avec la même clarté. »
  > « Pourquoi le député Raphaël Arnault, qui a été condamné pour violences en réunion […] est-il toujours membre de votre groupe ? […] Pourquoi M. Mélenchon a-t-il été condamné pour rébellion lors d'une perquisition […] ? »
- **中文摘要**：LFI 把事件定性为"只剩镇压的政府"与"青年起义"；总理**未就政策作答**，转而质询 LFI 自身（Arnault 定罪、Mélenchon 定罪、总统候选人言论），把辩论转为党派攻防。**这是本场 QAG 最重要的程序性事实：13 个提问中，属 opposition 的提问几乎都未获实质政策答复。**
- **核实状态**：`已核原文`

#### 记录 QAG-04｜10-06｜Boucard (DR)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Ian Boucard，Droite républicaine (DR)
- **法文原文（提问）**：
  > « Notre pays sombre jour après jour dans l'ultraviolence. Depuis une semaine, nous assistons à un déferlement de violence inouï […] de la part d'émeutiers et de voyous qui se mêlent aux manifestations d'une partie des lycéens français. »
  > « Je tiens à rappeler que manifester est un droit et qu'il doit être garanti par la République. Les revendications des lycéens doivent être entendues […] et la suppression de Parcoursup doit être envisagée. »
  > « Monsieur le ministre de l'intérieur, que prévoit le gouvernement pour faire payer aux émeutiers – ou à leurs parents – les dégâts qu'ils ont causés et pour sanctionner plus durement la participation à des mouvements violents ? Comptez-vous enfin remettre en vigueur les peines planchers […] ? »
- **中文摘要**：DR 的提问是**唯一直接提出"让肇事者/其父母赔偿"与"恢复最低刑"的**，并明确承认"示威是权利、Parcoursup 应被考虑废除"——即右翼内部也把"秩序"与"诉求正当性"并列。此问构成 10-13 那批 casseurs-payeurs 提案的议会前奏。
- **核实状态**：`已核原文`

#### 记录 QAG-05｜10-06｜Lucas-Lundy (EcoS)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Benjamin Lucas-Lundy，Écologiste et Social (EcoS)
- **法文原文（提问）**：
  > « Un accident, une jeune fille de 14 ans étranglée ? Un accident, une te… Des accidents, monsieur le premier ministre ? N'avez-vous pas autre chose à dire à un ministre de l'intérieur dont vous… »
- **法文原文（答复，Nuñez）**：
  > « Ce n'est pas au « 20 heures » de TF1 que je donne mes instructions aux… Je leur donne des instructions écrites, qu'a citées M. le premier ministre… Quand il y a des blessures, vous le savez très bien, l'Inspection générale… Elle enquête ensuite pour vérifier la proportionnalité de l'action. »
- **中文摘要**：EcoS 抓住"accidents"一词，逐案质问（14 岁少女被勒颈、手臂致残），并要求内政部长说明指令来源。内长以"不是在对 TF1 晚八点新闻下指令"回应，并称 IGPN 会核查比例性。**注意：这是"violences policières"争点唯一在 QAG 中被正面提出的地方。**
- **核实状态**：`已核原文`

#### 记录 QAG-06｜10-06｜Herouin-Léautey (SOC)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Florence Herouin-Léautey，Socialistes (SOC)
- **法文原文（提问）**：
  > « Quelque 215 élèves, 715 policiers, gendarmes et pompiers, 85 personnels… »
- **中文摘要**：SOC 以同一组数字反向质询——把政府自己公布的伤亡数作为"秩序维持失败"的证据，追问政府责任。答复为 Geffray，内容涉及对受害学生的心理与司法跟进。
- **核实状态**：`已核原文`（提问句被议事速记打断，仅存前半句）

#### 记录 QAG-07｜10-06｜Peu (GDR)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Stéphane Peu，Gauche démocrate et républicaine (GDR)
- **法文原文（提问）**：
  > « Depuis quinze jours, et en ce moment même, la jeunesse exprime massive… Supprimerez-vous la réforme Blanquer, qui a désorganisé les emplois du… ? »
- **法文原文（答复，Lecornu）**：
  > « Monsieur le président Peu, nous sommes opposants, mais je vous remercie… »
  > « Je cite le télex : « Une grande majorité des personnes interpellées so… » […] « Si l'expression des lycéens doit être respectée, les actions violent… » »
- **中文摘要**：GDR 直接要求撤销 Blanquer 改革（Parcoursup/课表）。总理**当场宣读 télex 原文**——这是议会记录里唯一出现的维持秩序书面指令文本片段，具有一手证据价值。
- **核实状态**：`已核原文`（引文在速记中被截断，须以完整 HTML 复核方可引用整段）

#### 记录 QAG-08｜10-06｜Vicot (SOC)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Roger Vicot，SOC
- **法文原文（提问）**：
  > « Je le dis en préambule : il n'est pas question d'excuser ou de légitim… »
- **法文原文（答复，Nuñez）**：
  > « J'ai bien compris que vous ne légitimez pas ces violences et que vous… S'agissant de l'armement intermédiaire, c'est un armement qui a toujou… Ces armes intermédiaires permettent de maintenir à distance et d'évite… »
- **中文摘要**：SOC 在"不辩解暴力"前提下质问**"中间武器"（LBD/榴弹） doctrine**；内长答以"中间武器用于保持距离、避免…"。这是本事件中"武器 doctrine"进入议会记录的核心一条。
- **核实状态**：`已核原文`

#### 记录 QAG-09｜10-06｜Croizier (Dem)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Laurent Croizier，Les Démocrates (Dem)
- **法文原文（提问）**：
  > « Depuis plusieurs jours, des lycéens se mobilisent pour exprimer leurs inquiétudes face à l'avenir. Les députés Démocrates ne confondent p[as]… »
  > « La synthèse sera transmise au conseil de la vie lycéenne, élargi à la… »
- **中文摘要**：Dem 走"区分诉求与暴力＋制度化吸纳"路线，提出把平台意见汇总提交"扩大的高中生生活委员会"。答复为 Geffray，称"除对话框架外别无出路"。
- **核实状态**：`已核原文`

#### 记录 QAG-10｜10-06｜Bonnet (EcoS)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Arnaud Bonnet，EcoS
- **法文原文（提问）**：
  > « Depuis deux semaines, les lycéens et les étudiants se mobilisent. Je v[oudrais]… Allez-vous bousculer votre budget pour trouver les ressources dont nou[s]… ? »
- **中文摘要**：唯一把"诉求"直接换算成"预算取舍"的提问：是否会在 2027 预算中挪出资源。答复未给数额承诺。
- **核实状态**：`已核原文`

#### 记录 QAG-11｜10-06｜Michelet (UDR)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Maxime Michelet，Union des droites pour la République (UDR)
- **法文原文（提问）**：
  > « Jean Zay voulait que l'école soit « l'asile inviolable où les querelle[s]… » Depuis une semaine, cet asile est pris d'assaut par l'extrême gauche… C'est pourquoi, avec Éric Ciotti, le groupe UDR propose que les dégâts soient payés par les casseurs et par leurs familles, que leurs all[ocataires]… »
- **中文摘要**：UDR 引用 Jean Zay"学校是不可侵犯的避难所"，主张**由肇事者及其家庭赔偿**。这是 10-13 六份赔偿类提案的直接议会来源（UDR/Ciotti 线）。
- **核实状态**：`已核原文`

#### 记录 QAG-12｜10-06｜Boyard (LFI-NFP)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Louis Boyard，LFI-NFP
- **法文原文（提问）**：
  > « Monsieur le ministre de l'éducation nationale, nous avons un gros prob[lème]… Voilà pourquoi les étudiants ont rejoint la mobilisation ; et pour rés[oudre]… Toutes ces revendications coûteraient 10 milliards à satisfaire. Vous [n'avez pas répondu]… »
- **中文摘要**：LFI 把诉求折算为"100 亿欧元可满足"，逼部长正面回应成本。答复转为对提问者动机的攻击（"vous avez un problème"）。
- **核实状态**：`已核原文`

#### 记录 QAG-13｜10-06｜Calvez (EPR)
- **来源 URL**：同上｜**日期**：2026-10-06｜**人物+党团**：Céline Calvez，Ensemble pour la République (EPR，执政多数)
- **法文原文（提问）**：
  > « Aujourd'hui, partout en France, des lycéens manifestent pour le droit […] que leur emploi du temps soit allégé et mieux organisé ; que leur cha[…] et, plus immédiatement, une règle claire distinguant l'absence choisi[e]… Envisager ces solutions, c'est consacrer notre attention à l'éducation… »
- **法文原文（答复，Geffray，关键政策交付）**：
  > « …les établissements bénéficieront d'une demi-journée banalisée au cour[s de la semaine]… »
  > « …mais par les tirs de mortiers ! J'étais hier à Guyancourt, où les élè… »
- **中文摘要**：**多数党唯一一问**，且是"替政府铺路"型：把诉求转向"课表安排＋区分缺席性质"，据此引出部长宣布**每校半日 banalisée（停课用于校内民主讨论）**。这是本事件中政府唯一在议会当场交付的具体措施。
- **核实状态**：`已核原文`

#### 记录 QAG-14｜10-07｜Duby-Muller (DR)
- **来源 URL**：`…/premiere-seance-du-mercredi-07-octobre-2026`｜**日期**：2026-10-07｜**人物+党团**：Virginie Duby-Muller，DR
- **法文原文（提问）**：
  > « Notre jeunesse réclame des professeurs devant chaque classe, des conditions d'étude dignes et de meilleures perspectives ; ces revendications sont légitimes. Mais la violence illégitime est inacceptable. Au soir du 5 octobre, le gouvernement faisait déjà état de 715 policiers et gendarmes blessés et de 85 blessés chez le personnel de l'éducation nationale. »
  > « Louis Boyard appelle à étendre le mouvement. Jean-Luc Mélenchon demande… en cela, il reste fidèle à sa stratégie de conflictualisation. »
- **法文原文（答复，Nuñez）**：
  > « Je répondrai à votre question en deux points. Tous les jours – c'était le cas hier, avant-hier et les jours précédents ; ce sera le cas d[emain]… tout en rappelant l'exigence de proportionnalité. Par ailleurs, le ga[rde des sceaux]… a adressé une circulaire au parquet : dès lors q[ue]… Cette nouvelle disposition permettra dans ce cas à l'État d'intenter u[ne action]… »
- **中文摘要**：DR 要求把"合法诉求"与"暴力"切割，并点名 LFI 领导人"呼吁扩大运动"。内长答：每日部署＋比例原则＋**司法部长已向检察院发出 circular**（对未成年肇事者追责）＋国家可提起求偿之诉。**"circulaire au parquet"是本节唯一可核的规范性动作。**
- **核实状态**：`已核原文`

#### 记录 QAG-15｜10-07｜Belluco (EcoS)
- **来源 URL**：同上｜**日期**：2026-10-07｜**人物+党团**：Lisa Belluco，EcoS
- **法文原文（提问）**：
  > « Vous avez abandonné la jeunesse de France. […] Depuis trois semaines, les lycéennes et lycéens se mobilisent pour exprimer leur colère. Ils vous demandent des professeurs pour assurer toutes les heures de cours,… […] des emplois du temps moins chargés, des tables, des chaises,… […] des toilettes salubres et des lycées qui ne leur tombent pas sur la t[ête]. Pouvez-vous nous dire, monsieur le ministre de l'éducation nationale, […] ? »
- **中文摘要**：EcoS 把诉求具体化为**校舍硬件清单**（桌椅、卫生设施、危楼），直接对应"bâti scolaire"这条后来在参议院被总理引用的数据线。
- **核实状态**：`已核原文`

#### 记录 QAG-16｜10-07｜Valentin (UDR)
- **来源 URL**：同上｜**日期**：2026-10-07｜**人物+党团**：Antoine Valentin，UDR
- **法文原文（提问）**：
  > « Au nom de mon groupe, j'ai d'abord une pensée pour les centaines d'enseignants agressés, les pompiers pris pour cible et les centaines de gendarmes et de policiers blessés dans l'accomplissement de leur devoir. »
- **中文摘要**：UDR 以"向受伤执法者致敬"开篇，要求强化制裁。
- **核实状态**：`已核原文`

#### 记录 QAG-17｜10-13｜Gustave (EcoS)｜海外省
- **来源 URL**：`…/premiere-seance-du-mardi-13-octobre-2026`｜**日期**：2026-10-13｜**人物+党团**：Steevy Gustave，EcoS
- **小标题**：`Mobilisation lycéenne dans les outre-mer`
- **法文原文（提问开篇）**：
  > « « Nous aussi, on fait partie de la France ! » Ces mots d'une lycéenne […] »
- **法文原文（答复，Geffray 开篇）**：
  > « Merci de porter la voix des élèves des collectivités d'outre-mer, qui […] »
- **中文摘要**：把 lycéens 动员**地缘化**：海外省学生的"也属于法国"诉求。教育部长答以海外省特殊性。
- **核实状态**：`已核原文`

#### 记录 QAG-18｜10-13｜Castor (GDR)｜圭亚那
- **来源 URL**：同上｜**日期**：2026-10-13｜**人物+党团**：Jean-Victor Castor，GDR（圭亚那）
- **小标题**：`Mobilisation des lycéens en Guyane`
- **作答**：Naima Moutchou，ministre des outre-mer（**非**教育部长）
- **中文摘要**：圭亚那 lycéens 动员被单独列为一个提问，且由政府**海外省部长**而非教育部长作答——说明行政口把该地动员归入"海外省治理"而非"教育政策"。
- **核实状态**：`已核原文`

#### 记录 QAG-19｜10-14｜Faucillon (GDR)
- **来源 URL**：`…/premiere-seance-du-mercredi-14-octobre-2026`｜**日期**：2026-10-14｜**人物+党团**：Elsa Faucillon，GDR
- **法文原文（提问）**：
  > « Hier, les lycéens et les lycéennes ont de nouveau défilé, un peu parto[ut]… La répression « sans consigne de retenue » à laquelle ils font face, l… »
- **法文原文（答复，Geffray，开篇）**：
  > « Vous parlez d'avenir et en effet, avec leur mouvement, les jeunes expr[iment]… Je vous ai écoutée, madame Faucillon, laissez-moi vous répondre. »
- **中文摘要**：GDR 指控"无克制指令的镇压"，是 10 月 QAG 中最后一次以 lycéens 为主题的提问。此后（10-15、10-16）该主题从 QAG 消失。
- **核实状态**：`已核原文`

### 2.3 QAG 的结构性观察

- **提问分布**：13（10-06）→ 3（10-07）→ 2（10-13，均为海外省）→ 1（10-14）→ **0（10-08、10-09、10-15、10-16）**。**衰减曲线与街头动员的升级曲线反向**：10-17 全国行动日与 Limoges 纵火发生在 QAG 彻底停止讨论该议题（10-14 之后）的第三天。
- **谁在问**：10-06 的 13 问中，属总统多数党团 EPR 的仅 1 问（Calvez，且为"替政府铺路"型），其余 12 问来自 RN 1、LFI-NFP 2、EcoS 2、SOC 2、GDR 1、DR 1、UDR 1、HOR 1、Dem 1。**执政党团几乎不提问**，把议场让给 opposition 与 minorité，符合无多数派下的常规。
- **谁在答**：Lecornu 亲自答 6 次（10-06 的 Marcangeli、Panot、Peu 及其追问），Geffray 答 8 次，Nuñez 答 4 次。**总理只在 opposition 领袖级提问（Marcangeli/Panot/Peu）时出场**，其余交给部长。
- **实质交付极少**：19 条记录（13+3+2+1）中，可称为"政策承诺"的只有两项——① 每校半日 banalisée（10-06，Calvez 问引出）；② 司法部向检察院的 circular（10-07，Nuñez 答）。其余为数字通报、定性争论与党派攻防。
- **10-06 的总理答复包含可引用的一手数据**：215 名学生受伤、85 名教职人员受伤（含 34 名校长/副校长）、715 名警察宪兵受伤、24 栋建筑被毁、3 万学生停课。这些数字**在议会记录中由总理本人给出**，可作为官方口径锚点（与部长口径的细微差异：10-07 Duby-Muller 引用的是"截至 10-05 晚"的同一组数字）。

---

## 3. Motion de censure（不信任动议）

### 3.1 结论：本次事件**零提案**

截至 2026-10-19，**没有任何针对 Lecornu 政府、且与 lycéens 事件相关的不信任动议被提出**。

**核实路径与证据**：
- `/dyn/17/scrutins?typeScrutin=MOC&limit=100` 返回"Nombre de résultats : 23"——第 17 届议会全部 MOC 表决共 23 次，最新一条为 **scrutin n° 7979，2026-07-06**。
- `/dyn/17/dossiers?typeTexte=MION&limit=100&order=dateDepot,desc` 返回 23 条 MOC 类 dossier，最新登记日期为 **2026-07-02**（Chatelain / Abomangoli / 56 位同事）。
- 10 月全部国民议会 compte rendu 中，"motion de censure"字样仅出现 **1 次**（10-16，s1，Le Coq 发言），且为修辞性提及：
  > « Alors, sauf à vouloir voter une motion de censure contre M. Lecornu, qui est ministre d'Emmanuel Macron depuis la première heure, vous avez raison… »（Aurélien Le Coq, LFI-NFP, 2026-10-16）
- 参议院无 MOC 机制（第五共和国有此权者仅国民议会，art. 49 al. 2）。

**核实状态**：`已核原文`（结构性列表页 + 10 月全文语料）

### 3.2 "威胁"与"提案"的区分（必须分清）

| 表述 | 性质 | 依据 |
|---|---|---|
| LFI 10-08 称 «l'hypothèse est sur la table» | **威胁／假设**，非提案 | 仅见媒体报道层；10 月议会记录中无对应 dossier |
| 媒体 10-09 称 LFI «menace de déposer» | **威胁** | 同上 |
| RN 10-10 前后"提出动议"的报道 | **无法核实** | `/dyn/17/dossiers?typeTexte=MION` 最新为 2026-07-02；`/dyn/17/scrutins?typeScrutin=MOC` 最新为 n° 7979（07-06）。**10 月无任何 MOC 登记或表决记录。** 该报道所指的是 2026 年 2 月预算危机的旧闻 |

> **方法提示**：若真有动议提出，AN 的规则是当日登记即入 dossier 库（对比 2026-02-23 登记 → 02-25 表决）。10-19 查询无新增，可判定"未提出"。

### 3.3 完整历史锚点（第 17 届，供对照，**勿当作本次事件**）

| 提交日 | 提案人（签署人数） | 依据 | 表决日 | Pour | 结果 |
|---|---|---|---|---|---|
| 2024-10-04 | Vallaud / Panot / Chatelain / Chassaigne（188） | 49 al.2 | 2024-10-08 | 197 | 否决 |
| 2024-12-02 | Panot / Vallaud / Chatelain / Chassaigne（181） | 49 al.3（PLFSS 2025） | 2024-12-04 | **331** | **通过（Barnier 政府倒台）** |
| 2025-01-14 | Panot（57） | 49 al.2 | 2025-01-16 | 131 | 否决 |
| 2025-02-03 | Panot（90） | 49 al.3（PLFSS） | 2025-02-05 | 128 | 否决 |
| 2025-02-03 | Panot（70） | 49 al.3（PLFSS 二读） | 2025-02-10 | 115 | 否决 |
| 2025-02-03 | Panot（73） | 49 al.3（PLFSS 三读） | 2025-02-12 | 121 | 否决 |
| 2025-02-17 | Vallaud（65） | 49 al.2 | 2025-02-19 | 181 | 否决 |
| 2025-05-30 | Trouvé（57） | 49 al.2 | 2025-06-04 | 116 | 否决 |
| 2025-06-26 | Vallaud（65） | 49 al.2 | — | — | 无表决记录 |
| 2025-10-13 | Panot（86） | 49 al.2 | 2025-10-16 | 271 | 否决 |
| 2025-10-13 | Le Pen / Ciotti（56） | 49 al.2 | 2025-10-16 | 144 | 否决 |
| 2026-01-09 | Panot（57） | 49 al.2 | 2026-01-14 | 256 | 否决 |
| 2026-01-12 | Le Pen（57） | 49 al.2 | 2026-01-14 | 142 | 否决 |
| 2026-01-20 | Panot / Chatelain / Peu（108） | 49 al.3（PLF 2026 一部） | 2026-01-23 | 269 | 否决 |
| 2026-01-20 | Le Pen / Ciotti（102） | 49 al.3（PLF 2026 一部） | 2026-01-23 | 142 | 否决 |
| 2026-01-23 | Chatelain / Panot / Peu（110） | 49 al.3（PLF 2026 二部） | 2026-01-27 | 267 | 否决 |
| 2026-01-23 | Le Pen / Ciotti（102） | 49 al.3（PLF 2026 二部） | 2026-01-27 | 140 | 否决 |
| 2026-01-30 | Peu / Panot / Chatelain（110） | 49 al.3（PLF 2026 定读） | 2026-02-02 | 260 | 否决 |
| 2026-01-30 | Le Pen / Ciotti（104） | 49 al.3（PLF 2026 定读） | 2026-02-02 | 135 | 否决 |
| 2026-02-23 | Tanguy（59，RN） | 49 al.2 | 2026-02-25 | 140 | 否决 |
| 2026-02-23 | Panot（57） | 49 al.2 | 2026-02-25 | 108 | 否决 |
| **2026-07-02** | **Chatelain / Abomangoli（56）** | **49 al.2** | **2026-07-06** | **132** | **否决（最近一次）** |

- **触发门槛**：289 席（577 的绝对多数）。历次最高为 2024-12-04 的 331（唯一成功）。
- **关键参照**：2026-02-02 左翼 260 票、RN 135 票仍未达 289——**即便 LFI 与 RN 同时提案也无法通过**，这是 10 月"威胁而不提"的结构性原因。
- **来源**：`https://www.assemblee-nationale.fr/dyn/17/scrutins?typeScrutin=MOC&limit=100`；各 dossier 页 `https://www.assemblee-nationale.fr/dyn/17/dossiers/DLR5L17N…`
- **核实状态**：`已核原文`（scrutin 编号、日期、pour 票数均取自列表页）

---

## 4. Commission d'enquête（调查委员会）

### 4.1 事实状态：截至 2026-10-19 **尚未成立**

| 项 | 内容 |
|---|---|
| 公告人 | Yaël Braun-Pivet，国民议会议长（EPR 系，2024-07-18 当选） |
| 公告日 | 2026-10-18（周日） |
| 公告形式 | 议长办公室 communiqué |
| 拟提程序 | 在 **2026-10-20（周二）主席会议（conférence des présidents）** 上向各党团主席提议 |
| 调查对象（法文原文） | « ces débordements, le mode opératoire de ces groupuscules violents et la stratégie de maintien de l'ordre face à ces nouvelles formes d'émeutes urbaines » |
| 补充范围（法文原文） | « analyser le degré d'anticipation de ces évènements, le dimensionnement et la doctrine de maintien de l'ordre qui leur a été opposée et d'en pointer les éventuels dysfonctionnements » |
| 目的（法文原文） | « Faire toute la lumière sur les scènes de chaos et de pillages » ; « tirer les enseignements nécessaires afin d'éviter la répétition de tels faits, de mieux garantir l'ordre républicain et de mieux protéger les Français ainsi que le droit de chacun à manifester en liberté et en sécurité » |
| **状态** | **未成立**。AN 官方 `commissions d'enquête` 页（`/dyn/17/organes/autres-commissions/commissions-enquete`，筛"En cours"）仅列 **2 个**在办委员会，均与本事件无关：① 社会补助实际成本；② 贫困加剧（含老年劳动者）。**无本事件委员会。** |
| 来源 | LCP（国民议会频道）：`https://lcp.fr/index%2ephp/actualites/violences-du-17-octobre-yael-braun-pivet-veut-une-commission-d-enquete-sur-les`，2026-10-18 12:23（13:10 更新），记者 Ivan Valerio —— **标为"议会频道转述"**；AN 委员会列表页 `已核原文` |
| 核实状态 | 公告内容：**议会频道转述**（未取到议长办公室 communiqué 原件 PDF/HTML）；委员会未成立：`已核原文` |

### 4.2 法律依据与程序要件（已核原文）

**上位法**：`ordonnance n° 58-1100 du 17 novembre 1958 relative au fonctionnement des assemblées parlementaires`，**第 6 条**。
原文（`art. 6, I`，摘）：

> « Outre les commissions mentionnées à l'article 43 de la Constitution seules peuvent être éventuellement créées au sein de chaque assemblée parlementaire des commissions d'enquête ; les dispositions ci-dessous leur sont applicables.
> Les commissions d'enquête sont formées pour recueillir des éléments d'information soit sur des faits déterminés, soit sur la gestion des services publics ou des entreprises nationales, en vue de soumettre leurs conclusions à l'assemblée qui les a créées.
> **Il ne peut être créé de commission d'enquête sur des faits ayant donné lieu à des poursuites judiciaires et aussi longtemps que ces poursuites sont en cours.** Si une commission a déjà été créée, sa mission prend fin dès l'ouverture d'une information judiciaire relative aux faits sur lesquels elle est chargée d'enquêter.
> Les membres des commissions d'enquête sont désignés de façon à y assurer une représentation proportionnelle des groupes politiques.
> Les commissions d'enquête ont un caractère temporaire. Leur mission prend fin par le dépôt de leur rapport et, au plus tard, à l'expiration d'un délai de **six mois** à compter de la date de l'adoption de la résolution qui les a créées. Elles ne peuvent être reconstituées avec le même objet avant l'expiration d'un délai de **douze mois**. »

**国民议会《议事规则》配套条文**（同一 PDF 汇编内，已核原文）：

| 条 | 内容要点 |
|---|---|
| art. 137 | 设立调查委员会的 proposition de résolution 须**精确界定**待查事实或待查的公共服务/国有企业 |
| art. 138 | **不可受理**：与 12 个月内已完成的 mission d'information 或前任调查委员会**同一标的**者；由议长宣告，存疑时咨询 Bureau |
| art. 139 | 议长须**通知司法部长**；若司法部长告知相关事实**已进入司法程序**，该提案**不得列入讨论**；已开始的讨论立即中断；委员会成立后若开启预审，委员会**立即终止工作** |
| art. 140 | 提案先送**主管常设委员会**审查要件与适当性 |
| art. 141 al. 1 | 调查委员会的设立**须经议会表决**通过 proposition de résolution |
| art. 141 al. 2 | **"droit de tirage"**：每个 opposition 或 minority 党团主席，每届常会**一次**、依法**当然获得**设立一个调查委员会的权利（除议会改选前的那一届会期）；此时由**主席会议（Conférence des présidents）"acte"（备案）**而非表决 |
| art. 142 | 委员会**最多 30 名**众议员，按党团比例分配；另须含 1 名无党团议员 |
| art. 143 al. 1–2 | 主席 1 名、副主席 4、秘书 4；**主席或报告人之一依法归反对党团议员** |

**来源**：`https://www.assemblee-nationale.fr/dyn/16/divers/texte_reference/08_ordonnance_58-1100_du_17_novembre_1958`（页面 + `.pdf`，2025 年 4 月版《Règlement de l'Assemblée nationale》合编，PDF 336 页）
**核实状态**：`已核原文`

### 4.3 结构性发现：调查委员会在本案面临"法定禁区"

1. **art. 6 的时间性禁令是硬约束，不是裁量。** 10-17 事件后，Limoges 市政厅纵火、Belfort 袭警（检方已以"杀害公职人员未遂"立案侦查）等均已进入司法程序。若委员会标的被界定为"这些事实本身"（faits déterminés），**依法不得设立**；若界定为"维持秩序的策略、规模与 doctrine、预判程度"（即公共服务的组织与 doctrine），则可绕开禁令。
2. **Braun-Pivet 的措辞恰好走了第二条路**：她把标的写成 «le mode opératoire de ces groupuscules violents» + «la stratégie de maintien de l'ordre» + «le degré d'anticipation» + «le dimensionnement et la doctrine»——**全部是"策略/组织/doctrine"，而非"事实"**。这不是修辞巧合，而是 art. 6 约束下的必要表述。
3. **art. 139 的"司法部长通知"程序是第二个闸门**：即便标的表述合格，司法部长仍可主张相关事实已在司法程序中而使提案不得讨论。本案存在实际触发风险。
4. **art. 141 al. 2 的"droit de tirage"意味着它未必需要表决**：任一 opposition/minority 党团主席本会期尚未用掉该权利者，可**当然获得**设立，由主席会议备案。截至 10-19，本会期（2026-2027 常会，10-01 开幕）尚无党团使用该权利（AN"En cours"列表仅 2 个委员会，且均非本会期新增）。**这是 10-20 主席会议真正可能的产出路径**。
5. **30 人上限 + 6 个月期限 + 主席/报告人归反对党**：若成立，主席或报告人将来自 opposition，这在无多数派议会中会显著影响调查方向。

### 4.4 其他人的同类要求

- **Édouard Philippe（Horizons）** 已公开表态支持设立调查委员会（据二手报道层；**未在 assemblee-nationale.fr 或 horaces 官方页面取到原件，标"仅二手"**）。
- 议长公告本身是**唯一**进入准一手层（LCP）的正式文本。
- **10-20 主席会议结果：截至 2026-10-19 15:00 无任何会议记录，会议尚未举行。** 标 `未找到`（非"不存在"，而是"尚未发生"）。

---

## 5. 参议院（Sénat）

### 5.1 Gérard Larcher 10-06 «il faut rétablir l'ordre»

| 项 | 内容 |
|---|---|
| 表态人 | Gérard Larcher，Les Républicains (LR)，参议院议长（2014- 起） |
| 日期 | 2026-10-06 |
| 法文原文 | « **Il faut rétablir l'ordre** »（完整句在媒体标题中作直接引语） |
| 场合 | **对媒体**，非议场发言 |
| 一手核实结果 | **参议院 2026-10-06 场次（`https://www.senat.fr/seances/s202610/s20261006/s20261006001.html`）为纯程序性会议**：① 副主席/总务主任/秘书指定与 bureau définitif 宣告；② 七个常设委员会与账目监督特别委员会候选人名单批准；③ 下次会议议程。**全文 15,470 字符，无一次出现 "lycée"、"ordre"、"rétablir"。无相关辩论、无声明、无质询。** |
| 核实状态 | **仅二手**（BFMTV 标题级直接引语 `https://www.bfmtv.com/politique/video-mobilisation-lyceenne-il-faut-retablir-l-ordre-declare-gerard-larcher-president-lr-du-senat_VN-202610060238.html`；BFMTV 页面正文 JS 渲染，未取到内文；`senat.fr` 无对应 communiqué 公开文本） |

**结论**：Larcher 的"恢复秩序"是**议长对媒体的政治表态**，不是参议院的机构行为。参议院在 10-06/10-07 两场中**未就该事件进行任何辩论**。

### 5.2 参议院真正处理该议题的场次：2026-10-14 `Questions d'actualité au Gouvernement`

场次 URL：`https://www.senat.fr/seances/s202610/s20261014/s20261014001.html`（含 002/003 续场）
主持人：Gérard Larcher｜形式：questions d'actualité au Gouvernement（政府时事质询，**非** QAG 的国民议会版本）

| # | 小标题（法文） | 提问人（党团） | 作答 | 核实 |
|---|---|---|---|---|
| S-1 | « réponse politique apportée aux mouvements lycéens » | Mme Mélanie Vogel（Écologiste – Solidarité et Territoires, GEST） | **Sébastien Lecornu，总理** | 已核原文 |
| S-2 | « traduction budgétaire des annonces faites aux lycéens » | Mme Sonia de La Provôté（Union centriste, UC） | Édouard Geffray，教育部长 | 已核原文 |
| S-3 | « la mobilisation qui secoue nos lycées »（无独立小标题，接于 S-2 后） | M. Ahmed Laouedj（RDSE） | Édouard Geffray | 已核原文 |
| S-4 | « situation dans les lycées » | （场次末段议题，接续讨论） | — | 已核原文（小标题存在） |

#### S-1｜Vogel (GEST) — 总理亲自答复
**法文原文（提问，节录）**：
> « Monsieur le Premier ministre, depuis un mois, la France a une chance immense : sa jeunesse se lève. […] Quelle a été votre réponse ? Le mépris, d'abord. Celui des pouvoirs qui ont du mal avec la contestation. Ces lycéens, vous les avez dits manipulés par La France insoumise. […] Ils n'ont pas besoin qu'on leur souffle leur colère. Ils la vivent eux-mêmes tous les jours, dans des classes de trente-cinq élèves, devant la chaise vide d'un professeur jamais remplacé, sous des plafonds qui s'effondrent […] »
> « Puis, plutôt que des réponses de fond, une répression inédite et inutile, avec du matériel de guerre. Du matériel de guerre, contre des enfants de 15 ans ! […] N'attendez pas un drame, interdisez dès maintenant, et définitivement, l'emploi des lanceurs de balles de défense (LBD) et des grenades. »

**法文原文（答复，Lecornu，节录）**：
> « Deux minutes, plus de deux minutes, et pas une seule condamnation de la violence ! Un millier de policiers et près de 300 enseignants blessés. Où est la gauche qui défendait les enseignants et les proviseurs ? […] Pas même un mot pour condamner des tirs de mortier sur des salles de classe ! »
> « C'est le moment de la grande clarification […] Oui, ce mouvement, au début, a été instrumentalisé par vos alliés de La France insoumise dans le Val-de-Marne. […] Est-ce que, dans un deuxième temps, ce mouvement s'est généralisé ? La réponse est oui, et sans La France insoumise. […] Troisième temps : est-ce que des violences urbaines inacceptables se sont installées et infiltrées dans le mouvement ? La réponse est oui. »
> « **aujourd'hui, en ce moment même, nous avons en France 200 lycées** – j'allais dire seulement 200, mais c'est déjà trop – **dans lesquels la situation est en train de s'enkyster, avec une violence inédite.** »
> « Les organisations syndicales étudiantes ou lycéennes déposent auprès des préfectures, auprès du ministère de l'intérieur, des déclarations de manifestation. **Celles-ci sont autorisées. Pour quelle raison ? Précisément parce qu'elles sont sécurisées.** »
> « Il y a une plateforme en ligne, qui donne la parole aux lycéennes et aux lycéens. […] elle a recueilli **100 000 contributions** ! […] **79,9 % des remontées de cette plateforme concernent l'organisation du temps scolaire et les emplois du temps** […] **51,5 % des remontées concernent les problèmes de bâti** […] **28,4 % des contributions portent sur les remplacements.** »
> « Ce gouvernement n'a pas d'échéance électorale, ce qui lui donne une très grande liberté pour examiner, **dès le mois de novembre**, avec la plus grande clarté et la plus grande transparence, dans cet hémicycle, les modifications qui pourront être apportées au budget de l'éducation nationale. »

**中文摘要**：这是整个 9–10 月危机中**唯一一次政府首脑在议会完整陈述其"三阶段叙事"**（LFI 工具化 → 运动自主扩大 → 城市暴力渗入），并**首次在议会公布平台数据**（10 万条反馈；课表 79.9%、校舍 51.5%、代课 28.4%）。他还给出"200 所高中局势正在固化"的官方判断，并承诺**11 月起**在参议院逐条修改教育预算。**注意：这段答复在参议院，不在国民议会。**

#### S-2｜de La Provôté (UC) — 教育部长答复
**法文原文（提问，节录）**：
> « Aujourd'hui encore, partout en France, des lycéens et des lycéennes se sont mobilisés. Si l'on s'accorde sur la condamnation ferme des violences et des destructions […] on comprend vite que ce mouvement d'ampleur d'une partie de la jeunesse est fondé sur des revendications que l'on doit entendre : le manque de moyens pour les lycées, les heures de cours non assurées et non remplacées, la réforme du baccalauréat et la désorganisation profonde des emplois du temps, le contrôle continu […] »
> « Face à l'urgence, vous avez annoncé le déploiement de **3 000 professeurs remplaçants** dans les lycées les plus en difficulté. […] Êtes-vous prêt, monsieur le ministre, à engager une [revalorisation]… ? »
> **追问**：「D'abord, il y a des mesures à mettre en place dès le budget 2027. Nous comptons sur vous pour que le débat avance très largement sur les évolutions demandées par les lycéens.»

**法文原文（答复，Geffray，节录）**：
> « Sur la question des emplois du temps, ce sera fait : nous examinons actuellement les meilleurs moyens d'y parvenir. Il en va de même pour la question de Parcoursup, **soulevée par 16 % des lycéens**, ainsi que pour celle des remplacements […] »
> « Si ce PLF est adopté, nous aurons pour la première fois, dans le premier degré, une moyenne d'élèves par classe inférieure à la moyenne de l'OCDE. »

**中文摘要**：中间派把"诉求清单"逐项列出并要求 2027 预算落实；部长给出**第四个平台数据（Parcoursup 16%）**，并承诺课表问题"会做"。**这是"3 000 名代课教师"承诺在议会中的唯一出处。**

#### S-3｜Laouedj (RDSE)
**法文原文（提问，节录）**：
> « Je souhaite tout d'abord saluer les élèves du lycée Jean-Zay d'Aulnay-sous-Bois et du lycée Liberté de Romainville, présents dans les tribunes et qui vous écoutent. »
> « Monsieur le ministre, la mobilisation qui secoue nos lycées n'est pas un simple mouvement de contestation : elle révèle une fracture profonde entre les engagements de la République et la réalité vécue par notre jeunesse. »
> « Je condamne fermement les violences et les dégradations, mais je refuse qu'elles servent à étouffer les revendications légitimes des lycéens. Je dénonce tout autant **l'usage disproportionné de la force** contre ces jeunes mobilisés. »
> « Dès le mois de juin, mon collègue Raphaël Daubet avait demandé, sur le fondement de l'article 57 de la loi organique du 1er août 2001 relative aux lois de finances (Lolf), des précisions sur l'exécution de la répartition territoriale des postes d'enseignement pour 2026. Les alertes étaient là. Pourquoi a-t-il fallu attendre la mobilisation des lycéens pour que l'urgence soit entendue ? »

**中文摘要**：参议院场次中**唯一同时谴责暴力与"过度使用武力"**的提问，并指出行政部门在 6 月即已收到 Lolf art. 57 的预警（即"可预见性"问题）。**现场有来自 Aulnay-sous-Bois 与 Romainville 两所高中的学生在旁听席**——这是参议院议事记录中罕见的"当事人在场"记载。

**核实状态**：S-1 至 S-3 全部 `已核原文`。

### 5.3 参议院的其他动作

| 项 | 状态 |
|---|---|
| 就本事件的专门辩论（débat） | **未找到**。10-01、10-06、10-07、10-13 各场次均为程序性或他题（公务员地位、药品储备、核医学、广播现代化、欧盟理事会预备辩论） |
| 书面质询（questions écrites） | **未找到可核实材料**。senat.fr 的 questions 数据库需交互检索，本次未取到该议题的书面质询编号 |
| 口头质询（questions orales sans débat） | **未找到**。10 月议程无对应条目 |
| rapport d'information / mission d'information | **未找到**在 lycéens 议题上新启动者。参议院"临时机构"页（commissions d'enquête / missions d'information communes）无对应条目 |
| 社会党党团 10-18 要求"延长既有 maintien de l'ordre 信息任务" | **未找到可核实材料**（senat.fr 无公开文本；未见 communiqué 页收录） |

### 5.4 参议院 n° 952 法案（casseurs-payeurs）——**唯一进入立法轨道的文本**

| 项 | 内容 |
|---|---|
| 正式标题 | « projet de loi relatif à la réparation des dommages résultant de violences ou de dégradations commises dans l'espace public et au recouvrement des dommages et intérêts » |
| 参议院编号 | **n° 952（2025-2026）** |
| 登记日 | **2026-09-16**（Enregistré à la Présidence du Sénat） |
| 提交人 | 以 **Sébastien Lecornu（总理）** 名义；由 **Laurent Nuñez（内政部长）**、**Gérald Darmanin（掌玺官/司法部长）**、**Stéphanie Rist（卫生、家庭、自主与残疾人部长）** 副署 |
| 程序 | **procédure accélérée**（加速程序，2026-09-16 由政府启动） |
| 受命审查 | 参议院 **commission des lois**（saisie au fond），2026-09-16 |
| 报告人指定 | **2026-10-07** |
| 一读公开辩论 | **2026-10-27 与 10-28** |
| 国民议会对应 dossier | `DLR5L17N54925`（`https://www.assemblee-nationale.fr/dyn/17/dossiers/DLR5L17N54925`） |
| 官方 dossier | `https://www.senat.fr/dossier-legislatif/pjl25-952.html` |
| 全文 PDF | `https://www.senat.fr/leg/pjl25-952.pdf`（1 924 985 字节，87 页含 étude d'impact） |
| NOR | INTD2618705L/Bleue-1 |
| **核实状态** | `已核原文`（dossier 页 + PDF 全文） |

#### 5.4.1 立法理由书的关键自陈（**本案最重要的"结构性发现"之一**）

> « **En mai dernier, la finale de la Ligue des champions a donné lieu à des violences d'une particulière gravité** qui ont profondément choqué nos concitoyens […] Ces violences sont loin de constituer un épisode isolé. Depuis plusieurs années, des individus profitent de manifestations ou de rassemblements sportifs pour commettre des actes de pillage, dégrader l'espace public […] »

> « Depuis la loi n° 2019-290 du 10 avril 2019, l'État peut se retourner contre les auteurs de dégâts, même sans condamnation pénale, pour récupérer les coûts des dommages causés lors d'attroupements, selon le principe « casseur-payeur ». **Cette action récursoire est limitée à raison d'une difficulté d'identification des mis en cause et des montants modestes récupérés.** »

> « Désormais, **toute personne participant à un groupement en vue de commettre des violences ou des dégradations, ou s'étant maintenue dans un attroupement violent** au cours duquel des dégradations sont commises pourra être tenue responsable civilement des dommages. »

> « Si le Gouvernement n'est pas favorable à la suspension des prestations sociales, **celles-ci doivent participer au financement des réparations**, dans des conditions encadrées, et **sans porter atteinte au reste à vivre**. »

**判断**：该法案的**起因写的是 2026 年 5 月欧冠决赛暴力，不是 lycéens 事件**（法案 9-16 登记，危机 9 月底才起）。政府**没有为 lycéens 事件另提专法**，而是让已在管道中的 952 号法案"顺带"承接。这是"立法供给滞后于事件"的直接文本证据。

#### 5.4.2 五条结构（**逐条已核原文**）

| 条 | 条文位置 | 内容 |
|---|---|---|
| **Art. 1er** | 在 **CSI（code de la sécurité intérieure）插入新条 L. 211-9-1** | 创设**民事连带责任**（responsabilité civile solidaire）。见下 5.4.3 原文 |
| **Art. 2** | 改写 **CSI L. 211-10** 第 2、3 款为 **5 款** | 国家求偿权（action récursoire）：① 可对"行为人"及"依 L. 211-9-1 负连带责任者"行使，按民法典第三卷第三编第二章第一节；② **亦可对 commune 行使**（当市镇责任成立时）；③ 国家以其他名义赔偿时同样可求偿；④ **国家须被通知**针对上述人员的追诉；⑤ 国家可**择一**连带债务人全额追偿，并可**和解（transiger）**——**"包括与经亲权人同意的未成年人"**；和解可采"恢复性义务"（参与公益行动），细则由**最高行政法院 decree** 定 |
| **Art. 3** | 在 **CPP art. 391** 末加一款 | 案件转至"民事利益"审理时，**未获首次开庭通知的被害人仍可在该庭登记为民事当事人**（例外于 CPP art. 421 与 CPJM art. L. 512-1） |
| **Art. 4** | 修 **CSS L. 553-4**（加 3°）与 **CCH L. 821-6**（加 4°） | 可**从家庭补助（allocations familiales）**、**个人住房补助（APL）**中扣取依终审判决确定的损害赔偿；且第 1、2°（及 3°）债权与不当得利追缴**优先于**该项扣取；APL 扣取在有 L. 824-1 举报情形下不得进行 |
| **Art. 5** | 修 **CSI L. 285-1 / L. 285-2** 等 | 海外省适用适配（含 references 替换、"4° ter"新增） |

#### 5.4.3 Art. 1er 的完整条文（**核心，全文引用**）

> **« Art. L. 211-9-1. – I. –** Toute personne ayant **participé sciemment à un groupement mentionné à l'article 222-14-2 du code pénal**, dans les temps et sur les lieux où ont été commis par tout participant à ce groupement, des violences volontaires contre les personnes, des vols ou des destructions ou dégradations de biens, est tenue **solidairement, dans la limite de 10 000 euros**, à la réparation des dommages résultant de ceux-ci.
>
> **« II. –** Toute personne ayant **continué volontairement à participer à un attroupement mentionné à l'article 431-3 du code pénal, malgré les sommations prévues à l'article L. 211-9** et alors qu'elle avait connaissance du fait que des membres de ce dernier étaient en train de commettre des violences volontaires contre les personnes, des vols ou des destructions ou dégradations de biens, est tenue **solidairement, dans la limite de 10 000 euros**, à la réparation des dommages résultant des crimes et délits commis, à force ouverte ou par violence, par tout participant de cet attroupement, **postérieurement aux sommations** et dans les circonstances de temps et de lieu ayant entraîné la dispersion. »

**三个要件结构（法律人的读法）**：
1. **I 款 = "groupement" 线**（code pénal 222-14-2：为实施暴力/毁坏而结成的团体）。要件：**明知**参加 + 在该团体成员实施暴力/盗窃/毁坏的**时间与地点**内。**不要求证明本人实施了个别损害**。
2. **II 款 = "attroupement" 线**（code pénal 431-3 + CSI L. 211-9 的 sommation 程序）。要件：**经 sommation 后仍自愿留在现场** + **明知**成员正在实施暴力/盗窃/毁坏。赔偿范围限于 **sommation 之后**、导致驱散之时空内实施的犯罪所致损害。
3. **两条线共用 10 000 € 上限**，且均为**连带**（solidaire）——即受害人可向任一责任人请求全额（在上限内），内部再分担。

**与 2019-290 法（loi Schiappa）的关系**：2019-290 建立的是**国家对行为人的求偿权**（action récursoire），受限于"识别难、回收少"；952 号法案把它改为**直接对受害人/保险人/国家的连带民事责任**，并将求偿对象扩大到"参加者"而非"损害实施者"。**这是从"国家先赔再追偿"到"参加者直接连带"的范式转换。**

---

## 6. 议会日程：本事件在 2026 年 10 月议事中的位置

### 6.1 国民议会 10 月议程实况（已核原文）

| 日期 | 场次 | 议程内容 |
|---|---|---|
| 10-01 | 3 场 | 会期开幕、议员替补、bureau 指定、性暴力法案 |
| 10-02 | 3 场 | 性暴力法案（全场） |
| 10-05 | 2 场 | 法摩协定；性暴力法案 |
| **10-06** | 2 场 | 悼念 Balladur；**QAG（lycéens 13 问）**；喀麦隆代表团；性暴力法案 |
| **10-07** | 2 场 | 诺贝尔化学奖；**QAG（lycéens 3 问）**；GloBe 税务信息交换协定；性暴力法案 |
| 10-08 | 3 场 | 议员替补；海外省饮用水；公共采购；Schengen 重构；ZFE 废除 |
| 10-09 | 2 场 | 性暴力法案（全场） |
| 10-12 | 2 场 | 餐券现代化；CREPS 维希实验；法哥引渡协定 |
| **10-13** | 2 场 | **QAG（lycéens 2 问，海外省）**；性暴力法案二读；债务辩论；**晚间：PLF 2027 一读开始** |
| **10-14** | 2 场 | **QAG（lycéens 1 问）**；**PLF 2027 一读**（全天） |
| 10-15 | 3 场 | PLF 2027 一读（全天） |
| 10-16 | 3 场 | PLF 2027 一读（全天）；**程序争议（见 6.3）** |

**结论**：lycéens 议题在国民议会**从未成为一个议程点（point de l'ordre du jour）**，只作为 QAG 的提问主题出现。**10-08 之后，该议题在 QAG 中完全消失**（10-09 零次、10-15 零次、10-16 零次），而 10-17 恰是全国行动日与 Limoges 纵火日。

### 6.2 是否挤占 2027 预算审议？

**没有证据显示 lycéens 事件挤占预算审议。** 相反：
- PLF 2027（n° 3210）于 **2026-10-01** 登记（`/dyn/17/dossiers?typeTexte=PRJL` 显示"Dépôt à l'Assemblée nationale le jeudi 1er octobre 2026"），与 PLFSS 同日。
- 一读辩论于 **10-13 晚**开始，10-14/15/16 连续三天全场。
- **真正挤占日程的是性暴力法案（`Réponse intégrale aux violences sexuelles et sexistes`），不是 lycéens 事件**：10-01 至 10-13 共 8 个整天/半场用于该法案。
- 教育预算的具体审议**被推到 11 月**：总理 10-14 在参议院明言 «dès le mois de novembre […] dans cet hémicycle, les modifications qui pourront être apportées au budget de l'éducation nationale»。

### 6.3 是否援引 49.3？

**10 月未援引 49.3。** 依据：
- 全部 10 月 compte rendu 中 `engagement de la responsabilité` 出现 **0 次**（该表述是 49.3 程序的正式用语）。
- `49, alinéa 3` / `49.3` 的命中均为**发言中的修辞性提及**，非程序启动。例：10-15，Mme Marianne Maximi（LFI-NFP）：
  > « Tous les ans, nous avons le même débat autour d'amendements similaires à ceux que nous examinons. Et, tous les ans, les petites avancées décidées sont balayées par le recours du gouvernement au 49.3. Cela devient insupportable ! »
- 最近一次 49.3 是 **2026-02-02**（PLF 2026 定读，scrutins n° 5284/5285）。
- **10-16 的程序争议用的是 49-1 al. 2（议事组织），不是 49.3**：M. Emeric Salmon（RN）：
  > « Il se fonde sur l’article 49-1, alinéa 2, qui porte sur l’organisation de nos travaux. **Il reste 3 015 amendements à examiner sur la première partie du projet de loi de finances (PLF), alors que le vote solennel est prévu mardi après-midi.** À ce rythme, nous n’y arriverons pas dans des conditions dignes d’un débat parlementaire. **Je demande donc au gouvernement d’user de son pouvoir et de convoquer l’Assemblée demain, samedi 17 octobre.** »
  （议长答："Je crois que nous y sommes tous prêts, monsieur le député, mais il ne faudrait pas qu'il y ait trop d'absences…"）
  **记事**：RN 要求 10-17（周六）加场审议预算；该日正是全国行动日。议长未采纳。

### 6.4 与 lycéens 事件直接相关的立法动议（**本报告最重要的更正**）

**10-13 一天之内登记 7 份直接针对该事件的文本**（`/dyn/17/dossiers?typeTexte=PION` 与 `?typeTexte=PNRE`，2026-10-13 批）：

| 编号 | 标题（法文原文） | 类型 | 受命审查 | 状态 |
|---|---|---|---|---|
| **n° 3299** | « Rétablir la justice en faisant payer les casseurs lors des émeutes » | Proposition de loi | commission des lois | renvoyée，未排期 |
| **n° 3302** | « Faire payer les casseurs des établissements scolaires et à sanctionner sévèrement leurs instigateurs » | Proposition de loi | commission des lois | renvoyée，未排期 |
| **n° 3304** | « La responsabilité des parents pour les dégradations commises par leur enfant mineur lors d'une manifestation » | Proposition de loi | commission des lois | renvoyée，未排期 |
| **n° 3305** | « Instaurer le principe de « casseur-payeur » lors des manifestations, attroupements et rassemblements violents » | Proposition de loi | commission des lois | renvoyée，未排期 |
| **n° 3308** | « Créer un délit d'entrave au droit à l'éducation » | Proposition de loi | commission des lois | renvoyée，未排期 |
| **n° 3321** | « Protéger les mineurs en interdisant l'utilisation des armes mutilantes et des techniques d'immobilisation létales dans les manifestations » | Proposition de loi | commission des lois | renvoyée，未排期 |
| **n° 3292** | « Condamner l'instrumentalisation politique des mobilisations lycéennes et la légitimation des violences aux abords des établissements scolaires » | **Proposition de résolution** | — | déposée le 13 oct. 2026，未排期 |

**解读**：
- **6 份 PPL 全部指向"追责/赔偿/加重制裁"**（pro-ordre），**1 份 PPL 指向"禁止致残武器"**（pro-liberté），**1 份résolution 指向"谴责对 lycéens 动员的政治工具化"**（pro-majorité/反 LFI）。
- 这个配比与 10-06 QAG 的提问结构高度一致：DR/UDR 的"casseurs-payeurs"线（Boucard、Michelet）→ 3299/3302/3304/3305；EcoS/GDR 的"武器/镇压"线（Lucas-Lundy、Vogel 在参议院）→ 3321；多数派/右翼的"反工具化"线 → 3292。
- **全部 renvoyées à la commission des lois，无一进入议程**。截至 10-19，`/dyn/17/dossiers` 中无任何一份的状态超出"1er dépôt d'une initiative"。
- **核实状态**：标题、编号、类型、日期、受命委员会均 `已核原文`（列表页 + dossier 页）；**提案人与党团未取到**（`/dyn/17/textes/l17b…` 页面仅返回骨架，作者列表为 JS 动态加载）。

**补充：9 月的对照**——`?typeTexte=PION` 显示 2026 年 9 月仅 4 份提案登记（n° 3150、3151、3184、3194），**无一与 lycéens 相关**。即：**9 月底动员开始时议会零动作，10-13 集中登记 7 份，此后到 10-19 再无新增。**

### 6.5 小结：议会回应的四层结构

| 层 | 动作 | 是否发生 |
|---|---|---|
| **质询层** | QAG / questions d'actualité | **发生且密集**（AN 19 问、Sénat 3 问），10-08 后衰减至零 |
| **立法层** | proposition de loi | **登记 6 份 + 1 份 résolution，全部滞留委员会**；政府自己的 952 号法案与本案无文本关联 |
| **监督层** | commission d'enquête | **公告已出，10-20 待决，尚未成立**；受 ordonnance 58-1100 art. 6 司法程序禁令约束 |
| **责任追究层** | motion de censure | **零提案**（最近一次为 2026-07-06） |

**一句话**：议会对这场危机的回应是"**问了很多、写了几份、一件没成**"。

---

## 7. 未取到项（明确列表）

| # | 项 | 原因 | 状态标记 |
|---|---|---|---|
| 1 | 10-20 主席会议结果 | 会议尚未举行（检索时点为 10-19 15:00） | `未找到`（尚未发生） |
| 2 | Braun-Pivet 议长办公室 communiqué 原件 | 未在 assemblee-nationale.fr / presidence.assemblee-nationale.fr 检索到公开文本；仅有 LCP 转述 | `议会频道转述` |
| 3 | Larcher «il faut rétablir l'ordre» 完整语境与一手录音/逐字稿 | 参议院 10-06 场次无此发言；BFMTV 页面正文 JS 渲染 | `仅二手` |
| 4 | 参议院社会党党团 10-18 要求延长 maintien de l'ordre 信息任务的原文 | senat.fr 无公开文本 | `未找到可核实材料` |
| 5 | 3299/3302/3304/3305/3308/3321/3292 的提案人与党团 | `/dyn/17/textes/…` 页面为 JS 骨架，未含作者段 | 标题/编号/日期 `已核原文`；作者 `未取到` |
| 6 | 参议院就该事件的书面质询（questions écrites）编号 | questions 数据库需交互检索，本次未取到 | `未找到可核实材料` |
| 7 | Édouard Philippe 支持设立调查委员会的一手声明 | 仅二手报道层 | `仅二手` |
| 8 | 10 月国民议会关于 lycéens 的 proposition de loi 是否已在委员会排入审查 | 委员会工作页未取到 10-19 前的最新议程 | `未找到` |

---

## 8. 引文与文件索引

**国民议会 compte rendu（一手）**
- 10-06 s1：`https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/premiere-seance-du-mardi-06-octobre-2026`
- 10-07 s1：`…/premiere-seance-du-mercredi-07-octobre-2026`
- 10-13 s1：`…/premiere-seance-du-mardi-13-octobre-2026`
- 10-14 s1：`…/premiere-seance-du-mercredi-14-octobre-2026`
- 10-15 s1 / 10-16 s1-s3：同构 URL
- 议程总表：`https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027`

**不信任动议（一手）**
- `https://www.assemblee-nationale.fr/dyn/17/scrutins?typeScrutin=MOC&limit=100`（23 条，最新 n° 7979 / 2026-07-06 / 132 pour）
- `https://www.assemblee-nationale.fr/dyn/17/dossiers?typeTexte=MION&limit=100&order=dateDepot,desc`（最新登记 2026-07-02）

**调查委员会（一手 + 准一手）**
- 委员会法定条文合编 PDF：`https://www.assemblee-nationale.fr/dyn/16/divers/texte_reference/08_ordonnance_58-1100_du_17_novembre_1958.pdf`（ordonnance art. 6 在 p.168-169；Règlement art. 137-143 在 p.103-105）
- 在办委员会列表：`https://www.assemblee-nationale.fr/dyn/17/organes/autres-commissions/commissions-enquete`（仅 2 个，均无关）
- LCP 转述：`https://lcp.fr/index%2ephp/actualites/violences-du-17-octobre-yael-braun-pivet-veut-une-commission-d-enquete-sur-les`

**参议院（一手）**
- 10-06：`https://www.senat.fr/seances/s202610/s20261006/s20261006001.html`（纯程序性，无本议题）
- 10-07：`https://www.senat.fr/seances/s202610/s20261007/s20261007001.html`（纯程序性）
- 10-13：`https://www.senat.fr/seances/s202610/s20261013/s20261013001.html`（+002/003）
- **10-14：`https://www.senat.fr/seances/s202610/s20261014/s20261014001.html`（+002/003）——本议题核心场次**
- 952 号法案：`https://www.senat.fr/dossier-legislatif/pjl25-952.html` ｜ 全文 `https://www.senat.fr/leg/pjl25-952.pdf`

**10-13 登记的提案（一手）**
- `https://www.assemblee-nationale.fr/dyn/17/dossiers/retablir_justice_faire_payer_casseurs_17e`（3299）
- `…/dossiers/_faire_payer_les_casseurs_des_etablissements_scolaires_et_a_sanctionner_severement_leurs_instigateurs_17e`（3302）
- `…/dossiers/responsabilite_parent_degradations_enfants_17e`（3304）
- `…/dossiers/instaurer_le_principe_de_casseur_payeur_lors_des_manifestations_attroupements_et_rassemblements_violents_17e`（3305）
- `…/dossiers/_creant_un_delit_d_entrave_au_droit_a_l_education_17e`（3308）
- `…/dossiers/_proteger_les_mineurs_en_interdisant_l_utilisation_des_armes_mutilantes_et_des_techniques_d_immobilisation_letale_dans_les_manifestations_17e`（3321）
- `…/dossiers/comdamner_instrumentalisation_politique_lyceens`（3292）
