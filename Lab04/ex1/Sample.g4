grammar Sample;

program: expression;

expression: expression ('+'|'-') term | term;

term: Integer;

Integer: [0-9]+ ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
