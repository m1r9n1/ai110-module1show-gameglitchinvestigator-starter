# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    - When inputting the first guessing number. The hint popped up stating that I should go lower. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hint was in fact backwards. Secret number was 64, I inputted 4, and the hint suggest to go lower.
  2. When I inputted second number, the hint did not suggest anything and the history of the number was not recorded in the debug info section.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 80| "go lower" (hint)|"go higher" (hint shown) | "none" |
|guess of 91 | "go lower" (hint)|(no hint suggest) | "none" |
|guess of 3 | "go higher (hint) | "go lower" (hint shown) | "none"
|submit new game | reset game | only reset secret, attempts, score  | could not play game(submit new guesses) |
|"press enter to submit guess" | "no response" | submits the guess when pressing enter (shows hint) | "none"


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
  - I used Copilot for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI suggestion to imlplement the change of the check_guess function was correct. It suggest to change what was outputted as a Hint ("string"), rather than changing any logic. After verifying the results by comparing the changes side by side, the hints that were once wrong and gave the opposite result was now giving the correct hint for each guess.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - In this case the results were straigt forward, upon review, the change that was implemented by the AI was correct on first try. However, when playing the game, the hint wasn't consistently correct. If the secret was 10, and I guessed 3 three times in a row, on the third attempt, the hint would be wrong. Leading to another bug that needed to be fixed. Another AI suggestion was when creating a test for one of the fixes, instead of actually testing for the behavior, it made a test to check if the code's structure was written correctly. This was confusing, but I was able to guide the AI to create a test that tested the behavior of the bug fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - By playing the game a few times and checking that the hint was working, I was able to finalize the decision that it was fixed. I also used pytest to check if all the tests passed, the pytest helped me figure out that there was another bug that had to due with the output of the hint. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - For the manual fix, I notice that when I entered an odd number, the hint was still inconsitent. When I inputted the same odd number back to back the hint became inconsistent. When I told AI about this bug, it was able to direct me to the line of code in the app.py where for some reason the odd number was getting converted into a string. After finding a fix, I asked AI to create a test that targets that bug. AI created a test, but the test failed. After telling AI, that the bug is fixed, but the test was failing, the change to fix this was to update the check_guess function to ensure that if secret was a string it will always convert it to an integer first.
- Did AI help you design or understand any tests? How?
    - Yes, AI helped me create files to run a pytest, it also wrote up a few test cases to check if the messages were matching up with the hint correctly. By creating a explaination of where the bug was first and explaining the logic behind it, I was able to understand in the line of code where the hint was getting inverted. So I finalized the AI to implement that change and then asked to create test that checked the changes that were made. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - The way I would explain Streamlit reruns and session state is by telling them to imagine that when playing a game like Mario, when you are on level one, and then the second you press the button to jump, the whole game restarts to the beginning of level one. So you will never advance thus making the game unplayable. The only way to make sure that the game doesnt restart, would be by using the Session State, or in this case "saving the game". 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - The habit I would like to keep that I learned from this project, is to use AI to help find where the issue may be in the code and just noting/commenting what the fix should be before fixing or implementing the fix. This is a great habit to use to keep work orginized and easier to work on especially when working in a large codebase. Documenting the fix is important to keep track of for current and future workflow. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  - One thing I woukld do differently next time is to use the mode correctly. At first I just used the agent mode and had to specically ask the agent to just explain without implementing. I learned that changing the mode to "ask" or "plan" is easier to prompt the AI without having to ask it to not make edits/changes. This also helps me break down the workflow into steps rather than just jumping into fixing the issue. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I learned alot about using AI generated code in this project. For one, it is not always reliable, you MUST verify the work, because the AI can generate code that is not relevant to what you want to do. I also learned that using AI generated code as a baseline or template can help you target an issue faster and may help you realize that there may be another underlining bug.
