grammar Sample;


// Parser rule: chỉ nhận đúng một dòng hợp lệ
start : HELLO_ID_EXCL EOF ;

// Lexer rule: bắt toàn bộ pattern "hello" + id + "!"
HELLO_ID_EXCL : 'hello' [a-z]+ '!' ;

// Bỏ khoảng trắng
WS : [ \t\r\n]+ -> skip ;

// Bắt và bỏ mọi ký tự không hợp lệ
ERROR_CHAR : . -> skip ;
