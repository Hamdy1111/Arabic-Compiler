#!/usr/bin/env python
# coding: utf-8

# In[16]:


from tkinter import scrolledtext, messagebox
import tkinter as tk
import re


# In[27]:


TOKENS = [
    ("KEYWORD", r"\b(اذا|طالما|متغير)\b"),
    ("IDENT", r"\b[_a-zA-Z\u0621-\u064A][_\w\u0621-\u064A]*\b"),  # Arabic and Latin letters
    ("NUM", r"\b\d+\b"),
    ("OPERATOR", r"==|!=|>=|<=|>|<|\+|-|\*|/"),
    ("ASSIGN", r"="),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("SEMICOLON", r";"),
    ("WHITESPACE", r"\s+"),  # Whitespace to ignore
    ("UNKNOWN", r".")  # Catch-all for unrecognized tokens
]

def tokenize(code):
    regex_parts = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKENS)
    regex = re.compile(regex_parts)
    tokens = []
    for match in regex.finditer(code):
        kind = match.lastgroup
        value = match.group()
        if kind == "WHITESPACE":  # Ignore whitespace
            continue
        if kind == "UNKNOWN":
            raise ValueError(f"Unknown token: {value}")
        tokens.append((kind, value))
    return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ("EOF", "")

    def advance(self):
        if self.pos < len(self.tokens):
            self.pos += 1

    def expect(self, kind):
        if self.current_token()[0] == kind:
            self.advance()
        else:
            raise SyntaxError(f"Expected {kind}, found {self.current_token()}")

    def parse_program(self, stop_at_rbrace=False):
        while self.current_token()[0] != "EOF":
            if stop_at_rbrace and self.current_token()[0] == "RBRACE":
                break
            self.parse_statement()

    def parse_statement(self):
        if self.current_token()[0] == "KEYWORD" and self.current_token()[1] == "متغير":
            self.parse_declaration()
        elif self.current_token()[0] == "IDENT":
            self.parse_assignment()
        elif self.current_token()[0] == "KEYWORD" and self.current_token()[1] == "اذا":
            self.parse_if_statement()
        elif self.current_token()[0] == "KEYWORD" and self.current_token()[1] == "طالما":
            self.parse_while_statement()
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token()}")

    def parse_declaration(self):
        self.expect("KEYWORD")  # متغير
        self.expect("IDENT")
        self.expect("ASSIGN")
        self.parse_expression()
        self.expect("SEMICOLON")

    def parse_assignment(self):
        self.expect("IDENT")
        self.expect("ASSIGN")
        self.parse_expression()
        self.expect("SEMICOLON")

    def parse_if_statement(self):
        self.expect("KEYWORD")  # اذا
        self.expect("LPAREN")
        self.parse_condition()
        self.expect("RPAREN")
        self.expect("LBRACE")
        self.parse_program(stop_at_rbrace=True)
        self.expect("RBRACE")

    def parse_while_statement(self):
        self.expect("KEYWORD")  # طالما
        self.expect("LPAREN")
        self.parse_condition()
        self.expect("RPAREN")
        self.expect("LBRACE")
        self.parse_program(stop_at_rbrace=True)
        self.expect("RBRACE")

    def parse_condition(self):
        self.parse_expression()
        if self.current_token()[0] == "OPERATOR" and self.current_token()[1] in {"==", "!=", ">", "<", ">=", "<="}:
            self.advance()
        else:
            raise SyntaxError(f"Expected relational operator, found {self.current_token()}")
        self.parse_expression()

    def parse_expression(self):
        self.parse_term()
        while self.current_token()[0] == "OPERATOR" and self.current_token()[1] in {"+", "-"}:
            self.advance()
            self.parse_term()

    def parse_term(self):
        if self.current_token()[0] == "IDENT":
            self.advance()
        elif self.current_token()[0] == "NUM":
            self.advance()
        else:
            raise SyntaxError(f"Expected IDENT or NUM, found {self.current_token()}")


# In[28]:


'''code = input("Enter your code: ")
try:
    tokens = tokenize(code)
    print("Tokens:")
    for token in tokens:
        print(token)
    print("\nParsing...")
    parser = Parser(tokens)
    parser.parse_program()
    print("Parsing completed successfully.")
except ValueError as e:
    print(f"Lexical error: {e}")
except SyntaxError as e:
    print(f"Syntax error: {e}")'''


# In[33]:


def run_scanner_and_parser():
    code = input_text.get("1.0", tk.END).strip()
    try:
        # Tokenize the input
        tokens = tokenize(code)
        tokens_output = "Tokens:\n" + "\n".join(f"{kind}: {value}" for kind, value in tokens)
        
        # Parse the input
        parser = Parser(tokens)
        parser.parse_program()
        parse_output = "\nParsing completed successfully."
        
        # Show the results
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, tokens_output + parse_output)
    except ValueError as e:
        messagebox.showerror("Lexical Error", str(e))
    except SyntaxError as e:
        messagebox.showerror("Syntax Error", str(e))


root = tk.Tk()
root.title("Arabic Compiler Scanner and Parser")

# Input Text Area
tk.Label(root, text="Enter your code:").pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
input_text.pack()

# Output Text Area
tk.Label(root, text="Output:").pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50, state=tk.NORMAL)
output_text.pack()

# Run Button
run_button = tk.Button(root, text="Run Scanner and Parser", command=run_scanner_and_parser)
run_button.pack()

# Start Tkinter event loop
root.mainloop()


# In[ ]:


'''
def run_scanner_and_parser():
    code = input_text.get("1.0", tk.END).strip()
    try:
        # Tokenize the input
        tokens = tokenize(code)
        tokens_output = "Tokens:\n" + "\n".join(f"{kind}: {value}" for kind, value in tokens)
        
        # Parse the input
        parser = Parser(tokens)
        parser.parse_program()
        parse_output = "Parsing completed successfully."
        
        # Display the scanner tokens in one box
        tokens_output_box.delete("1.0", tk.END)
        tokens_output_box.insert(tk.END, tokens_output)
        
        # Display the parser result in another box
        parse_result_box.delete("1.0", tk.END)
        parse_result_box.insert(tk.END, parse_output)
        
    except ValueError as e:
        messagebox.showerror("Lexical Error", str(e))
    except SyntaxError as e:
        messagebox.showerror("Syntax Error", str(e))

# Tkinter GUI setup
root = tk.Tk()
root.title("Arabic Compiler Scanner and Parser")

# Input Text Area
tk.Label(root, text="Enter your code:").pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
input_text.pack()

# Output Text Areas
tk.Label(root, text="Scanner Tokens:").pack()
tokens_output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
tokens_output_box.pack()

tk.Label(root, text="Parser Result:").pack()
parse_result_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
parse_result_box.pack()

# Run Button
run_button = tk.Button(root, text="Run Scanner and Parser", command=run_scanner_and_parser)
run_button.pack()

# Start Tkinter event loop
root.mainloop()
'''

