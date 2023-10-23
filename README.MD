# AGF - Article Generation Framework

Let this framework be a starting point for anyone looking to generate articles using GPT-3.

## Design Goals
- Modular
- Extensible
- Focused

## Basis
1. Summarize
2. Identify Key Points
3. Paraphrase
4. Eliminate Redundancy
5. Maintain Clarity
6. Use Your Own Words
7. Shorten Lengthy Explanations
8. Organize by Importance 
9. Expand 
10. Maintain Coherence 
11. Transitions 
12. Conclusion 
13. Proofread and Finalyze 
14. Review for Consistency

## New System For Each Prompt
In my experience I have found that assigining a more task focused identity to GPT3.5 heavily increases the quality of the output. 

For this reason I will never be using the same system for multiple actions like what you would normally do while using chatgpt.

AGF is designed to be something more than what we could achieve with chatgpt and for this reason I will be using a new system for each prompt.

## Option to switch between GPT4 and GPT3.5
AGF is opinionated as in for tasks that require simple tasks we wont be consuming from gpt4. We will be using GPT4 for some complex tasks.

## Why not async
It takes a lot of time to generate the final article. 
However, this is for good reason.

The input of each stage depends on the other stage to be completed and that is the reason
why we dont do all requests at once.


## Usage

- Create a .env file with `OPENAI_API_KEY`
