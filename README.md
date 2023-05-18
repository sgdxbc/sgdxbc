<img src="https://github.com/sgdxbc/sgdxbc/assets/59077595/429095da-c65d-44a4-a60c-c3292dc41efd" width="150">

### **Sun Guangda 孙广大**

* Email: sung@comp.nus.edu.sg
* GitHub: [sgdxbc](https://github.com/sgdxbc) (research) / [whoiscc](https://github.com/whoiscc) (personal)

# Education

* Bachelor's degree from Xian JiaoTong University (2020)
* Ph.D student at National University of Singapore (2020-)

# Interests

Currently focused research topics are **distributed and decentralized systems**.
Previous works also relate to software defined network and network middleboxes.

Signaficant personal interests: interpreter and runtime for programming language, graphics, simulation and model checking.

Playing piano and listening to electronic music for all the time.

# Works

## NeoBFT

Byzantine fault tolerant (BFT) protocols are capable of masking these types of failures, but are rarely deployed due to their performance cost and complexity. 
In this work, we propose a new approach to designing high performance BFT protocols in data centers. 
By re-examining the ordering responsibility between the network and the BFT protocol, we advocate a new abstraction offered by the data center network infrastructure. 
Feasibility of the design is demonstrated by two hardware implementations - one using HMAC and the other using public key cryptography for authentication - on new-generation programmable switches. 
We then co-design a new BFT protocol, NeoBFT, that eliminates cross-replica coordination and authentication in the common case.

**Guangda Sun**, Xin Zhe Khooi, Yunfan Li, Mingliang Jiang, Jialin Li \
*NeoBFT: Accelerating Byzantine Fault Tolerance Using Authenticated In-Network Ordering* [pdf (preprint version)](https://arxiv.org/pdf/2210.12955) \
SIGCOMM '23

**Repository**: [sgdxbc/dsys at sigcomm23](https://github.com/sgdxbc/dsys/tree/sigcomm23)

## LemonNFV

A novel NFV framework that can consolidate heterogeneous NFs without code modification. LemonNFV loads NFs into a single process down to the binary level, schedules them using an intercepted I/O, and isolates them with the help of a restricted memory allocator.

Hao Li, Yihan Dang, **Guangda Sun**, Guyue Liu, Danfeng Shan and Peng Zhang \
*LemonNFV: Consolidating Heterogeneous Network Functions at Line Speed* [pdf](https://www.usenix.org/system/files/nsdi23-li-hao.pdf) \
NSDI '23

**Repository**: [ants-xjtu/neptune](https://github.com/ants-xjtu/neptune).

## Rubik

Rubik is a network stack parser generator for network function middleboxes. It provides a programming model for network protocols and protocol stacks with handful abstractions like flow table and reordered buffer. With Rubik, user can write only hundreds of lines of configuration, which will be transformed into tens of thousands of lines of C code. The generated protocol parser is more efficient than any human-writing ones.

Hao Li, Changhao Wu, **Guangda Sun**, Peng Zhang, Danfeng Shan, Tian Pan, Chengchen Hu \
*Programming Network Stack for Middleboxes with Rubik* [pdf](https://www.usenix.org/system/files/nsdi21-li.pdf) \
NSDI '21

**Repository**: [ants-xjtu/rubik](https://github.com/ants-xjtu/rubik) as the major contributor.

## CODER

To configure devices in a software defined network (SDN), e.g., packets routes, network functions location and resource allocation, serveral high-level abstractions and languages, like Merlin and SNAP, are developed. CODER provides an common immediate representation for all SDN languages, defines precise semantic of combining SDN programs, and lets SDN programs written in different languages work together. With CODER user has more power on configuring SDN.

Hao Li, Peng Zhang, **Guangda Sun**, Wanyue Cao, Chengchen Hu, Danfeng Shan, Tian Pan, Qiang Fu \
*Compiling Cross-Language Network Programs Into Hybrid Data Plane* [pdf](https://aquatoney.github.io/files/coder-ton22-li.pdf) \
ToN '22, doi: 10.1109/TNET.2021.3132303.

Hao Li, Peng Zhang, **Guangda Sun**, Chengchen Hu, Danfeng Shan, Tian Pan, Qiang Fu \
*A Modular Compiler for Network Programming Languages* [pdf](https://nskeylab.xjtu.edu.cn/people/pzhang/files/2020/11/conext20.pdf) \
CoNEXT '20, doi: 10.1145/3386367.3432063

Hao Li, Peng Zhang, **Guangda Sun**, Chengchen Hu, Danfeng Shan, Tian Pan, Qiang Fu \
*An Intermediate Representation for Network Programming Languages* [pdf](https://conferences.sigcomm.org/events/apnet2020/material/apnet20-final4.pdf) \
APNet '20, doi: 10.1145/3411029.3411030

**Repository**: [ants-xjtu/sidfam-v3](https://github.com/ants-xjtu/sidfam-v3) as the only contributor.

# Projects

## Shift Saver

* Repository: [whoiscc/shift-saver](https://github.com/whoiscc/shift-saver)
* Marketplace: [Shift Saver](https://marketplace.visualstudio.com/items?itemName=correctizer.shift-saver)
* [Video](https://www.bilibili.com/video/BV1FT4y1K7fn)

---

Last revised on May 18 2023. Online version of this CV is on https://github.com/sgdxbc.
