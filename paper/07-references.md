# References

The BibTeX block supplies the manuscript bibliography. Source IDs follow the project reference inventory. The locations below support the claims used in this manuscript.

| Key | Evidence ID | Source location | Claim supported |
| --- | --- | --- | --- |
| `moi` | EXT-001 | [Official FAQ](https://lvr.land.moi.gov.tw/jsp/qa.jsp), disclosure principles and average price calculation | Disclosure limits, parking conventions, and aggregate average calculation. |
| `wang` | EXT-003 | [Published abstract and institutional record](https://scholar.nycu.edu.tw/zh/publications/deep-learning-model-for-house-price-prediction-using-heterogeneou/) | The study combines 2017–2018 transaction data, facility information, and satellite imagery for Taipei and New Taipei price prediction. The paper uses only claims supported by the abstract. |
| `roberts` | EXT-004 | [Publisher full text](https://doi.org/10.1111/ecog.02881), Abstract and discussion of blocked cross-validation | Validation splits should reflect dependence and the intended predictive task. |
| `shap` | EXT-007 | [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html), Abstract | SHAP attributes importance to features of a particular model prediction. |
| `react` | EXT-005 | [ICLR record](https://openreview.net/forum?id=WE_vluYUL-X) and [author preprint](https://arxiv.org/abs/2210.03629), Abstract and Section 2 | Reasoning and actions are interleaved with observations. The manuscript's action limits come from the team proposal. |
| `rag` | EXT-006 | [NeurIPS proceedings](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html), Abstract | Retrieval-augmented generation conditions generation on retrieved information. |
| `haurum` | EXT-008 | [Author-institution copy](https://vbn.aau.dk/files/771240153/1-s2.0-S1877050924019185-main.pdf), pp. 1082 and 1085–1087 | The study develops a LangChain agent for real-estate information and illustrates its evaluation with example queries. |
| `taichung` | EXT-002 / SUP-006 | [Dataset 103038](https://data.gov.tw/dataset/103038), resource `1095e2c3-4ccc-4766-b1ce-98aa2ddf0204` and the reproduced single-snapshot audit | Identifies the sales CSV and its release label. The filter and counts appear in Experiment. |

Sources were reconciled by DOI or, where a DOI was unavailable, by title and authoritative record. The NotebookLM and Perplexity analyses are research leads. The bibliography includes the sources cited in the paper.

```bibtex
@misc{moi,
  author = {{Ministry of the Interior, Taiwan}},
  title = {Real Estate Transaction Price Inquiry Service: Frequently Asked Questions},
  url = {https://lvr.land.moi.gov.tw/jsp/qa.jsp},
  note = {Accessed: Nov. 25, 2026}
}

@article{wang,
  author = {Wang, Pei Ying and Chen, Chiao Ting and Su, Jain Wun and Wang, Ting Yun and Huang, Szu-Hao},
  title = {Deep Learning Model for House Price Prediction Using Heterogeneous Data Analysis Along With Joint Self-Attention Mechanism},
  journal = {IEEE Access},
  volume = {9},
  pages = {55244--55259},
  year = {2021},
  doi = {10.1109/ACCESS.2021.3071306}
}

@article{roberts,
  author = {Roberts, David R. and others},
  title = {Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure},
  journal = {Ecography},
  volume = {40},
  number = {8},
  pages = {913--929},
  year = {2017},
  doi = {10.1111/ecog.02881}
}

@inproceedings{shap,
  author = {Lundberg, Scott M. and Lee, Su-In},
  title = {A Unified Approach to Interpreting Model Predictions},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {30},
  year = {2017}
}

@inproceedings{react,
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  title = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  booktitle = {International Conference on Learning Representations},
  year = {2023},
  url = {https://openreview.net/forum?id=WE_vluYUL-X}
}

@inproceedings{rag,
  author = {Lewis, Patrick and others},
  title = {Retrieval-Augmented Generation for Knowledge-Intensive {NLP} Tasks},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {33},
  pages = {9459--9474},
  year = {2020}
}

@article{haurum,
  author = {Haurum, Kasper Raupach and Ma, Ruiqi and Long, Wen},
  title = {Real Estate with {AI}: An agent based on {LangChain}},
  journal = {Procedia Computer Science},
  volume = {242},
  pages = {1082--1088},
  year = {2024},
  doi = {10.1016/j.procs.2024.08.199}
}

@misc{taichung,
  author = {{Land Administration Bureau, Taichung City Government}},
  title = {Taichung Real Estate Transaction Price Registration: Sales Since {ROC} Year 110},
  howpublished = {Taiwan Government Open Data Platform, dataset 103038},
  url = {https://data.gov.tw/dataset/103038},
  note = {Accessed: Nov. 25, 2026}
}
```
