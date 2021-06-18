<img alt="Selfie at late 2019, best one until now" src="./selfie.jpg" width=256>

### **Sun Guangda 孙广大**

* Email: sung@comp.nus.edu.sg
* GitHub: [sgdxbc](https://github.com/sgdxbc) (research) / [whoiscc](https://github.com/whoiscc) (personal)

# Education

* Bachelor's degree from Xian JiaoTong University (2020)
* Ph.D student at National University of Singapore (2020-)

# Interests

* **Research:** Network system
    * Distributed protocols
    * Software defined network
    * Network function virtualization
    * Programmable switch
* Programming language
    * Front-end design
    * Garbage collector
    * Interpreter implementation
* Graphic
* Web/desktop applications
* Software verification
* Music
    * Piano
    * Electronic

<div style="page-break-before: right;"></div>

# Works

## CODER

To configure devices in a software defined network (SDN), e.g., packets routes, network functions location and resource allocation, serveral high-level abstractions and languages, like Merlin and SNAP, are developed. CODER provides an common immediate representation for all SDN languages, defines precise semantic of combining SDN programs, and lets SDN programs written in different languages work together. With CODER user has more power on configuring SDN.

### Publication

Hao Li, Peng Zhang, **Guangda Sun**, Chengchen Hu, Danfeng Shan, Tian Pan, Qiang Fu \
*A Modular Compiler for Network Programming Languages* [pdf](https://nskeylab.xjtu.edu.cn/people/pzhang/files/2020/11/conext20.pdf) \
Proceedings of the 16th International Conference on emerging Networking EXperiments and Technologies (CoNEXT '20)

Hao Li, Peng Zhang, **Guangda Sun**, Chengchen Hu, Danfeng Shan, Tian Pan, Qiang Fu \
*An Intermediate Representation for Network Programming Languages* [pdf](https://conferences.sigcomm.org/events/apnet2020/material/apnet20-final4.pdf) \
Proceedings of the 4th Asia-Pacific Workshop on Networking (APNet '20)

### Repository

[ants-xjtu/sidfam-v3](https://github.com/ants-xjtu/sidfam-v3) (contributed 100% by me)

## Rubik

Rubik is a network stack parser generator for network function middleboxes. It provides a programming model for network protocols and protocol stacks with handful abstractions like flow table and reordered buffer. With Rubik, user can write only hundreds of lines of configuration, which will be transformed into tens of thousands of lines of C code. The generated protocol parser is more efficient than any human-writing ones.

### Publication

Hao Li, Changhao Wu, **Guangda Sun**, Peng Zhang, Danfeng Shan, Tian Pan, Chengchen Hu \
*Programming Network Stack for Middleboxes with Rubik* [pdf](https://www.usenix.org/system/files/nsdi21-li.pdf) \
Proceeding of the 18th USENIX Symposium on Networked Systems Design and Implementation (NSDI '21)

### Repository

[ants-xjtu/rubik](https://github.com/ants-xjtu/rubik) (contributed 99% by me)

## [WIP]

* A run-to-complete NFV framework which can provide isolation with PKU, and can run existing NFs with custom dynimical library loader.
* A BFT protocol which eliminate consensus overhead with programmable switch.

<div style="page-break-before: right;"></div>

# Projects

## Shift Saver

A VSCode extension which provides a "shift saving" mode. In the mode all space and hypen typing will be treated as underscore or capitilization, which makes naming variables shift-key-free. I also made a [video](https://www.bilibili.com/video/BV1FT4y1K7fn) to introduce it.

### Repository

[whoiscc/shift-saver](https://github.com/whoiscc/shift-saver), [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=correctizer.shift-saver)

## Shattuck

A script language inspired by Rust. Shattuck gives user a chance to use perfect Rust without worring about scary lifetime stuff. The prototype is implemented in Python and offical interpreter is implemented in Rust. I wrote [a serise of articles](https://zhuanlan.zhihu.com/p/65376093) for it on Zhihu.

### Repository

[whoiscc/shattuck](https://github.com/whoiscc/shattuck)

## RIoG

The reference implementation of games project aims to provide a general interface for web-based tiny games, with implementation of several popular games.

### Repository

[whoiscc/riog-project](https://github.com/whoiscc/riog-project)

----

Online version of this cv is on my [GitHub profile](https://github.com/sgdxbc).
