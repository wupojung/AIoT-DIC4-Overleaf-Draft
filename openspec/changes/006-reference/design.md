# 006-reference — Design

## Context

參見 [proposal.md](proposal.md) 與[證據報告](../../../research/academic-plan/INSPECTION.md)。可在其他章節之前建立查核規則並平行整理文獻；最後隨正文順序關閉引用、重複、未引用及懸空檢查。

## Goals / Non-Goals

- 交付。書目 metadata 與 DOI／網址查核紀錄、主張對應表、去重紀錄，以及核准後的 IEEE bibliography 與編譯檢查。
- 本次規格審閱只涵蓋寫作方法與可驗收產物。正文、原型、實驗執行及投稿依核准範圍另行安排。

## Decisions

- 由來源 ID 管理證據，BibTeX 鍵或手動引用鍵用於排版，最後以單一書目來源組稿。
- DOI 優先向出版者核對，無 DOI 的正式會議來源可用 proceedings URL。以正規化 DOI 及題名作者比對去重。
- 來源。參考盤點、MR-001／002 來源角色、SUP-001 References、既有 DR-001 引用鍵、EXT-001 至 EXT-010，以及 001–005 的引用主張。 MR-003 §§2.3、3.2 的文獻名稱僅作搜尋線索；MR-004 所指官方資料需查原站與適用條件。

## Risks / Trade-offs

- 方案、AI 衍生資料與可公開的學術引文分欄；全文可得性與主張核查獨立記錄。
- 引文和數值皆依 [spec.md](specs/citation-traceability/spec.md) 及全稿規格驗收，審查紀錄保留原文件頁節、來源 ID 與證據狀態。
