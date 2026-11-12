## What is AI?

ai -machines that solve problems

-   text input -> totkenisation 
-   ->embedding (numerical vector) --> transformer (context)
-   output --> predictions the highest likelihood 
- 
attention, repeat layers, context mixing feed-forward (refine the meaning)
each layer adds context , each layer adds context and repeats understanding

final token vectors -> calc probabilities 
embedding -> 

|token | vector rep |
|--|--|
|word | [22,30,03]|

transformer 

comparing tokens against their context 
transformer learning
- early: what are the key tokens?
- middle: recognises if its a factual question
- understands some of the words
- late -- focuses on the relation, checks the most represented token for this

output -> greedy approach - whats most likely 

optimisation

inference parameters
- temperature : choosing tokens that have lower probabilities
- top-k : keeps top 20 so 20% of the most likely tokens
- nucleus sampling -> picks most likely token keeps adding until cumulative probability
- reaches a set threshold, unlike top-k num of candidate tokens adapt to model conf
- fidence
- presence penalties : helps prevent the model from fixating on already used tokens 
- to minimise repetitive output
- open vs closed: open models you can modify e.g temp allows access to modify inference
- closed: not adjust
- in Action 

capability consideration
- entity disambiguation
- cant distinguish 2 people with the same name, one person can be on the registry and 
- ai can spread it

context window size
- amount fo ai can consider at once - each chat has its own context window
- increased comp complexity

model collapse theory -> llms trained on llms 

risk mitigation -> 
hallucinations  -> double check all facts+ references - use RAG
bias            -> pick diverse sources + perspectives
tokenisation limits -> prompt engineering
context window -> manage chats carefully by summarising key info
model collapse -> require more human generated content

RAG -> retrival augmented generation
search for relevant info from docs, databases , websites 
solves 2 problems- > knowldge cutoff

sycophancy -> describes ai's need to prioritise user agreement over independant 
reasoning
overconfidence -> ai systems are regularly optimised through RL
penalise incorrect answers 
they would rather get the answer wrong for a chance for a reward

RL is being changed  -> Rl with calibration rewards, confidence vs correctness
lower reward if the answer is guessed 

general mitigation:
- human verification
- better evidence rag
- better detail
- better prompts +context
- 

prompting framework:
1. Persona - define role, expertise or perspective
2. Task - state tje deliverable, action, the outcome
3. context - what information should the ai use - provide relevant background
4. constraints - set requirements for format, length, tone ,audience, scope 
5. evaluate
6. iterate

context -files



try different techniques 




