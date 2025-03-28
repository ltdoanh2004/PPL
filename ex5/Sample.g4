grammar Sample;


// Parser rule
start : ID EOF ;

// Lexer rule: Bắt đầu bằng "abc", theo sau là các ký tự cho phép
ID : 'abc' [abdez]* ;

// Bỏ qua khoảng trắng
WS : [ \t\r\n]+ -> skip ;

// Bỏ qua ký tự không hợp lệ
ERROR_CHAR : . -> skip ;
