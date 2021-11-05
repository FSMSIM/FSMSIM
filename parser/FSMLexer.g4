lexer grammar FSMLexer;

SEMICOLON: ';';
LEFTBRACKET: '(';
RIGHTBRACKET: ')';

IMPORT: 'import';

INT
:
	POSINT | NEGINT
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
	ID_LETTER
	(
		ID_LETTER
		| DIGIT
	)*
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

