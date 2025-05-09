grammar Sample;

// Parser rule
start : FLOAT EOF ; // Input must be a float and nothing else

// Lexer rule for float number
FLOAT : [0-9]+ '.' [0-9]+ ;

// Skip whitespace
WS : [ \t\r\n]+ -> skip ;

// Catch all invalid characters
ERROR_CHAR : . -> skip ;
