Langchain, LamaIndex, Haystack -> offer similar capability

what is Langchain?
    a open source framework to create applications powered with LLM. It helps/handles in orcehstration, branching, decision, failures, retrival with LLM when created

LangChain: Helps you build the components and interactions of an LLM application.
LangGraph: Helps you control how those components execute as a stateful workflow or agent.

what we can build?
    conversational chatbots
    AI Knowledge Assistant
    AI Agents
    Workflow Automation
    Summarization/Research Assistant


components of LangChain:    
    Model
    Prompts
    Chains
    Memory
    Indexs
    Agents


####### Models. ##########

In LangChain "models" are the core interfaces through which you interact with ai models. 
    when we develop a chatbots -> there are two major problem arises with it : first that model able to understand the context of problem. second: It should give correct result based on the same problem. With intro to LLM this problem solved. Now let say company want to integrate a bot then putting whole LLM to their server will be a insane problem for API integration introduced. Now with API another problem arises that different model have different way/syntax of calling which will again cause problem if we want to switch from one model to another. This problem again solved by LangChain as it act as interfaces black box just need a small change to change the model

    The Model component in LangChain is a crucial part of the framework, design to falicitate interaction with various language models and models 

    It abstract the complexicity of working directly with different LLMs, chat models, & embedding models provinding a uniform interface to communicate with them. This makes it easier to build applications that rely on AI generated text, text embeddings for similarity search and retrieval augmented generation


    It is of two types: Language Model, Embedding Models

    Language Models : text input -> text output
    LLMs : General purpose models that is used for generating text, summary, codes. They take a (or plain text) as input and returns a string. They are traditionally older models and are not used much now.
    chat models : Language models that are specialized for conversational tasks. They take a sequence of messages as inputs and return chat message inputs and return chat messages as output (as opposed to using plain text). these are traditionally newer models and used mode in comparision to the LLM

    Feature: 
        Purpose -> LLM: Free form text generation  Chat models: optimzed for multi turn conversation
        Training Data -> LLM: General text corpora(book & articles)  Chat models: Fine tuned on chat datasets (dialogue, user assitant conversation)
        Memory & Context -> LLM: No built in memory  Chat models: Supports structured conversation history
        Role & Awareness -> LLM: No understanding of user & assistant roles  Chat models: understand "system", "user", & "assistant" roles
        Example Models -> LLM: GPT-3, Llama 2 - 7B, OPT-1.3B  Chat models: GPT-4, GPT - 3.5-turbo, Llama-2-chat, Mistral-instruct, claude
        Use cases -> LLM: Text Generation, Summarization, translation, creative writing, code generation.  Chat models: conversational AI, chatbots, virtual assistants, customer support, AI tutors


    Temperature: It is a parameter which control the randomness of a language model's output. It affect how creative or deterministic the response are.'
        Lower values(0.0-0.5): More deterministic & predictable
        Higher values(0.7 - 1.5): More random, creative & diverse

    Usercase: Factual answer -> 0.0 - 0.3
    Balanced response -> 0.5 - 0.7
    creative writing, storytelling, jokes -> 0.9 - 1.2
    Maximum randomness (wild ideas & randomness) -> 1.5+

    max_complete_tokens: 

Open Source Models: freely available AI models that can be downloadable


Accordiing to definition: Language Models are of two types
    LLM -> general purpose models response to any NLP query whether text, code, Summarization, etc.
    ChatModels -> highly focused on conversation task. take multiple input and give response in text

    LLM vs ChatModels ******
        1. Purpose:  Free Form text generation, optimized for multi turn conversation
        2. Training Data: General text corpora(Books, articles) , Fine tuned on chat datasets
        3. Memory & Context: No built in memory, Support Structured conversation history
        4. Role & Awareness: No understanding of user & assistant roles,  understand system, user, & assistant roles
        5. Example Models:  

######### Prompts.   ############
with LangChain we can add following types of prompts to increase user experience with chatbots
1. Dynamic & Resuseable Prompts 2. Role based Prompts  3. Few Shots Prompts



######### CHAINS.   ###########

it is a concept to create pipeline such that output of previous response is auto passed to next chain


###### Indexes   ##########

indexes connect your application to external Knowledge - such as pdf, website or db. it consist of Doc loader, text splitter, vector storage, Retrievers


######## Memory #######

LLM API calls are stateless. the memory feature in langchain help to solve this problem.
    eg: Conversation buffer memory, Conversation buffer window memory, Summarization based memory, Custom memory


######## Agents  #########

chatbots with reasoning and decision capibility and having access to external tools are termed as agents.