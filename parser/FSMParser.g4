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
}

start : importStmt* modDecl* ;

importStmt : IMPORT STRING SEMICOLON;

modDecl returns [mod]
    : {$mod = Module()} {self.curr_state = $mod.default_state}
    MODULE ID (LEFTBRACKET INT RIGHTBRACKET)? LEFTCURLY
    inputDecl* outputDecl* childDecl*
    (outputAssignment | childAssignment | forExpr)*
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

childDecl : ID declarationTerm SEMICOLON;

declarationTerm returns [name, len, defVal]
    : ID {$name = $ID.text} {$len = 1}
    (LEFTANGLE intExpr RIGHTANGLE {$len = $intExpr.val})?
    (ASSIGN strExpr {$defVal = $strExpr.se})?;

forExpr : FOR ID IN LEFTANGLE intExpr COMMA intExpr RIGHTANGLE LEFTCURLY (childAssignment | forExpr)* RIGHTCURLY ;

stateDecl returns [name]
    : {isInitial = False} (INITIAL {isInitial = True})?
    STATE ID {$name = $ID.text} {self.$modDecl::mod.define_state($name)}
    {if isInitial: self.$modDecl::mod.define_initial_state($name)}
    {self.curr_state = self.$modDecl::mod.states[$name]}
    LEFTCURLY (transitionDecl | outputAssignment)* RIGHTCURLY;

transitionDecl
    : LEFTARROW boolExpr SEMICOLON {self.$modDecl::mod.default_state.define_transition($boolExpr.be, self.$stateDecl::name)}
    | optionalBool RIGHTARROW ID SEMICOLON {self.curr_state.define_transition($optionalBool.be, $ID.text)}
    ;

outputAssignment : ID ASSIGN strExpr SEMICOLON {self.curr_state.define_output($ID.text, $strExpr.se)} ;

childAssignment : ID DOT ID ASSIGN strExpr SEMICOLON 
                | ID LEFTANGLE intExpr RIGHTANGLE DOT ID ASSIGN strExpr SEMICOLON
                ;

strExpr returns [se]
    : LEFTBRACKET strExpr RIGHTBRACKET {$se = $strExpr.se}
    | strExpr LEFTANGLE intExpr RIGHTANGLE {$se = SliceExpr($strExpr.se, $intExpr.val, $intExpr.val + 1)}
    | strExpr LEFTANGLE s=optionalInt COLON e=optionalInt RIGHTANGLE {$se = SliceExpr($strExpr.se, $s.f (0), $e.f (-1))}
    | l=strExpr PLUS r=strExpr {$se = ConcatExpr($l.se, $r.se)}
    | ID {$se = self.$modDecl::mod.inputs[$ID.text]}
    | c=ID DOT i=ID {$se = self.$modDecl::mod.children[$c.text].outputs[$i.text]}
    | arrayExpr DOT ID
    | STRING {$se = StringExpr($STRING.text[1:-1])}
    ;

arrayExpr : ID LEFTANGLE intExpr RIGHTANGLE
          | ID LEFTANGLE intExpr? COLON intExpr? RIGHTANGLE
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
    | intExpr TIMES intExpr {$val = $i1.val * $i2.val}
    | intExpr PLUS intExpr {$val = $i1.val + $i2.val}
    | i1=intExpr MINUS i2=intExpr {$val = $i1.val - $i2.val}
    | INT {$val = $INT.int}
    //| ID
    ;

optionalInt returns [f]
    : {$f = lambda x: x}
    | intExpr {$f = lambda x: $intExpr.val}
    ;
