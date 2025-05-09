grammar Sample;

program: sentence;

sentence: IS ID E_Mask;

IS: 'Is';
ID: [a-z] ;
E_Mask: '?';

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines