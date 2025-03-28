grammar Sample;


// Parser rule: chỉ nhận 1 ID duy nhất rồi EOF
start : ID EOF ;

// Lexer rule: ID chỉ chứa các ký tự được cho phép
ID : [abdez]+ ;

// Bỏ qua khoảng trắng
WS : [ \t\r\n]+ -> skip ;

// Bỏ qua các ký tự không hợp lệ
ERROR_CHAR : . -> skip ;
