grammar Sample;

program: expression;

expression: expression ('+' | '-') term # AddSub
          | term                       # SingleTerm;

term: Integer;

Integer: [0-9]+;

WS : [ \t\r\n]+ -> skip; // Skip spaces, tabs, newlines