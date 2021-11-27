parser grammar FSMParser;

options {
	tokenVocab = FSMLexer;
}

start : importStmt* moduleDeclaration* ;

importStmt : IMPORT STRING SEMICOLON;

moduleDeclaration : 
	MODULE ID (LEFTBRACKET INT RIGHTBRACKET)? LEFTCURLY
	inputDeclaration* outputDeclaration* childDeclaration*
	(outputAssignment | childAssignment | forExpr)*
	stateDeclaration*
	RIGHTCURLY;

inputDeclaration : INPUT declarationTerm (COMMA declarationTerm)* SEMICOLON;

outputDeclaration : OUTPUT declarationTerm (COMMA declarationTerm)* SEMICOLON;

childDeclaration : ID declarationTerm SEMICOLON;

declarationTerm : ID (LEFTANGLE intExpr RIGHTANGLE)? (ASSIGN strExpr)?;

forExpr : FOR ID IN LEFTANGLE intExpr COMMA intExpr RIGHTANGLE LEFTCURLY (childAssignment | forExpr)* RIGHTCURLY ;

stateDeclaration : (INITIAL)? STATE ID LEFTCURLY (transitionDeclaration | outputAssignment)* RIGHTCURLY;

transitionDeclaration : LEFTARROW boolExpr SEMICOLON
                      | boolExpr? RIGHTARROW ID SEMICOLON
					  ;

outputAssignment : ID ASSIGN strExpr SEMICOLON ;
childAssignment : ID DOT ID ASSIGN strExpr SEMICOLON 
                | ID LEFTANGLE intExpr RIGHTANGLE DOT ID ASSIGN strExpr SEMICOLON
				;

strExpr : LEFTBRACKET strExpr RIGHTBRACKET
		| strExpr LEFTANGLE intExpr RIGHTANGLE
		| strExpr LEFTANGLE intExpr? COLON intExpr? RIGHTANGLE
        | strExpr PLUS strExpr
        | ID
        | ID DOT ID
		| arrayExpr DOT ID
		| STRING
		;

arrayExpr : ID LEFTANGLE intExpr RIGHTANGLE
		  | ID LEFTANGLE intExpr? COLON intExpr? RIGHTANGLE
          ;

boolExpr : LEFTBRACKET boolExpr RIGHTBRACKET
         | NOT boolExpr
		 | boolExpr AND boolExpr
		 | boolExpr OR boolExpr
		 | strExpr EQ strExpr
		 | strExpr NEQ strExpr
		 | TRUE
		 | FALSE
		 ;

intExpr : LEFTBRACKET intExpr RIGHTBRACKET
        | intExpr TIMES intExpr
		| intExpr PLUS intExpr
		| intExpr MINUS intExpr
		| INT
		| ID
		;
