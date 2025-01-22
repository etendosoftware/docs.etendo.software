---
title: Etendo Copilot
tags: 
 - Etendo Copilot
 - AI Integration
 - Assistants
 - Intelligent Tools
 - Agents
 - User Guide
---

![cover-getting-started.png](../../assets/getting-started/overview/cover-getting-started.png)

# Etendo Copilot

## Overview

Etendo Copilot is a powerful tool integrated into the Etendo Classic interface, or accessible via API, that provides an efficient way to interact with assistants and use tools developed to solve specific problems. It is an innovative project designed to streamline your processes by harnessing the power of Artificial Intelligence. This page will guide you through the main features of Etendo Copilot.

!!! info
    To install Etendo copilot, you can read the [Copilot Installation](../../developer-guide/etendo-copilot/installation.md) guide in the developer's guide section.

!!! note
    Remember that, to use this functionality, it is necessary to configure an API Key. For this, you can use one of your own, or you can contact the Etendo support team to purchase one.

## What is Etendo Copilot?

![Copilot Chat](../../assets/user-guide/etendo-copilot/getting-started/copilot.png){align=right  width="300"}

At its core, Etendo Copilot is a groundbreaking initiative that redefines how developers and users interact with tools and information. It revolves around a central component, the *Assistant* which acts as the mastermind behind task delegation. This Agent has secondary modules referred to as *Tools*. The seamless communication between these components is facilitated via a RESTful API, ensuring a stateless and scalable interaction model.


## Assistant

The Assistant serves you making on-the-fly decisions about which Tool is best suited to respond to a particular query. This intelligent decision-making ensures that you receive the most accurate and efficient assistance.

Each assistant has defined instructions, as well as the possibility to configure a knowledge base and a set of skills or tools.
The assistant is able to make decisions based on a question, using the most appropriate knowledge base or tool set to answer a particular query.

In turn, it is possible to configure assistant managers, able to delegate a specific query to other specialized assistants and coordinate between the different assistants in your team to achieve an assertive response.  This intelligent decision-making ensures that you receive the most accurate and efficient assistance. Assistants can be distributed in Etendo modules as datasets or created per environment.

## Tools

Each tool represents a dedicated and self-contained project, meticulously designed to excel at specialized tasks. Whether it involves code translation, text analysis, or data manipulation, the diverse suite of tools operates in seamless coordination.  

!!! info 
    For a overview of the available tools and their technical details, please refer to the [Available Tools - Developer Guide](../../developer-guide/etendo-copilot/available-tools/overview.md).


##  Key Features


- **Effortless Integration**: Etendo Copilot seamlessly integrates into your environment, adding an extra layer of intelligence to your workflow.

- **On-Demand Assistance**: Send your queries to Etendo Copilot, and the Agent will guide you towards the most suitable Tool for the job.

- **Diverse Expertise**: Our ever-growing selection of Tools covers a wide range of domains, ensuring you always have the right solution.

- **Open AI Assistants**: Copilot is integrated with the Assistants technology developed by Open AI, allowing you to set up your assistants, trained with your own knowledge base, able to generate and interpret new code, and use the specific tools already distributed by Etendo or new ones.  

- **LangGraph**: In this case, this option works as a manager of other assistants and allows to select team members. 

- **Langchain Agent**: These assistants can perform specific tasks in natural language and provide contextualized responses, enabling the implementation of multiple AI models, the use of a proprietary vector database and internal memory management.
- **Multi-Model Assistant** This type of assistant can be used with multi-vendor models such as *Anthropic* and *Gemini*, in addition to existing *OpenAI* models.
- **Attach Files** Etendo Copilot allows users to attach one or multiple files for assistants.

## Copilot Interface
---

![Copilot Navbar](../../assets/user-guide/etendo-copilot/getting-started/copilot-navbar.png)

In the Etendo Classic navigation bar, you'll find a Copilot icon that leads you to the chat pop-up.

Here, you can select an Assistant and engage in a conversation with it. Copilot facilitates communication with `Langchain Agent`, `Multi-Model Assistant`, `LangGraph` and `Open AI Assistant` types, for more information visit [Assistant Windows](../etendo-copilot/setup-and-usage.md#assistant-window) documentation.

### Attach Files
---

![Attach-Files](../../assets/user-guide/etendo-copilot/getting-started/attach-files.png){align=right  width="300"}

Etendo Copilot allows users to attach one or multiple files for assistants to process. This feature supports any file format, enabling flexibility in use cases. However, the ability to interpret and process these files depends on the specific assistant configuration, the defined tools, and the underlying model used.

This functionality ensures that users can seamlessly incorporate external data into their workflows, whether it involves parsing documents, analyzing spreadsheets, or processing images. Assistants and tools can be tailored to address specific requirements based on the type of attached files, providing contextualized and intelligent responses.

<br>
<br>

### Visualization Mode
---
<figure markdown>
![](../../assets/user-guide/etendo-copilot/getting-started/regular-size-copilot.png){align=right width=300}
<br><br>
Copilot, by default, can be used as a pop-up window. This is comfortable to use as an integrated assistant available in any window you are using.
</figure>
---

<figure markdown>
![](../../assets/user-guide/etendo-copilot/getting-started/full-screen-copilot.png)
<br><br>
Select the fullscreen mode for a more comfortable use when having long conversations.
</figure>

---
<figure markdown>
![](../../assets/user-guide/etendo-copilot/getting-started/minimized-copilot.png){align=right width=200}
<br><br>
It can also be minimized. In this case, the logo will be shown in the lower-right section of the screen.
</figure>
---
When asked something, Copilot informs the user about the assistants and tools used when processing each message.

!!!note
    When closed and opened again, by default, Copilot will select the last assistant previously used.