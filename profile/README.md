# Retico

Retico is an open-source framework for building state-of-the-art incremental processing systems. This python package contains the functionality of the major supported retico modules and makes them easily accessible. 

"Incremental" means that the system processes inputs (e.g., speech recognition) at a fine-grained level, typically word-by-word. Large language models like ChatGPT allow a user to type a full input before submitting it to the chatbot, but when humans speak or write to each other, they produce and comprehend language incrementally, word-by-word. Not all practical systems need to function incrementally, but some would benefit from word-level processing. For example, a recent [NSF-sponsored workshop report](https://www.sciencedirect.com/science/article/pii/S0885230821000620?via%3Dihub) on spoken interaction with robots recommends that systems and modules should work in real-time to enable them to be more natural and responsive. 

Retico is based on the [Incremental Unit](https://journals.uic.edu/ojs/index.php/dad/article/view/10712) model of incremental dialogue processing. You can read about the [basics of incremental processing](https://github.com/retico-team/retico-core/blob/main/docs/basics.md). A typical Retico system is made up of processing modules. For example, a system could be made up of five modules: a speech recognizer, language understander, dialogue manager, natural language generator, and speech synthesizer. An "Incremental Unit" (IU) is a piece of information that passes between them. For example, a speech recognizer recognizes individual words packaged as an IU and outputs them to the language understander which takes in the speech recognition IU and interprets the intent of the user, then sends an IU that contains information about the intent to the dialogue manager, and so on.

Other incremental processing frameworks exist like [InproTK](https://github.com/timobaumann/inprotk) which is written in Java. 

---

## Support

The development of Retico is partially supported by the National Science Foundation

<img src="https://noirlab.edu/public/media/archives/logos/screen/logo245.jpg" width=25% height=100%>

---


## Installation

Some of the modules are available on pypi. Minimally, you need the `retico_core` ([documentation](https://retico-core.readthedocs.io/en/latest/)). Individual modules have more information about their respective installation requirements. 

---

## Example Retico Systems

- VQA [github](https://github.com/DavidC001/retico-VQA) (live VQA with multiple camera streams)
- Emotion Tracking [github](https://github.com/zihaurpang/retico-emotion-tracking)
- Language Practice [github](https://github.com/mi-1000/retico-language-practice-network)
- Argumentation Tracking [github](https://github.com/dexterwilliams96/retico-argumentation/tree/main)
- Retico Agent-VQA [github](https://github.com/AnhBui1108/retico-agent-VQA) (a Retico agent that integrates [Huggingface Agents](https://huggingface.co/learn/agents-course/en/unit0/introduction) tools)
- Simple Retico Agent [github](https://github.com/articulab/simple-retico-agent) | [documentation](https://simple-conversational-retico-agent.readthedocs.io/en/latest/index.html)
- Game of NIM with Misty II Robot with RL [github](https://github.com/bjBSU/nim)
- Robot "Tutor" with Misty II Robot [github](https://github.com/amanaser/Misty-Tutor)
- Compare two Object Recgonition Models [github](https://github.com/porterrigby/HRI-Final-Project)
- Cozmo on CoppelliaSim [github](https://github.com/retico-team/retico-coppelia/blob/main/example/coppelia_runner.py)

---


## Example Runner Script

```python
from retico import *
# imports for other modules


def callback(update_msg):
    for x, ut in update_msg:
        print(f"{ut}: {x.text} ({x.stability}) - {x.final}")


m1 = MicrophoneModule()
m2 = Wav2VecModule()
m3 = TextDispatcherModule()
m4 = GoogleTTSModule("en-US", "en-US-Wavenet-A")
m5 = SpeakerModule()
m6 = CallbackModule(callback)

m1.subscribe(m2)
m2.subscribe(m3)
m3.subscribe(m4)
m4.subscribe(m5)
m2.subscribe(m6)

run(m1)

input()

stop(m1)
```

---


## Monitoring and Logging

Some individual modules have visualization tools. We are currently working on a system-level visualization tool.

There are three options for loggers:

1. The [Platform for Situated Intelligence](https://github.com/microsoft/psi) (psi) is a powerful framework for building complex AI systems, written in C#. Logging to psi is straight-forward using the `retico-zeromq` module.
2. Full Logging of all incremental units can be done direclty with the [Articulab fork of retico](https://github.com/articulab/simple-retico-agent).
3. [Simple logging into a json file](https://github.com/retico-team/retico-simplelogger)

---

## Research with Retico

### The Quality and Usability Lab at Technische Universität Berlin

**Research that uses Retico**

Michael, T. (2023). [Simulating Conversations for the Prediction of Speech Quality](https://depositonce.tu-berlin.de/items/bd35be30-6add-4712-b763-d31b44f84284). Springer International Publishing AG.

Thilo Michael. 2020. Retico: [An incremental framework for spoken dialogue systems](https://aclanthology.org/2020.sigdial-1.6/). In Proceedings of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 49–52, 1st virtual meeting. Association for Computational Linguistics.

Thilo Michael and Sebastian Möller. 2020. [Simulating Turn-Taking in Conversations with Delayed Transmission](https://aclanthology.org/2020.sigdial-1.20/). In Proceedings of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 157–161, 1st virtual meeting. Association for Computational Linguistics.



### Speech, Language and Interactive Machines Lab at Boise State University

The SLIM Lab maintains many of the module repositories in `retico-team`.

**Research that uses Retico**

Henry, C., & Kennington, C. (2024). [Unsupervised, Bottom-up Category Discovery for Symbol Grounding with a Curious Robot](https://aclanthology.org/2022.sigdial-1.14/). arXiv preprint arXiv:2404.03092.

Whetten, R., Levandovsky, E., Imtiaz, M. T., & Kennington, C. (2023, August). [Evaluating Automatic Speech Recognition and Natural Language Understanding in an Incremental Setting](https://www.semdial.org/anthology/papers/Z/Z23/Z23-3012/). In Proceedings of the 27th Workshop on the Semantics and Pragmatics of Dialogue (SemDial). Maribor, Slovenia.

Josue Torres-Fonseca, Catherine Henry, and Casey Kennington. 2022. [Symbol and Communicative Grounding through Object Permanence with a Mobile Robot](https://aclanthology.org/2022.sigdial-1.14/). In Proceedings of the 23rd Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 124–134, Edinburgh, UK. Association for Computational Linguistics.

Imtiaz, M.T., Kennington, C. (2022). [Incremental Unit Networks for Distributed, Symbolic Multimodal Processing and Representation](https://doi.org/10.1007/978-3-031-06018-2_24). In: Duffy, V.G. (eds) Digital Human Modeling and Applications in Health, Safety, Ergonomics and Risk Management. Health, Operations Management, and Design. HCII 2022. Lecture Notes in Computer Science, vol 13320. Springer, Cham.

Casey Kennington, Daniele Moro, Lucas Marchand, Jake Carns, and David McNeill. 2020. [rrSDS: Towards a Robot-ready Spoken Dialogue System](https://aclanthology.org/2020.sigdial-1.17/). In Proceedings of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 132–135, 1st virtual meeting. Association for Computational Linguistics.



### Articulab at Carnegie Mellon University & Almanach Team at Inria Paris


Simple Retico Agent [github repo](https://github.com/articulab/simple-retico-agent) | [documentation](https://simple-conversational-retico-agent.readthedocs.io/en/latest/index.html)

---

## Citation

```
@inproceedings{michael-2020-retico,
    title = "Retico: An incremental framework for spoken dialogue systems",
    author = "Michael, Thilo",
    booktitle = "Proceedings of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue",
    month = jul,
    year = "2020",
    address = "1st virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.sigdial-1.6",
    doi = "10.18653/v1/2020.sigdial-1.6",
    pages = "49--52"
}
```
If you use any of the multiomdal modules (vision, robots, etc.) please also cite this paper:
```
@inproceedings{kennington-etal-2020-rrsds,
    title = "rr{SDS}: Towards a Robot-ready Spoken Dialogue System",
    author = "Kennington, Casey  and
      Moro, Daniele  and
      Marchand, Lucas  and
      Carns, Jake  and
      McNeill, David",
    editor = "Pietquin, Olivier  and
      Muresan, Smaranda  and
      Chen, Vivian  and
      Kennington, Casey  and
      Vandyke, David  and
      Dethlefs, Nina  and
      Inoue, Koji  and
      Ekstedt, Erik  and
      Ultes, Stefan",
    booktitle = "Proceedings of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue",
    month = jul,
    year = "2020",
    address = "1st virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.sigdial-1.17/",
    doi = "10.18653/v1/2020.sigdial-1.17",
    pages = "132--135",
    abstract = "Spoken interaction with a physical robot requires a dialogue system that is modular, multimodal, distributive, incremental and temporally aligned. In this demo paper, we make significant contributions towards fulfilling these requirements by expanding upon the ReTiCo incremental framework. We outline the incremental and multimodal modules and how their computation can be distributed. We demonstrate the power and flexibility of our robot-ready spoken dialogue system to be integrated with almost any robot."
}
```

