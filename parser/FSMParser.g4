parser grammar FSMParser;

options {
    tokenVocab = FSMLexer;
}

@header {
from ..expr import *
from .. import Module
}

@members {
def init(self, loader):
    self.loader = loader
    self.vars = dict()
}

start : importStmt* modDecl* ;

importStmt : IMPORT STRING SEMICOLON {self.loader.load($STRING.text[1:-1])};

modDecl returns [mod]
    : {$mod = Module()} {self.curr_state = $mod.default_state} {self.vars = dict()}
    MODULE ID (LEFTBRACKET INT RIGHTBRACKET {$mod.define_clock_cycles($INT.int)})? LEFTCURLY
    assignVar*
    inputDecl* outputDecl* childDecl*
    (outputAssignment | childAssignment | assignVar | forExpr)*
    stateDecl*
    RIGHTCURLY
    {self.loader.register($ID.text, $mod)}
    ;

inputDecl
    : INPUT d1=declarationTerm {self.$modDecl::mod.define_input($d1.name, $d1.len, $d1.defVal)}
    (COMMA d2=declarationTerm {self.$modDecl::mod.define_input($d2.name, $d2.len), $d2.defVal})*
    SEMICOLON;

outputDecl
    : OUTPUT d1=declarationTerm {self.$modDecl::mod.define_output($d1.name, $d1.len, $d1.defVal)}
    (COMMA d2=declarationTerm {self.$modDecl::mod.define_output($d2.name, $d2.len, $d2.defVal)})*
    SEMICOLON;

childDecl
    : ID d=declarationTerm SEMICOLON
    {self.$modDecl::mod.children[$d.name] = self.loader.modules[$ID.text].init() if $d.len == 1 else [self.loader.modules[$ID.text].init() for _ in range($d.len)]};

declarationTerm returns [name, len, defVal]
    : ID {$name = $ID.text} {$len = 1}
    (LEFTANGLE intExpr RIGHTANGLE {$len = $intExpr.val})?
    (ASSIGN strExpr {$defVal = $strExpr.se})?;

assignVar : DOLLAR ID ASSIGN intExpr SEMICOLON {self.vars[$ID.text] = $intExpr.val};

// deleteVar : DEL DOLLAR ID SEMICOLON {del self.vars[$ID.text]};

// Not actually used. For loops are unrolled before parsing.
forExpr : FOR ID IN LEFTANGLE INT COMMA INT COMMA INT RIGHTANGLE LEFTCURLY (childAssignment | forExpr)* RIGHTCURLY ;

stateDecl returns [name]
    : {isInitial = False} (INITIAL {isInitial = True})?
    STATE ID {$name = $ID.text} {self.$modDecl::mod.define_state($name)}
    {if isInitial: self.$modDecl::mod.define_initial_state($name)}
    {self.curr_state = self.$modDecl::mod.states[$name]}
    LEFTCURLY (transitionDecl | outputAssignment)* RIGHTCURLY;

transitionDecl
    : LEFTARROW optionalBool SEMICOLON {self.$modDecl::mod.default_state.define_transition($optionalBool.be, self.$stateDecl::name)}
    | optionalBool RIGHTARROW ID SEMICOLON {self.curr_state.define_transition($optionalBool.be, $ID.text)}
    ;

outputAssignment : ID ASSIGN strExpr SEMICOLON {self.curr_state.define_output($ID.text, $strExpr.se)} ;

childAssignment
    : c=ID DOT f=ID ASSIGN v=strExpr SEMICOLON {self.$modDecl::mod.children[$c.text].inputs[$f.text].set($v.se)}
    | c=ID LEFTANGLE i=intExpr RIGHTANGLE DOT f=ID ASSIGN v=strExpr SEMICOLON
      {self.$modDecl::mod.children[$c.text][$i.val].inputs[$f.text].set($v.se)}
    ;

strExpr returns [se]
    : LEFTBRACKET strExpr RIGHTBRACKET {$se = $strExpr.se}
    | l=strExpr LEFTANGLE intExpr RIGHTANGLE {$se = SliceExpr($l.se, $intExpr.val, $intExpr.val + 1)}
    | l=strExpr LEFTANGLE s=optionalInt COLON e=optionalInt RIGHTANGLE {$se = SliceExpr($l.se, $s.f (0), $e.f (None))}
    | l=strExpr PLUS r=strExpr {$se = ConcatExpr($l.se, $r.se)}
    | ID {$se = self.$modDecl::mod.inputs[$ID.text]}
    | c=ID DOT i=ID {$se = self.$modDecl::mod.children[$c.text].outputs[$i.text]}
    | arrayExpr DOT ID {$se = ArrayAccessExpr($arrayExpr.ae, $ID.text)}
    | STRING {$se = StringExpr($STRING.text[1:-1])}
    ;

arrayExpr returns [ae]
    : ID LEFTANGLE i=intExpr RIGHTANGLE {$ae = ArrayExpr(self.$modDecl::mod.children[$ID.text], $i.val, $i.val + 1)}
    | ID LEFTANGLE s=optionalInt COLON e=optionalInt RIGHTANGLE {$ae = ArrayExpr(self.$modDecl::mod.children[$ID.text], $s.f (0), $e.f (None))}
    ;

boolExpr returns [be]
    : LEFTBRACKET boolExpr RIGHTBRACKET {$be = $boolExpr.be}
    | NOT boolExpr {$be = NotExpr($boolExpr.be)}
    | l=boolExpr AND r=boolExpr {$be = AndExpr($l.be, $r.be)}
    | l=boolExpr OR r=boolExpr {$be = OrExpr($l.be, $r.be)}
    | s1=strExpr EQ s2=strExpr {$be = EqExpr($s1.se, $s2.se)}
    | s1=strExpr NEQ s2=strExpr {$be = NeqExpr($s1.se, $s2.se)}
    | TRUE {$be = BoolExpr(True)}
    | FALSE {$be = BoolExpr(False)}
    ;

optionalBool returns [be]
    : {$be = BoolExpr(True)}
    | boolExpr {$be = $boolExpr.be}
    ;

intExpr returns [val]
    : LEFTBRACKET intExpr RIGHTBRACKET {$val = $intExpr.val}
    | i1=intExpr TIMES i2=intExpr {$val = $i1.val * $i2.val}
    | i1=intExpr PLUS i2=intExpr {$val = $i1.val + $i2.val}
    | i1=intExpr MINUS i2=intExpr {$val = $i1.val - $i2.val}
    | INT {$val = $INT.int}
    | ID {$val = self.vars[$ID.text]}
    ;

optionalInt returns [f]
    : {$f = lambda x: x}
    | intExpr {$f = lambda x: $intExpr.val}
    ;
