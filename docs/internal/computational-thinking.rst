Computational Thinking
======================

Our goal should be to:

* To teach the core competences of computational thinking
* To have a clear goal of each lesson
* To have engaging and well structured material
* Promote the use of programming for more than school activities

Challenges to overcome:

* Unengaged students
* Vulnerary material
* Placement of workshops

Most students will down prioritize voluntary classes or workshops to focus
on mandatory activities. This means that our biggest problem will be to 
convince students that we can teach them something that they won't learn 
from anywhere else. We therefore also have a big task to find out how to
best promote and reach out to the students that struggle with programming.

1. Core competences
-------------------

We will be basing the core competences on the Python programming language
since DTU has decided to include this language in the Polytechnical foundation.
Lessons in computational might not strictly be based on Python, but the
understanding gained from any of the material should lead to a better 
knowhow about the usage the language. In the following bullets we list 
some of the most important concepts when programming.

1. **Knowledge of the state of a program**

In order to solve complex problems a programmer will always have the state
of the program in mind. This is a crucial skill for a new computational thinker
to practice since it leads them to better reason about the code, predict outcomes
and debug more efficiently.

*What are the the current declared variables?*

*Where in the program is the instruction pointer?*


2. **The flow of the program**

Most good programmers have a good idea of how their code will end up looking 
like before they even start to code. This intuition that takes time to develop
and is practiced by learning how to do software architecture.

*What is the overarching goal of the given code and how does it achieve that?*

*What methods we as programmers have in our toolbox to solve problems?*

3. **Tools to make life easier for a programmer**

Most programmers do not code everything from scratch, we rely on existing 
software to make coding more efficient and enjoyable. This is not limited 
to how we code but also how to gain the understanding needed to solve a
problem. Therefore knowing how to search or seek information will help on almost
every problem, especially when combined with generative AI.

*Examples: debugger, type annotation, git, linting, formatters, generative AI*

4. **Communication of what a program does**

Computational thinking is more than just solving a problem in an efficient
way, it is also being able to communicate what a program does and why it
what considerations lead to the implementation. This skill is crucial to learn
since it facilitates better documentation which in turn makes teamwork more
efficient.

*How do programmers document their code for better teamwork?*


3. Lesson goals
---------------

In order to facilitate the above competences the following workshops are proposed.
Each workshop is given a catchy title, but with its content not constrained to that
title (give them what they came for but lets add a little extra).

.. card::

    **Title**: Tour de Python

    **Subtitle**: *Catchup workshop for python programming*

    **Schedule**: Beginning of each 13-week periods

    **Goal**: Gives students the opportunity to catch up on how to use Python for the following semester

    **Content**: Basic syntax, use of common packages

    **Material**: Give students the knowhow of where to find and use python documentation


.. card::

    **Title**: Git Your Grades Up! Track, Collaborate, Succeed.

    **Subtitle**: *How to use git efficiently in your studies*

    **Goal**: Get students started with using git in their coding projects

    **Content**: Basic git and GitHub

    **Material**: Basic guide on how to use GitHub desktop or cheatsheet for the commandline

.. card::

    **Title**: DTU Brushup coding

    **Subtitle**: *Get ready for your studies at DTU!*

    **Goal**: Give a basic knowledge of computational thinking

    **Content**: Use board games such as Robo Rally to teach computational thinking. Move then to a computer and show the similarities.

    **Material**: Board games and pygame.

.. card::

    **Title**: Next gen AI for coding

    **Subtitle**: *How to utilize generative AI to maximize productivity*

    **Goal**: Give students an overview of how modern machine learning tools work and how to utilize them

    **Content**: Give examples on how to be an effective prompt engineer and how to use AI agents.

    **Material**: The use of GitHub Copilot (Free access using GitHub Education)


2. Material
-----------

Throughout a student time a DTU we should recognize that we can't offer a
course or a workshop that teaches all the necessary prerequisites for using
python for all possible engineering projects. Many of the simple questions 
in regard to using Python can be answered surprisingly well by the use of 
generative AI. For more complicated questions AI prompts we often see
responses that do not work because of special technical details. For students
to overcome these roadblocks themselves they need to understand what they are
working with, which in most cases comes from reading the package documentation. 
We should therefore strive to teach students how to use documentation in the
cases where AI falls short or is not available. 

Another problem is engaging students in using python in innovative ways.
Here the biggest problem for unexperienced programmers is unknown unknowns.
That is, there are things that students are not aware of that they do not
understand.

1. **Known Knows**: Things you do know (e.g., "I know how to use a for loop").
2. **Known Unknowns**: Things you know you don't know (e.g., "I don't know how to implement a binary search tree"). These are manageable, you can research them.
3. **Unknown Unknowns**: The real danger zone. You're unaware that there's something crucial missing from your understanding or skillset needed for the problem.

Unknown Unknowns could be:

1. Not knowing about assumptions needed to use a function
2. Not knowing that your program uses a specific package: "well, the code runs works on my machine..."
3. You're unaware of potential security vulnerabilities in your code.

For new programmers this manifests itself most clearly in them not knowing
what they are able to do with their new coding skills. Most new programmers 
have never seen a well structured codebase, or how a big project looks like.
Providing a Python "bible" or "cookbook" that includes examples of the most 
used packages and language features could enable students to realize how to 
solve different problems. Such a book should have a strong empathies on the 
content not be connected to any coursework but how to generally solve problems 
with "Computational thinking". Such notes should be clear, concise and be
helpful throughout their time at university.

**Proposals**:

.. Card::
    Runnable tutorials in the browser

    A novel idea would be to provide runnable scripts in the browser that
    showcased the basics of numpy, pandas, and matplotlib.

    Note: https://livinnector.github.io/live-py-tutor

.. Card::
    Exmaples of miniprojects

    Provide guides and examples for students on how to structure code projects.
    These examples could be in the form of miniprojects that are unrelated to
    any specific course, but should showcase what kinds of programs you are able 
    to code with python. 

    Note: Pygame, P5 for visual appealing examples