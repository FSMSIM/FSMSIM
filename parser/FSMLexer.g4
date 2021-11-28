lexer grammar FSMLexer;

SEMICOLON: ';';
COLON: ':' ;
LEFTBRACKET: '(';
RIGHTBRACKET: ')';
LEFTCURLY: '{';
RIGHTCURLY: '}';
LEFTANGLE: '[';
RIGHTANGLE: ']';

DOLLAR: '$';
DEL: 'del';

EQ: '==';
NEQ: '!=';
AND: '&&';
OR: '||';
NOT: '!';

DOT: '.';
COMMA: ',';
LEFTARROW: '<-';
RIGHTARROW: '->';
ASSIGN: '=';

PLUS: '+';
MINUS: '-';
TIMES: '*';

TRUE: 'true';
FALSE: 'false';

IMPORT: 'import';
MODULE: 'module';
INPUT: 'input';
OUTPUT: 'output';
STATE: 'state';
INITIAL: 'initial';


FOR: 'for';
IN: 'in';

INT
:
    POSINT // | NEGINT
;

fragment
POSINT
:
    DIGIT+
;


fragment
NEGINT
:
    ('-')DIGIT+
;

STRING
:
    '"' DoubleStringCharacter* '"'
    | '\'' SingleStringCharacter* '\''
;

fragment
DoubleStringCharacter
:
    ~["\r\n]
;
fragment
SingleStringCharacter
:
    ~['\r\n]
;
fragment
DIGIT
:
    [0-9]
;
ID
:
    LETTER
    (
        ID_LETTER
        | DIGIT
    )*
;
fragment
LETTER
:
    [a-zA-Z]
;
fragment
ID_LETTER
:
    [a-zA-Z_]
;
// Whitespace and comments
NEWLINE
:
    [\r\n]+ -> skip
;
WS
:
    [ \t\r\n\u000C]+ -> skip
;
COMMENT
:
    '/*' .*? '*/' -> skip
;
LINE_COMMENT
:
    '//' .*? '\r'? '\n' -> skip
;

