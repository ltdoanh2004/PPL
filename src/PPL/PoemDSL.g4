grammar PoemDSL;

// Parser Rules
command
    : generatePoem
    | generateControlledPoem
    ;

generatePoem
    : GENERATE POEM MODEL INT CONTEXT STRING STANZAS INT
    ;

generateControlledPoem
    : GENERATE CONTROLLED POEM CONTEXT STRING TOPIC INT
    ;

// Lexer Rules
GENERATE : 'GENERATE' | 'GEN' ;
POEM : 'POEM' ;
MODEL : 'MODEL' | 'M' ;
CONTEXT : 'CONTEXT' | 'C' ;
STANZAS : 'STANZAS' | 'S' ;
CONTROLLED : 'CONTROLLED' ;
TOPIC : 'TOPIC' | 'T' ;

INT : [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;

// Skip whitespace
WS : [ \t\r\n]+ -> skip ; 