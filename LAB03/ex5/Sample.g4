grammar Sample;

program: sentence;

sentence: START option? compoundID;

START: 'turn on' | 'turn off' | 'play';

option: 'the';

ID: [a-z]+;

// compoundID có thể là 1 hoặc 2 từ
compoundID: ID (ID)*;

WS: [ \t\r\n]+ -> skip;
