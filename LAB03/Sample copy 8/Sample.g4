grammar Sample;

program: sentence;

sentence: HELLO ID E_Mask;

HELLO: 'Hello';
ID: [a-z]+ ;
E_Mask: '!';

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines