# compiler
## Description
* This is a python code that does a lexical and syntax analyses for an input code.
* It uses the Java Context Free Grammar to analyze the input code. So the input code should be a Java code
* It is not a full compiler, it only does the lexical and syntax analysis/check of the code. No bytecode is generated (yet)

## How to use
* Run `python3 main.py`
* Java tokens grammar is defined in `language_grammar.txt`
* Java CFG is defined in `java_cfg.txt`
* The code to be processed is read from `input.txt`
* Output is in `syntax_analyzer_output.txt`. It is divided into two parts:
  * Production rules after converting grammar to LL(1) grammar
  * Production rules used to generate the input code
* Line length in the output file can reach up to 700 characters, set the line length limit to be 800 on your text editor so that the printed table is not corrupted.
