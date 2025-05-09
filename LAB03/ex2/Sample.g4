grammar Sample;

program: sentence;

sentence: START ID E_Mask;

START: 'Do' | 'Does' | 'Are' | 'Is';
ID: [a-z]+;
E_Mask: '?';

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
