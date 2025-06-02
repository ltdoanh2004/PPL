grammar PoemDSL;

// Parser Rules
command
    : generatePoem
    | generateControlledPoem
    | helpCommand
    | listTopics
    | showModelInfo
    ;

generatePoem
    : GENERATE POEM MODEL INT CONTEXT STRING STANZAS INT
    ;

generateControlledPoem
    : GENERATE CONTROLLED POEM CONTEXT STRING TOPIC INT
    ;

helpCommand
    : HELP
    | SHOW COMMANDS
    ;

listTopics
    : LIST TOPICS
    | SHOW TOPICS
    ;

showModelInfo
    : SHOW MODEL INFO
    ;

// Lexer Rules
GENERATE : 'GENERATE' | 'GEN' ;
POEM : 'POEM' ;
MODEL : 'MODEL' | 'M' ;
CONTEXT : 'CONTEXT' | 'C' ;
STANZAS : 'STANZAS' | 'S' ;
CONTROLLED : 'CONTROLLED' ;
TOPIC : 'TOPIC' | 'T' ;

// User interaction commands
HELP : 'HELP' ;
SHOW : 'SHOW' ;
COMMANDS : 'COMMANDS' ;
LIST : 'LIST' ;
TOPICS : 'TOPICS' ;
INFO : 'INFO' ;

INT : [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;

// Skip whitespace
WS : [ \t\r\n]+ -> skip ; 