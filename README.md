# GPTScan

A new version of LLM detector for smart contract bugs based on [the LLM4Vuln paper](https://arxiv.org/abs/2401.16185) can be found at [https://app.metatrust.io/](https://app.metatrust.io/).

~~You can try GPTScan at https://app.metatrust.io/ for the moment, but we will replace it later with a new version (covering all kinds of logic bug rules).~~

This repository contains the prompts and rules used in MetaTrust Labs' GPTScan.

More rules and APIs will coming later.

## Preprint paper

[![](https://img.shields.io/badge/arXiv-2308.03314-B31B1B?style=flat-square)](https://arxiv.org/abs/2308.03314) Yuqiang Sun, Daoyuan Wu, Yue Xue, Han Liu, Haijun Wang, Zhengzi Xu, Xiaofei Xie, Yang Liu, **GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis**. *2024 IEEE/ACM 45th International Conference on Software Engineering (ICSE)*. [[arxiv](https://arxiv.org/abs/2308.03314)]

Bibtex:
```bibtex
@INPROCEEDINGS{sunicse2023gpt,
  author={Yuqiang Sun and Daoyuan Wu and Yue Xue and Han Liu and Haijun Wang and Zhengzi Xu and Xiaofei Xie and Yang Liu},
  booktitle={2024 IEEE/ACM 45th International Conference on Software Engineering (ICSE)}, 
  title={GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis}, 
  year={2024}
```

## Dataset

Dataset used to evaluate GPTScan in the paper, are the following:
1. Web3Bugs: [https://github.com/MetaTrustLabs/GPTScan-Web3Bugs](https://github.com/MetaTrustLabs/GPTScan-Web3Bugs)
2. DefiHacks: [https://github.com/MetaTrustLabs/GPTScan-DefiHacks](https://github.com/MetaTrustLabs/GPTScan-DefiHacks)
3. Top200: [https://github.com/MetaTrustLabs/GPTScan-Top200](https://github.com/MetaTrustLabs/GPTScan-Top200)
