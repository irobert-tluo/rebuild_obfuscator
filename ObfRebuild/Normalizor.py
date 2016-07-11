from slimit.lexer import Lexer
from bs4 import BeautifulSoup

class Normalizor:
  def __init__(self):
    self.mapping = {
      "TRY"     :"A",
      "CATCH"   :"A",
      "IF"      :"E",
      "ELSE"    :"E",
      "SWITCH"  :"X",
      "CASE"    :"X",
      "DEFAULT" :"X",
      "WHILE"   :"W",
      "DO"      :"W",
      "REGEX"   :"G",
      "RETURN"  :"R",
      "NEW"     :"N",
      "FOR"     :"O",
      "VAR"     :"V",
      "THIS"    :"T",
      "DELETE"  :"L",
      "IN"      :"N",
      "TYPEOF"  :"Y",
      "NULL"    :"U",
      "BREAK"   :"B",
      "FUNCTION":"F",
      "NUMBER"  :"i",
      "STRING"  :"S",
      "ID"      :"I",
      "LBRACKET":"[",
      "RBRACKET":"]",
      "LBRACE"  :"{",
      "RBRACE"  :"}",
      "LPAREN"  :"(",
      "RPAREN"  :")",
      "COMMA"   :",",
      "PERIOD"  :".",
      "COLON"   :":",
      "SEMI"    :";",
      "MULT"    :"*",
      "DIV"     :"/",
      "MINUS"   :"-",
      "PLUS"    :"+",
      "PLUSPLUS":"+",
      "EQ"      :"=",
      "ANDEQUAL"  :"=",
      "PLUSEQUAL" :"=",
      "MINUSEQUAL":"=",
      "XOREQUAL"  :"=",
      "LSHIFTEQUAL":"=",
      "OREQUAL" :"=",
      "EQEQ"    :"Q",
      "CONDOP"  :"?",
      "NOT"     :"!",
      "STRNEQ"  :"!",
      "OR"      :"|",
      "MOD"     :"%",
      "NE"      :"!",
      "TRUE"    :"1",
      "FALSE"   :"0",
      "LT"      :"<",
      "GT"      :">",
      "LE"      :"<",
      "GE"      :">",
      "STREQ"   :"_",
      "AND"     :"&",
      "URSHIFT" :">",
      "RSHIFT"  :">",
      "LRSHIFT" :"<",
      "LSHIFT"  :"<",
      "BAND"    :"&",
      "BOR"     :"|",
      "BXOR"    :"^",
    }

  def extract_script(self, page):
    soup = BeautifulSoup(page, "html.parser")
    scripts = []
    for script in soup.findAll("script"):
      if script.get("src"):
        continue
      try:
        scripts.append(script.get_text())
      except:
        pass
    return scripts

  def tokenize(self, code):
    try:
      script = code.decode('ascii', 'ignore')
      lexer = Lexer()
      lexer.input(script)
      return lexer
    except:
      return None

  def normalize(self, page):
    scripts = self.extract_script(page)
    encode = ""
    for script in scripts:
      tokens = self.tokenize(script)
      if not tokens:
        continue
      for token in tokens:
        if token.type not in self.mapping:
          continue
        encode += self.mapping[token.type]
    return encode
