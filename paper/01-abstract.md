# Abstract

Taiwan's public real-estate transaction records enable residential price comparison, but differences in property type, transferred area, and parking treatment complicate the interpretation of prices. We propose a housing intelligence agent that combines bounded reasoning and acting (ReAct), retrieval-augmented generation, and deterministic transaction analytics. The agent uses approved read-only tools and attaches claim-level evidence, including data versions, calculation rules, and applicable dates. An evidence gate validates tool outputs and withholds price claims when supporting transaction evidence is unavailable. A preliminary project audit examined one Taichung City release with 10,638 records and 32 fields. An exploratory filter retained 9,152 residential candidates, supporting further investigation of field definitions and residential eligibility. The planned evaluation compares adaptive tool selection with a fixed workflow using identical tools and evidence. Its outcomes include supported task completion, citation support, appropriate abstention, latency, and resource use. The snapshot audit is the empirical work reported here. Agent implementation and comparative evaluation are planned.

## Index Terms

housing transactions, ReAct, data provenance, decision support
