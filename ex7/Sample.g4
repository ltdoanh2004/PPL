grammar Sample;


// Parser rule
start : QUESTION EOF ;

// Lexer rule: cụm câu hợp lệ
QUESTION : ( 'Do' | 'Does' | 'Are' | 'Is' ) ' ' [a-z]+ '?' ;

// Bỏ khoảng trắng thừa
WS : [ \t\r\n]+ -> skip ;

// Bỏ ký tự không hợp lệ
ERROR_CHAR : . -> skip ;
