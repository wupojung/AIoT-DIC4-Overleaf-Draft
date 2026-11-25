# 003-proposed-design — Design

## Context

參見 [proposal.md](proposal.md) 與[證據報告](../../../research/academic-plan/INSPECTION.md)。以原案和 002 方法文獻為依據，向 004 提供共用工具、證據閘門及失敗行為的明確規格。

## Goals / Non-Goals

- 交付。英文 Proposed Design、可編輯架構圖與流程圖、偽碼或準確工作流、技術取捨與來源映射。
- 本次規格審閱只涵蓋寫作方法與可驗收產物。正文、原型、實驗執行及投稿依核准範圍另行安排。

## Decisions

- 以 MR-004 流程為準，保留八模組及資料分支。核對六步上限和完整偽碼時查 SUP-002，將未核准值標為提案參數。
- 架構圖與控制流程圖共用術語。呈現可用替代來源、選配失效和核心證據不足三條路徑。
- 來源。MR-001 PA–PM、MR-002 §4、SUP-001 §4、SUP-002 §§17–18 與附錄頁 31–32、SUP-003 §§4–12、EXT-005／EXT-006。 MR-004 §§4–12、15 是優先技術來源。MR-003 §§2.4、3.4–3.5 用於對照圖與偽碼。

## Risks / Trade-offs

- 選配 GIS、ML、XAI 依資料適用性設定，主流程維持描述性比較。
- 引文和數值皆依 [spec.md](specs/housing-evidence-workflow/spec.md) 及全稿規格驗收，審查紀錄保留原文件頁節、來源 ID 與證據狀態。
