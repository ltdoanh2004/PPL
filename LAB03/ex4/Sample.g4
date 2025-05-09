grammar Sample;

program: sentence;

sentence: START option? compoundID E_Mask;

START: 'Do' | 'Does' | 'Are' | 'Is';
E_Mask: '?';
ID: [a-z]+;

option: 'a' | 'an' | 'the';

// Match either 1 or 2 lowercase words
compoundID: ID (ID)?;
 
WS: [ \t\r\n]+ -> skip;
