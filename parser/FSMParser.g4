parser grammar FSMParser;

options {
	tokenVocab = FSMLexer;
}

importStmt : IMPORT STRING SEMICOLON;
