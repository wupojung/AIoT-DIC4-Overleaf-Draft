# ICEIB 研究來源盤點

盤點日期 2026-11-25，版本 v0.1，供研究者審閱。MR 代表本次提供的唯讀來源，SUP 代表既有工作區補充資料，EXT 代表外部來源，DR 代表排版初稿。章節欄使用 OpenSpec 三位數編號。資料內容、書目 metadata 和個別主張各自查核。資料不明時記為 UNKNOWN。

## myRef 唯讀來源

| ID | 原始檔名／類型 | 題名 | 作者／年份 | DOI／來源 | 相關章節 | 證據可得性與查核狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| MR-001 | [A2Z outline example.pdf](../myRef/A2Z%20outline%20example.pdf)／教師寫作範例 PDF | 2020 A-Z SOP | 作者 UNKNOWN，內文標示 2020，PDF 建立於 2025，正式出版年 UNKNOWN | 教師提供，同 TCH-002，無已知 DOI | 000–005 | 完整讀取 1 頁。A–Z 結構指引，無個案研究結果。與原索引檔雜湊一致。 |
| MR-002 | [台灣住宅智慧代理研究提案資訊圖表.png](../myRef/台灣住宅智慧代理研究提案資訊圖表.png)／提案圖 | Taiwan Housing Intelligence Agent 專題提案系統性解析資訊圖表 | ChatGPT Image，2026（生成年） | INFO-001，無已知 DOI | 000–005 | 已檢視 1491 × 1055 圖，與 INFO-001 雜湊一致。圖中的符合度是 AI 分析，成效標為預期，OpenSpec 狀態已過時。 |
| MR-003 | [01_Proposal_Document_Analysis.md](../myRef/01_Proposal_Document_Analysis.md)／AI 衍生提案分析 | Taiwan Housing Intelligence Agent：專題提案深度解析與學術規範評估報告 | NotebookLM，生成及出版年 UNKNOWN | NBLM-001，依教師規範、A2Z 與團隊提案材料 | 000–006 | 全文已讀，正規化文字與 NBLM-001 一致。A–Z 映射、文獻名稱與口試建議可作檢查線索。評等、首創和文獻結論需一手來源。 |
| MR-004 | [DESIGN.md](../myRef/DESIGN.md)／團隊技術設計 | DESIGN｜Taiwan Housing Intelligence Agent | 專題團隊，2026 提案語境，出版年 UNKNOWN | TEAM-003，內部設計文件 | 000–005 | 全文已讀，正規化文字與 TEAM-003 一致。技術提案、有界流程及未決決策可追溯，實作與效能仍待驗證。 |

| ID | SHA-256（此次讀取的原始位元組） |
| --- | --- |
| MR-001 | `777386d58818577471bb02067cd01b7b14d24dc55b497a6d667febdb2c207ef4` |
| MR-002 | `7d4b11011f38332986ccb135a301ca531122c75acc18638e56425e4f5be35439` |
| MR-003 | `8ed37251ed6665449b79e77f44a8b0276068cb96ef62c731e06c54df8b572e05` |
| MR-004 | `896a485d3f9b20f4ee58daf50f8af1574a51e8e5408681104e24c67c7781a567` |

MR-003／004 的既有工作區副本位元組雜湊不同，UTF-8 BOM 與換行正規化後全文相同。沿用 MR ID 追溯來源，避免把重複版本算作獨立證據。引用與公開權利依原資產索引及來源授權分別確認。

## 工作區補充材料

| ID | 原始檔名／類型 | 題名、作者、年份 | DOI／來源 | 相關章節 | 證據與狀態 |
| --- | --- | --- | --- | --- | --- |
| SUP-001 | [01_Proposal_Document.pdf](../research/originals/01_Proposal_Document.pdf)／研究提案 | Taiwan Housing Intelligence Agent，專題團隊，2026（封面日期） | TEAM-001，無 DOI | 000–006 | §4 系統、§5 feasibility、References；文獻清單待逐筆核對。 |
| SUP-002 | [02_Proposal_Presentation.pptx](../research/originals/02_Proposal_Presentation.pptx)／簡報 | Taiwan Housing Intelligence Agent，專題團隊，2026 | TEAM-002，無 DOI | 003–005 | 投影片 17–18、31–32 提供設計與偽碼。屬提案。 |
| SUP-003 | [DESIGN.md](../research/originals/DESIGN.md)／技術設計 | 同 MR-004 | TEAM-003，無 DOI | 001、003–005 | 與 MR-004 正規化文字一致。 |
| SUP-004 | [期末專題提案作業規範.pdf](../research/originals/期末專題提案作業規範.pdf)／課堂規範 | Final Project Proposal Requirements，授課教師，出版年 UNKNOWN | TCH-001，無 DOI | 000–006 | 課程脈絡，投稿要求由 EXT-009／010 查核。 |
| SUP-005 | [01_Proposal_Document_Analysis.md](../research/notebooklm/01_Proposal_Document_Analysis.md)／AI 分析 | 同 MR-003 | NBLM-001，無 DOI | 000–006 | 同一衍生來源，等同 MR-003 的文字內容。 |
| SUP-006 | [INDEX.md](../research/cross-validation/INDEX.md)／查核紀錄 | 臺中市交易快照盤點，研究工作區，2026 | EXT-002 之資料重算與指紋 | 000、004、005 | 支持該快照計數與篩選。 |
| SUP-007 | [PPLX-002_deep-research-q1-q3.md](../research/perplexity/PPLX-002_deep-research-q1-q3.md)／AI 文獻與問題分析 | PPLX-002，Perplexity，出版年 UNKNOWN | PPLX-002 | 001–004、006 | 補充線索；單篇原文與 DOI 狀態由 006 查核。 |
| DR-001 | [main.tex](../research/refactor/main.tex)／既有 LaTeX 初稿 | Evidence-Grounded Housing Transaction Comparison in Taiwan Using a Bounded ReAct Agent，作者待確認，2026 | REF-001，無 DOI | 000–006 | 既有 IEEE 雙欄排版初稿和引用鍵，衍生自上游材料。 |

## 官網、資料與初稿引用線索

外部來源沒有另存副本。官方入口可支持其所列範圍或規格，文章的內容查核需記錄到主張與段落。後續 006 應從 SUP-001 及 MR-003 補列其他擬引用候選；本表先收錄現稿的八個來源及兩份格式規則。

| ID／引用鍵 | 文件類型及題名 | 作者／年份 | DOI 或一手來源 | 章節 | 目前可用證據及查核狀態 |
| --- | --- | --- | --- | --- | --- |
| EXT-001／moi | 官方網站，實價查詢常見問題 | 內政部／持續更新，出版年 UNKNOWN | [官方 FAQ](https://lvr.land.moi.gov.tw/jsp/qa.jsp) | 001、003–004 | 已讀揭露原則與均價說明，可支持樣本與口徑限制。 |
| EXT-002／taichung | 官方資料目錄和 CSV，臺中市不動產實價登錄資訊 | 臺中市政府地政局／2026 快照 | [資料集 103038](https://data.gov.tw/dataset/103038) | 000、001、004–005 | 資料目錄與 CSV 計數已查核，日期欄語義仍待確認。 |
| EXT-003／wang | 期刊，Deep Learning Model for House Price Prediction Using Heterogeneous Data Analysis Along With Joint Self-Attention Mechanism | P.-Y. Wang、C.-T. Chen、J.-W. Su、T.-Y. Wang、S.-H. Huang／2021 | [10.1109/ACCESS.2021.3071306](https://doi.org/10.1109/ACCESS.2021.3071306) | 001–002、004 | 機構書目與摘要已比對 DOI、研究區及資料類型。全文逐項查核待完成。 |
| EXT-004／roberts | 期刊，Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure | D. R. Roberts 等／2017 | [10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881) | 002、004 | DOI 可連出版者，原文支持用與任務相符的區塊驗證。實驗分割方式待設計。 |
| EXT-005／react | 會議論文，ReAct: Synergizing Reasoning and Acting in Language Models | S. Yao 等／2023（ICLR） | [OpenReview 論文](https://openreview.net/pdf?id=WE_vluYUL-X) | 002–003 | 原文支持推理、行動與觀察交錯；本研究上限由提案指定。 |
| EXT-006／rag | 會議論文，Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | P. Lewis 等／2020 | [NeurIPS 論文](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) | 002–003 | 出版頁與原文可得，支持檢索增強生成概念。 |
| EXT-007／shap | 會議論文，A Unified Approach to Interpreting Model Predictions | S. M. Lundberg、S.-I. Lee／2017 | [NeurIPS 論文](https://proceedings.neurips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html) | 002–004 | 原文可得，支持模型特徵歸因的說明。 |
| EXT-008／haurum | 會議論文集文章，Real Estate with AI: An agent based on LangChain | K. R. Haurum、R. Ma、W. Long／2024 | [10.1016/j.procs.2024.08.199](https://doi.org/10.1016/j.procs.2024.08.199) | 002 | 作者機構原文和書目可得，支持該研究使用 LangChain 及不動產資訊。 |
| EXT-009 | 大會網站，ICEIB 2027 Submission | ICEIB 2027 主辦方／2027 會期 | [大會官網](https://www.iceib.asia/#submission) | 000–006 | 本次查到英文及 4–8 頁。指定出版路線與對應範本待確認。 |
| EXT-010 | 官方 LaTeX 模板，IEEE Conference Template | IEEE／出版年 UNKNOWN | [IEEE Overleaf Template](https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn/) | 000–006 | 已查 IEEEtran conference 版式，供本專案撰稿。 |

下一步查核紀錄由 006 維護。對每個擬刊載主張保留來源 ID、檔案或 URL、頁節／資料版本、查核狀態及負責人。
