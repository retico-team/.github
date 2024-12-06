# retico

Retico is an open-source framework for building state-of-the-art incremental processing systems. This python package contains the functionality of the major supported retico modules and makes them easily accessible. 

"Incremental" means that the system processes inputs (e.g., speech recognition) at a fine-grained level, typically word-by-word. Large language models like ChatGPT allow a user to type a full input before submitting it to the chatbot, but when humans speak or write to each other, they produce and comprehend language incrementally, word-by-word. Not all practical systems need to function incrementally, but some would benefit from word-level processing. For example, a recent [NSF-sponsored workshop report](https://www.sciencedirect.com/science/article/pii/S0885230821000620?via%3Dihub) on spoken interaction with robots recommends that systems and modules should work in real-time to enable them to be more natural and responsive. 

Retico is based on the [Incremental Unit](https://journals.uic.edu/ojs/index.php/dad/article/view/10712) model of incremental dialogue processing. A typical system is made up of processing modules. For example, a system could be made up of give modules: a speech recognizer, language understander, dialogue manager, natural language generator, and speech synthesizer. An "Incremental Unit" (IU) is a piece of information that passes between them. For example, a speech recognizer recognizes individual words packaged as an IU and outputs them to the language understander which takes in the speech recognition IU and interprets the intent of the user, then sends an IU that contains information about the intent to the dialogue manager, and so on.

Other incremental processing frameworks exist like [InproTK](https://github.com/timobaumann/inprotk) which is written in Java. 


## Installation

Some of the modules are available on pypi. Minimally, you need the `retico_core` ([documentation](https://retico-core.readthedocs.io/en/latest/). Individual modules have more information about their respective installation requirements. 


## Example

```python
from retico import *
from retico.modules import *


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

## Monitoring and Logging

Some individual modules have visualization tools. We are currently working on a system-level visualization tool.

There are three options for loggers:

1. The [Platform for Situated Intelligence](https://github.com/microsoft/psi) (psi) is a powerful framework for building complex AI systems, written in C#. Logging to psi is straight-forward using the `retico-zeromq` module.
2. Full Logging of all incremental units can be done direclty with the [Articulab fork of retico](https://github.com/articulab/simple-retico-agent).
3. Simple logging into a .csv file (in progress)

## Research with Retico

### Speech, Language and Interactive Machines Lab at Boise State University

The SLIM Lab maintains many of the module repositories in `retico-team`.

**Research that uses Retico**

```
Henry, C., & Kennington, C. (2024). [Unsupervised, Bottom-up Category Discovery for Symbol Grounding with a Curious Robot](https://aclanthology.org/2022.sigdial-1.14/). arXiv preprint arXiv:2404.03092.

Whetten, R., Levandovsky, E., Imtiaz, M. T., & Kennington, C. (2023, August). [Evaluating Automatic Speech Recognition and Natural Language Understanding in an Incremental Setting](https://www.semdial.org/anthology/papers/Z/Z23/Z23-3012/). In Proceedings of the 27th Workshop on the Semantics and Pragmatics of Dialogue (SemDial). Maribor, Slovenia.

Josue Torres-Fonseca, Catherine Henry, and Casey Kennington. 2022. [Symbol and Communicative Grounding through Object Permanence with a Mobile Robot](https://aclanthology.org/2022.sigdial-1.14/). In Proceedings of the 23rd Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 124–134, Edinburgh, UK. Association for Computational Linguistics.

Imtiaz, M.T., Kennington, C. (2022). [Incremental Unit Networks for Distributed, Symbolic Multimodal Processing and Representation](https://doi.org/10.1007/978-3-031-06018-2_24). In: Duffy, V.G. (eds) Digital Human Modeling and Applications in Health, Safety, Ergonomics and Risk Management. Health, Operations Management, and Design. HCII 2022. Lecture Notes in Computer Science, vol 13320. Springer, Cham.

Casey Kennington, Daniele Moro, Lucas Marchand, Jake Carns, and David McNeill. 2020. [rrSDS: Towards a Robot-ready Spoken Dialogue System](https://aclanthology.org/2020.sigdial-1.17/). In Proceedings of the 21th Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 132–135, 1st virtual meeting. Association for Computational Linguistics.
```




### Articulab at Carnegie Mellon University & Almanach Team at Inria Paris

```
Simple Retico Agent [github repo](https://github.com/articulab/simple-retico-agent) [documentation](https://simple-conversational-retico-agent.readthedocs.io/en/latest/index.html)
```

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

