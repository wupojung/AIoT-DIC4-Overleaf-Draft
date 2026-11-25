# Result 01 — 初稿生成報告

封存時間 2026-11-25T12:03:03+08:00。本次交付依既有七項 OpenSpec 變更完成英文初稿，採 IEEEtran conference 雙欄。PDF 為 4 頁。

## 來源與生成

- 以 MR-001（教師 A–Z 寫作範例）指引結構，利用 MR-004 §§4–15 與團隊提案 SUP-001 §§4–5、SUP-002 投影片 17–18 和 31–32 支撐設計與評估。MR-002 資訊圖和 MR-003 NotebookLM 分析提供整理線索。四件原始來源及 SHA-256 均見 [來源盤點](../../papers/REFERENCE-INVENTORY.md)。
- 沿用 DR-001 單檔排版初稿，將內容整理到 `paper/` 的八份 Markdown，透過 `generate.py` 產生 IEEEtran 主檔、六個 LaTeX 節檔與 BibTeX。可編輯 TikZ 架構圖改由 `figures/architecture.tex` 載入。逐筆書目來源及主張位置見 [07-references.md](source/07-references.md)。
- 以臺中資料集 103038 的資源 `1095e2c3-4ccc-4766-b1ce-98aa2ddf0204` 重算 10,638 筆、32 欄及 9,152 筆候選。住宅大樓 5,933、華廈 1,553、透天厝 1,461、公寓 205。CSV SHA-256 為 `6efc5b049e1e64cf438ac36fd243ae7eb92a98ba851f5d8e0cf71134b6142eac`。這些是單一快照的篩選計數。[原盤點紀錄](../../research/cross-validation/INDEX.md)

## 各節交付

| OpenSpec | 初稿與證據 |
| --- | --- |
| 000 摘要 | 依正文整理背景、問題、擬議方法、計畫評估、快照觀察和貢獻。摘要的計數對應 Experiment，並註明 Agent 評估仍為計畫。 |
| 001 緒論 | 以內政部資料口徑與 002 的文獻定位說明問題。RQ1 對應固定與自適應流程的成對比較，RQ2 對應適當停止、部分回答與資源使用。 |
| 002 相關研究 | 比較住宅估價、時空驗證、模型歸因、ReAct、RAG 和房地產代理。Wang 的描述限於出版摘要支持的資料與方法。其餘主張定位見 07。 |
| 003 研究設計 | 說明儀表板、型別化查詢、調度、資料檢索、確定性統計、版本化文件檢索、證據驗證及回應。圖 1、表 I 與案例描述對應補問、重試、替代來源、部分回答和停止條件。 |
| 004 實驗 | 表 II 呈現已重算的快照。成對比較載明共同工具、相同資料、盲評、案例分層、計分與不確定性，正式資料母體與實驗執行證據待補。 |
| 005 結論 | 彙整資料快照、方法貢獻及限制。RQ1 與 RQ2 等待成對評估結果。 |
| 006 參考文獻 | 使用 IEEEtran BibTeX 樣式。8 筆文獻按首次引用排序，書目與正文引用鍵完全對應。 |

## 本機編譯與重建

從封存的 `source/` 本機使用 Tectonic 0.17.0、BibTeX 0.99d 及 IEEEtran.bst 1.14 編譯成功。檢查過四頁 PDF、8 筆文獻和交叉引用，均有解析。建置日誌有字型初始化和 Underfull hbox 訊息。PDF 文字、圖表和參考文獻可讀。

在有 Python 3 與 Tectonic 的環境中，從 `source/` 執行 `python generate.py --check`，再執行 `tectonic --keep-logs --keep-intermediates main.tex`。首次建置可能需要下載標準 TeX 套件，包括 IEEEtran 類別與書目樣式。修改稿件時使用 `paper/` 的 Markdown，再執行 `python generate.py` 更新 LaTeX。

## 限制及封存

- 日期欄業務語義、正式中古屋納排、歷史資料涵蓋、模型及評估環境仍待研究確認。現有可報告結果限於快照篩選。Agent 對照、模型訓練和使用者研究仍在計畫中。
- 署名沿用暫留欄位，正式作者資訊與 ICEIB 投稿路線待確認。ICEIB 2027 官網列英文全文 4–8 頁，並列有 Engineering Proceedings 模板。這份交付採課堂要求的 IEEE 樣式。[ICEIB 2027](https://www.iceib.asia/#submission) · [IEEE 模板](https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn/)
- `source/` 是封存來源，後續編修使用 `paper/`。`initial-paper.pdf` SHA-256 為 `8af1e93a31c8448c677e48e4aef57d798cafc192a0787461e31704dcf81f7f00`。封存來源共 18 個檔案。

## 封存來源 SHA-256

```text
f99aa38a80aaf287d27b890fd729bde234a891c8c69f5ac05e7bdceb96824787  source/00-main.md
aa1ce6fd52681cb7307acd43ff31de63b677174368c45fbf61b7a4883246f561  source/01-abstract.md
5a08ef247874375e47b61d556c1a7178961391787b9f732924125c71aa3046ad  source/02-introduction.md
5ea21fb32ad39b61a6f390d6419c3321bf2083abca145b64378cf233236987a1  source/03-related-work.md
406421959e78017be7e22ff7906fcf2a789465e05b1929140f633c544a52a2ed  source/04-proposed-design.md
18ab6f0287a72445c5f0eea37e95351bb9c0dce7247b0ef8c4b5d07c4a277439  source/05-experiment.md
3bf3703119ea12366625b10325eb96536b50761f52a069eaccc55060ba840c28  source/06-conclusion.md
552f0f6d341a3240ccd380a96761d9293e1c7dcea1d7ddb6376908cd3dafea16  source/07-references.md
cd0105b65a79ba4ffe1bc6faea856e67962abdeee20843d42f43e8751037b6c7  source/figures/architecture.tex
7e15b65c6ed7dc6c741d7c723d5ecbadbe470a355fe51a49dc444f1184d1bc20  source/generate.py
bb70dc62f8ac71ff4178edf2158e65e214f99dd1b49c6c4f8c630d59b40ba278  source/main.tex
9d91d8d587034329e2ddbcd466000850ce14ca54ca62c927eb3f0d032d47f58d  source/references.bib
caef2f69a73f3e0b1fcf5958c6c2459eb16aa18c6dd6759d3c22aff107dcc6bb  source/sections/01-abstract.tex
75b66775358fda35f7192f262e2bd0d3290f352e57b3a368c965a8b9b411ae5d  source/sections/02-introduction.tex
eb6629a013907fd4fdf425ea4640096400a9996f684304bb148a797a75b260ac  source/sections/03-related-work.tex
4b7f272b98e5506ad27af6401761a0dc2e8af32f52c1ff124e1fc3d0c5b7f13a  source/sections/04-proposed-design.tex
20cbabbf3c026d308c903b091d2db0167e96f9ec99c8191ec8de95d3421c928a  source/sections/05-experiment.tex
e265b02ca9bf4f6a6dc6887d84843739be089f59eb642b3d9c3496eaeb1e3842  source/sections/06-conclusion.tex
```
