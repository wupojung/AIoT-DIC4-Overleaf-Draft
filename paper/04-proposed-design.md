# Proposed Design {#sec:method}

```latex
\begin{figure}[t]
\centering
\input{figures/architecture}
\caption{Proposed control and evidence flow. The dashed path returns a validated observation to the controller.}
\label{fig:architecture}
\end{figure}
```


## Typed Query and Bounded Orchestration
Fig.~\ref{fig:architecture} shows the control flow. The dashboard accepts the question and displays the result. The parser converts a natural-language question into a typed request containing the comparison intent, district, period, property type, attributes, and applicable date where needed. An unclear district or price convention can trigger a clarification request. The design allows up to two clarification rounds. Scope checks also identify requests that require evidence or capabilities outside the project.

The proposed controller allows up to six ReAct steps per request. The runtime, model, and framework remain open. Before execution, each proposed action must match an approved read-only tool and supply valid typed arguments. A transient failure permits one retry of the affected call within the same step. An alternative source requires a new step within the remaining budget. A trace records selected tools, validated arguments, source versions, observation status, and the response decision. The trace limits the retention of personal and fine-grained location data.

## Evidence Contracts and Validation
The authorized retrieval tool returns records for a typed cohort request. The separate analytics tool accepts validated records and a named price convention. A transaction observation includes the snapshot identifier, sample predicate, schema version, calculation version, output units, and quality flags. The output associates each statistic with its eligible sample. The response layer copies numbers from valid tool outputs and associates each with the metadata required to reproduce the calculation.

A domain observation includes the source authority, document identifier and passage, version, jurisdiction, publication or effective dates, and applicability conditions. Retrieval uses the requested as-of date. The design distinguishes regulatory facts, market evidence, expert opinion, and hypotheses in the source registry. A topically relevant document may fail the applicability check because a newer version supersedes it or its jurisdiction or property category differs from the query.

The evidence gate applies the checks in Table~\ref{tab:gate}. Invalid, stale, or inapplicable results are excluded from computation and claim generation. Before a response is shown, each displayed number must match a validated output and each documentary claim must be supported by an applicable passage. Separately supported findings can be returned with an explanation of the missing evidence. When all authorized core sources fail validation, the response withholds the price claim and explains the reason.


```latex
\begin{table}[t]
\caption{Proposed Evidence Checks and Response Behavior}
\label{tab:gate}
\centering
\small
\begin{tabularx}{\columnwidth}{@{}>{\raggedright\arraybackslash}p{.30\columnwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Check & Behavior when evidence fails \\
\midrule
Authorization and arguments & Reject the proposed tool call before execution. \\
Schema, units, or provenance & Exclude the result from calculations and claims. \\
Version, date, or applicability & Withhold the affected claim and disclose the omission. \\
Core transaction evidence & Check an authorized alternative within budget. Withhold prices when valid evidence is unavailable. \\
Optional GIS or model output & Omit that output and retain independently supported transaction findings. \\
\bottomrule
\end{tabularx}
\end{table}
```


## Illustrative Query
Suppose a user requests the median parking-excluded unit price for residential towers in two Taichung districts over a specified period. After validation, the system identifies the two cohorts using the same snapshot and metric. If one district has adequate support and the other has too few eligible records with separate parking fields, the dashboard can show the supported district summary and identify the missing evidence. If neither cohort can support a price, the dashboard returns the eligibility or coverage issue without a numerical finding. Controlled records will be used to test this expected behavior.

## Design Trade-offs
Adaptive tool selection may recover from an unusable source or retrieve documents only when needed. This flexibility may increase resource use and introduce inconsistent decisions. The shared evidence policy and the fixed workflow make those costs measurable. Optional valuation introduces additional error and explanation requirements. Optional geographic information system (GIS) features depend on approved use, location precision, coordinate references, and geographic coverage. When those conditions are unmet, the comparison remains at the supported aggregation level.
