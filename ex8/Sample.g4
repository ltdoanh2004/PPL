grammar Sample;


// Parser rule: phải là 1 câu hợp lệ duy nhất
start : VALID_INPUT EOF ;

// VALID_INPUT: ít nhất 2 chữ thường, sau đó có thể có chữ thường hoặc số, kết thúc bằng ok|fail|maybe
VALID_INPUT : [a-z][a-z] [a-z0-9_]* ( 'ok' | 'fail' | 'maybe' ) ;

// Bỏ khoảng trắng
WS : [ \t\r\n]+ -> skip ;

// Bỏ ký tự không hợp lệ
ERROR_CHAR : . -> skip ;
